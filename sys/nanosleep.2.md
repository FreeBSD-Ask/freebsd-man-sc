# nanosleep(2)

`nanosleep` — 高精度睡眠

## 名称

`nanosleep`

## 库

Lb libc

## 概要

`#include <time.h>`

```c
int
clock_nanosleep(clockid_t clock_id, int flags,
    const struct timespec *rqtp, struct timespec *rmtp);

int
nanosleep(const struct timespec *rqtp, struct timespec *rmtp);
```

## 描述

如果 `flags` 参数中未设置 `TIMER_ABSTIME` 标志，则 `clock_nanosleep()` 挂起调用线程的执行，直到 `rqtp` 参数指定的时间间隔已过，或者一个信号被传递给调用进程且其动作是调用信号捕获函数或终止进程。用于测量时间的时钟由 `clock_id` 参数指定。

如果 `flags` 参数中设置了 `TIMER_ABSTIME` 标志，则 `clock_nanosleep()` 挂起调用线程的执行，直到 `clock_id` 参数指定的时钟的值到达 `rqtp` 参数指定的绝对时间，或者一个信号被传递给调用进程且其动作是调用信号捕获函数或终止进程。如果在调用时，`rqtp` 指定的时间值小于或等于指定时钟的时间值，则 `clock_nanosleep()` 立即返回，调用线程不被挂起。未被屏蔽的信号会提前终止睡眠，无论中断信号上的 `SA_RESTART` 值如何。`rqtp` 和 `rmtp` 参数可以指向同一个对象。

支持以下 `clock_id` 值：

- CLOCK_MONOTONIC
- CLOCK_MONOTONIC_FAST
- CLOCK_MONOTONIC_PRECISE
- CLOCK_REALTIME
- CLOCK_REALTIME_FAST
- CLOCK_REALTIME_PRECISE
- CLOCK_SECOND
- CLOCK_TAI
- CLOCK_UPTIME
- CLOCK_UPTIME_FAST
- CLOCK_UPTIME_PRECISE

由于系统中其他活动的调度，挂起时间可能比请求的更长。带 `_FAST` 后缀的时钟和 `CLOCK_SECOND` 受 `kern.timecounter.alloweddeviation` [sysctl(8)](../man8/sysctl.8.md) 变量指定的时间间隔允许偏差约束。带 `_PRECISE` 后缀的时钟始终尽可能精确。`CLOCK_MONOTONIC`、`CLOCK_REALTIME` 和 `CLOCK_UPTIME` 默认是精确的。将 `kern.timecounter.nanosleep_precise` [sysctl(8)](../man8/sysctl.8.md) 设置为假值会使这些时钟的行为类似于 `_FAST` 时钟。

`nanosleep()` 函数的行为类似于 `clock_id` 参数为 `CLOCK_REALTIME` 且 `flags` 参数中不含 `TIMER_ABSTIME` 标志的 `clock_nanosleep()`。

## 返回值

当请求的时间已过时，这些函数返回零。

如果这些函数因任何其他原因返回，则 `clock_nanosleep()` 将直接返回错误码，而 `nanosleep()` 将返回 -1，并设置全局变量 `errno` 以指示错误。如果相对睡眠被信号中断且 `rmtp` 非 `NULL`，则其引用的 timespec 结构会被更新为包含未睡眠的时长（请求时间减去实际睡眠时间）。

## 错误

这些函数可能因以下错误而失败。

**[`EFAULT`]** `rqtp` 或 `rmtp` 指向的内存不是进程地址空间的有效部分。

**[`EINTR`]** 函数被信号传递中断。

**[`EINVAL`]** `rqtp` 参数指定的纳秒值小于零或大于等于 10 亿。

**[`EINVAL`]** `flags` 参数包含无效标志。

**[`EINVAL`]** `clock_id` 参数为 `CLOCK_THREAD_CPUTIME_ID` 或无法识别的值。

**[`ENOTSUP`]** `clock_id` 参数有效但此 `clock_nanosleep()` 实现不支持。

## 参见

[clock_gettime(2)](clock_gettime.2.md), [sigaction(2)](sigaction.2.md), [sleep(3)](../man3/sleep.3.md)

## 标准

这些函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。

## 历史

此系统调用的前身 `sleep()` 出现于 Version 3 AT&T UNIX，但在 [alarm(3)](../man3/alarm.3.md) 引入 Version 7 AT&T UNIX 时被移除。`nanosleep()` 系统调用自 NetBSD 1.3 起可用，并被移植到 OpenBSD 2.1 和 FreeBSD 3.0。`clock_nanosleep()` 系统调用自 FreeBSD 11.1 起可用。

在 FreeBSD 15.0 中，`clock_nanosleep()` 使用 `CLOCK_MONOTONIC`、`CLOCK_REALTIME`、`CLOCK_UPTIME` 时钟以及 `nanosleep()` 的默认行为已切换为使用精确时钟。