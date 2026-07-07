# pause(3)

`pause` — 等待信号时停止

## 名称

`pause` — 等待信号时停止

## 库

Lb libc

## 概要

```c
#include <unistd.h>

int
pause(void);
```

## 描述

> **注意** `pause` 已被 [sigsuspend(2)](../sys/sigsuspend.2.md) 取代。

`pause` 函数强制进程暂停，直到收到来自 [kill(2)](../sys/kill.2.md) 函数或间隔定时器的信号。（参见 setitimer(2)）在 `pause` 期间启动的信号处理程序终止时，`pause` 调用将返回。

## 返回值

始终返回 -1。

## 错误

`pause` 函数始终返回：

**[`EINTR`]** 调用被中断。

## 参见

[kill(2)](../sys/kill.2.md), [select(2)](../sys/select.2.md), [sigsuspend(2)](../sys/sigsuspend.2.md)

## 历史

`pause` 系统调用首次出现于 Programmer's Workbench (PWB/UNIX)，随后被移植到 Version 7 AT&T UNIX。在 4.2BSD 中，它被重新实现为 `sigpause` 和 `sigblock` 系统调用的封装；在 4.3BSD 中，被重新实现为 [sigsuspend(2)](../sys/sigsuspend.2.md) 和 [sigprocmask(2)](../sys/sigprocmask.2.md) 系统调用的封装。

