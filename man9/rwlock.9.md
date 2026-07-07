# rwlock(9)

`rwlock` — 内核读/写锁

## 名称

`rwlock`, `rw_init`, `rw_init_flags`, `rw_destroy`, `rw_rlock`, `rw_wlock`, `rw_runlock`, `rw_wunlock`, `rw_unlock`, `rw_try_rlock`, `rw_try_upgrade`, `rw_try_wlock`, `rw_downgrade`, `rw_sleep`, `rw_initialized`, `rw_wowned`, `rw_assert`, `RW_SYSINIT`, `RW_SYSINIT_FLAGS`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/lock.h>
```

```c
#include <sys/rwlock.h>
```

```c
void
rw_init(struct rwlock *rw, const char *name)

void
rw_init_flags(struct rwlock *rw, const char *name, int opts)

void
rw_destroy(struct rwlock *rw)

void
rw_rlock(struct rwlock *rw)

void
rw_wlock(struct rwlock *rw)

int
rw_try_rlock(struct rwlock *rw)

int
rw_try_wlock(struct rwlock *rw)

void
rw_runlock(struct rwlock *rw)

void
rw_wunlock(struct rwlock *rw)

void
rw_unlock(struct rwlock *rw)

int
rw_try_upgrade(struct rwlock *rw)

void
rw_downgrade(struct rwlock *rw)

int
rw_sleep(void *chan, struct rwlock *rw, int priority, const char *wmesg, int timo)

int
rw_initialized(const struct rwlock *rw)

int
rw_wowned(const struct rwlock *rw)
```

```c
options INVARIANTS
options INVARIANT_SUPPORT

