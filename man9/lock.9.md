# lock(9)

`lockinit` — lockmgr 函数系列

## 名称

`lockinit`, `lockdestroy`, `lockmgr`, `lockmgr_args`, `lockmgr_args_rw`, `lockmgr_disown`, `lockmgr_disowned`, `lockmgr_lock_flags`, `lockmgr_printinfo`, `lockmgr_recursed`, `lockmgr_rw`, `lockmgr_slock`, `lockmgr_unlock`, `lockmgr_xlock`, `lockstatus`, `lockmgr_assert`

## 概要

```c
#include <sys/types.h>

#include <sys/lock.h>

#include <sys/lockmgr.h>

void
lockinit(struct lock *lkp, int prio, const char *wmesg, int timo, int flags)

void
lockdestroy(struct lock *lkp)

int
lockmgr(struct lock *lkp, u_int flags, struct mtx *ilk)

int
lockmgr_args(struct lock *lkp, u_int flags, struct mtx *ilk,
    const char *wmesg, int prio, int timo)

int
lockmgr_args_rw(struct lock *lkp, u_int flags, struct rwlock *ilk,
    const char *wmesg, int prio, int timo)

void
lockmgr_disown(struct lock *lkp)

int
lockmgr_disowned(const struct lock *lkp)

int
lockmgr_lock_flags(struct lock *lkp, u_int flags, struct lock_object *ilk,
    const char *file, int line)

void
lockmgr_printinfo(const struct lock *lkp)

int
lockmgr_recursed(const struct lock *lkp)

int
lockmgr_rw(struct lock *lkp, u_int flags, struct rwlock *ilk)

int
lockmgr_slock(struct lock *lkp, u_int flags, const char *file, int line)

int
lockmgr_unlock(struct lock *lkp)

int
lockmgr_xlock(struct lock *lkp, u_int flags, const char *file, int line)

int
lockstatus(const struct lock *lkp)
```

```c
options INVARIANTS
options INVARIANT_SUPPORT

void
lockmgr_assert(const struct lock *lkp, int what)
```

## 描述

`lockinit` 函数用于初始化锁。在可以对锁执行任何操作之前必须调用它。其参数为：

**`LK_CANRECURSE`** 允许递归独占锁。

**`LK_NOPROFILE`** 禁用此锁的锁分析。

**`LK_NOSHARE`** 仅允许独占锁。

**`LK_NOWITNESS`** 指示 [witness(4)](../man4/witness.4.md) 忽略此锁。

**`LK_NODUP`** [witness(4)](../man4/witness.4.md) 应记录获取重复锁的消息。

**`LK_QUIET`** 禁用此锁的 [ktr(4)](../man4/ktr.4.md) 日志记录。

**`lkp`** 指向要初始化的锁的指针。

**`prio`** 传递给 [sleep(9)](sleep.9.md) 的优先级。

**`wmesg`** 锁消息。用于调试输出和 [sleep(9)](sleep.9.md)。

**`timo`** 传递给 [sleep(9)](sleep.9.md) 的超时值。

**`flags`** 锁初始化的标志：

`lockdestroy` 函数用于销毁锁，虽然它在内核中的多处被调用，但目前什么也不做。

`lockmgr` 和 `lockmgr_rw` 函数处理内核中的一般锁定功能，包括对共享锁和独占锁以及递归的支持。`lockmgr` 和 `lockmgr_rw` 还能升级和降级锁。

其参数为：

```c
#include <sys/lockmgr.h>
```

**`LK_SHARED`** 获取共享锁。如果当前持有独占锁，返回 `EDEADLK`。

**`LK_EXCLUSIVE`** 获取独占锁。如果已持有独占锁且未设置 `LK_CANRECURSE`，系统将 [panic(9)](panic.9.md)。

**`LK_DOWNGRADE`** 将独占锁降级为共享锁。不允许降级共享锁。如果独占锁已递归，系统将 [panic(9)](panic.9.md)。

**`LK_UPGRADE`** 将共享锁升级为独占锁。如果此调用失败，即使指定了 `LK_NOWAIT` 标志，共享锁也会丢失。升级期间，共享锁可能被临时释放。尝试升级独占锁将导致 [panic(9)](panic.9.md)。

**`LK_TRYUPGRADE`** 尝试将共享锁升级为独占锁。升级失败不会导致共享锁所有权的丢失。

**`LK_RELEASE`** 释放锁。释放未持有的锁可能导致 [panic(9)](panic.9.md)。

**`LK_DRAIN`** 等待锁上的所有活动结束，然后标记为退役。用于释放即将被释放的内存中的锁之前。（如以下文档所述

**`LK_SLEEPFAIL`** 如果操作已休眠则失败。

**`LK_NOWAIT`** 不允许调用休眠。可用于测试锁。

**`LK_TIMELOCK`** 休眠期间使用 `timo`；否则使用 0。

**`LK_NOWITNESS`** 跳过此实例的 [witness(4)](../man4/witness.4.md) 检查。

**`LK_CANRECURSE`** 允许独占锁递归。每个锁都必须有对应的释放。

**`LK_INTERLOCK`** 解锁互锁（应已锁定）。

**`LK_NODDLKTREAT`** 通常，如果存在独占等待者，`lockmgr` 推迟为共享锁定的锁提供进一步的共享请求，以避免独占锁饥饿。但是，如果请求共享锁的线程已拥有共享 lockmgr 锁，即使存在并行的独占锁请求也授予该请求，这是为避免递归共享获取中的死锁而做的。`LK_NODDLKTREAT` 标志只能由请求非递归共享锁的代码使用。此标志允许独占请求抢占当前共享请求，即使当前线程拥有共享锁。这是安全的，因为共享锁保证不递归，用于已知线程持有不相关共享锁时不造成不必要饥饿的情况。一个例子是 VFS lookup(9) 中的 `vp` 锁定，当 `dvp` 已锁定时。

