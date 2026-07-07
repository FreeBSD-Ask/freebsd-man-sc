# ffclock(2)

`ffclock_getcounter` — 检索 feed-forward 计数器，获取和设置 feed-forward 时钟估计值

## 名称

`ffclock_getcounter`, `ffclock_getestimate`, `ffclock_setestimate`

## 库

Lb libc

## 概要

`#include <sys/timeffc.h>`

```c
int
ffclock_getcounter(ffcounter *ffcount);

int
ffclock_getestimate(struct ffclock_estimate *cest);

int
ffclock_setestimate(struct ffclock_estimate *cest);
```

## 描述

ffclock 是同步系统时钟的替代方法。ffclock 实现了 feed-forward 范式，将时间戳和时间保持内核功能解耦。这确保了过去的时钟误差不会影响当前的时间保持，这种方法与 ntpd 守护进程在调整系统时钟时实现的反馈方法截然不同。feed-forward 方法在网络同步方面展现出了比反馈方法更好的性能和更高的鲁棒性。

在 feed-forward 上下文中，*timestamp*（时间戳）是 timecounter 滴答的累计值，可以使用 feed-forward *clock estimates*（时钟估计值）将其转换为秒。

`ffclock_getcounter()` 系统调用允许调用进程检索内核维护的 feed-forward 计数器的当前值。

`ffclock_getestimate()` 和 `ffclock_setestimate()` 系统调用分别允许调用者获取和设置内核的 feed-forward 时钟参数估计值。`ffclock_setestimate()` 系统调用应由 feed-forward 同步守护进程的单个实例调用。`ffclock_getestimate()` 系统调用可由任何进程调用来检索 feed-forward 时钟估计值。

feed-forward 方法不要求每次将时间戳转换为秒时都检索时钟估计值。因此，如果调用进程改为从时钟同步守护进程检索时钟估计值，系统调用的数量可以大大减少。当 feed-forward 同步守护进程未运行时，必须使用 `ffclock_getestimate()`（参见下方的[用法](#用法)）。

`cest` 所指向的时钟参数估计结构体定义在 `<sys/timeffc.h>` 中：

```c
struct ffclock_estimate {
        struct bintime update_time;    /* 上次估计更新的时间。 */
        ffcounter      update_ffcount; /* 上次更新时的计数器值。 */
        ffcounter      leapsec_next;   /* 下一个闰秒的计数器值。 */
        uint64_t       period;         /* 计数器周期的估计值。 */
        uint32_t       errb_abs;       /* 绝对时钟误差的上界 [ns]。 */
        uint32_t       errb_rate;      /* 计数器速率误差的上界 [ps/s]。 */
        uint32_t       status;         /* 时钟状态。 */
        int16_t        leapsec_total;  /* 迄今为止的所有闰秒。 */
        int8_t         leapsec;        /* 下一个闰秒（取值为 {-1,0,1}）。 */
};
```

仅超级用户可以设置 feed-forward 时钟估计值。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

以下错误代码可能被设置在 `errno` 中：

**[`EFAULT`]** `ffcount` 或 `cest` 指针引用了无效的内存。

**[`EPERM`]** 非超级用户尝试设置 feed-forward 时钟参数估计值。

## 用法

feed-forward 范式支持定义专用的时钟函数。

在最简单的形式中，`ffclock_getcounter()` 可用于建立事件之间的严格顺序，或以最低的性能开销非常精确地测量小时间间隔。

访问绝对时间（或“wall-clock time”，即挂钟时间）的方法有多种，ffclock 所跟踪的也是如此。最简单的方法是使用 ffclock sysctl 接口 `kern.ffclock` 使系统时钟返回 ffclock 时间。然后可以使用 [clock_gettime(2)](clock_gettime.2.md) 系统调用来检索 feed-forward 时钟所看到的当前时间。请注意，此设置会影响整个系统，且应运行 feed-forward 同步守护进程。

一种较不自动化的方法是从内核检索 feed-forward 计数器时间戳，并使用 feed-forward 时钟参数估计值将时间戳转换为秒。feed-forward 时钟参数估计值可以从内核或直接从同步守护进程检索（首选后者）。此方法允许根据应用程序的需要使用不同的时钟模型转换时间戳，同时收集有意义的当前时钟误差上界。

## 参见

[date(1)](../man1/date.1.md), [adjtime(2)](adjtime.2.md), [clock_gettime(2)](clock_gettime.2.md), [ctime(3)](../man3/ctime.3.md)

## 历史

Feed-forward 时钟支持首次出现于 FreeBSD 10.0。

## 作者

Feed-forward 时钟支持由 Julien Ridoux <jridoux@unimelb.edu.au> 与 Darryl Veitch <dveitch@unimelb.edu.au> 在 FreeBSD Foundation 赞助下于墨尔本大学合作编写。
