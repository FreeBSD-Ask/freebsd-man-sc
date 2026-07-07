# sched_get_priority_max(2)

`sched_get_priority_max` — 获取调度参数限制

## 名称

`sched_get_priority_max`, `sched_get_priority_min`, `sched_rr_get_interval`

## 库

Lb libc

## 概要

`#include <sched.h>`

```c
int
sched_get_priority_max(int policy);

int
sched_get_priority_min(int policy);

int
sched_rr_get_interval(pid_t pid, struct timespec *interval);
```

## 描述

`sched_get_priority_max()` 和 `sched_get_priority_min()` 系统调用分别返回由 `policy` 指定的调度策略的相应最大值或最小值。`sched_rr_get_interval()` 系统调用更新由 `interval` 参数所引用的 `timespec` 结构，使其包含由 `pid` 指定进程的当前执行时间限制（即时间片）。如果 `pid` 为零，则返回调用进程的当前执行时间限制。

`policy` 的值应为 `<sched.h>` 中定义的调度策略值之一：

**[`SCHED_FIFO`]** 先进先出的固定优先级调度，不进行轮转调度；

**[`SCHED_OTHER`]** 标准的分时调度器；

**[`SCHED_RR`]** 对相同优先级的进程进行轮转调度。

## 返回值

如果成功，`sched_get_priority_max()` 和 `sched_get_priority_min()` 系统调用将返回相应的最大值或最小值。如果失败，将返回值 -1，并设置 `errno` 以指示错误。

`sched_rr_get_interval()` 系统调用在成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

失败时，`errno` 将被设置为相应的值：

**[`EINVAL`]** `policy` 参数的值不代表一个已定义的调度策略。

**[`ENOSYS`]** 该实现不支持 `sched_get_priority_max()`、`sched_get_priority_min()` 和 `sched_rr_get_interval()` 系统调用。

**[`ESRCH`]** 找不到与 `pid` 所指定进程相对应的进程。

## 参见

[sched_getparam(2)](sched_getparam.2.md), [sched_getscheduler(2)](sched_getscheduler.2.md), [sched_setparam(2)](sched_setparam.2.md), [sched_setscheduler(2)](sched_setscheduler.2.md)

## 标准

`sched_get_priority_max()`、`sched_get_priority_min()` 和 `sched_rr_get_interval()` 系统调用遵循 -p1003.1b-93。
