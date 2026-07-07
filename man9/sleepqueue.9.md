# sleepqueue(9)

`init_sleepqueues` — 管理睡眠线程的队列

## 名称

`init_sleepqueues`, `sleepq_abort`, `sleepq_add`, `sleepq_alloc`, `sleepq_broadcast`, `sleepq_free`, `sleepq_lock`, `sleepq_lookup`, `sleepq_release`, `sleepq_remove`, `sleepq_signal`, `sleepq_set_timeout`, `sleepq_set_timeout_sbt`, `sleepq_sleepcnt`, `sleepq_timedwait`, `sleepq_timedwait_sig`, `sleepq_type`, `sleepq_wait`, `sleepq_wait_sig`

## 概要

```c
#include <sys/param.h>
#include <sys/sleepqueue.h>

void
init_sleepqueues(void)

int
sleepq_abort(struct thread *td)

void
sleepq_add(const void *wchan, struct lock_object *lock,
    const char *wmesg, int flags, int queue)

struct sleepqueue *
sleepq_alloc(void)

int
sleepq_broadcast(const void *wchan, int flags, int pri, int queue)

void
sleepq_free(struct sleepqueue *sq)

struct sleepqueue *
sleepq_lookup(const void *wchan)

void
sleepq_lock(const void *wchan)

void
sleepq_release(const void *wchan)

void
sleepq_remove(struct thread *td, const void *wchan)

int
sleepq_signal(const void *wchan, int flags, int pri, int queue)

void
sleepq_set_timeout(const void *wchan, int timo)

void
sleepq_set_timeout_sbt(const void *wchan, sbintime_t sbt,
    sbintime_t pr, int flags)

u_int
sleepq_sleepcnt(const void *wchan, int queue)

int
sleepq_timedwait(const void *wchan, int pri)

int
sleepq_timedwait_sig(const void *wchan, int pri)

int
sleepq_type(const void *wchan)

void
sleepq_wait(const void *wchan, int pri)

int
sleepq_wait_sig(const void *wchan, int pri)
```

## 描述

睡眠队列提供了一种机制，用于挂起线程的执行直到满足某些条件。每个队列在活动时与特定的等待通道关联，且在任何给定时刻一个等待通道只能与一个队列关联。每个等待通道的实现将其 sleepqueue 拆分为 2 个子队列，以便在线程唤醒时进行一些优化。活动队列持有一个阻塞在关联等待通道上的线程列表。未阻塞在等待通道上的线程关联有一个非活动的睡眠队列。当线程阻塞在等待通道上时，它会将其非活动的睡眠队列捐赠给该等待通道。当线程被恢复时，它所阻塞的等待通道会向它提供一个非活动的睡眠队列供后续使用。

`sleepq_alloc` 函数分配一个非活动的睡眠队列，用于在线程创建期间为线程分配睡眠队列。`sleepq_free` 函数释放与非活动睡眠队列关联的资源，用于在线程销毁期间释放队列。

活动睡眠队列存储在以等待通道所指向地址为哈希键的哈希表中。哈希表中的每个桶包含一个睡眠队列链。一个睡眠队列链包含一个自旋互斥体和哈希到该特定链的睡眠队列列表。活动睡眠队列由其链的自旋互斥体保护。`init_sleepqueues` 函数初始化睡眠队列链的哈希表。

`sleepq_lock` 函数锁定与等待通道 `wchan` 关联的睡眠队列链。

`sleepq_lookup` 返回与 `wchan` 关联的等待通道当前活动睡眠队列的指针，如果没有与参数 `wchan` 关联的活动睡眠队列则返回 `NULL`。它要求与 `wchan` 关联的睡眠队列链已通过先前调用 `sleepq_lock` 锁定。

`sleepq_release` 函数解锁与 `wchan` 关联的睡眠队列链，主要在调用某个等待函数之前中止挂起的睡眠请求时有用。

`sleepq_add` 函数将当前线程放置在与等待通道 `wchan` 关联的睡眠队列上。调用此函数时，与参数 `wchan` 关联的睡眠队列链必须已通过先前调用 `sleepq_lock` 锁定。如果通过 `lock` 参数指定了锁，且内核编译时使用了 `options INVARIANTS`，则睡眠队列代码将执行额外检查，以确保该锁被所有在 `wchan` 上睡眠的线程使用。`wmesg` 参数应为 `wchan` 的简短描述。`flags` 参数是一个位掩码，由所睡眠的睡眠队列类型及零个或多个可选标志组成。`queue` 参数指定要插入争用线程的子队列。

目前有三种类型的睡眠队列：

**`SLEEPQ_CONDVAR`** 用于实现条件变量的睡眠队列。

**`SLEEPQ_SLEEP`** 用于实现 [sleep(9)](sleep.9.md)、wakeup(9) 和 wakeup_one(9) 的睡眠队列。

