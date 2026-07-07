# sx(9)

`sx` — 内核共享/独占锁

## 名称

`sx`, `sx_init`, `sx_init_flags`, `sx_destroy`, `sx_slock`, `sx_xlock`, `sx_slock_sig`, `sx_xlock_sig`, `sx_try_slock`, `sx_try_xlock`, `sx_sunlock`, `sx_xunlock`, `sx_unlock`, `sx_try_upgrade`, `sx_downgrade`, `sx_sleep`, `sx_xholder`, `sx_xlocked`, `sx_has_waiters`, `sx_assert`, `SX_SYSINIT`, `SX_SYSINIT_FLAGS`

## 概要

```c
#include <sys/param.h>
#include <sys/lock.h>
#include <sys/sx.h>

void
sx_init(struct sx *sx, const char *description)

void
sx_init_flags(struct sx *sx, const char *description, int opts)

void
sx_destroy(struct sx *sx)

void
sx_slock(struct sx *sx)

void
sx_xlock(struct sx *sx)

int
sx_slock_sig(struct sx *sx)

int
sx_xlock_sig(struct sx *sx)

int
sx_try_slock(struct sx *sx)

int
sx_try_xlock(struct sx *sx)

void
sx_sunlock(struct sx *sx)

void
sx_xunlock(struct sx *sx)

void
sx_unlock(struct sx *sx)

int
sx_try_upgrade(struct sx *sx)

void
sx_downgrade(struct sx *sx)

int
sx_sleep(void *chan, struct sx *sx, int priority, const char *wmesg,
    int timo)

struct thread *
sx_xholder(struct sx *sx)

int
sx_xlocked(const struct sx *sx)

int
sx_has_waiters(const struct sx *sx)
```

```c
options INVARIANTS
options INVARIANT_SUPPORT

void
sx_assert(const struct sx *sx, int what)
```

```c
#include <sys/kernel.h>

SX_SYSINIT(name, struct sx *sx, const char *desc)
SX_SYSINIT_FLAGS(name, struct sx *sx, const char *desc, int flags)
```

## 描述

共享/独占锁用于保护读取远多于写入的数据。共享/独占锁不像互斥体和读写锁那样实现优先级传播以防止优先级反转，因此应谨慎使用共享/独占锁。

共享/独占锁通过 `sx_init` 或 `sx_init_flags` 创建，其中 `sx` 是指向 `struct sx` 空间的指针，`description` 是指向描述共享/独占锁的以空字符结尾字符串的指针。`sx_init_flags` 的 `opts` 参数指定一组可选标志以更改 `sx` 的行为。它包含以下一个或多个标志：

**`SX_DUPOK`** Witness 不应记录有关获取重复锁的消息。

**`SX_NOWITNESS`** 指示 [witness(4)](../man4/witness.4.md) 忽略此锁。

**`SX_NOPROFILE`** 不分析此锁。

**`SX_RECURSE`** 允许线程递归获取 `sx` 的独占锁。

**`SX_QUIET`** 不通过 [ktr(4)](../man4/ktr.4.md) 记录此锁的任何操作。

**`SX_NEW`** 如果内核编译时使用了 `options INVARIANTS`，除非指定此选项，否则 `sx_init` 将断言 `sx` 没有在没有调用 `sx_destroy` 的情况下多次初始化。

共享/独占锁通过 `sx_destroy` 销毁。锁 `sx` 在销毁时不能被任何线程锁定。

线程通过调用 `sx_slock`、`sx_slock_sig` 或 `sx_try_slock` 以及 `sx_sunlock` 或 `sx_unlock` 获取和释放共享锁。线程通过调用 `sx_xlock`、`sx_xlock_sig` 或 `sx_try_xlock` 以及 `sx_xunlock` 或 `sx_unlock` 获取和释放独占锁。线程可以通过调用 `sx_try_upgrade` 尝试将当前持有的共享锁升级为独占锁。持有独占锁的线程可以通过调用 `sx_downgrade` 将其降级为共享锁。

