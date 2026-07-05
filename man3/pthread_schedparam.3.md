# pthread_schedparam.3

`pthread_setschedparam` — 线程调度参数操作

## 名称

`pthread_setschedparam`, `pthread_getschedparam`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_setschedparam(pthread_t thread, int policy,
    const struct sched_param *param)

int
pthread_getschedparam(pthread_t thread, int *restrict policy,
    struct sched_param *restrict param)
```

## 描述

`pthread_setschedparam` 和 `pthread_getschedparam` 函数分别用于设置和获取单个线程的调度参数。线程的调度策略可以是 `SCHED_FIFO`（先入先出）、`SCHED_RR`（轮转）或 `SCHED_OTHER`（分时共享）。有效的线程优先级（通过 `param->sched_priority` 访问）必须在 sched_get_priority_min(2) 和 sched_get_priority_max(2) 系统调用返回的范围内。

## 返回值

如果成功，这些函数返回 0。否则返回一个错误号以指示错误。

## 错误

`pthread_setschedparam` 函数将在以下情况失败：

**`[EINVAL]`** `policy` 的值无效。

**`[ENOTSUP]`** 调度参数的值无效。

**`[EPERM]`** 调用线程没有足够的权限执行该操作。

**`[ESRCH]`** 线程 `thread` 不存在。

`pthread_getschedparam` 函数将在以下情况失败：

**`[ESRCH]`** 线程 `thread` 不存在。

## 参见

sched_get_priority_max(2), sched_get_priority_min(2)

## 标准

`pthread_setschedparam` 和 `pthread_getschedparam` 函数符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。
