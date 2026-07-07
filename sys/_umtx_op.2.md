# _umtx_op(2)

`_umtx_op` — 用户空间线程同步原语实现的接口

## 名称

`_umtx_op`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/umtx.h>`

```c
int
_umtx_op(void *obj, int op, u_long val, void *uaddr,
    void *uaddr2);
```

## 描述

`_umtx_op()` 系统调用为用户空间实现线程同步原语提供内核支持。Lb libthr 使用该系统调用来实现 IEEE Std 1003.1-2001 ("POSIX.1") pthread 锁，如互斥锁、条件变量等。

### 结构

由 `_umtx_op()` 系统调用执行的操作作用于用户空间对象，这些对象由以下结构描述。保留字段和填充被省略。所有对象都要求符合 ABI 规定的对齐方式，但目前并非在所有架构上都一致地强制执行。

以下标志为所有结构的标志字段定义：

**`USYNC_PROCESS_SHARED`** 允许在无法立即授予锁所有权且操作必须睡眠时，为线程睡眠容器选择进程共享的睡眠队列。根据包含该结构首字节的内存映射的属性来选择进程共享或进程私有的睡眠队列，参见 [mmap(2)](mmap.2.md)。否则，如果未指定该标志，则无论内存映射属性如何，都选择进程私有的睡眠队列，作为一种优化。有关睡眠队列的更多细节，请参见下文的 SLEEP QUEUES（睡眠队列）小节。

**Mutex**

```c
struct umutex {
        volatile lwpid_t m_owner;
        uint32_t         m_flags;
        uint32_t         m_ceilings[2];
        uintptr_t        m_rb_lnk;
};
```

`m_owner` 字段是实际的锁。在锁定状态下，它包含锁所有者的线程标识符；在未锁定时为零。最高位被设置表示锁上存在竞争。为特殊值定义了以下常量：

**`UMUTEX_UNOWNED`** 零，存储在未锁定锁中的值。

**`UMUTEX_CONTESTED`** 竞争指示符。

**`UMUTEX_RB_OWNERDEAD`** 拥有健壮互斥锁的线程已终止。该互斥锁处于未锁定状态。

**`UMUTEX_RB_NOTRECOV`** 健壮互斥锁处于不可恢复状态。在重新初始化之前无法锁定。

`m_flags` 字段除了通用标志外，还可以包含以下 umutex 特有的标志：

**`UMUTEX_PRIO_INHERIT`** 互斥锁实现 *优先级继承* 协议。

**`UMUTEX_PRIO_PROTECT`** 互斥锁实现 *优先级保护* 协议。

**`UMUTEX_ROBUST`** 互斥锁是健壮的，如下文 ROBUST UMUTEXES（健壮 UMUTEX）小节所述。

**`UMUTEX_NONCONSISTENT`** 健壮互斥锁处于瞬态非一致状态。内核不使用。

在本手册页中，未设置 `UMUTEX_PRIO_INHERIT` 和 `UMUTEX_PRIO_PROTECT` 标志的互斥锁称为普通互斥锁。每种类型的互斥锁（普通、优先级继承和优先级保护）都有与给定键关联的独立睡眠队列。对于优先级保护互斥锁，`m_ceilings` 数组包含优先级上限值。`m_ceilings[0]` 是互斥锁的上限值，如 IEEE Std 1003.1-2008 ("POSIX.1") 为 *优先级保护* 互斥锁协议所规定。`m_ceilings[1]` 仅用于优先级保护互斥锁的解锁，当解锁顺序与加锁顺序的逆序不同时。在这种情况下，`m_ceilings[1]` 必须包含最后锁定的优先级保护互斥锁的上限值，以便正确重新分配优先级。相反，如果正在解锁的互斥锁是该线程锁定的最后一个优先级传播互斥锁，则 `m_ceilings[1]` 应包含 -1。这是必需的，因为内核不维护有序的锁列表。

**条件变量**

```c
struct ucond {
        volatile uint32_t c_has_waiters;
        uint32_t          c_flags;
        uint32_t          c_clockid;
};
```

非零的 `c_has_waiters` 值表示该条件有内核内等待者，正在执行 `UMTX_OP_CV_WAIT` 请求。`c_flags` 字段包含标志。只有通用标志（`USYNC_PROCESS_SHARED`）是为 ucond 定义的。`c_clockid` 成员提供用于超时的时钟标识符，当 `UMTX_OP_CV_WAIT` 请求同时具有 `CVWAIT_CLOCKID` 标志和指定的超时时使用。有效的时钟标识符是 [clock_gettime(2)](clock_gettime.2.md) 的子集：

- `CLOCK_MONOTONIC`
- `CLOCK_MONOTONIC_FAST`
- `CLOCK_MONOTONIC_PRECISE`
- `CLOCK_PROF`
- `CLOCK_REALTIME`
- `CLOCK_REALTIME_FAST`
- `CLOCK_REALTIME_PRECISE`
- `CLOCK_SECOND`
- `CLOCK_TAI`
- `CLOCK_UPTIME`
- `CLOCK_UPTIME_FAST`
- `CLOCK_UPTIME_PRECISE`
- `CLOCK_VIRTUAL`

**读写锁**

```c
struct urwlock {
        volatile int32_t rw_state;
        uint32_t         rw_flags;
        uint32_t         rw_blocked_readers;
        uint32_t         rw_blocked_writers;
};
```

`rw_state` 字段是实际的锁。它既包含标志也包含已授予读锁的计数。`rw_state` 位的名称如下：

**`URWLOCK_WRITE_OWNER`** 已授予写锁。

**`URWLOCK_WRITE_WAITERS`** 存在写锁等待者。

**`URWLOCK_READ_WAITERS`** 存在读锁等待者。

**`URWLOCK_READER_COUNT(c)`** 返回当前已授予读锁的计数。

在任何给定时刻，`struct rwlock` 上只能有一个线程被授予写锁，且没有线程被授予读锁。或者，在给定时刻，最多可有 `URWLOCK_MAX_READERS` 个线程同时被授予读锁，但不向任何线程授予写锁。除了通用标志外，还为 `struct urwlock` 的 `rw_flags` 成员定义了以下标志：

**`URWLOCK_PREFER_READER`** 如果指定，当 `urwlock` 已被读锁定时，即使存在未满足的写锁请求，也立即授予读锁请求。默认情况下，如果存在写锁等待者，则不授予进一步的读请求，以防止写锁等待者被不公平地饿死。

`rw_blocked_readers` 和 `rw_blocked_writers` 成员包含在内核中睡眠、等待关联请求类型被授予的线程计数。这些字段由内核使用，用于在请求线程被唤醒后更新 `rw_state` 锁的 `URWLOCK_READ_WAITERS` 和 `URWLOCK_WRITE_WAITERS` 标志。

**信号量**

```c
struct _usem2 {
        volatile uint32_t _count;
        uint32_t          _flags;
};
```

`_count` 字表示一个计数信号量。非零值表示未锁定（已 post）的信号量，而零表示锁定状态。支持的最大信号量计数为 `USEM_MAX_COUNT`。`_count` 字除了 post（解锁）计数器外，还包含 `USEM_HAS_WAITERS` 位，指示锁定的信号量有等待线程。应用于 `_count` 字的 `USEM_COUNT()` 宏返回当前信号量计数器值，即对该信号量发出的 post 数量。除了通用标志外，为 `struct _usem2` 的 `_flags` 成员定义了以下位：

**`USEM_NAMED`** 该标志被内核忽略。

**超时参数**

```c
struct _umtx_time {
        struct timespec _timeout;
        uint32_t        _flags;
        uint32_t        _clockid;
};
```

若干 `_umtx_op()` 操作允许限制阻塞时间，如果请求无法在指定的时间段内满足则失败。超时通过将 `struct timespec` 或其扩展变体 `struct _umtx_time` 的地址作为 `_umtx_op()` 的 `uaddr2` 参数传递来指定。它们通过 `uaddr` 值来区分，该值必须等于 `uaddr2` 所指向结构的大小（转换为 `uintptr_t`）。`_timeout` 成员指定超时应发生的时间。时钟标识符 `_clockid` 的合法值与 [clock_gettime(2)](clock_gettime.2.md) 函数的 `clock_id` 参数共享，并使用相同的底层时钟。指定的时钟用于获取当前时间值。间隔计数始终由单调挂钟执行。`_flags` 参数允许以下标志进一步定义超时行为：

**`UMTX_ABSTIME`** `_timeout` 值是绝对时间。当指定的时钟值等于或超过 `_timeout` 时，线程将被解除阻塞且请求失败。如果该标志不存在，超时值是相对的，即从请求开始时刻起由单调挂钟测量的时间量。

### 睡眠队列

当锁定请求无法立即满足时，线程通常被置于 *睡眠* 状态，这是一种由 *唤醒* 操作终止的不可运行状态。锁操作包括一个 *try* 变体，如果无法获得锁则返回错误而非睡眠。此外，`_umtx_op()` 提供显式使线程睡眠的请求。

唤醒需要知道使哪些线程可运行，因此睡眠线程被分组到称为 *睡眠队列* 的容器中。睡眠队列由一个键标识，对于 `_umtx_op()`，该键定义为某个变量的物理地址。注意使用的是 *物理* 地址，这意味着同一变量被多次映射将给出一个键值。此机制使得构造 *进程共享* 锁成为可能。

键的一个相关属性是可共享性。某些请求始终将键解释为当前进程私有，即使内存是共享的，也创建作用域为当前进程的睡眠队列。其他请求要么根据映射属性自动选择可共享性，要么通过 `USYNC_PROCESS_SHARED` 通用标志接受额外输入。这是一种优化，允许无论后备内存的种类如何都限制锁的作用域。

只有指定为键的变量起始字节的地址对于确定对应的睡眠队列是重要的。变量的大小无关紧要，因此例如，在同一地址上解释为 `uint32_t` 和 `long` 的睡眠在小端 64 位平台上会发生冲突。

键的最后一个属性是对象类型。分配给睡眠线程的睡眠队列对于简单等待请求、互斥锁、读写锁、条件变量和其他原语是各自的独立队列，即使键的物理地址相同。

当从给定睡眠队列唤醒有限数量的线程时，选择在队列上被阻塞时间最长且优先级最高的线程。

### 健壮 UMUTEX

*健壮 umutex* 作为用户空间库实现 POSIX 健壮互斥锁的基础提供。健壮 umutex 必须设置 `UMUTEX_ROBUST` 标志。

在线程终止时，内核遍历两个互斥锁列表。这两个列表的头地址必须通过先前的 `UMTX_OP_ROBUST_LISTS` 请求调用提供。列表是单链的。到下一个元素的链接由 `struct umutex` 的 `m_rb_lnk` 成员提供。

如果内核发现具有以下任一条件的互斥锁，则健壮列表处理被中止：

- 未设置 `UMUTEX_ROBUST` 标志
- 非当前线程所有，除非互斥锁由为当前线程注册的 `struct umtx_robust_lists_params` 的 `robust_inactive` 成员指向
- 互斥锁标志组合无效
- 读取 umutex 内存时发生缺页
- 达到 [libthr(3)](../man3/libthr.3.md) 中描述的列表长度限制。

两个列表中的每个互斥锁都被解锁，如同对其执行 `UMTX_OP_MUTEX_UNLOCK` 请求，但 `m_owner` 字段写入的不是 `UMUTEX_UNOWNED` 值，而是 `UMUTEX_RB_OWNERDEAD` 值。当处于 `UMUTEX_RB_OWNERDEAD` 状态的互斥锁被内核由于 `UMTX_OP_MUTEX_TRYLOCK` 和 `UMTX_OP_MUTEX_LOCK` 请求而锁定时，授予锁并返回 `EOWNERDEAD` 错误。

此外，内核特殊处理 `m_owner` 字段的 `UMUTEX_RB_NOTRECOV` 值，对于锁尝试始终返回 `ENOTRECOVERABLE` 错误，不授予锁。

### 操作

以下操作由传递给函数的 `op` 参数请求实现：

**`UMTX_OP_WAIT`** 等待。该请求的参数为：

- `obj` 指向 `long` 类型变量的指针。
- `val` `*obj` 的当前值。

将 `obj` 参数所指向变量的当前值与 `val` 进行比较。如果它们相等，请求线程被置于可中断睡眠，直到被唤醒或可选指定的超时到期。比较和睡眠是原子执行的。换句话说，如果另一个线程向 `*obj` 写入新值然后发出 `UMTX_OP_WAKE`，请求保证不会错过唤醒，否则唤醒可能在比较和阻塞之间丢失。`*obj` 变量所在内存的物理地址用作索引睡眠线程的键。`*obj` 变量当前值的读取不受屏障保护。特别是，如果 `UMTX_OP_WAIT` 和 `UMTX_OP_WAKE` 请求被用作实现简单锁的基础，则用户有责任确保锁获取和释放的内存语义。该请求不可重启。在等待期间传递的未屏蔽信号始终导致睡眠中断和 `EINTR` 错误。可选地，可以为请求指定超时。

**`UMTX_OP_WAKE`** 唤醒可能因 `UMTX_OP_WAIT` 而睡眠的线程。该请求的参数为：

- `obj` 指向变量的指针，用作查找睡眠线程的键。
- `val` 此请求最多唤醒 `val` 个线程。指定 `INT_MAX` 以唤醒所有等待者。

**`UMTX_OP_MUTEX_TRYLOCK`** 尝试锁定 umutex。该请求的参数为：

- `obj` 指向 umutex 的指针。

操作与 `UMTX_OP_MUTEX_LOCK` 请求相同，但如果无法立即获得锁，则返回 `EBUSY` 而非睡眠。

**`UMTX_OP_MUTEX_LOCK`** 锁定 umutex。该请求的参数为：

- `obj` 指向 umutex 的指针。

通过将当前线程 ID 写入 `struct umutex` 的 `m_owner` 字来执行锁定。该写入是原子的，保留 `UMUTEX_CONTESTED` 竞争指示符，并为锁进入语义提供获取屏障。如果由于另一个线程拥有锁而无法立即获得锁，当前线程被置于睡眠，在此之前设置 `UMUTEX_CONTESTED` 位。唤醒后，重新测试锁条件。该请求遵循互斥锁的优先级保护或继承协议，分别由 `UMUTEX_PRIO_PROTECT` 或 `UMUTEX_PRIO_INHERIT` 标志指定。可选地，可以为请求指定超时。指定超时的请求不可重启。在等待期间传递的未屏蔽信号始终导致睡眠中断和 `EINTR` 错误。未指定超时的请求在从信号处理程序返回后始终重启。

**`UMTX_OP_MUTEX_UNLOCK`** 解锁 umutex。该请求的参数为：

- `obj` 指向 umutex 的指针。

通过将 `UMUTEX_UNOWNED`（零）值写入 `struct umutex` 的 `m_owner` 字来解锁互斥锁。该写入带有释放屏障，以提供锁离开语义。如果有线程在与 umutex 关联的睡眠队列中睡眠，则唤醒一个线程。如果有多个线程在睡眠队列中睡眠，则在将 `UMUTEX_UNOWNED` 值写入 `m_owner` 的同时设置 `UMUTEX_CONTESTED` 位。该请求遵循互斥锁的优先级保护或继承协议，分别由 `UMUTEX_PRIO_PROTECT` 或 `UMUTEX_PRIO_INHERIT` 标志指定。有关优先级保护协议互斥锁上请求操作的更多细节，请参见 `struct umutex` 结构的 `m_ceilings` 成员的描述。

**`UMTX_OP_SET_CEILING`** 为优先级保护 umutex 设置上限。该请求的参数为：

- `obj` 指向 umutex 的指针。
- `val` 新的上限值。
- `uaddr` `uint32_t` 类型变量的地址。如果不为 `NULL` 且更新成功，则先前的上限值被写入 `uaddr` 所指向的位置。

该请求锁定由 `obj` 参数指向的 umutex，如果无法立即获得则等待。获得锁后，新上限值 `val` 被写入 `struct umutex` 的 `m_ceilings[0]` 成员，之后 umutex 被解锁。锁定不遵循优先级保护协议，以符合 POSIX 对 pthread_mutex_setprioceiling(3) 接口的要求。

**`UMTX_OP_CV_WAIT`** 等待条件。该请求的参数为：

- `obj` 指向 `struct ucond` 的指针。
- `val` 请求标志，见下文。
- `uaddr` 指向 umutex 的指针。
- `uaddr2` 可选的指向 `struct timespec` 的指针，用于超时指定。

该请求必须由拥有 `uaddr` 参数所指向互斥锁的线程发出。由 `obj` 参数指向的 `struct ucond` 的 `c_hash_waiters` 成员被设置为任意非零值，之后 `uaddr` 互斥锁被解锁（遵循相应的协议），当前线程被置于以 `obj` 参数为键的睡眠队列上睡眠。这些操作是原子执行的。保证不会错过在互斥锁解锁和将当前线程置于睡眠队列之间发送的来自 `UMTX_OP_CV_SIGNAL` 或 `UMTX_OP_CV_BROADCAST` 的唤醒。唤醒时，如果超时已到期且同一睡眠队列上没有其他线程在睡眠，则清除 `c_hash_waiters` 成员。唤醒后，`uaddr` umutex 不会被重新锁定。定义了以下标志：

- `CVWAIT_ABSTIME` 超时是绝对时间。
- `CVWAIT_CLOCKID` 提供了时钟标识符。

可选地，可以为请求指定超时。与其他请求不同，超时值直接由 `uaddr2` 参数指向的 `struct timespec` 指定。如果提供了 `CVWAIT_CLOCKID` 标志，超时使用由 `obj` 参数指向的 `struct ucond` 的 `c_clockid` 成员中的时钟。否则，使用 `CLOCK_REALTIME`，无论 `struct _umtx_time` 中可能指定的时钟标识符如何。如果提供了 `CVWAIT_ABSTIME` 标志，超时指定绝对时间值，否则表示相对时间间隔。该请求不可重启。在等待期间传递的未屏蔽信号始终导致睡眠中断和 `EINTR` 错误。

**`UMTX_OP_CV_SIGNAL`** 唤醒一个条件等待者。该请求的参数为：

- `obj` 指向 `struct ucond` 的指针。

该请求最多唤醒一个在以 `obj` 参数为键的睡眠队列上睡眠的线程。如果被唤醒的线程是睡眠队列上的最后一个，则清除 `struct ucond` 的 `c_has_waiters` 成员。

**`UMTX_OP_CV_BROADCAST`** 唤醒所有条件等待者。该请求的参数为：

- `obj` 指向 `struct ucond` 的指针。

该请求唤醒所有在以 `obj` 参数为键的睡眠队列上睡眠的线程。清除 `struct ucond` 的 `c_has_waiters` 成员。
**`UMTX_OP_WAIT_UINT`** 与 `UMTX_OP_WAIT` 相同，但 `obj` 所指向变量的类型为 `u_int`（32 位整数）。

**`UMTX_OP_RW_RDLOCK`** 读锁定 `struct rwlock` 锁。该请求的参数为：

- `obj` 指向要读锁定的锁（类型为 `struct rwlock`）的指针。
- `val` 增强锁定行为的附加标志。`val` 参数中的有效标志为：`URWLOCK_PREFER_READER`。

该请求通过递增结构的 `rw_state` 字中的读者计数来获取指定 `struct rwlock` 上的读锁。如果 `rw_state` 字中设置了 `URWLOCK_WRITE_OWNER` 位，表示锁已授予一个尚未放弃其所有权的写者。在这种情况下，当前线程被置于睡眠直到值得重试。如果 `URWLOCK_PREFER_READER` 标志设置在结构的 `rw_flags` 字中或请求的 `val` 参数中，试图获取同一结构写锁的线程的存在不会阻止当前线程尝试获取读锁。否则，如果未设置该标志且 `rw_state` 中设置了 `URWLOCK_WRITE_WAITERS` 标志，当前线程不尝试获取读锁。相反，它在 `rw_state` 字中设置 `URWLOCK_READ_WAITERS` 并将自身置于对应的睡眠队列上睡眠。唤醒后，重新评估锁定条件。可选地，可以为请求指定超时。该请求不可重启。在等待期间传递的未屏蔽信号始终导致睡眠中断和 `EINTR` 错误。

**`UMTX_OP_RW_WRLOCK`** 写锁定 `struct rwlock` 锁。该请求的参数为：

- `obj` 指向要写锁定的锁（类型为 `struct rwlock`）的指针。

该请求通过在结构的 `rw_state` 字中设置 `URWLOCK_WRITE_OWNER` 位来获取指定 `struct rwlock` 上的写锁。如果已有写锁所有者（由 `URWLOCK_WRITE_OWNER` 位被设置指示），或存在读锁所有者（由读锁计数器指示），当前线程不尝试获取写锁。相反，它在 `rw_state` 字中设置 `URWLOCK_WRITE_WAITERS` 并将自身置于对应的睡眠队列上睡眠。唤醒后，重新评估锁定条件。可选地，可以为请求指定超时。该请求不可重启。在等待期间传递的未屏蔽信号始终导致睡眠中断和 `EINTR` 错误。

**`UMTX_OP_RW_UNLOCK`** 解锁 rwlock。该请求的参数为：

- `obj` 指向要解锁的锁（类型为 `struct rwlock`）的指针。

解锁类型（读或写）由当前锁状态决定。注意 `struct rwlock` 不保存有关获取锁的线程身份的信息。如果解锁后有挂起的写者，且 `*obj` 结构的 `rw_flags` 成员中未设置 `URWLOCK_PREFER_READER` 标志，则唤醒一个写者，其选择如 SLEEP QUEUES（睡眠队列）小节所述。如果设置了 `URWLOCK_PREFER_READER` 标志，则仅在没有挂起的读者时才唤醒挂起的写者。如果没有挂起的写者，或者在设置了 `URWLOCK_PREFER_READER` 标志的情况下，则解锁唤醒所有挂起的读者。

**`UMTX_OP_WAIT_UINT_PRIVATE`** 与 `UMTX_OP_WAIT_UINT` 相同，但无条件选择进程私有睡眠队列。

**`UMTX_OP_WAKE_PRIVATE`** 与 `UMTX_OP_WAKE` 相同，但无条件选择进程私有睡眠队列。

**`UMTX_OP_MUTEX_WAIT`** 等待互斥锁可用。该请求的参数为：

- `obj` 互斥锁的地址。

类似于 `UMTX_OP_MUTEX_LOCK`，如果无法立即获得互斥锁，则将请求线程置于睡眠。在线程被添加到睡眠队列之前，互斥锁的 `m_owner` 字中设置 `UMUTEX_CONTESTED` 位以指示存在等待者。与 `UMTX_OP_MUTEX_LOCK` 请求不同，不获取锁。该操作未针对优先级保护和优先级继承协议的互斥锁实现。可选地，可以为请求指定超时。指定超时的请求不可重启。在等待期间传递的未屏蔽信号始终导致睡眠中断和 `EINTR` 错误。未指定超时的请求在信号处置通过 `struct sigaction` 的 `sa_flags` 成员中的 `SA_RESTART` 标志请求重启时自动重启。

**`UMTX_OP_NWAKE_PRIVATE`** 唤醒一批睡眠线程。该请求的参数为：

- `obj` 指向指针数组的指针。
- `val` `obj` 所指向数组中的元素数量。

对于 `obj` 所指向数组中的每个元素，唤醒所有在 *私有* 睡眠队列上等待、键为该数组元素所寻址字节的线程。

**`UMTX_OP_MUTEX_WAKE`** 检查普通 umutex 是否已解锁并唤醒一个等待者。该请求的参数为：

- `obj` 指向 umutex 的指针。

如果 `obj` 参数所指向互斥锁的 `m_owner` 字指示互斥锁未锁定且其竞争指示符位 `UMUTEX_CONTESTED` 已设置，则清除该位并唤醒与 `obj` 所寻址字节关联的睡眠队列中的一个等待者（如果有）。该请求仅支持普通互斥锁。睡眠队列对于普通互斥锁类型始终是一个。此请求已弃用，推荐使用 `UMTX_OP_MUTEX_WAKE2`，因为使用它的互斥锁无法同步自身的销毁。也就是说，当发出此请求时，`m_owner` 字已被设置为 `UMUTEX_UNOWNED`，因此另一个线程可以锁定、解锁并销毁该互斥锁（如果之后没有其他线程使用该互斥锁）。清除 `UMUTEX_CONTESTED` 位可能随后修改已释放的内存。

**`UMTX_OP_MUTEX_WAKE2`** 检查 umutex 是否已解锁并唤醒一个等待者。该请求的参数为：

- `obj` 指向 umutex 的指针。
- `val` umutex 标志。

该请求不读取 `struct umutex` 的 `m_flags` 成员；相反，`val` 参数提供标志信息，特别是用于确定唤醒时找到等待者的睡眠队列。如果互斥锁未锁定，则唤醒一个等待者。如果无法访问互斥锁内存，则唤醒所有等待者。如果睡眠队列上有多个等待者，或只有一个等待者但互斥锁由某线程拥有，则在 `struct umutex` 的 `m_owner` 字中设置 `UMUTEX_CONTESTED` 位。

**`UMTX_OP_SEM2_WAIT`** 等待直到信号量可用。该请求的参数为：

- `obj` 指向信号量（类型为 `struct _usem2`）的指针。
- `uaddr` 通过 `uaddr2` 参数传入的内存大小。
- `uaddr2` 可选的指向 `struct _umtx_time` 类型结构的指针，其后可跟一个 `struct timespec` 类型的结构。

如果信号量计数器为零，则将请求线程置于睡眠队列。如果线程被置于睡眠，则在 `_count` 字中设置 `USEM_HAS_WAITERS` 位以指示存在等待者。函数由于 `_count` 指示信号量可用（因 post 而非零计数）或由于唤醒而返回。返回并不保证信号量可用，也不在成功返回时消费信号量锁。可选地，可以为请求指定超时。非绝对超时值的请求不可重启。在此类等待期间传递的未屏蔽信号导致睡眠中断和 `EINTR` 错误。如果未设置 `UMTX_ABSTIME`，且操作被中断且调用者传入的 `uaddr2` 足够大以容纳跟在初始 `struct _umtx_time` 之后的 `struct timespec`，则该 `struct timespec` 被更新为包含未睡眠的时长。

**`UMTX_OP_SEM2_WAKE`** 唤醒信号量锁上的等待者。该请求的参数为：

- `obj` 指向信号量（类型为 `struct _usem2`）的指针。

该请求唤醒信号量锁的一个等待者。函数不递增信号量锁计数。如果 `_count` 字中设置了 `USEM_HAS_WAITERS` 位，且最后一个睡眠线程被唤醒，则清除该位。

**`UMTX_OP_SHM`** 管理匿名 POSIX 共享内存对象（参见 [shm_open(2)](shm_open.2.md)），这些对象可以附加到映射到进程地址空间的物理内存字节上。这些对象用于在 `libthr` 中实现进程共享锁。`val` 参数指定 `UMTX_OP_SHM` 请求的子请求：

**`UMTX_SHM_CREAT`** 创建匿名共享内存对象，可以使用指定的键 `uaddr` 查找。如果与 `uaddr` 键关联的对象已存在，则返回该对象而非创建新对象。对象大小为一页。成功时返回引用该对象的文件描述符。该描述符可用于使用 [mmap(2)](mmap.2.md) 映射对象，或用于其他共享内存操作。

**`UMTX_SHM_LOOKUP`** 与 `UMTX_SHM_CREAT` 请求相同，但如果没有与指定键 `uaddr` 关联的共享内存对象，则返回错误，且不创建新对象。

**`UMTX_SHM_DESTROY`** 解除共享对象与指定键 `uaddr` 的关联。该对象在最后一个打开的文件描述符关闭且其最后一个映射被销毁后销毁。

**`UMTX_SHM_ALIVE`** 检查是否存在与提供的键 `uaddr` 关联的存活共享对象。如果存在则返回零，否则返回错误。此请求是 `UMTX_SHM_LOOKUP` 请求的优化。当仅询问关联对象的存活状态时更廉价，因为成功时不会在进程 fd 表中安装文件描述符。

`uaddr` 参数指定虚拟地址，其底层物理内存字节标识用作匿名共享对象创建或查找的键。

**`UMTX_OP_ROBUST_LISTS`** 为当前线程的健壮互斥锁列表注册列表头。该请求的参数为：

- `val` 在 `uaddr` 参数中传入的结构的大小。
- `uaddr` 指向 `struct umtx_robust_lists_params` 类型结构的指针。

该结构定义为：

```c
struct umtx_robust_lists_params {
        uintptr_t       robust_list_offset;
        uintptr_t       robust_priv_list_offset;
        uintptr_t       robust_inact_offset;
};
```

`robust_list_offset` 成员包含已锁定健壮共享互斥锁列表中第一个元素的地址。`robust_priv_list_offset` 成员包含已锁定健壮私有互斥锁列表中第一个元素的地址。私有和共享健壮锁定列表被分开，以允许在 fork 时在子进程中快速终止共享列表。`robust_inact_offset` 包含指向可能在不久的将来被锁定或可能刚刚被解锁的互斥锁的指针。它通常由锁或解锁互斥锁实现代码在整个操作周围设置，因为列表只能在线程拥有互斥锁时无竞争地更改。内核除了遍历共享和私有列表外，还检查 `robust_inact_offset`。此外，由 `robust_inact_offset` 指向的互斥锁在线程终止时的处理比列表上的其他互斥锁更宽松。允许该互斥锁不由当前线程拥有，在这种情况下继续列表处理。详情请参见 ROBUST UMUTEXES（健壮 UMUTEX）小节。

**`UMTX_OP_GET_MIN_TIMEOUT`** 将最小 umtx 操作超时的当前值（以纳秒为单位）写入 `uaddr1` 所指向的 long 整数变量。

**`UMTX_OP_SET_MIN_TIMEOUT`** 设置使用绝对时钟指定超时的 umtx 操作线程所需睡眠的最小时间量（以纳秒为单位）。该值取自调用的 `val` 参数。零表示无最小值。

`op` 参数可以是上述单个命令与以下一个或多个标志的按位或：

**`UMTX_OP__I386`** 从原生 `_umtx_op` 系统调用请求 i386 ABI 兼容性。具体而言，这意味着：

- 指向字的 `obj` 参数指向 32 位整数。
- `UMTX_OP_NWAKE_PRIVATE` 的 `obj` 参数是指向 32 位指针数组的指针。
- `struct umutex` 的 `m_rb_lnk` 成员是 32 位指针。
- `struct timespec` 使用 32 位 time_t。

如果设置了此标志，`UMTX_OP__32BIT` 无效。此标志对所有架构有效，但在 i386 上被忽略。

**`UMTX_OP__32BIT`** 从原生 `_umtx_op` 系统调用请求非 i386 的 32 位 ABI 兼容性。具体而言，这意味着：

- 指向字的 `obj` 参数指向 32 位整数。
- `UMTX_OP_NWAKE_PRIVATE` 的 `obj` 参数是指向 32 位指针数组的指针。
- `struct umutex` 的 `m_rb_lnk` 成员是 32 位指针。
- `struct timespec` 使用 64 位 time_t。

如果设置了 `UMTX_OP__I386`，此标志无效。此标志对所有架构有效。

注意，如果请求任何 32 位 ABI 兼容性，则必须小心处理健壮列表。单个线程不能混合 32 位兼容的健壮列表与原生健壮列表。给定线程中的第一次 `UMTX_OP_ROBUST_LISTS` 调用决定该线程今后用于健壮列表的 ABI。

## 返回值

如果成功，除 `UMTX_OP_SHM` 请求的 `UMTX_SHM_CREAT` 和 `UMTX_SHM_LOOKUP` 子请求外的所有请求将返回零。`UMTX_SHM_CREAT` 和 `UMTX_SHM_LOOKUP` 成功时返回共享内存文件描述符。出错时返回 -1，并设置 `errno` 变量以指示错误。

## 错误

`_umtx_op()` 操作可能因以下错误而失败：

**[`EFAULT`]** 某个参数指向无效内存。

**[`EINVAL`]** 为 `struct _umtx_time` 超时参数指定的时钟标识符，或 `struct ucond` 的 `c_clockid` 成员中的时钟标识符无效。

**[`EINVAL`]** 由 `struct umutex` 的 `m_flags` 成员编码的互斥锁类型无效。

**[`EINVAL`]** `struct umutex` 的 `m_owner` 成员在解锁期间更改了锁所有者线程标识符。

**[`EINVAL`]** `struct _umtx_time` 的 `timeout.tv_sec` 或 `timeout.tv_nsec` 成员小于零，或 `timeout.tv_nsec` 大于 1000000000。

**[`EINVAL`]** `op` 参数指定了无效操作。

**[`EINVAL`]** `UMTX_OP_SHM` 请求的 `uaddr` 参数指定了无效操作。

**[`EINVAL`]** `UMTX_OP_SET_CEILING` 请求指定了非优先级保护互斥锁。

**[`EINVAL`]** `UMTX_OP_SET_CEILING` 请求的新上限值，或在锁定或解锁操作期间从 `m_ceilings` 数组读取的一个或多个值，大于 `RTP_PRIO_MAX`。

**[`EPERM`]** 试图解锁非当前线程拥有的对象。

**[`EOWNERDEAD`]** 在 `m_owner` 字段设置为 `UMUTEX_RB_OWNERDEAD` 值（指示已终止的健壮互斥锁）的 umutex 上请求锁。锁被授予调用者，因此此错误实际上指示成功但带有附加条件。

**[`ENOTRECOVERABLE`]** 在 `m_owner` 字段等于 `UMUTEX_RB_NOTRECOV` 值（指示终止后被放弃的健壮互斥锁）的 umutex 上请求锁。锁未授予调用者。

**[`ENOTTY`]** 与传递给 `UMTX_OP_SHM` 请求的 `UMTX_SHM_ALIVE` 子请求的地址关联的共享内存对象已被销毁。

**[`ESRCH`]** 对于 `UMTX_OP_SHM` 请求的 `UMTX_SHM_LOOKUP`、`UMTX_SHM_DESTROY` 和 `UMTX_SHM_ALIVE` 子请求，没有与提供的键关联的共享内存对象。

**[`ENOMEM`]** `UMTX_OP_SHM` 请求的 `UMTX_SHM_CREAT` 子请求无法满足，因为共享内存对象的分配将超过 `RLIMIT_UMTXP` 资源限制，参见 [setrlimit(2)](getrlimit.2.md)。

**[`EAGAIN`]** 已有最大数量的读者（`URWLOCK_MAX_READERS`）被授予给定 `struct rwlock` 的读所有权。

**[`EBUSY`]** try 互斥锁锁定操作无法获得锁。

**[`ETIMEDOUT`]** 请求在 `uaddr` 和 `uaddr2` 参数中指定了超时，并在获得锁或被唤醒之前超时。

**[`EINTR`]** 在不可重启操作的等待期间传递了信号。带超时的操作通常不可重启，但以绝对时间指定的超时可能可重启。

**[`ERESTART`]** 在可重启操作的等待期间传递了信号。未指定超时的互斥锁锁定请求可重启。该错误不返回给用户空间代码，因为重启由指令计数器的通常调整处理。

## 参见

[clock_gettime(2)](clock_gettime.2.md), [mmap(2)](mmap.2.md), [setrlimit(2)](getrlimit.2.md), [shm_open(2)](shm_open.2.md), [sigaction(2)](sigaction.2.md), [thr_exit(2)](thr_exit.2.md), [thr_kill(2)](thr_kill.2.md), [thr_kill2(2)](thr_kill.2.md), [thr_new(2)](thr_new.2.md), [thr_self(2)](thr_self.2.md), [thr_set_name(2)](thr_set_name.2.md), [signal(3)](../gen/signal.3.md)

## 标准

`_umtx_op()` 系统调用是非标准的，由 Lb libthr 用于实现 IEEE Std 1003.1-2001 ("POSIX.1") [pthread(3)](../man3/pthread.3.md) 功能。

## 缺陷

在解锁健壮互斥锁与重置已注册 `struct umtx_robust_lists_params` 的 `robust_inact_offset` 成员中的指针之间存在一个窗口，允许另一个线程销毁该互斥锁，从而使内核检查已释放或重用的内存。`libthr` 实现仅在操作共享互斥锁时易受此竞争影响。当前实现的一个可能修复是加强共享互斥锁终止前的检查，特别是验证互斥锁内存是否映射自由 `UMTX_OP_SHM` 请求分配的共享内存对象。这未做是因为相信该竞争已被其他一致性检查充分覆盖，而添加该检查将阻止 `libpthread` 的替代实现。