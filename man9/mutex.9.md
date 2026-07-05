# mutex.9.md

`mutex` — 内核同步原语

## 名称

`mutex`, `mtx_init`, `mtx_destroy`, `mtx_lock`, `mtx_lock_spin`, `mtx_lock_flags`, `mtx_lock_spin_flags`, `mtx_trylock`, `mtx_trylock_flags`, `mtx_trylock_spin`, `mtx_trylock_spin_flags`, `mtx_unlock`, `mtx_unlock_spin`, `mtx_unlock_flags`, `mtx_unlock_spin_flags`, `mtx_sleep`, `mtx_initialized`, `mtx_owned`, `mtx_recursed`, `mtx_assert`, `MTX_SYSINIT`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/lock.h>
```

```c
#include <sys/mutex.h>
```

```c
void
mtx_init(struct mtx *mutex, const char *name, const char *type, int opts)

void
mtx_destroy(struct mtx *mutex)

void
mtx_lock(struct mtx *mutex)

void
mtx_lock_spin(struct mtx *mutex)

void
mtx_lock_flags(struct mtx *mutex, int flags)

void
mtx_lock_spin_flags(struct mtx *mutex, int flags)

int
mtx_trylock(struct mtx *mutex)

int
mtx_trylock_flags(struct mtx *mutex, int flags)

int
mtx_trylock_spin(struct mtx *mutex)

int
mtx_trylock_spin_flags(struct mtx *mutex, int flags)

void
mtx_unlock(struct mtx *mutex)

void
mtx_unlock_spin(struct mtx *mutex)

void
mtx_unlock_flags(struct mtx *mutex, int flags)

void
mtx_unlock_spin_flags(struct mtx *mutex, int flags)

int
mtx_sleep(void *chan, struct mtx *mtx, int priority, const char *wmesg, int timo)

int
mtx_initialized(const struct mtx *mutex)

int
mtx_owned(const struct mtx *mutex)

int
mtx_recursed(const struct mtx *mutex)
```

```c
options INVARIANTS
options INVARIANT_SUPPORT

