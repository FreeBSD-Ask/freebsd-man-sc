# clocks(7)

`clocks` — 各种系统定时器

## 名称

`clocks`

## 概要

`#include <time.h>`

## 描述

`HZ` 不是 BSD 中应用程序接口的一部分。

存在许多不同的真实和虚拟（计时）时钟，具有不同的频率：

- 调度时钟。这是真实时钟，频率恰好为 100。应用程序不可用。
- 统计时钟。这是真实时钟，频率恰好为 128。不直接对应用程序可用。
- clock(3) 报告的时钟。这是虚拟时钟，频率恰好为 128。其实际频率由宏 `CLOCKS_PER_SEC` 给出。注意 `CLOCKS_PER_SEC` 可能是浮点数。不要在 FreeBSD 下的新程序中使用 clock(3)。与 getrusage(2) 相比它很薄弱。提供它是为了符合 ANSI。它通过调用 getrusage(2) 并丢弃信息和分辨率来实现。
- times(3) 报告的时钟。这是虚拟时钟，频率恰好为 128。其实际频率由宏 `CLK_TCK`（已弃用；不要使用）和 Fn sysconf _SC_CLK_TCK 以及 sysctl(3) 给出。注意其频率可能与 `CLOCKS_PER_SEC` 不同。不要在 FreeBSD 下的新程序中使用 times(3)。与 gettimeofday(2) 结合 getrusage(2) 相比它很薄弱。提供它是为了符合 POSIX。它通过调用 gettimeofday(2) 和 getrusage(2) 并丢弃信息和分辨率来实现。
- 性能分析时钟。这是真实时钟，频率为 1024。主要由 moncontrol(3) 和 gprof(1) 使用。应用程序应使用 sysctl(3) 或从性能分析数据文件的头文件中读取来确定其实际频率。
- mc146818a 时钟。这是真实时钟，标称频率为 32768。它被分频以提供统计时钟和性能分析时钟。应用程序不可用。
- 微秒时钟。这是虚拟时钟，频率为 1000000。它用于 BSD 中的大多数计时，并导出给应用程序的 getrusage(2)、gettimeofday(2)、select(2)、getitimer(2) 等。这是 BSD 应用程序通常应使用的时钟。
- i8254 时钟。这是真实时钟/定时器，标称频率为 1193182。它有三个可用的独立时间计数器。它被分频以提供调度时钟。应用程序不可用。
- 第五代或更晚 x86 系统上的 TSC 时钟（64 位寄存器）。这是真实时钟，频率等同于 CPU 的每秒周期数。如果可用，可使用 `machdep.tsc_freq` sysctl 找到其频率。用于在调度时钟值之间插值。
- ACPI 时钟。这是真实时钟/定时器，标称频率为 3579545。通过 24 或 32 位寄存器访问。与 TSC 时钟不同，即使 CPU 睡眠或其时钟速率改变，它仍保持恒定的滴答速率。应用程序不可用。

总结：如果 `HZ` 不是 1000000，则应用程序可能使用了错误的时钟。

## 参见

gprof(1), clock_gettime(2), getitimer(2), getrusage(2), gettimeofday(2), select(2), clock(3), moncontrol(3), times(3)

## 作者

本手册页由 J(:org Wunsch 根据 Bruce Evans 发布的描述编写。
