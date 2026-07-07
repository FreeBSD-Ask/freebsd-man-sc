# sigqueue(2)

`sigqueue` — 向进程排队信号（REALTIME）

## 名称

`sigqueue`

## 库

Lb libc

## 概要

```c
#include <signal.h>

int
sigqueue(pid_t pid, int signo, const union sigval value);
```

## 描述

`sigqueue()` 系统调用使 `signo` 指定的信号连同 `value` 指定的值发送给 `pid` 指定的进程。如果 `signo` 为零（空信号），执行错误检查但不实际发送信号。空信号可用于检查 PID 的有效性。

进程向另一个进程排队信号所需的权限条件与 [kill(2)](kill.2.md) 系统调用相同。`sigqueue()` 系统调用向 `pid` 参数指定的单个进程排队信号。

`sigqueue()` 系统调用立即返回。如果有可用资源排队信号，信号将被排队并发送给接收进程。

如果 `pid` 的值导致 `signo` 为发送进程生成，且 `signo` 未被调用线程阻塞，且没有其他线程解除阻塞 `signo` 或在 `sigwait()` 系统调用中等待 `signo`，则 `signo` 或至少一个待处理的未阻塞信号将在 `sigqueue()` 返回之前传递给调用线程。如果有 `SIGRTMIN` 到 `SIGRTMAX` 范围内的多个待处理信号被选择传递，选择编号最小的一个。实时信号与非实时信号之间，或多个待处理的非实时信号之间的选择顺序未指定。

作为 FreeBSD 扩展，`signo` 的值可以与以下标志进行或运算：

**`__SIGQUEUE_TID`** `pid` 参数是当前进程中某个线程的线程标识符，指定信号排入该指定线程的队列。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`sigqueue()` 系统调用在以下情况下将失败：

**[EAGAIN]** 没有可用资源排队信号。进程已经排队了 {`SIGQUEUE_MAX`} 个在接收方仍待处理的信号，或超出了系统范围的资源限制。

**[EINVAL]** `signo` 参数的值是无效或不支持的信号编号。

**[EPERM]** 进程没有向接收进程发送信号的适当权限。

**[ESRCH]** 进程 `pid` 不存在。

**[ESRCH]** 当前进程中不存在 ID 为 `pid` 的线程。

## 参见

[kill(2)](kill.2.md), [sigaction(2)](sigaction.2.md), [sigpending(2)](sigpending.2.md), [sigsuspend(2)](sigsuspend.2.md), [sigtimedwait(2)](sigtimedwait.2.md), [sigwait(2)](sigwait.2.md), [sigwaitinfo(2)](sigwaitinfo.2.md), [pause(3)](../man3/pause.3.md), [pthread_sigmask(3)](../man3/pthread_sigmask.3.md), [siginfo(3)](../man3/siginfo.3.md)

## 标准

`sigqueue()` 系统调用遵循 IEEE Std 1003.1-2004 ("POSIX.1")。

## 历史

对 POSIX 实时信号排队的支持首次出现于 FreeBSD 7.0。

## 注意事项

使用 `sigqueue` 向可能具有不同 ABI 的进程发送信号时（例如，一个是 32 位，另一个是 64 位），`value` 的 `sival_int` 成员可以可靠传递，但 `sival_ptr` 可能以依赖字节序的方式被截断，不可依赖。此外，许多指针完整性方案不允许向其他进程发送指针，此技术不应在旨在可移植的程序中使用。