**`lkp`** 指向要操作的锁的指针。

**`flags`** 指示要采取什么操作的标志。

**`ilk`** 用于控制对锁的组访问的互锁互斥量。如果指定 `LK_INTERLOCK`，`lockmgr` 和 `lockmgr_rw` 假定 `ilk` 当前已拥有且未递归，并返回时解锁它。参见 mtx_assert(9)。

`lockmgr_args` 和 `lockmgr_args_rw` 函数工作方式类似于 `lockmgr` 和 `lockmgr_rw`，但按实例接受 `wmesg`、`timo` 和 `prio`。指定的值将覆盖默认值，但仍可分别传递 `LK_WMESG_DEFAULT`、`LK_PRIO_DEFAULT` 和 `LK_TIMO_DEFAULT` 来使用默认值。

`lockmgr_lock_flags` 函数工作方式类似于 `lockmgr`，但接受显式的 `file` 和 `line` 参数用于锁跟踪。

`lockmgr_slock`、`lockmgr_xlock` 和 `lockmgr_unlock` 函数是轻量级入口点，分别功能类似于 `lockmgr` 的 `LK_SHARED`、`LK_EXCLUSIVE` 和 `LK_RELEASE` 操作。它们提供类似于 [sx(9)](sx.9.md) 锁的功能，不支持任何额外的 lockmgr(9) 特性。具体而言，这些函数不支持解锁互锁、`LK_SLEEPFAIL` 标志或通过 `LK_NOSHARE` 禁用共享锁定的锁。它们还接受显式的 `file` 和 `line` 参数用于锁跟踪。

`lockmgr_disown` 函数如果锁已持有，将所有者从当前线程切换为 `LK_KERNPROC`。

`lockmgr_disowned` 函数根据锁是否由 `LK_KERNPROC` 持有返回真或假。

`lockmgr_printinfo` 函数打印有关锁的调试信息。主要由 [VOP_PRINT(9)](vop_print.9.md) 函数使用。

`lockmgr_recursed` 函数如果锁已递归返回真，否则返回 0。

`lockstatus` 函数返回锁相对于当前线程的状态。

当编译时启用 `options INVARIANTS` 和 `options INVARIANT_SUPPORT` 时，`lockmgr_assert` 函数测试 `lkp` 是否满足 `what` 中指定的断言，如果不满足则 panic。必须指定以下断言之一：

**`KA_LOCKED`** 断言当前线程对第一个参数指向的 `lkp` 锁持有共享或独占锁。

**`KA_SLOCKED`** 断言当前线程对第一个参数指向的 `lkp` 锁持有共享锁。

**`KA_XLOCKED`** 断言当前线程对第一个参数指向的 `lkp` 锁持有独占锁。

**`KA_UNLOCKED`** 断言当前线程对第一个参数指向的 `lkp` 锁不持有任何锁。

此外，以下可选断言之一可与 `KA_LOCKED`、`KA_SLOCKED` 或 `KA_XLOCKED` 断言一起使用：

**`KA_RECURSED`** 断言当前线程对 `lkp` 持有递归锁。

**`KA_NOTRECURSED`** 断言当前线程对 `lkp` 不持有递归锁。

## 返回值

`lockmgr` 和 `lockmgr_rw` 函数成功时返回 0，失败时返回非零。

`lockstatus` 函数返回：

**`LK_EXCLUSIVE`** 当前线程持有独占锁。

**`LK_EXCLOTHER`** 当前线程以外的其他人持有独占锁。

**`LK_SHARED`** 持有共享锁。

**`0`** 无人持有锁。

## 错误

`lockmgr` 和 `lockmgr_rw` 在以下情况下失败：

**[`EBUSY`]** 请求了 `LK_FORCEUPGRADE` 且另一个线程已请求锁升级。

**[`EBUSY`]** 设置了 `LK_NOWAIT` 且需要休眠，或 `LK_TRYUPGRADE` 操作无法升级锁。

**[`EDEADLK`]** 线程已持有独占锁时尝试获取共享锁。

**[`ENOLCK`]** 设置了 `LK_SLEEPFAIL` 且 `lockmgr` 或 `lockmgr_rw` 已休眠。

**[`EINTR`]** 锁优先级中设置了 `PCATCH`，且在休眠期间传递了信号。注意下方的 `ERESTART` 错误。

**[`ERESTART`]** 锁优先级中设置了 `PCATCH`，在休眠期间传递了信号，且系统调用将被重启。

**[`EWOULDBLOCK`]** 给定了非零超时且超时已到期。

## 锁

如果在 `flags` 参数中向 `lockmgr` 或 `lockmgr_rw` 传递 `LK_INTERLOCK`，则在调用 `lockmgr` 或 `lockmgr_rw` 之前必须持有 `ilk`，并在返回时解锁。

失败的升级尝试会导致当前持有的锁丢失。此外，升级独占锁是无效的，尝试这样做将导致 [panic(9)](panic.9.md)。

## 参见

[witness(4)](../man4/witness.4.md), [condvar(9)](condvar.9.md), [locking(9)](locking.9.md), mtx_assert(9), [mutex(9)](mutex.9.md), [panic(9)](panic.9.md), [rwlock(9)](rwlock.9.md), [sleep(9)](sleep.9.md), [sx(9)](sx.9.md), [VOP_PRINT(9)](vop_print.9.md)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
