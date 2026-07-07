# getsid(2)

`getsid` — 获取进程会话

## 名称

`getsid`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
pid_t
getsid(pid_t pid);
```

## 描述

`getsid()` 返回由 `pid` 标识的进程的会话 ID。如果 `pid` 为零，`getsid()` 返回当前进程的会话 ID。

## 返回值

成功完成时，`getsid()` 系统调用返回指定进程的会话 ID；否则返回 -1，并设置 `errno` 以指示错误。

## 错误

`getsid()` 系统调用在以下情况下会失败：

**[`ESRCH`]** 没有进程的进程 ID 等于 `pid`。

注意，实现可能将此系统调用限制为与调用进程在同一会话 ID 内的进程。

## 参见

[getpgid(2)](getpgrp.2.md), [getpgrp(2)](getpgrp.2.md), [setpgid(2)](setpgid.2.md), [setsid(2)](setsid.2.md), [termios(4)](../man4/termios.4.md)

## 历史

`getsid()` 系统调用出现于 FreeBSD 3.0。`getsid()` 系统调用源自 AT&T System V UNIX 中的用法。
