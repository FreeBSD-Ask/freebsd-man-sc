# time(9)

`boottime` — 系统时间变量

## 名称

`boottime`, `time_second`, `time_uptime`

## 概要

`#include <sys/time.h>`

`extern struct timeval boottime;`

`extern time_t time_second;`

`extern time_t time_uptime;`

## 描述

`boottime` 变量保存系统启动时间的估计值。此时间在系统启动时最初设置，可来自 RTC，也可来自根据系统根文件系统估计的时间。当设置当前系统时间、由 ntpd(8) 步进或在系统恢复时从 RTC 读取新时间时，`boottime` 将重新计算为 new_time - uptime。[sysctl(8)](../man8/sysctl.8.md) `kern.boottime` 返回此值。

`time_second` 变量是系统到秒级精度的"墙上时间"时钟。

`time_uptime` 变量是自启动以来的秒数。

bintime(9)、getbintime(9)、[microtime(9)](microtime.9.md)、getmicrotime(9)、nanotime(9) 和 getnanotime(9) 函数可用于以更精确和原子的方式获取当前时间。类似地，binuptime(9)、getbinuptime(9)、[microuptime(9)](microuptime.9.md)、getmicrouptime(9)、nanouptime(9) 和 getnanouptime(9) 函数可用于以更精确和原子的方式获取自启动以来经过的时间。`boottime` 变量可以在不加特殊保护的情况下读写。它会在系统时间相位改变时调整。

## 参见

clock_settime(2), ntp_adjtime(2), settimeofday(2), bintime(9), binuptime(9), getbintime(9), getbinuptime(9), getmicrotime(9), getmicrouptime(9), getnanotime(9), getnanouptime(9), [microtime(9)](microtime.9.md), [microuptime(9)](microuptime.9.md), nanotime(9), nanouptime(9)

> Poul-Henning Kamp, "Timecounters: Efficient and precise timekeeping in SMP kernels", *Proceedings of EuroBSDCon 2002, Amsterdam*, **/usr/share/doc/papers/timecounter.ascii.gz**.

> Marshall Kirk McKusick, George V. Neville-Neil, *The Design and Implementation of the FreeBSD Operating System*, pp. 57-61,65-66, Addison-Wesley, July 2004.
