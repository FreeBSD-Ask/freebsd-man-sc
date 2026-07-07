# kill(2)

`kill` — 向进程发送信号

## 名称

`kill`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <signal.h>`

```c
int
kill(pid_t pid, int sig);
```

## 描述

`kill()` 系统调用将 `sig` 给定的信号发送到 `pid` 所指定的进程或进程组。`sig` 参数可以是 [sigaction(2)](sigaction.2.md) 中指定的信号之一，也可以为 0，此时仅执行错误检查但不实际发送信号。这可用于检查 `pid` 的有效性。

要使进程有权向 `pid` 指定的进程发送信号，用户必须是超级用户，或者接收进程的实际或保存的用户 ID 必须与发送进程的实际或有效用户 ID 匹配。一个例外是信号 SIGCONT，它始终可以发送给与发送者具有相同会话 ID 的任何进程。此外，如果 `security.bsd.conservative_signals` [sysctl(9)](../man9/sysctl.9.md) 设置为 1，用户不是超级用户，且接收者是 set-uid，则只能发送作业控制和终端控制信号（特别是仅 SIGKILL、SIGINT、SIGTERM、SIGALRM、SIGSTOP、SIGTTIN、SIGTTOU、SIGTSTP、SIGHUP、SIGUSR1、SIGUSR2）。

**如果** `pid` 大于零：`sig` 信号发送给 ID 等于 `pid` 的进程。

**如果** `pid` 为零：`sig` 信号发送给组 ID 等于发送者进程组 ID 且进程有权限的所有进程；这是 [killpg(2)](../compat-43/killpg.2.md) 的一个变体。

**如果** `pid` 为 -1：如果用户具有超级用户权限，信号将发送给除系统进程（设置了 `P_SYSTEM` 标志的进程）、ID 为 1 的进程（通常是 [init(8)](../man8/init.8.md)）以及发送信号的进程之外的所有进程。如果用户不是超级用户，信号将发送给调用者有权限的所有进程，但不包括发送信号的进程。只要有任何进程能被发送信号，就不会返回错误。

如果进程号为负但不为 -1，信号将发送给所有进程组 ID 等于该进程号绝对值的进程。这是 [killpg(2)](../compat-43/killpg.2.md) 的一个变体。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 errno 以指示错误。

## 错误

`kill()` 系统调用在以下情况下会失败且不会发送信号：

**[EINVAL]** `sig` 参数不是有效的信号编号。

**[ESRCH]** 找不到与 `pid` 指定的相对应的进程或进程组。

**[EPERM]** 发送进程没有权限向任何接收进程发送 `sig`。

## 参见

[getpgrp(2)](getpgrp.2.md), [getpid(2)](getpid.2.md), [killpg(2)](../compat-43/killpg.2.md), [sigaction(2)](sigaction.2.md), [sigqueue(2)](sigqueue.2.md), [raise(3)](../gen/raise.3.md), [init(8)](../man8/init.8.md)

## 标准

`kill()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1")。

## 历史

`kill()` 函数的一个版本首次出现于 Version 3 AT&T UNIX。信号编号在 Version 4 AT&T UNIX 中被添加到 `kill()` 函数。
