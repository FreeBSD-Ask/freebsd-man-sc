# smr.9

`smr` — 用于无锁数据结构的安全内存回收

## 名称

`smr`

## 概要

```c
#include <sys/smr.h>

smr_seq_t
smr_advance(smr_t smr)

smr_t
smr_create(const char *name)

void
smr_destroy(smr_t smr)

void
smr_enter(smr_t smr)

void
smr_exit(smr_t smr)

bool
smr_poll(smr_t smr, smr_seq_t goal, bool wait)

void
smr_synchronize(smr_t smr)

void
smr_wait(smr_t smr, smr_seq_t goal)
```

## 描述

安全内存回收（SMR）是一种支持实现内存安全无锁数据结构的机制。在典型用法中，对受 SMR 保护的数据结构（如哈希表或树）的读取访问在由 `smr_enter` 和 `smr_exit` 调用包围的代码组成的"读区段"中执行，而数据结构的修改则由传统的互斥体（如 [mutex(9)](mutex.9.md)）串行化。与 [rwlock(9)](rwlock.9.md)、[rmlock(9)](rmlock.9.md) 和 [sx(9)](sx.9.md) 等读写锁不同，SMR 允许读者和写者并发访问数据结构。读者始终可以立即进入读区段（`smr_enter` 永不阻塞），因此修改不会引入读取延迟。此外，`smr_enter` 和 `smr_exit` 仅操作每 CPU 数据，从而避免了传统读写互斥体实现中固有的某些性能问题。因此，SMR 可以作为频繁访问但很少修改的数据结构的有用构建块。

注意，任何受 SMR 保护的数据结构都必须谨慎实现，使得操作在读者和写者之间没有互斥的情况下也能正确执行。数据结构必须设计为无锁的；SMR 仅促进实现，例如使跟踪悬空指针安全，并有助于避免 ABA 问题。

当对数据结构的共享访问和修改可以并发进行时，写者必须注意确保从结构中移除的任何项在读者并行访问它们时不会被释放和回收。这一要求导致项的移除采用两阶段方法：首先，取消该项的链接，使得指向该项的所有指针都从结构中移除，防止任何新读者观察到该项。然后，写者等待直到某种机制保证没有现有读者仍在访问该项。此时可以安全地释放和重用该项的内存。SMR 提供了这种机制：读者可以在调用 `smr_enter` 和 `smr_exit` 函数之间访问无锁数据结构，这两个函数共同创建一个读区段，而 `smr_advance`、`smr_poll`、`smr_wait` 和 `smr_synchronize` 函数可用于等待读区段中的线程完成。所有这些函数都操作一个 `smr_t` 状态块，该状态块持有每 CPU 和全局状态。读者加载全局状态并修改每 CPU 状态，而写者必须扫描所有每 CPU 状态以检测活动读者。SMR 设计为通过批处理来分摊此成本，从而在写密集型工作负载中提供可接受的性能。

### 读者

线程通过调用 `smr_enter` 进入读区段。读区段应保持简短，且在读区段中不允许执行许多操作。具体而言，禁用上下文切换，因此读者不能获取阻塞互斥体（如 [mutex(9)](mutex.9.md)）。另一个后果是线程在读区段期间被固定到当前 CPU。此外，读区段不能嵌套：当已经在某个 `smr_t` 状态块的读区段中时，再用该状态块调用 `smr_enter` 是不正确的。

### UMA 集成

为简化 SMR 集成到消费者中，uma(9) 内核内存分配器提供了一些 SMR 指定的功能。这消除了消费者实现中的大量复杂性，并自动批处理写操作。

在典型用法中，一个 UMA 区（使用 `UMA_ZONE_SMR` 标志创建或使用 `uma_zone_set_smr` 函数初始化）与一个 `smr_t` 状态块耦合。要向受 SMR 保护的数据结构中插入项，使用 `uma_zalloc_smr` 函数从区中分配内存。插入和移除使用传统的互斥来串行化，项使用 `uma_zfree_smr` 函数释放。只读查找操作在 SMR 读区段中执行。`uma_zfree_smr` 等待所有可能正在访问被释放项的活动读者完成其读区段后，再回收该项的内存。

如果区有关联的每项析构函数，它将在没有读者能够访问给定项的某个时刻被调用。析构函数可用于释放与该项关联的附加资源。但请注意，不保证析构函数会在有界时间段内被调用。

### 写者

预期消费者将 SMR 与 UMA 结合使用，因此只需使用 `smr_enter` 和 `smr_exit` 函数，以及 `sys/smr_types.h` 中定义的 SMR 辅助宏。然而，介绍 SMR 的写侧接口可能有用。

在内部，SMR 维护一个全局的 `write sequence` 编号。进入读区段时，`smr_enter` 加载写入序列号的副本并将其存储在每 CPU 内存中，从而"观察"该值。退出读区段时，此每 CPU 内存被无效值覆盖，使 CPU 变为非活动状态。写者执行两种操作：推进写入序列号，以及轮询所有 CPU 以查看活动读者是否已观察到给定序列号。这些操作分别由 `smr_advance` 和 `smr_poll` 执行，它们不需要多个写者之间的串行化。

写者从数据结构中取消链接一个项后，它递增写入序列号，并使用 `smr_advance` 返回的新值标记该项。一旦所有 CPU 都观察到新值，写者可以使用 `smr_poll` 推断没有活动读者访问被取消链接的项，因此该项可以安全回收。由于这对操作相对昂贵，通常通过累积多个被取消链接项的集合并用目标写入序列号标记整个批处理来分摊此成本。

`smr_poll` 是非阻塞操作，仅当保证所有活动读者都已观察到目标序列号值时才返回真。`smr_wait` 是 `smr_poll` 的变体，它等待直到所有 CPU 都观察到目标序列号值。`smr_synchronize` 将 `smr_advance` 与 `smr_wait` 组合，等待所有 CPU 观察到新的写入序列号。这是一个昂贵的操作，仅当无法以某种方式推迟轮询时才应使用。

### 内存排序

`smr_enter` 函数具有获取语义，`smr_exit` 函数具有释放语义。不应假设 `smr_advance`、`smr_poll`、`smr_wait` 和 `smr_synchronize` 函数在内存排序方面有任何保证。实际上，其中一些函数具有比此处所述更强的排序语义，但这是特定于实现的，不应依赖。更多细节参见 [atomic(9)](atomic.9.md)。

## 注释

在 FreeBSD 之外，缩写 SMR 通常指一系列算法，这些算法支持对数据结构进行内存安全的只读访问，同时并发修改该数据结构。这里，SMR 指属于此家族的特定算法及其在 FreeBSD 中的实现。有关算法和上下文的更多细节，请参见 FreeBSD 源码树中的 **`sys/sys/smr.h`** 和 **`sys/kern/subr_smr.c`**。

缩写 SMR 也用于表示"叠瓦式磁记录"（shingled magnetic recording），这是一种用于在硬盘驱动器上存储数据且需要操作系统支持的技术。这两种缩写用法互不相关。

## 参见

[atomic(9)](atomic.9.md), [locking(9)](locking.9.md), uma(9)

## 作者

SMR 算法及其实现由 Jeff Roberson <jeff@FreeBSD.org> 提供。本手册页由 Mark Johnston <markj@FreeBSD.org> 编写。
