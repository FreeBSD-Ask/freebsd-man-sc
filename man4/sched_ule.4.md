# sched_ule.4

`sched_ule` — ULE 调度器

## 名称

`sched_ule`

## 概要

`options SCHED_ULE`

## 描述

`sched_ule` 调度器提供了许多传统系统调度器 [sched_4bsd(4)](sched_4bsd.4.md) 中没有的高级调度器功能。这些功能针对 SMP 和交互性，包括：

- 线程 CPU 亲和性。
- CPU 拓扑感知，包括超线程。
- 每 CPU 运行队列。
- 交互式启发式算法，可检测交互式应用程序并在高负载下优先调度。

以下 sysctl 与 `sched_ule` 的操作相关：

**`kern.sched.name`** 此只读 sysctl 报告活动调度器的名称。

**`kern.sched.quantum`** 此读写 sysctl 报告或设置授予线程的时间片长度（以微秒为单位）。

## 参见

[sched_4bsd(4)](sched_4bsd.4.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`sched_ule` 调度器最早出现于 FreeBSD 5.1。

## 作者

Jeff Roberson <jeff@FreeBSD.org>
