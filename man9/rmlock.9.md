# rmlock(9)

`rmlock` — 内核读/写锁，针对以读为主的访问模式进行了优化

## 名称

`rmlock`, `rm_init`, `rm_init_flags`, `rm_destroy`, `rm_rlock`, `rm_try_rlock`, `rm_wlock`, `rm_runlock`, `rm_wunlock`, `rm_wowned`, `rm_sleep`, `rm_assert`, `RM_SYSINIT`, `RM_SYSINIT_FLAGS`, `rms_init`, `rms_destroy`, `rms_rlock`, `rms_wlock`, `rms_runlock`, `rms_wunlock`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/lock.h>
```

```c
#include <sys/rmlock.h>
```

```c
void
rm_init(struct rmlock *rm, const char *name)

void
rm_init_flags(struct rmlock *rm, const char *name, int opts)

void
rm_destroy(struct rmlock *rm)

void
rm_rlock(struct rmlock *rm, struct rm_priotracker *tracker)

int
rm_try_rlock(struct rmlock *rm, struct rm_priotracker *tracker)

void
rm_wlock(struct rmlock *rm)

void
rm_runlock(struct rmlock *rm, struct rm_priotracker *tracker)

void
rm_wunlock(struct rmlock *rm)

int
rm_wowned(const struct rmlock *rm)

int
rm_sleep(void *wchan, struct rmlock *rm, int priority, const char *wmesg, int timo)
```

```c
options INVARIANTS
options INVARIANT_SUPPORT

void
rm_assert(struct rmlock *rm, int what)
```

```c
#include <sys/kernel.h>
```

```c
RM_SYSINIT(name, struct rmlock *rm, const char *desc)
RM_SYSINIT_FLAGS(name, struct rmlock *rm, const char *desc, int flags)

void
rms_init(struct rmslock *rms, const char *name)

void
rms_destroy(struct rmslock *rms)

void
rms_rlock(struct rmslock *rms)

void
rms_wlock(struct rmslock *rms)

void
rms_runlock(struct rmslock *rms)

