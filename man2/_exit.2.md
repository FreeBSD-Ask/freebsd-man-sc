# _exit(2)

`_exit` — 终止调用进程

## 名称

`_exit`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
void
_exit(int status);
```

## 描述

`_exit()` 系统调用终止一个进程，会产生以下结果：

- 调用进程中打开的所有描述符都会被关闭。这可能会引起延迟，例如等待输出排空；处于此状态的进程无法被杀死，因为它已在终止过程中。
- 如果调用进程的父进程有未完成的 [wait(2)](wait.2.md) 调用或捕获 `SIGCHLD` 信号，父进程会收到调用进程终止的通知，并且 `status` 会按照 [wait(2)](wait.2.md) 的定义设置。
- 调用进程的所有现有子进程的父进程 ID 会被设置为调用进程的回收者（reaper）的进程 ID；回收者（通常是 init 进程）继承这些进程（参见 [procctl(2)](procctl.2.md)、[init(8)](../man8/init.8.md) 以及 [intro(2)](intro.2.md) 的 DEFINITIONS 章节）。
- 如果进程的终止导致某个进程组成为孤儿进程组（通常因为该组所有成员的父进程都已退出；参见 [intro(2)](intro.2.md) 中的“孤儿进程组”），并且孤儿进程组中有任何成员处于停止状态，那么 `SIGHUP` 信号和 `SIGCONT` 信号会被发送到新成为孤儿的进程组的所有成员。
- 如果该进程是控制进程（参见 [intro(2)](intro.2.md)），`SIGHUP` 信号会被发送到控制终端的前台进程组，并且对控制终端的所有当前访问权限都会被撤销。

大多数 C 程序调用库例程 [exit(3)](../man3/exit.3.md)，该例程在调用 `_exit()` 之前会刷新缓冲区、关闭流、删除临时文件、调用 [atexit(3)](../man3/atexit.3.md) 处理程序等。

## 返回值

`_exit()` 系统调用永远不会返回。

## 参见

[fork(2)](fork.2.md), [sigaction(2)](sigaction.2.md), [wait(2)](wait.2.md), [atexit(3)](../man3/atexit.3.md), [exit(3)](../man3/exit.3.md), [init(8)](../man8/init.8.md)

## 标准

`_exit()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1")。

## 历史

`_exit()` 函数首次出现于 Version 7 AT&T UNIX。
