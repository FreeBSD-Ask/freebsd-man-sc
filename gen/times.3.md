# times(3)

`times` — 进程时间

## 名称

`times`

## 库

Lb libc

## 概要

`#include <sys/times.h>`

```c
clock_t
times(struct tms *tp);
```

## 描述

> **注意** 此接口已被 [getrusage(2)](../sys/getrusage.2.md) 和 [gettimeofday(2)](../sys/gettimeofday.2.md) 取代。

`times` 函数返回自系统启动以来以 `CLK_TCK` 分之一秒为单位的时间值。`CLK_TCK` 的当前值（即统计时钟的频率，以每秒滴答数为单位）可通过 [sysconf(3)](sysconf.3.md) 接口获取。

它还会用时间统计信息填充 `tp` 所指向的结构。

`tms` 结构定义如下：

```c
struct tms {
	clock_t tms_utime;
	clock_t tms_stime;
	clock_t tms_cutime;
	clock_t tms_cstime;
};
```

该结构的元素定义如下：

**`tms_utime`** 为执行用户指令而计费的 CPU 时间。

**`tms_stime`** 系统代表进程执行而计费的 CPU 时间。

**`tms_cutime`** 子进程的 `tms_utime` 与 `tms_cutime` 之和。

**`tms_cstime`** 子进程的 `tms_stime` 与 `tms_cstime` 之和。

所有时间均以 `CLK_TCK` 分之一秒为单位。

当某个 [wait(2)](../sys/wait.2.md) 函数将已终止子进程的进程 ID 返回给父进程时，已终止子进程的时间将被计入父进程的 `tms_cutime` 和 `tms_cstime` 元素中。如果发生错误，`times` 返回值 ((`clock_t`)-1)，并设置 `errno` 以指示错误。

## 错误

`times` 函数可能失败并为 [getrusage(2)](../sys/getrusage.2.md) 和 [gettimeofday(2)](../sys/gettimeofday.2.md) 库例程指定的任何错误设置全局变量 `errno`。

## 参见

[time(1)](../man1/time.1.md), [getrusage(2)](../sys/getrusage.2.md), [gettimeofday(2)](../sys/gettimeofday.2.md), [wait(2)](../sys/wait.2.md), [sysconf(3)](sysconf.3.md), [clocks(7)](../man7/clocks.7.md)

## 标准

`times` 函数遵循 IEEE Std 1003.1-1988 ("POSIX.1")。
