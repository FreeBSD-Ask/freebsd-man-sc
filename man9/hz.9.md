# hz.9

`hz` — 系统时间模型

## 名称

`hz`, `tick`, `stathz`, `profhz`

## 概要

```c
#include <sys/kernel.h>
```

```c
extern int hz;
extern int tick;
extern int stathz;
extern int profhz; /* deprecated */
```

## 描述

FreeBSD 使用 [eventtimers(9)](eventtimers.9.md) 利用周期性、一次性、全局或每 CPU 的定时硬件来产生传统的时钟行为。这些时钟调节系统中的周期性事件。

主时钟用于通过 timecounters(9) 更新系统的时间概念，并按 [hardclock(9)](hardclock.9.md) 中所述的节奏调节周期性系统处理。该例程可能每 1 / `hz` 秒调用一次，但如果下一个 tick 无需工作且自上次调用以来未超过 0.5 秒，则省略调用。

以 `stathz` 运行的统计时钟收集系统及其进程的统计信息。它计算 getrusage(2) 的值以及 [ps(1)](../man1/ps.1.md) 和 [top(1)](../man1/top.1.md) 显示的统计信息。

最后，分析时钟可能以 `profhz` 运行，以采样用户程序计数器值用于分析目的。此分析机制已被功能更全面的 [hwpmc(4)](../man4/hwpmc.4.md) 取代，并可能在未来的 FreeBSD 版本中移除。

`tick` 是一个系统 tick 的微秒时长。

这些系统变量也可通过 sysctl(3) 的 *struct clockinfo* 和 [sysctl(8)](../man8/sysctl.8.md) 的 **kern.clockrate** 获得。

当前全局和每 CPU 的 CPU 时间使用量以 1 / `stathz` tick 为单位通过 **kern.cp_time** 和 **kern.cp_times** sysctl MIB 返回给用户。

`hz` 频率可通过在内核配置文件中定义 `HZ` 或通过 loader.conf(5) 设置 **kern.hz** 系统可调参数来覆盖。

当前默认值对于真实硬件为 1000 Hz（tick 为 1 ms）。对于虚拟机客户机，默认值为 100 Hz（tick 为 10 ms）。仅在你真正知道自己在做什么时才覆盖默认值。由于超时的自适应性质，更改此值的影响比过去小。

## 参见

[ps(1)](../man1/ps.1.md), [top(1)](../man1/top.1.md), `setitimer(2)`, `timer_settime(2)`, `loader.conf(5)`, [eventtimers(9)](eventtimers.9.md), [hardclock(9)](hardclock.9.md), [microtime(9)](microtime.9.md), `time_second(9)`, `timecounters(9)`

## 实现说明

历史上，`stathz` 和 `profhz` 时钟都从同一物理定时器运行，当没有进程使用分析功能时以较慢速率运行，当至少一个进程使用时以较快速率运行。虽然该接口已被 IEEE Std 1003.1-2008 ("POSIX.1") 弃用以支持 timer_settime(2)，但若干程序仍使用 setitimer(2) 和 `ITIMER_PROF` 来获得比传统可用更高分辨率的周期性中断。

历史上，[hardclock(9)](hardclock.9.md) 也从单独的中断运行，除非在没有足够周期性中断源的受限平台上。FreeBSD 使用 [eventtimers(9)](eventtimers.9.md) 来抽象这些细节，但某些旧代码可能仍保留与此抽象不完全匹配的假设。

timecounters(9) 限于 32 位并在约一秒后回绕，因此我们必须至少每半秒更新它们维护的时间手，以获得正确的回绕数学。此外，`kern.cp_times` 需要至少每秒更新一次，以便 [top(1)](../man1/top.1.md) 显示的值每秒更新。