void
rms_wunlock(struct rmslock *rms)
```

## 描述

读优先锁（read-mostly lock）允许多个线程共享访问受保护的数据，或单个线程独占访问。具有共享访问权限的线程被称为*读者*，因为它们只读取受保护的数据。具有独占访问权限的线程被称为*写者*，因为它可以修改受保护的数据。

读优先锁的设计目标是高效处理几乎只用作读者锁的锁，因此应用于保护很少变更的数据。在锁已被共享锁定后获取独占锁是一项开销很大的操作。

普通的读优先锁类似于 [rwlock(9)](rwlock.9.md) 锁，并遵循与 [rwlock(9)](rwlock.9.md) 锁相同的加锁顺序规则。读优先锁具有与互斥锁类似的完整优先级传播。与 [rwlock(9)](rwlock.9.md) 不同的是，读优先锁会向读者和写者都传播优先级。这是通过传递给 `rm_rlock` 和 `rm_runlock` 的 `rm_priotracker` 结构参数实现的。如果锁以 `RM_RECURSE` 选项初始化，读者可以递归加锁；但写者永远不允许递归。

通过向 `rm_init_flags` 传递 `RM_SLEEPABLE` 标志，可以允许写者睡眠。这会将加锁顺序规则更改为与 [sx(9)](sx.9.md) 锁相同。此类锁不会向写者传播优先级，但会向读者传播优先级。注意，无论该标志如何设置，读者都不允许睡眠。

可睡眠的读优先锁（通过 `rms_init` 创建）允许读者和写者都睡眠，但不会向任何一方传播优先级。它们遵循 [sx(9)](sx.9.md) 的加锁顺序。

### 宏和函数

**`RM_NOWITNESS`** 指示 [witness(4)](../man4/witness.4.md) 忽略此锁。

**`RM_RECURSE`** 允许线程递归获取 `rm` 的共享锁。

**`RM_SLEEPABLE`** 创建可睡眠的读优先锁。

**`RM_NEW`** 如果内核编译时启用了 `option INVARIANTS`，`rm_init_flags` 会断言 `rm` 未在前一次调用 `rm_destroy` 之前被多次初始化，除非指定了此选项。

**`RM_DUPOK`** [witness(4)](../man4/witness.4.md) 不应记录获取重复锁的消息。

**`RA_LOCKED`** 断言当前线程持有 `rm` 的共享锁或独占锁。

**`RA_RLOCKED`** 断言当前线程持有 `rm` 的共享锁。

**`RA_WLOCKED`** 断言当前线程持有 `rm` 的独占锁。

**`RA_UNLOCKED`** 断言当前线程既不持有 `rm` 的共享锁，也不持有独占锁。

**`RA_RECURSED`** 断言当前线程持有 `rm` 的递归锁。

**`RA_NOTRECURSED`** 断言当前线程不持有 `rm` 的递归锁。

**`rm_init(struct rmlock *rm, const char *name)`** 初始化读优先锁 `rm`。`name` 描述仅用于调试目的。在对此锁执行任何其他操作之前，必须调用此函数。

**`rm_init_flags(struct rmlock *rm, const char *name, int opts)`** 类似于 `rm_init`，使用一组可选标志初始化读优先锁 `rm`。`opts` 参数包含以下一个或多个标志：

**`rm_rlock(struct rmlock *rm, struct rm_priotracker *tracker)`** 以读者身份锁定 `rm`，使用 `tracker` 跟踪锁的读者所有者以进行优先级传播。此数据结构仅由 `rms_wunlock` 内部使用，必须持续存在直到调用 `rm_runlock`。由于读者不能睡眠，此数据结构可以在栈上分配。如果有线程独占持有此锁，当前线程将阻塞，其优先级会传播给独占持有者。如果锁以 `RM_RECURSE` 选项初始化，则当当前线程已获取 `rm` 的读者访问权限时，仍可调用 `rm_rlock`。

**`rm_try_rlock(struct rmlock *rm, struct rm_priotracker *tracker)`** 尝试以读者身份锁定 `rm`。如果无法立即获取锁，`rm_try_rlock` 将返回 0；否则将获取锁并返回非零值。注意，即使锁当前未被写者持有，`rm_try_rlock` 也可能失败。如果锁以 `RM_RECURSE` 选项初始化，当当前线程已获取读者访问权限时，`rm_try_rlock` 将成功。

**`rm_wlock(struct rmlock *rm)`** 以写者身份锁定 `rm`。如果有任何共享持有者，当前线程将阻塞。`rm_wlock` 不能递归调用。

**`rm_runlock(struct rmlock *rm, struct rm_priotracker *tracker)`** 此函数释放先前由 `rm_rlock` 获取的共享锁。`tracker` 参数必须与获取共享锁时使用的 `tracker` 参数匹配。

**`rm_wunlock(struct rmlock *rm)`** 此函数释放先前由 `rm_wlock` 获取的独占锁。

**`rm_destroy(struct rmlock *rm)`** 此函数销毁先前由 `rm_init` 初始化的锁。`rm` 锁必须处于未锁定状态。

**`rm_wowned(const struct rmlock *rm)`** 如果当前线程拥有 `rm` 的独占锁，此函数返回非零值。

**`rm_sleep(void *wchan, struct rmlock *rm, int priority, const char *wmesg, int timo)`** 此函数在等待事件时原子性地释放 `rm`。`rm` 锁必须以独占方式持有。有关此函数参数的更多详情，请参见 [sleep(9)](sleep.9.md)。

**`rm_assert(struct rmlock *rm, int what)`** 此函数断言 `rm` 锁处于 `what` 所指定的状态。如果断言不成立，且内核编译时启用了 `options INVARIANTS` 和 `options INVARIANT_SUPPORT`，内核将发生 panic。当前支持以下基本断言：此外，可与 `RA_LOCKED`、`RA_RLOCKED` 或 `RA_WLOCKED` 一起指定以下可选标志之一：

**`rms_init(struct rmslock *rms, const char *name)`** 初始化可睡眠的读优先锁 `rms`。`name` 描述用作 msleep(9) 例程的 `wmesg` 参数。在对此锁执行任何其他操作之前，必须调用此函数。

**`rms_rlock(struct rmlock *rm)`** 以读者身份锁定 `rms`。如果有线程独占持有此锁，当前线程将阻塞。

**`rms_wlock(struct rmslock *rms)`** 以写者身份锁定 `rms`。如果锁已被占用，当前线程将阻塞。`rms_wlock` 不能递归调用。

**`rms_runlock(struct rmslock *rms)`** 此函数释放先前由 `rms_rlock` 获取的共享锁。

**`rms_wunlock(struct rmslock *rms)`** 此函数释放先前由 `rms_wlock` 获取的独占锁。

**`rms_destroy(struct rmslock *rms)`** 此函数销毁先前由 `rms_init` 初始化的锁。`rms` 锁必须处于未锁定状态。

## 参见

[locking(9)](locking.9.md), [mutex(9)](mutex.9.md), [panic(9)](panic.9.md), [rwlock(9)](rwlock.9.md), [sema(9)](sema.9.md), [sleep(9)](sleep.9.md), [sx(9)](sx.9.md)

## 历史

这些函数出现在 FreeBSD 7.0 中。

## 作者

`rms_wunlock` 设施由 Stephan Uphoff 编写。本手册页面由 Gleb Smirnoff 为 rwlock 编写，并由 Stephan Uphoff 修改以反映 rmlock。

## 缺陷

`rms_wunlock` 的实现当前未针对单处理器系统进行优化。

当没有写者时，`rm_try_rlock` 也可能瞬时失败，此时另一个读者正在本地 CPU 上更新状态。

`rms_wunlock` 的实现使用系统中所有 rmlock 共享的单个每 CPU 列表。如果 rmlock 变得流行，可能需要散列到多个每 CPU 队列以加速写者锁过程。
