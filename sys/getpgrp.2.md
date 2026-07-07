# getpgrp(2)

`getpgrp` — 获取进程组

## 名称

`getpgrp`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
pid_t
getpgrp(void);

pid_t
getpgid(pid_t pid);
```

## 描述

`getpgrp()` 返回当前进程的进程组。`getpgid()` 返回由 `pid` 标识的进程的进程组。如果 `pid` 为零，`getpgid()` 返回当前进程的进程组。

进程组用于分发信号，以及由终端仲裁对其输入的请求：与终端具有相同进程组的进程为前台，可以读取；其他进程如果尝试读取，将因信号而阻塞。

因此，诸如 [csh(1)](../man1/csh.1.md) 之类的程序使用该系统调用在实现作业控制时创建进程组。`tcgetpgrp()` 和 `tcsetpgrp()` 调用用于获取/设置控制终端的进程组。

## 返回值

`getpgrp()` 系统调用总是成功。成功完成时，`getpgid()` 系统调用返回指定进程的进程组；否则返回 -1，并设置 `errno` 以指示错误。

## 兼容性

此版本的 `getpgrp()` 与过去的 Berkeley 版本不同，不接受 `pid_t pid` 参数。IEEE Std 1003.1-1990 ("POSIX.1") 要求此不兼容性。

引自 IEEE Std 1003.1-1990 ("POSIX.1") 原理说明：

4.3BSD 提供了一个 `getpgrp()` 系统调用，返回指定进程的进程组 ID。尽管此函数用于支持作业控制，但所有已知的作业控制 shell 在使用此函数时总是指定调用进程本身。因此，更简单的 AT&T System V UNIX `getpgrp()` 即可满足需求，4.3BSD `getpgrp()` 的额外复杂性已从 POSIX.1 中省略。旧功能可由 `getpgid()` 系统调用提供。

## 错误

`getpgid()` 系统调用在以下情况下会失败：

**[`ESRCH`]** 没有进程的进程 ID 等于 `pid`。

## 参见

[getsid(2)](getsid.2.md), [setpgid(2)](setpgid.2.md), [termios(4)](../man4/termios.4.md)

## 标准

`getpgrp()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1") 规范。

## 历史

`getpgrp()` 系统调用出现于 4.0BSD。`getpgid()` 系统调用源自 AT&T System V Release 4 UNIX 中的用法。