**`SLEEPQ_PAUSE`** 用于实现 pause(9) 的睡眠队列。

目前有两个可选标志：

**`SLEEPQ_INTERRUPTIBLE`** 当前线程正在进入可中断睡眠。

**`SLEEPQ_STOP_ON_BDRY`** 当线程进入可中断睡眠时，不要在收到停止动作（如 `SIGSTOP`）时停止它，而是唤醒它。

睡眠的超时可以在调用 `sleepq_add` 之后通过调用 `sleepq_set_timeout` 指定。`wchan` 参数应与先前调用 `sleepq_add` 时的值相同，且与 `wchan` 关联的睡眠队列链必须已通过先前调用 `sleepq_lock` 锁定。`timo` 参数应以时钟滴答为单位指定超时值。

`sleepq_set_timeout_sbt` 函数接受 `sbt` 参数而不是 `timo`。它允许以 `sbintime_t` 形式指定更高分辨率的相对或绝对唤醒时间。`pr` 参数允许指定所需的绝对事件精度。`flags` 参数允许传递额外的 `callout_reset_sbt` 标志。

一旦线程准备好挂起，就调用其中一个等待函数将当前线程置于睡眠状态直到被唤醒，并切换到另一个线程的上下文。`sleepq_wait` 函数用于没有超时的不可中断睡眠。`sleepq_timedwait` 函数用于通过 `sleepq_set_timeout` 设置了超时的不可中断睡眠。`sleepq_wait_sig` 函数用于没有超时的可中断睡眠。`sleepq_timedwait_sig` 函数用于设置了超时的可中断睡眠。所有等待函数的 `wchan` 参数都是所睡眠的等待通道。与参数 `wchan` 关联的睡眠队列链需要已通过先前调用 `sleepq_lock` 锁定。`pri` 参数用于设置线程被唤醒时的优先级。如果设置为零，则线程的优先级保持不变。

当线程被恢复时，如果线程是由于信号或超时以外的中断而被唤醒，等待函数返回非零值。如果睡眠超时，则返回 `EWOULDBLOCK`。如果睡眠被信号以外的事物中断，则返回其他一些返回值。

睡眠中的线程通常由 `sleepq_broadcast` 和 `sleepq_signal` 函数恢复。`sleepq_signal` 函数唤醒在等待通道上睡眠的最高优先级线程（如果设置了 `SLEEPQ_UNFAIR` 标志，则唤醒最近入睡的线程），而 `sleepq_broadcast` 唤醒在等待通道上睡眠的所有线程。`wchan` 参数指定要唤醒的等待通道。`flags` 参数必须与在等待通道上睡眠的线程传递给 `sleepq_add` 的 `flags` 参数中包含的睡眠队列类型匹配。如果 `pri` 参数不等于 -1，则每个被唤醒的线程如果优先级较低，则其优先级将提升到 `pri`。与参数 `wchan` 关联的睡眠队列链在调用这些函数之前必须通过先前调用 `sleepq_lock` 锁定。`queue` 参数指定需要从中唤醒线程的子队列。

处于可中断睡眠中的线程可以通过 `sleepq_abort` 函数被另一个线程中断。`td` 参数指定要中断的线程。也可以通过 `sleepq_remove` 函数将单个线程从特定等待通道上的睡眠中唤醒。`td` 参数指定要唤醒的线程，`wchan` 参数指定要从中唤醒它的等待通道。如果线程 `td` 未阻塞在等待通道 `wchan` 上，则此函数不会执行任何操作，即使线程在不同的等待通道上睡眠。仅当上述其他函数不足以满足需求时才应使用此函数。一种可能的用途是从广泛共享的睡眠通道中唤醒特定线程。

`sleepq_sleepcnt` 函数提供了一种简单的方法，在给定 `wchan` 的情况下检索指定 `queue` 上睡眠的线程数量。

`sleepq_type` 函数返回与睡眠队列关联的 `wchan` 的类型。

`sleepq_abort`、`sleepq_broadcast` 和 `sleepq_signal` 函数均返回布尔值。如果返回值为真，则至少有一个被恢复的线程当前已被换出。调用者负责唤醒调度器进程，以便被恢复的线程被换回。这通过在调用 `sleepq_release` 释放睡眠队列链锁之后调用 `kick_proc0` 函数来完成。

睡眠队列接口目前用于实现 [sleep(9)](sleep.9.md) 和 [condvar(9)](condvar.9.md) 接口。内核中几乎所有其他代码都应使用其中一种接口，而不是直接操作睡眠队列。

## 参见

[callout(9)](callout.9.md), [condvar(9)](condvar.9.md), [runqueue(9)](runqueue.9.md), [scheduler(9)](scheduler.9.md), [sleep(9)](sleep.9.md)
