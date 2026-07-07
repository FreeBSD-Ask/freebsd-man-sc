# pthread_sigqueue(3)

`pthread_sigqueue` — 向指定线程排队信号

## 名称

`pthread_sigqueue`

## 库

libpthread

## 概要

```c
#include <pthread.h>
#include <signal.h>

int
pthread_sigqueue(pthread_t thread, int sig, const union sigval value)
```

## 描述

`pthread_sigqueue` 函数将 `sig` 指定的信号排队到 `thread` 指定的线程。如果 `sig` 为 0，则执行错误检查，但不会实际发送信号。`value` 与信号一起排队，并在传递给信号处理函数的 `siginfo_t` 数据中变为可用。

`pthread_sigqueue` 函数类似于 sigqueue(2)，但针对的是当前进程中的线程而非进程。有关信号排队和递送选择的详细信息，请参见 sigqueue(2)。

## 返回值

如果成功，`pthread_sigqueue` 返回 0。否则返回一个错误号。

## 错误

`pthread_sigqueue` 函数将在以下情况失败：

**`[EAGAIN]`** 没有可用资源来排队信号。当前进程已经排队了 `SIGQUEUE_MAX` 个仍处于挂起状态的信号，或已超出系统范围的资源限制。

**`[ESRCH]`** `thread` 是无效的线程 ID。

**`[EINVAL]`** `sig` 是无效或不支持的信号编号。

## 参见

sigqueue(2)

## 标准

`pthread_sigqueue` 函数是 FreeBSD 扩展。其他操作系统中也有语义相同的同名函数。
