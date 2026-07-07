# sigwaitinfo(2)

`sigtimedwait` — 等待排队的信号（REALTIME）

## 名称

`sigtimedwait`, `sigwaitinfo`

## 库

Lb libc

## 概要

```c
#include <signal.h>

int
sigtimedwait(const sigset_t *restrict set,
    siginfo_t *restrict info,
    const struct timespec *restrict timeout);

int
sigwaitinfo(const sigset_t * restrict set,
    siginfo_t * restrict info);
```

## 描述

`sigtimedwait()` 系统调用等同于 `sigwaitinfo()`，区别在于如果 `set` 指定的信号均未处于待处理状态，`sigtimedwait()` 会等待 `timeout` 引用的 `timespec` 结构中指定的时间间隔。如果 `timeout` 指向的 `timespec` 结构值为零且 `set` 指定的信号均未处于待处理状态，则 `sigtimedwait()` 立即返回并报错。如果 `timeout` 为 `NULL` 指针，`sigtimedwait()` 将无限期阻塞。使用 `CLOCK_MONOTONIC` 时钟来测量 `timeout` 参数指定的时间间隔。

`sigwaitinfo()` 系统调用从 `set` 指定的集合中选择待处理信号。如果在 `SIGRTMIN` 到 `SIGRTMAX` 范围内的多个待处理信号中有任一被选中，应选择编号最低的那个。实时信号与非实时信号之间，或多个待处理的非实时信号之间的选择顺序未指定。如果调用时 `set` 中没有信号处于待处理状态，调用线程将被挂起，直到 `set` 中的一个或多个信号变为待处理，或直到被未阻塞的、被捕获的信号中断。

如果 `info` 参数为 `NULL`，`sigwaitinfo()` 系统调用等同于 `sigwait()` 系统调用。如果 `info` 参数非 `NULL`，`sigwaitinfo()` 函数等同于 `sigwait()`，区别在于选定的信号编号将存储在 `si_signo` 成员中，信号的原因将存储在 `si_code` 成员中。此外，`sigwaitinfo()` 和 `sigtimedwait()` 系统调用如果被信号中断可能返回 `EINTR`，而 `sigwait()` 函数不允许如此。

如果有任何值排队到选定信号，第一个这样的排队值将被出队，并且如果 `info` 参数非 `NULL`，该值将存储在 `info` 的 `si_value` 成员中。用于排队信号的系统资源将被释放并返回给系统供其他用途。如果没有值排队，`si_value` 成员的内容为零值。如果选定信号没有更多信号排队，该信号的待处理指示将被重置。

## 返回值

成功完成时（即 `set` 指定的信号之一处于待处理或被生成），`sigwaitinfo()` 和 `sigtimedwait()` 返回选定的信号编号。否则，函数返回 -1 并设置全局变量 `errno` 以指示错误。

## 错误

`sigtimedwait()` 系统调用在以下情况下失败：

**[`EAGAIN`]** 在指定的超时时间内，set 指定的信号均未被生成。

`sigtimedwait()` 和 `sigwaitinfo()` 系统调用在以下情况下失败：

**[`EINTR`]** 等待被未阻塞的、被捕获的信号中断。

`sigtimedwait()` 系统调用在以下情况下也可能失败：

**[`EINVAL`]** `timeout` 参数指定的 `tv_nsec` 值小于零或大于等于 10 亿。仅在 set 中无信号待处理且需要等待时，内核才检查此错误。

## 参见

[sigaction(2)](sigaction.2.md), [sigpending(2)](sigpending.2.md), [sigqueue(2)](sigqueue.2.md), [sigsuspend(2)](sigsuspend.2.md), [sigwait(2)](sigwait.2.md), [pause(3)](../gen/pause.3.md), [pthread_sigmask(3)](../man3/pthread_sigmask.3.md), [siginfo(3)](../man3/siginfo.3.md)

## 标准

`sigtimedwait()` 和 `sigwaitinfo()` 系统调用遵循 ISO/IEC 9945-1:1996 ("POSIX.1")。POSIX 未指定 `sigtimedwait()` 在 `timeout` 指针为 `NULL` 时的行为。
