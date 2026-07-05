# tracing.7

`tracing` — FreeBSD 跟踪和性能监控简介

## 名称

`tracing`

## 描述

FreeBSD 提供了多种跟踪和性能监控工具。在 [development(7)](development.7.md) 期间以及潜在的生产系统上，可使用它们来测量性能并排查内核和用户空间问题。这些工具在范围、易用性、开销、设计和限制方面各不相同。

### DTrace

[dtrace(1)](../man1/dtrace.1.md) 是 FreeBSD 上最通用的跟踪框架，能够跟踪从内核到用户空间中运行的应用程序的整个 FreeBSD 软件栈。有关更多详细信息，请参阅 [dtrace(1)](../man1/dtrace.1.md) 和 [SDT(9)](../man9/SDT.9.md)。

dwatch(1) 是 DTrace 的用户友好型封装。它简化了常见的 DTrace 使用模式，运行所需的专家知识更少。

### 用户空间跟踪

[truss(1)](../man1/truss.1.md) 跟踪系统调用。它使用 sysdecode(3) 美化打印系统调用参数，使用 ptrace(2) 跟踪进程。

[ktrace(1)](../man1/ktrace.1.md) 对于调试用户程序很有用。它为指定进程启用内核跟踪日志记录。与 [truss(1)](../man1/truss.1.md) 一样，它主要跟踪系统调用，但它不使用 ptrace(2)，而是异步将条目记录到用 ktrace(2) 配置的跟踪文件中（通常是 `ktrace.out`），并且它可以记录其他类型的内核事件，如页面错误和名称查找（参阅 [ktrace(1)](../man1/ktrace.1.md) 中的 `-t`）。此外，程序可以使用 utrace(2) 系统调用记录到 [ktrace(1)](../man1/ktrace.1.md) 流。

### 内核跟踪

[ktr(4)](../man4/ktr.4.md) 是用于在内核中记录字符串的工具。它在内核开发期间的一些特殊用途中非常方便。它允许内核程序员将事件记录到全局环形缓冲区，稍后可使用 ktrdump(8) 转储。

### 硬件加速跟踪

[hwt(4)](../man4/hwt.4.md) 是一个内核跟踪框架，为硬件辅助跟踪提供基础设施。

### 硬件计数器

[pmcstat(8)](../man8/pmcstat.8.md) 及其内核对应部分 [hwpmc(4)](../man4/hwpmc.4.md) 是 FreeBSD 使用硬件计数器进行性能测量的工具。

### 引导和关机跟踪

[boottrace(4)](../man4/boottrace.4.md) 是用于跟踪引导和关机事件的工具。其目标受众是系统管理员。

[tslog(4)](../man4/tslog.4.md) 是面向开发者的引导时事件跟踪工具。

## 历史

`tracing` 手册页由 Mateusz Piotrowski <0mp@FreeBSD.org> 编写。首次出现于 FreeBSD 15.0。
