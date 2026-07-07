# sched_setparam(2)

`sched_setparam` — 设置/获取调度参数

## 名称

`sched_setparam`, `sched_getparam`

## 库

Lb libc

## 概要

```c
#include <sched.h>

int
sched_setparam(pid_t pid, const struct sched_param *param);

int
sched_getparam(pid_t pid, struct sched_param *param);
```

## 描述

`sched_setparam()` 系统调用将 `pid` 指定进程的调度参数设置为 `param` 所指向的 `sched_param` 结构中指定的值。`param` 结构中 `sched_priority` 成员的值必须是 `pid` 指定进程当前调度策略的包含优先级范围内的任意整数。优先级的数值越大表示优先级越高。

在本实现中，如果 `pid` 的值为负，系统调用将失败。

如果 `pid` 指定的进程存在且调用进程具有权限，则为进程 ID 等于 `pid` 的进程设置调度参数。

如果 `pid` 为零，则为调用进程设置调度参数。

在本实现中，进程何时可以影响另一进程的调度参数的策略在 -p1003.1b-93 中被指定为写式操作。

目标进程，无论是否正在运行，都将在所有其他同等或更高优先级的可运行进程被调度运行后恢复执行。

如果 `pid` 参数指定进程的优先级被设置为高于最低优先级运行进程的优先级，且指定的进程已就绪可运行，则 `pid` 参数指定的进程将抢占最低优先级的运行进程。类似地，如果调用 `sched_setparam()` 的进程将其自身优先级设置为低于一个或多个其他非空进程列表的优先级，那么最高优先级列表的头部进程也将抢占调用进程。因此，在任一情况下，发起进程可能直到更高优先级的进程执行完毕后才会收到所请求优先级更改完成的通知。

在本实现中，当 `pid` 指定进程的当前调度策略为正常分时（SCHED_OTHER，非 POSIX 源代码时又称 SCHED_NORMAL）或空闲策略（SCHED_IDLE，非 POSIX 源代码时）时，其行为如同该进程在 SCHED_RR 下以低于任何实际实时优先级的优先级运行。

`sched_getparam()` 系统调用将在 `param` 所指向的 `sched_param` 结构中返回 `pid` 指定进程的调度参数。

如果 `pid` 指定的进程存在且调用进程具有权限，则返回进程 ID 等于 `pid` 的进程的调度参数。

在本实现中，进程何时可以获取另一进程的调度参数的策略在 -p1003.1b-93 中被详细说明为读式操作。

如果 `pid` 为零，将返回调用进程的调度参数。在本实现中，如果 `pid` 为负，`sched_getparam()` 系统调用将失败。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

失败时 `errno` 将被设置为相应的值：

**[`ENOSYS`]** 系统未配置支持此功能。

**[`EPERM`]** 请求进程没有 -p1003.1b-93 中所详述的权限。

**[`ESRCH`]** 找不到与 `pid` 所指定进程相对应的进程。

**[`EINVAL`]** 对于 `sched_setparam()`：一个或多个所请求的调度参数超出了指定 `pid` 的调度策略所定义的范围。

## 参见

[sched_get_priority_max(2)](sched_get_priority_max.2.md), sched_get_priority_min(2), sched_getscheduler(2), sched_rr_get_interval(2), [sched_setscheduler(2)](sched_setscheduler.2.md), [sched_yield(2)](sched_yield.2.md)

## 标准

`sched_setparam()` 和 `sched_getparam()` 系统调用符合 -p1003.1b-93。
