# sched_setscheduler(2)

`sched_setscheduler` — 设置/获取调度策略和调度器参数

## 名称

`sched_setscheduler`, `sched_getscheduler`

## 库

Lb libc

## 概要

```c
#include <sched.h>

int
sched_setscheduler(pid_t pid, int policy,
    const struct sched_param *param);

int
sched_getscheduler(pid_t pid);
```

## 描述

`sched_setscheduler()` 系统调用将 `pid` 指定进程的调度策略和调度参数分别设置为 `policy` 和 `param` 所指向的 `sched_param` 结构中指定的参数。`param` 结构中 `sched_priority` 成员的值必须是指定 `policy` 调度策略的包含优先级范围内的任意整数。

在本实现中，如果 `pid` 的值为负，系统调用将失败。

如果 `pid` 指定的进程存在且调用进程具有权限，将为进程 ID 等于 `pid` 的进程设置调度策略和调度参数。

如果 `pid` 为零，则为调用进程设置调度策略和调度参数。

在本实现中，进程何时可以影响另一进程的调度参数的策略在 -p1003.1b-93 中被指定为写式操作。

调度策略定义在 `<sched.h>` 中：

**`SCHED_FIFO`** 先进先出的固定优先级调度，无轮转调度；

**`SCHED_OTHER`** 标准分时调度器；

**`SCHED_RR`** 相同优先级进程间的轮转调度。

`sched_param` 结构定义在 `<sched.h>` 中：

```c
struct sched_param {
	int sched_priority;	/* 调度优先级 */
};
```

`sched_getscheduler()` 系统调用返回 `pid` 指定进程的调度策略。

如果 `pid` 指定的进程存在且调用进程具有权限，返回进程 ID 等于 `pid` 的进程的调度参数。

在本实现中，进程何时可以获取另一进程的调度参数的策略在 -p1003.1b-93 中被详细说明为读式操作。

如果 `pid` 为零，将返回调用进程的调度参数。在本实现中，如果 `pid` 为负，`sched_getscheduler()` 系统调用将失败。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

失败时 `errno` 将被设置为相应的值：

**[`ENOSYS`]** 系统未配置支持此功能。

**[`EPERM`]** 请求进程没有 -p1003.1b-93 中所详述的权限。

**[`ESRCH`]** 找不到与 `pid` 所指定进程相对应的进程。

**[`EINVAL`]** `policy` 参数的值无效，或 `param` 中包含的一个或多个参数超出了指定调度策略的有效范围。

## 参见

[sched_get_priority_max(2)](sched_get_priority_max.2.md), sched_get_priority_min(2), [sched_getparam(2)](sched_setparam.2.md), sched_rr_get_interval(2), [sched_setparam(2)](sched_setparam.2.md), [sched_yield(2)](sched_yield.2.md)

## 标准

`sched_setscheduler()` 和 `sched_getscheduler()` 系统调用符合 -p1003.1b-93。
