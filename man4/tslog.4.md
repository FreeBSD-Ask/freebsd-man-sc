# tslog.4

`tslog` — 引导时事件跟踪设施

## 名称

`tslog`

## 概要

`要将此引导时事件跟踪设施编译进内核，请在内核配置文件中加入以下行：`

> option TSLOG

## 描述

`tslog` 是一种引导时事件跟踪设施。它适用于跟踪基于函数进入和退出的递归事件。其目的是通过生成详细的计时信息来简化定位和减少整体 FreeBSD 引导时间的工作。

`tslog` 能够跟踪引导加载器、内核初始化和用户态进程。

在用户态中，它为每个进程 ID 记录以下详情：

- 创建给定进程 ID 的 fork(2) 的时间戳和父进程 ID。
- 传递给 execve(2) 的路径（如果有）。
- [namei(9)](../man9/namei.9.md) 解析的第一个路径（如果有）。
- 终止进程的 exit(3) 的时间戳。

## SYSCTL 变量

以下 [sysctl(8)](../man8/sysctl.8.md) 变量可用：

**`debug.tslog`** 转储已记录的加载器和内核事件时间戳的 `tslog` 缓冲区。

**`debug.tslog_user`** 转储已记录的用户态事件时间戳的 `tslog` 缓冲区。

## 火焰图

`tslog` 缓冲区转储可用于生成 FreeBSD 引导过程的火焰图以进行可视化分析。详见 Lk <https://github.com/cperciva/freebsd-boot-profiling> 。

## 参见

[dtrace(1)](../man1/dtrace.1.md), [boottrace(4)](boottrace.4.md), [ktr(4)](ktr.4.md)

## 历史

`tslog` 首次出现于 FreeBSD 12.0。在 FreeBSD 13.2 中添加了对跟踪引导加载器和用户态进程的支持。

### TSLOG 与 Boottrace

`tslog` 面向系统开发者，而 [boottrace(4)](boottrace.4.md) 旨在便于系统管理员使用。两种设施都提供引导过程的计时和资源使用概览。

### TSLOG 与 DTrace

[dtrace(1)](../man1/dtrace.1.md) 并不总是分析早期内核初始化的正确工具。原因是它需要一些在引导过程早期尚不可用的内核子例程，例如：陷阱、内存分配或线程调度。`tslog` 依赖于比 [dtrace(1)](../man1/dtrace.1.md) 更少的内核子例程，因此可以跟踪早期内核初始化。

### TSLOG 与 KTR

[ktr(4)](ktr.4.md) 有几个限制，使其无法在引导过程开始时运行。相比之下，`tslog` 专为记录引导分析的时间戳事件而设计。

## 作者

`tslog` 由 Colin Percival <cperciva@FreeBSD.org> 编写。

本手册页由 Mateusz Piotrowski <0mp@FreeBSD.org> 编写。
