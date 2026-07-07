# timer_settime(2)

`timer_getoverrun` — 每进程定时器（REALTIME）

## 名称

`timer_getoverrun`, `timer_gettime`, `timer_settime`

## 库

Lb librt

## 概要

```c
#include <time.h>

int
timer_getoverrun(timer_t timerid);

int
timer_gettime(timer_t timerid, struct itimerspec *value);

int
timer_settime(timer_t timerid, int flags,
    const struct itimerspec *restrict value,
    struct itimerspec *restrict ovalue);
```

## 描述

`timer_gettime()` 系统调用将指定定时器 `timerid` 到期前的时间量和定时器的重载值存储到 `value` 参数所指向的空间。该结构的 `it_value` 成员包含定时器到期前的时间量，若定时器已解除则为零。即使定时器以绝对时间武装，该值也作为到定时器到期的间隔返回。`value` 的 `it_interval` 成员包含上次由 `timer_settime()` 设置的重载值。

`timer_settime()` 系统调用从 `value` 参数的 `it_value` 成员设置 `timerid` 所指定定时器的下次到期时间，并在 `value` 的 `it_value` 成员非零时武装定时器。如果调用 `timer_settime()` 时指定定时器已武装，此调用将下次到期时间重置为指定值。如果 `value` 的 `it_value` 成员为零，定时器被解除。如果定时器被解除，则待处理信号被移除。

如果 `flags` 参数中未设置 `TIMER_ABSTIME` 标志，`timer_settime()` 的行为如同将下次到期时间设置为等于 `value` 的 `it_value` 成员所指定的间隔。即定时器在调用后 `it_value` 纳秒后到期。如果 `flags` 参数中设置了 `TIMER_ABSTIME` 标志，`timer_settime()` 的行为如同将下次到期时间设置为等于 value 的 it_value 成员所指定的绝对时间与 `timerid` 关联时钟的当前值之差。即当时钟达到 `value` 的 `it_value` 成员所指定的值时定时器到期。如果指定时间已过，系统调用成功并进行到期通知。

定时器的重载值设置为 `value` 的 `it_interval` 成员所指定的值。当定时器以非零 `it_interval` 武装时，指定了一个周期性（或重复性）定时器。

介于指定定时器分辨率的两个连续非负整数倍之间的时间值向上舍入到分辨率的较大倍数。量化误差不会导致定时器早于舍入时间值到期。

如果 `ovalue` 参数不为 `NULL`，`timer_settime()` 系统调用在 `ovalue` 所引用的位置存储一个值，表示定时器本应到期前的先前时间量，若定时器已解除则为零，以及先前的定时器重载值。定时器不会在预定时间之前到期。

在任何时刻，对于给定定时器，只有一个信号排队到进程。当一个信号仍待处理的定时器到期时，不排队信号，将发生定时器溢出。当进程接受定时器到期信号时，`timer_getoverrun()` 系统调用返回指定定时器的定时器到期溢出计数。返回的溢出计数包含在信号生成（排队）到被接受之间发生的额外定时器到期次数，最多可达但不包括 {`DELAYTIMER_MAX`}。如果此类额外到期次数大于或等于 {`DELAYTIMER_MAX`}，则溢出计数设置为 {`DELAYTIMER_MAX`}。`timer_getoverrun()` 返回的值适用于定时器的最近一次到期信号接受。如果定时器尚未传递过到期信号，`timer_getoverrun()` 的返回值未指定。

## 返回值

如果 `timer_getoverrun()` 系统调用成功，它返回上述的定时器到期溢出计数。否则返回 -1，并设置全局变量 `errno` 以指示错误。

成功完成时，`timer_gettime()` 和 `timer_settime()` 返回 0；否则返回 -1，并设置 `errno` 以指示错误。

## 错误

`timer_settime()` 系统调用在以下情况下将失败：

**[EINVAL]** `value` 结构指定的纳秒值小于零或大于等于 10 亿，且该结构的 `it_value` 成员未指定零秒和零纳秒。

这些系统调用在以下情况下可能失败：

**[EINVAL]** `timerid` 参数不对应于由 `timer_create()` 返回但尚未被 `timer_delete()` 删除的 ID。

`timer_settime()` 系统调用在以下情况下可能失败：

**[EINVAL]** `value` 的 `it_interval` 成员非零，且定时器创建时通知方式为创建新线程（`sigev_sigev_notify` 为 `SIGEV_THREAD`），且 `sigev_notify_attributes` 所指向的线程属性中已设置固定栈地址。

`timer_gettime()` 和 `timer_settime()` 系统调用在以下情况下可能失败：

**[EFAULT]** 任何参数指向分配地址空间之外，或发生内存保护错误。

## 参见

[clock_getres(2)](clock_getres.2.md), [timer_create(2)](timer_create.2.md), [timer_delete(2)](timer_delete.2.md), [siginfo(3)](../man3/siginfo.3.md)

## 标准

`timer_getoverrun()`、`timer_gettime()` 和 `timer_settime()` 系统调用遵循 IEEE Std 1003.1-2004 ("POSIX.1")。

## 历史

对 POSIX 每进程定时器的支持首次出现于 FreeBSD 7.0。