`sx_try_slock` 和 `sx_try_xlock` 在无法立即获取共享/独占锁时返回 0；否则将获取共享/独占锁并返回非零值。

`sx_try_upgrade` 在无法立即将共享锁升级为独占锁时返回 0；否则将获取独占锁并返回非零值。

`sx_slock_sig` 和 `sx_xlock_sig` 与其正常版本相同，但执行可中断睡眠。如果睡眠被信号或中断中断，则返回非零值，否则返回 0。

线程可以通过调用 `sx_sleep` 在等待事件时原子地释放共享/独占锁。有关此函数参数的更多细节，参见 [sleep(9)](sleep.9.md)。

当编译时使用 `options INVARIANTS` 和 `options INVARIANT_SUPPORT` 时，`sx_assert` 函数测试 `sx` 是否满足 `what` 中指定的断言，如果不满足则 panic。必须指定以下断言之一：

**`SA_LOCKED`** 断言当前线程对第一个参数指向的 `sx` 锁持有共享或独占锁。

**`SA_SLOCKED`** 断言当前线程对第一个参数指向的 `sx` 锁持有共享锁。

**`SA_XLOCKED`** 断言当前线程对第一个参数指向的 `sx` 锁持有独占锁。

**`SA_UNLOCKED`** 断言当前线程对第一个参数指向的 `sx` 锁没有持有锁。

此外，以下可选断言之一可以与 `SA_LOCKED`、`SA_SLOCKED` 或 `SA_XLOCKED` 断言一起包含：

**`SA_RECURSED`** 断言当前线程对 `sx` 持有递归锁。

**`SA_NOTRECURSED`** 断言当前线程对 `sx` 没有持有递归锁。

`sx_xholder` 将返回指向当前对 `sx` 持有独占锁的线程的指针。如果没有线程对 `sx` 持有独占锁，则返回 `NULL`。

`sx_xlocked` 在当前线程持有独占锁时返回非零值；否则返回零。

`sx_has_waiters` 在有线程等待此锁时返回非零值；否则返回零。该函数假设（但不断言）调用者已持有锁，且对其他线程等待其释放锁感兴趣。

为便于编程，`sx_unlock` 作为相应函数 `sx_sunlock` 和 `sx_xunlock` 的宏前端提供。知道锁处于何种状态的算法应使用两个特定函数之一以获得轻微的性能优势。

`SX_SYSINIT` 宏用于在系统启动时生成对 `sx_sysinit` 例程的调用，以初始化给定的 `sx` 锁。参数与 `sx_init` 相同，但有一个额外参数 `name`，用于为与锁和 sysinit 例程关联的相关结构生成唯一变量名。`SX_SYSINIT_FLAGS` 宏可类似地用于使用 `sx_init_flags` 初始化给定的 `sx` 锁。

线程不能同时对同一锁持有共享锁和独占锁；尝试这样做将导致死锁。

## 上下文

线程可以在睡眠时对 `SX_SYSINIT_FLAGS` 锁持有共享或独占锁。因此，不能在持有互斥体时获取 `SX_SYSINIT_FLAGS` 锁。否则，如果一个线程在持有 `SX_SYSINIT_FLAGS` 锁时睡眠，而另一个线程在获取互斥体后在同一 `SX_SYSINIT_FLAGS` 锁上阻塞，则第二个线程实际上最终会在持有互斥体时睡眠，这是不允许的。

## 参见

[lock(9)](lock.9.md), [locking(9)](locking.9.md), [mutex(9)](mutex.9.md), [panic(9)](panic.9.md), [rwlock(9)](rwlock.9.md), [sema(9)](sema.9.md)

## 缺陷

没有 `WITNESS` 的内核无法断言当前线程是否持有共享锁。`SA_LOCKED` 和 `SA_SLOCKED` 只能断言*任何*线程持有共享锁。它们不能确保当前线程持有共享锁。此外，`SA_UNLOCKED` 只能断言当前线程不持有独占锁。
