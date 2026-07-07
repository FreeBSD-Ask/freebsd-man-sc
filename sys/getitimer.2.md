# getitimer(2)

`getitimer` — 获取/设置间隔定时器的值

## 名称

`getitimer`, `setitimer`

## 库

Lb libc

## 概要

`#include <sys/time.h>`

```c
#define ITIMER_REAL      0
#define ITIMER_VIRTUAL   1
#define ITIMER_PROF      2

int
getitimer(int which, struct itimerval *value);

int
setitimer(int which, const struct itimerval *value,
    struct itimerval *ovalue);
```

## 描述

系统为每个进程提供三个间隔定时器，定义在 `<sys/time.h>` 中。`getitimer()` 系统调用返回由 `which` 指定的定时器的当前值，结果存放在 `value` 所指向的结构中。`setitimer()` 系统调用将定时器设置为指定的 `value`（如果 `ovalue` 不是空指针，则返回该定时器先前的值）。

定时器的值由 `itimerval` 结构定义：

```c
struct itimerval {
        struct  timeval it_interval;    /* 定时器间隔 */
        struct  timeval it_value;       /* 当前值 */
};
```

如果 `it_value` 非零，它表示到下次定时器到期的时间。如果 `it_interval` 非零，它指定了定时器到期时用于重新加载 `it_value` 的值。将 `it_value` 设置为 0 会禁用定时器，无论 `it_interval` 的值如何。将 `it_interval` 设置为 0 会使定时器在下次到期后被禁用（假设 `it_value` 非零）。

小于系统时钟分辨率的时间值会被向上取整到该分辨率（通常为 10 毫秒）。

`ITIMER_REAL` 定时器按实际时间递减。该定时器到期时会发送 `SIGALRM` 信号。

`ITIMER_VIRTUAL` 定时器按进程虚拟时间递减。它仅在进程执行时运行。该定时器到期时会发送 `SIGVTALRM` 信号。

`ITIMER_PROF` 定时器在进程虚拟时间以及系统代表进程运行时均会递减。它设计用于解释器对解释执行的程序进行统计性性能分析。每次 `ITIMER_PROF` 定时器到期时，会发送 `SIGPROF` 信号。由于该信号可能中断正在进行的系统调用，使用此定时器的程序必须准备好重启被中断的系统调用。

`setitimer()` 中 `it_interval` 和 `it_value` 允许的最大秒数为 100000000。

## 注释

三个用于操作时间值的宏定义在 `<sys/time.h>` 中。`timerclear` 宏将时间值置零，`timerisset` 测试时间值是否非零，`timercmp` 比较两个时间值。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`getitimer()` 和 `setitimer()` 系统调用在以下情况下会失败：

**[`EFAULT`]** `value` 参数指定了一个无效地址。

**[`EINVAL`]** `value` 参数指定的时间过大，无法处理。

## 参见

[gettimeofday(2)](gettimeofday.2.md), [select(2)](select.2.md), [sigaction(2)](sigaction.2.md), [clocks(7)](../man7/clocks.7.md)

## 标准

`getitimer()` 和 `setitimer()` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。然而，后来的 IEEE Std 1003.1-2008 ("POSIX.1") 修订版将这两个函数标记为过时，建议改用 [timer_gettime(2)](timer_gettime.2.md) 和 [timer_settime(2)](timer_settime.2.md)。

## 历史

`getitimer()` 系统调用首次出现于 4.2BSD。
