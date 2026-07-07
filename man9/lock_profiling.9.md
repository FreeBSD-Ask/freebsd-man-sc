# LOCK_PROFILING(9)

`LOCK_PROFILING` — 内核锁性能分析支持

## 名称

`LOCK_PROFILING`

## 概要

```c
options LOCK_PROFILING
```

## 描述

`LOCK_PROFILING` 内核选项添加了对测量和报告锁使用及竞争统计信息的支持。这些统计信息按“获取点”进行整理。获取点是内核源代码中获取锁的不同位置（由源文件名和行号标识）。

对于每个获取点，会累计以下统计信息：

- 该锁在从此点获取后曾经连续持有的最长时间。
- 该锁在从此点获取后持有的总时间。
- 线程为获取该锁而等待的总时间。
- 非递归获取的总次数。
- 到达此点时该锁已被其他线程持有（需要自旋或睡眠）的总次数。
- 该锁在从此点获取后被持有时，其他线程尝试获取该锁的总次数。

此外，平均持有时间和平均等待时间分别由总持有时间和总等待时间以及获取次数推导得出。

`LOCK_PROFILING` 内核选项还添加了以下 [sysctl(8)](../man8/sysctl.8.md) 变量来控制和监视性能分析代码：

**`max`** 最长连续持有时间（以微秒为单位）。

**`wait_max`** 最长连续等待时间（以微秒为单位）。

**`total`** 总（累计）持有时间（以微秒为单位）。

**`wait_total`** 总（累计）等待时间（以微秒为单位）。

**`count`** 获取总次数。

**`avg`** 平均持有时间（以微秒为单位），由总持有时间和获取次数推导得出。

**`wait_avg`** 平均等待时间（以微秒为单位），由总等待时间和获取次数推导得出。

**`cnt_hold`** 该锁被持有且另一线程尝试获取该锁的次数。

**`cnt_lock`** 到达此点时该锁已被持有的次数。

**`name`** 获取点的名称，由源文件名和行号推导而来，后跟括号中的锁名称。

**`debug.lock.prof.enable`** 启用或禁用锁性能分析代码。默认为 0（关闭）。

**`debug.lock.prof.reset`** 重置当前的锁性能分析缓冲区。

**`debug.lock.prof.stats`** 以纯文本形式显示的实际性能分析统计信息。各列从左到右依次为：

**`debug.lock.prof.rejected`** 在表填满后被忽略的获取点数量。

**`debug.lock.prof.skipspin`** 禁用或启用自旋锁的锁性能分析代码。默认为 0（对自旋锁进行性能分析）。

**`debug.lock.prof.skipcount`** 大约每 N 次锁获取进行一次采样。

## 参见

[sysctl(8)](../man8/sysctl.8.md), [mutex(9)](mutex.9.md)

## 历史

互斥锁性能分析支持出现于 FreeBSD 5.0。通用锁性能分析支持出现于 FreeBSD 7.0。

## 作者

`MUTEX_PROFILING` 代码由 Eivind Eklund <eivind@FreeBSD.org>、Dag-Erling Smørgrav <des@FreeBSD.org> 和 Robert Watson <rwatson@FreeBSD.org> 编写。`MUTEX_PROFILING` 代码由 Kip Macy <kmacy@FreeBSD.org> 编写。本手册页由 Dag-Erling Smørgrav <des@FreeBSD.org> 编写。

## 注意事项

`LOCK_PROFILING` 选项会增加 `struct lock_object` 的大小，因此使用该选项构建的内核无法与未使用该选项构建的模块一起工作。

`LOCK_PROFILING` 选项还会阻止互斥锁代码的内联，这可能导致相当严重的性能损失。但情况并非总是如此。`LOCK_PROFILING` 可能引入显著的性能开销，使用其他性能分析工具很容易监视到这一点，因此不建议将性能分析工具与 `LOCK_PROFILING` 组合使用。

测量使用 nanotime(9) 以纳秒为单位进行和存储（在没有同步 TSC 的架构上），但以微秒为单位呈现。对于最希望进行性能分析的锁（持有时间长和/或获取频率高的锁），这仍然足够了。

`LOCK_PROFILING` 通常不应与其他调试选项组合使用，因为结果可能受到各特性之间交互的强烈影响。特别是，`LOCK_PROFILING` 在与 `INVARIANTS` 一起运行时会报告高于正常水平的 uma(9) 锁竞争，这是因为 `INVARIANTS` 存在时会发生额外的加锁；同样，与 `WITNESS` 组合使用会导致性能分析输出中的锁持有时间和竞争大幅增加。
