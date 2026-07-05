# pthread_sigmask.3

`pthread_sigmask` — 检查和/或更改线程的信号掩码

## 名称

`pthread_sigmask`

## 库

libpthread

## 概要

```c
#include <pthread.h>
#include <signal.h>

int
pthread_sigmask(int how, const sigset_t * restrict set,
    sigset_t * restrict oset)
```

## 描述

`pthread_sigmask` 函数检查和/或更改调用线程的信号掩码。

如果 `set` 不是 `NULL`，它指定要修改的信号集，`how` 指定将信号掩码设置为什么：

**`SIG_BLOCK`** 当前掩码与 `set` 的并集。

**`SIG_UNBLOCK`** 当前掩码与 `set` 补集的交集。

**`SIG_SETMASK`** `set`。

如果 `oset` 不是 `NULL`，先前的信号掩码存储在 `oset` 所指向的位置。

`SIGKILL` 和 `SIGSTOP` 无法被阻塞，如果包含在信号掩码中将被静默忽略。

## 返回值

如果成功，`pthread_sigmask` 返回 0。否则返回一个错误号。

## 错误

`pthread_sigmask` 函数将在以下情况失败：

**`[EINVAL]`** `how` 不是定义的值之一。

## 参见

sigaction(2), sigpending(2), sigprocmask(2), sigsuspend(2), sigsetops(3)

## 标准

`pthread_sigmask` 函数符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。
