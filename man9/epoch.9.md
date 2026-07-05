# epoch.9

`epoch` — 基于 epoch 的内核回收

## 名称

`epoch`, `epoch_context`, `epoch_alloc`, `epoch_free`, `epoch_enter`, `epoch_exit`, `epoch_wait`, `epoch_enter_preempt`, `epoch_exit_preempt`, `epoch_wait_preempt`, `epoch_call`, `epoch_drain_callbacks`, `in_epoch`, `in_epoch_verbose`

## 概要

```c
#include <sys/param.h>
#include <sys/proc.h>
#include <sys/epoch.h>
```

```c
struct epoch;		/* 不透明 */
```

```c
typedef struct epoch *epoch_t;
```

```c
struct epoch_context {
	void	*data[2];
};
```

```c
typedef struct epoch_context *epoch_context_t;
typedef void epoch_callback_t(epoch_context_t);
```

```c
struct epoch_tracker;	/* 不透明 */
```

```c
typedef struct epoch_tracker *epoch_tracker_t;

epoch_t
epoch_alloc(const char *name, int flags)

void
epoch_free(epoch_t epoch)

void
epoch_enter(epoch_t epoch)

void
epoch_exit(epoch_t epoch)

void
epoch_wait(epoch_t epoch)

void
epoch_enter_preempt(epoch_t epoch, epoch_tracker_t et)

void
epoch_exit_preempt(epoch_t epoch, epoch_tracker_t et)

void
epoch_wait_preempt(epoch_t epoch)

void
epoch_call(epoch_t epoch, epoch_callback_t callback, epoch_context_t ctx)

void
epoch_drain_callbacks(epoch_t epoch)

int
in_epoch(epoch_t epoch)

int
in_epoch_verbose(epoch_t epoch, int dump_onfail)
```

## 描述

epoch 通过将回收和修改推迟到宽限期之后，保证数据的活跃性和不可变性。epoch 没有任何锁顺序问题。进入和离开一个 epoch 区段永远不会阻塞。

epoch 通过 `epoch_alloc` 分配。`name` 参数在配置了 `EPOCH_TRACE` 内核选项时用于调试便利。默认情况下，epoch 在区段内不允许抢占，且跨 `epoch_wait_preempt` 不能持有互斥锁。指定的 `flags` 由以下值按位 OR 形成：

**`EPOCH_LOCKED`** 允许跨 `epoch_wait_preempt` 持有互斥锁（需要 `EPOCH_PREEMPT`）。这样做时必须小心，避免出现可能死锁的情况。

**`EPOCH_PREEMPT`** 该 `epoch` 在区段内允许抢占。在可抢占 epoch 中只能获取不可睡眠的锁。必须使用 `epoch_enter_preempt`、`epoch_exit_preempt` 和 `epoch_wait_preempt` 分别替代 `epoch_enter`、`epoch_exit` 和 `epoch_wait`。

`epoch` 通过 `epoch_free` 释放。

线程通过调用 `epoch_enter`（对于可抢占 epoch 则为 `epoch_enter_preempt`）来指示一个 epoch 临界区段的开始。线程调用 `epoch_exit`（对于可抢占 epoch 则为 `epoch_exit_preempt`）来指示临界区段的结束。`struct epoch_tracker` 是栈对象，其指针被传递给 `epoch_enter_preempt` 和 `epoch_exit_preempt`（类似于 `struct rm_priotracker`）。

线程可以同步或异步地将工作推迟到宽限期过后执行，该宽限期从任何线程进入该 epoch 时开始计算。`epoch_call` 通过在稍后时间调用提供的 `callback` 来异步推迟工作。`epoch_wait`（或 `epoch_wait_preempt`）阻塞当前线程，直到宽限期已过且工作可以安全执行。

默认的不可抢占 epoch 等待（`epoch_wait`）相对于可抢占 epoch 等待（`epoch_wait_preempt`）保证有更短的完成时间。（在默认类型中，epoch 区段中的任何线程都不会在完成其区段之前被抢占。）

INVARIANTS 可通过 `in_epoch` 断言线程处于 epoch 中。`in_epoch(epoch)` 等价于调用 `in_epoch_verbose(epoch, 0)`。如果启用了 `EPOCH_TRACE`，`in_epoch_verbose(epoch, 1)` 提供额外的详细调试信息。

epoch API 当前不支持在 epoch_preempt 区段中睡眠。调用者绝不应在同一个 epoch 的 epoch 区段中间调用 `epoch_wait`，否则会导致死锁。

`epoch_drain_callbacks` 函数用于排空此前对同一 epoch 调用 `epoch_call` 触发的所有挂起回调。当存在 epoch 回调引用的、未进行引用计数且很少释放的共享内存结构时，此函数很有用。调用此函数的典型位置是在释放或失效 epoch 回调所使用的共享资源之前。此函数可以睡眠，且未针对性能优化。

## 返回值

如果 curthread 处于 curepoch 中，`in_epoch(curepoch)` 返回 1，否则返回 0。

## 实例

异步释放示例：线程 1：

```c
int
in_pcbladdr(struct inpcb *inp, struct in_addr *faddr, struct in_laddr *laddr,
    struct ucred *cred)
{
    /* ... */
    epoch_enter(net_epoch);
    CK_STAILQ_FOREACH(ifa, &ifp->if_addrhead, ifa_link) {
        sa = ifa->ifa_addr;
	if (sa->sa_family != AF_INET)
	    continue;
	sin = (struct sockaddr_in *)sa;
	if (prison_check_ip4(cred, &sin->sin_addr) == 0) {
	     ia = (struct in_ifaddr *)ifa;
	     break;
	}
    }
    epoch_exit(net_epoch);
    /* ... */
}
```

线程 2：

```c
void
ifa_free(struct ifaddr *ifa)
{
    if (refcount_release(&ifa->ifa_refcnt))
        epoch_call(net_epoch, ifa_destroy, &ifa->ifa_epoch_ctx);
}
void
if_purgeaddrs(struct ifnet *ifp)
{
    /* .... */
    IF_ADDR_WLOCK(ifp);
    CK_STAILQ_REMOVE(&ifp->if_addrhead, ifa, ifaddr, ifa_link);
    IF_ADDR_WUNLOCK(ifp);
    ifa_free(ifa);
}
```

线程 1 在一个 epoch 中遍历 ifaddr 列表。线程 2 用对应的 epoch 安全宏将其解除链接，标记为逻辑上已释放，然后推迟删除。更一般的修改或同步释放必须在调用 `epoch_wait` 之后进行。

## 参见

[callout(9)](callout.9.md), [locking(9)](locking.9.md), [mtx_pool(9)](mtx_pool.9.md), [mutex(9)](mutex.9.md), [rwlock(9)](rwlock.9.md), [sema(9)](sema.9.md), [sleep(9)](sleep.9.md), [sx(9)](sx.9.md)

## 历史

`in_epoch_verbose` 框架首次出现于 FreeBSD 11.0。

## 注意事项

使用 `epoch_wait_preempt` 时必须小心。线程在 epoch 区段内固定运行，因此如果区段中的线程随后被该 CPU 上更高优先级的计算密集型线程抢占，可能无法离开该区段，且时间可能无限期延长。

epoch 不能直接替代读锁。调用者必须在 epoch 中使用安全的 list 和 tailq 遍历例程（参见 ck_queue）。修改从 epoch 区段引用的列表时，必须使用安全移除例程，且调用者不能再原地修改列表条目。要修改的项必须以写时复制方式处理，且释放必须推迟到宽限期过后。