void
rw_assert(const struct rwlock *rw, int what)
```

```c
#include <sys/kernel.h>
```

```c
RW_SYSINIT(name, struct rwlock *rw, const char *desc)
RW_SYSINIT_FLAGS(name, struct rwlock *rw, const char *desc, int flags)
```

## 描述

读/写锁允许多个线程共享访问受保护的数据，或单个线程独占访问。具有共享访问权限的线程被称为*读者*，因为它们只读取受保护的数据。具有独占访问权限的线程被称为*写者*，因为它可以修改受保护的数据。

虽然读/写锁看起来与 [sx(9)](sx.9.md) 锁非常相似，但它们的使用模式不同。读/写锁可以被视为具有共享/独占语义的互斥锁（参见 [mutex(9)](mutex.9.md)）。与 [sx(9)](sx.9.md) 不同的是，`rwlock` 可以在持有非自旋互斥锁时加锁，但不能在睡眠时持有。`rwlock` 锁具有与互斥锁类似的优先级传播，但优先级只能传播给写者。此限制源于读者是匿名的这一事实。另一个重要属性是读者始终可以递归，而独占锁可以选择性地设为可递归。

### 宏和函数

**`RW_DUPOK`** witness 不应记录获取重复锁的消息。

**`RW_NOPROFILE`** 不对此锁进行性能分析。

**`RW_NOWITNESS`** 指示 [witness(4)](../man4/witness.4.md) 忽略此锁。

**`RW_QUIET`** 不通过 [ktr(4)](../man4/ktr.4.md) 记录此锁的任何操作。

**`RW_RECURSE`** 允许线程递归获取 `rw` 的独占锁。

**`RW_NEW`** 如果内核编译时启用了 `option INVARIANTS`，`rw_init_flags` 会断言 `rw` 未在前一次调用 `rw_destroy` 之前被多次初始化，除非指定了此选项。

**`RA_LOCKED`** 断言当前线程持有 `rw` 的共享锁或独占锁。

**`RA_RLOCKED`** 断言当前线程持有 `rw` 的共享锁。

**`RA_WLOCKED`** 断言当前线程持有 `rw` 的独占锁。

**`RA_UNLOCKED`** 断言当前线程既不持有 `rw` 的共享锁，也不持有独占锁。

**`RA_RECURSED`** 断言当前线程持有 `rw` 的递归锁。

**`RA_NOTRECURSED`** 断言当前线程不持有 `rw` 的递归锁。

**`rw_init(struct rwlock *rw, const char *name)`** 将位于 `rw` 的结构初始化为读/写锁，由名称 `name` 描述。此描述仅用于调试目的。在对此锁执行任何其他操作之前，必须调用此函数。

**`rw_init_flags(struct rwlock *rw, const char *name, int opts)`** 像 `rw_init` 函数一样初始化 rw 锁，但通过 `opts` 参数指定一组可选标志来改变 `rw` 的行为。它包含以下一个或多个标志：

**`rw_rlock(struct rwlock *rw)`** 以读者身份锁定 `rw`。如果有线程独占持有此锁，当前线程将阻塞，其优先级会传播给独占持有者。当线程已获取 `rw` 的读者访问权限时，仍可调用 `rw_rlock`。这称为"递归加锁"。

**`rw_wlock(struct rwlock *rw)`** 以写者身份锁定 `rw`。如果有任何共享持有者，当前线程将阻塞。仅当 `rw` 已启用 `RW_RECURSE` 选项初始化时，`rw_wlock` 才能递归调用。

**`rw_try_rlock(struct rwlock *rw)`** 尝试以读者身份锁定 `rw`。如果操作成功，此函数将返回 true，否则返回 0。

**`rw_try_wlock(struct rwlock *rw)`** 尝试以写者身份锁定 `rw`。如果操作成功，此函数将返回 true，否则返回 0。

**`rw_runlock(struct rwlock *rw)`** 此函数释放先前由 `rw_rlock` 获取的共享锁。

**`rw_wunlock(struct rwlock *rw)`** 此函数释放先前由 `rw_wlock` 获取的独占锁。

**`rw_unlock(struct rwlock *rw)`** 此函数释放先前由 `rw_rlock` 获取的共享锁或先前由 `rw_wlock` 获取的独占锁。

**`rw_try_upgrade(struct rwlock *rw)`** 尝试将单个共享锁升级为独占锁。当前线程必须持有 `rw` 的共享锁。仅当当前线程持有 `rw` 上唯一的共享锁，且仅持有单个共享锁时，此操作才会成功。如果尝试成功，`rw_try_upgrade` 将返回非零值，当前线程将持有独占锁。如果尝试失败，`rw_try_upgrade` 将返回零，当前线程仍持有共享锁。

**`rw_downgrade(struct rwlock *rw)`** 将独占锁转换为单个共享锁。当前线程必须持有 `rw` 的独占锁。

**`rw_sleep(void *chan, struct rwlock *rw, int priority, const char *wmesg, int timo)`** 在等待事件时原子性地释放 `rw`。有关此函数参数的更多详情，请参见 [sleep(9)](sleep.9.md)。

**`rw_initialized(const struct rwlock *rw)`** 如果 `rw` 已初始化，此函数返回非零值，否则返回零。

**`rw_destroy(struct rwlock *rw)`** 此函数销毁先前由 `rw_init` 初始化的锁。`rw` 锁必须处于未锁定状态。

**`rw_wowned(const struct rwlock *rw)`** 如果当前线程拥有 `rw` 的独占锁，此函数返回非零值。

**`rw_assert(const struct rwlock *rw, int what)`** 此函数允许对 `rw` 作出 `what` 中指定的断言。如果断言不成立，且内核编译时启用了 `options INVARIANTS` 和 `options INVARIANT_SUPPORT`，内核将发生 panic。当前支持以下基本断言：此外，可与 `RA_LOCKED`、`RA_RLOCKED` 或 `RA_WLOCKED` 一起指定以下可选标志之一：

## 参见

[locking(9)](locking.9.md), [mutex(9)](mutex.9.md), [panic(9)](panic.9.md), [sema(9)](sema.9.md), [sx(9)](sx.9.md)

## 历史

这些函数出现在 FreeBSD 7.0 中。

## 作者

`rwlock` 设施由 John Baldwin 编写。本手册页面由 Gleb Smirnoff 编写。

## 缺陷

没有 `WITNESS` 的内核无法断言当前线程是否持有读锁。`RA_LOCKED` 和 `RA_RLOCKED` 只能断言*任何*线程持有读锁。它们无法确保当前线程持有读锁。此外，`RA_UNLOCKED` 只能断言当前线程不持有写锁。

读/写（reader/writer）这个名字有点别扭。如果需要，`rwlock` 也可以称为"Robert Watson"锁。