void
mtx_assert(const struct mtx *mutex, int what)
```

```c
#include <sys/kernel.h>
```

```c
MTX_SYSINIT(name, struct mtx *mtx, const char *description, int opts)
```

## 描述

互斥锁是线程同步的最基本、最主要的方法。互斥锁的主要设计考量包括：

- 获取和释放无竞争的互斥锁应尽可能廉价。
- 它们必须具有支持优先级传播所需的信息和存储空间。
- 线程必须能够递归获取互斥锁，前提是该互斥锁已初始化为支持递归。

目前有两种类型的互斥锁：在阻塞时进行上下文切换的和不进行上下文切换的。

默认情况下，`MTX_DEF` 互斥锁在已被持有时会进行上下文切换。作为一种优化，它们可以在上下文切换之前自旋一段时间。重要的是要记住，由于线程可能随时被抢占，获取互斥锁可能引入的上下文切换保证不会破坏任何尚未损坏的内容。

不进行上下文切换的互斥锁是 `MTX_SPIN` 互斥锁。这些互斥锁只应用于保护与主中断代码共享的数据。这包括中断过滤器和低层调度代码。在所有架构上，获取和释放无竞争的自旋互斥锁都比非自旋互斥锁上的相同操作更昂贵。为了保护中断服务例程不被自身阻塞，在持有自旋锁时，处理器上的所有中断都会被阻塞或延迟。允许持有多个自旋互斥锁。

一旦获取了自旋互斥锁，就不允许再获取阻塞型互斥锁。

实现互斥锁所需的存储空间由 `struct mtx` 提供。一般来说，应将其视为不透明对象，仅通过互斥锁原语来引用。

`mtx_init` 函数必须用于初始化互斥锁，然后才能将其传递给任何其他互斥锁函数。`name` 选项用于在调试输出等中标识该锁。`type` 选项由 witness 代码用于在检查锁排序时对互斥锁进行分类。如果 `type` 为 `NULL`，则使用 `name` 代替。作为 `name` 和 `type` 传入的是指针而非其所指向的数据，会被保存下来。所指向的数据必须保持稳定，直到互斥锁被销毁。`opts` 参数用于设置互斥锁的类型。它可以包含 `MTX_DEF` 或 `MTX_SPIN`，但不能同时包含两者。如果内核编译时启用了 `option INVARIANTS`，`mtx_init` 会断言 `mutex` 没有在没有中间调用 `mtx_destroy` 的情况下被多次初始化，除非指定了 `MTX_NEW` 选项。其他初始化选项见下文。

`mtx_lock` 函数代表当前运行的内核线程获取 `MTX_DEF` 互斥锁。如果另一个内核线程持有该互斥锁，调用者将从 CPU 上断开，直到互斥锁可用（即它将阻塞）。

`mtx_lock_spin` 函数代表当前运行的内核线程获取 `MTX_SPIN` 互斥锁。如果另一个内核线程持有该互斥锁，调用者将自旋直到互斥锁可用。自旋期间中断被禁用，并且在获取锁后保持禁用状态。

只要在互斥锁初始化期间向 `mtx_init` 传递了 `MTX_RECURSE` 位，同一个线程就可以递归获取互斥锁而不会产生不良影响。

`mtx_lock_flags` 和 `mtx_lock_spin_flags` 函数分别获取 `MTX_DEF` 或 `MTX_SPIN` 锁，并且还接受 `flags` 参数。在这两种情况下，目前可用于锁获取的唯一标志是 `MTX_QUIET` 和 `MTX_RECURSE`。如果在 `flags` 参数中设置了 `MTX_QUIET` 位，则在进行 `KTR_LOCK` 跟踪时，锁获取期间的跟踪将被静默。如果在 `flags` 参数中设置了 `MTX_RECURSE` 位，则该互斥锁可以被递归获取。

`mtx_trylock` 和 `mtx_trylock_spin` 函数尝试获取由 `mutex` 指向的 `MTX_DEF` 或 `MTX_SPIN` 互斥锁。如果无法立即获取互斥锁，函数将返回 0，否则将获取互斥锁并返回非零值。

`mtx_trylock_flags` 和 `mtx_trylock_spin_flags` 函数的行为分别与 `mtx_trylock` 和 `mtx_trylock_spin` 相同，但应在调用者希望传入 `flags` 值时使用。目前，`mtx_trylock` 和 `mtx_trylock_spin` 情况下唯一有效的值是 `MTX_QUIET`，其效果与上述 `mtx_lock` 中描述的相同。

`mtx_unlock` 函数释放 `MTX_DEF` 互斥锁。如果有更高优先级的线程正在等待该互斥锁，当前线程可能被抢占。

`mtx_unlock_spin` 函数释放 `MTX_SPIN` 互斥锁。

`mtx_unlock_flags` 和 `mtx_unlock_spin_flags` 函数的行为与上述标准互斥锁解锁例程完全相同，同时允许接受可能指定 `MTX_QUIET` 的 `flags` 参数。`MTX_QUIET` 的行为与互斥锁加锁例程中的行为相同。

`mtx_destroy` 函数用于销毁 `mutex`，以便可以释放或以其他方式覆盖与之关联的数据。任何被销毁的互斥锁必须先前已用 `mtx_init` 初始化。销毁互斥锁时允许存在单个持有计数。销毁互斥锁时不允许递归持有，也不允许有另一个线程在该互斥锁上阻塞。

`mtx_sleep` 函数用于在等待事件时原子性地释放 `mtx`。有关该函数参数的更多细节，参见 [sleep(9)](sleep.9.md)。

`mtx_initialized` 函数在 `mutex` 已初始化时返回非零值，否则返回零。

`mtx_owned` 函数在当前线程持有 `mutex` 时返回非零值。如果当前线程不持有 `mutex`，则返回零。

`mtx_recursed` 函数在 `mutex` 处于递归状态时返回非零值。只有在运行线程已拥有 `mutex` 时才应进行此检查。

`mtx_assert` 函数允许对 `mutex` 进行 `what` 中指定的断言。如果断言不为真，且内核编译时启用了 `options INVARIANTS` 和 `options INVARIANT_SUPPORT`，内核将 panic。目前支持以下断言：

**`MA_OWNED`** 断言当前线程持有第一个参数所指向的互斥锁。

**`MA_NOTOWNED`** 断言当前线程不持有第一个参数所指向的互斥锁。

**`MA_RECURSED`** 断言当前线程已对第一个参数所指向的互斥锁递归。此断言仅在与 `MA_OWNED` 结合使用时有效。

**`MA_NOTRECURSED`** 断言当前线程未对第一个参数所指向的互斥锁递归。此断言仅在与 `MA_OWNED` 结合使用时有效。

`MTX_SYSINIT` 宏用于在系统启动时生成对 `mtx_sysinit` 例程的调用，以初始化给定的互斥锁。参数与 `mtx_init` 相同，但多了一个附加参数 `name`，用于为与锁和 sysinit 例程关联的相关结构生成唯一的变量名。

### 默认互斥锁类型

大多数内核代码应使用默认锁类型 `MTX_DEF`。默认锁类型在锁已被另一个线程持有时允许线程从 CPU 上断开。在某些情况下，实现可以将锁视为短期自旋锁。然而，在中断线程中使用这些形式的锁总是安全的，不必担心与同一 CPU 上被中断的线程发生死锁。

### 自旋互斥锁类型

`MTX_SPIN` 互斥锁在无法立即获得所请求的锁时不会放弃 CPU，而是循环等待互斥锁被另一个 CPU 释放。如果另一个线程中断了持有互斥锁的线程，然后试图获取该互斥锁，则可能导致死锁。因此，自旋锁会在本地 CPU 上禁用所有中断。

自旋锁是相当特殊的锁，旨在持有非常短的时间。它们的主要目的是保护实现其他同步原语（如默认互斥锁、线程调度和中断线程）的代码部分。

### 初始化选项

传递给 `mtx_init` 的 `opts` 参数中的选项指定互斥锁类型。`MTX_DEF` 或 `MTX_SPIN` 选项之一是必需的，且只能指定这两个选项中的一个。可能的选项有：

**`MTX_DEF`** 默认互斥锁将始终允许当前线程被挂起，以避免与中断线程发生死锁情况。此锁类型的实现可能会在挂起当前线程之前自旋一段时间。

**`MTX_SPIN`** 自旋互斥锁永远不会放弃 CPU。在持有任何自旋锁时，本地 CPU 上的所有中断都被禁用。

**`MTX_RECURSE`** 指定初始化的互斥锁允许递归。如果允许互斥锁递归，则必须存在此位。注意，`mtx_trylock` 和 `mtx_trylock_spin` 都不支持递归；也就是说，尝试获取已拥有的互斥锁会失败。

**`MTX_QUIET`** 不记录此锁的任何互斥锁操作。

**`MTX_NOWITNESS`** 指示 [witness(4)](../man4/witness.4.md) 忽略此锁。

**`MTX_DUPOK`** Witness 不应记录获取重复锁的消息。

**`MTX_NOPROFILE`** 不对此锁进行性能分析。

**`MTX_NEW`** 不检查重复初始化。

### 加锁和解锁标志

传递给 `mtx_lock_flags`、`mtx_lock_spin_flags`、`mtx_unlock_flags` 和 `mtx_unlock_spin_flags` 函数的标志向调用者提供一些基本选项，通常仅在特殊情况下用于修改加锁或解锁行为。标准加锁和解锁应使用 `mtx_lock`、`mtx_lock_spin`、`mtx_unlock` 和 `mtx_unlock_spin` 函数。只有在需要某个标志时，才应使用相应的接受标志的例程。

修改互斥锁行为的选项：

**`MTX_QUIET`** 此选项用于在单个互斥锁操作期间静默日志消息。可用于在调试时削减多余的日志消息。

### Giant

如果必须获取 `Giant`，必须在获取其他互斥锁之前获取。换言之：在持有另一个互斥锁时无法非递归地获取 `Giant`。在持有 `Giant` 时可以获取其他互斥锁，在持有其他互斥锁时也可以递归获取 `Giant`。

### 睡眠

在持有互斥锁（`Giant` 除外）时睡眠从不安全，应予以避免。如果尝试这样做，会有许多断言失败。

### 访问用户空间内存的函数

在访问用户空间内存的函数（如 copyin(9)、copyout(9)、uiomove(9)、fuword(9) 等）之间不应持有任何互斥锁（`Giant` 除外）。调用这些函数时不需要任何锁。

## 参见

[condvar(9)](condvar.9.md), [LOCK_PROFILING(9)](LOCK_PROFILING.9.md), [locking(9)](locking.9.md), [mtx_pool(9)](mtx_pool.9.md), [panic(9)](panic.9.md), [rwlock(9)](rwlock.9.md), [sema(9)](sema.9.md), [sleep(9)](sleep.9.md), [sx(9)](sx.9.md)

## 历史

这些函数出现于 BSD/OS 和 FreeBSD 5.0。`mtx_trylock_spin` 函数在 FreeBSD 11.1 中添加。
