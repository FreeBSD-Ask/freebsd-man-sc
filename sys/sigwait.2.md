# sigwait(2)

`sigwait` — 选择一组信号

## 名称

`sigwait`

## 库

Lb libc

## 概要

`#include <signal.h>`

```c
int
sigwait(const sigset_t * restrict set, int * restrict sig);
```

## 描述

`sigwait()` 系统调用选择一组由 `set` 指定的信号。如果所选信号均未处于待处理状态，`sigwait()` 会等待直到一个或多个所选信号被生成。然后 `sigwait()` 以原子方式从待处理信号集合（针对进程或当前线程）中清除其中一个所选信号，并将 `sig` 所指向的位置设置为被清除的信号编号。

调用 `sigwait()` 时，由 `set` 指定的信号应被阻塞。

如果有多个线程使用 `sigwait()` 等待同一信号，至多只有一个线程会从 `sigwait()` 返回该信号编号。如果当某信号为进程生成时，有多个线程因该信号阻塞在 `sigwait()` 中，则未指定哪个等待线程从 `sigwait()` 返回。如果信号是为特定线程生成的（例如通过 `pthread_kill()`），则只有该线程会返回。

在 `SIGRTMIN` 到 `SIGRTMAX` 范围内的多个待处理信号中，如果有任一信号被选中，则编号最低的那个会被选中。实时信号与非实时信号之间，或多个待处理的非实时信号之间的选择顺序未指定。

## 实现说明

`sigwait()` 函数实现为对 `__sys_sigwait()` 系统调用的封装，后者在遇到 `EINTR` 错误时会重试该调用。

## 返回值

如果成功，`sigwait()` 返回 0，并将 `sig` 所指向的位置设置为被清除的信号编号。否则返回一个错误编号。

## 错误

`sigwait()` 系统调用在以下情况下会失败：

**[EINVAL]** `set` 参数指定了一个或多个无效的信号编号。

## 参见

[sigaction(2)](sigaction.2.md), [sigpending(2)](sigpending.2.md), [sigqueue(2)](sigqueue.2.md), [sigsuspend(2)](sigsuspend.2.md), [sigtimedwait(2)](sigtimedwait.2.md), [sigwaitinfo(2)](sigwaitinfo.2.md), [pause(3)](../man3/pause.3.md), [pthread_sigmask(3)](../man3/pthread_sigmask.3.md)

## 标准

`sigwait()` 函数遵循 ISO/IEC 9945-1:1996 ("POSIX.1")。
