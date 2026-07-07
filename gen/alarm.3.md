# alarm(3)

`alarm` — 设置信号定时器警报

## 名称

`alarm` — 设置信号定时器警报

## 库

Lb libc

## 概要

```c
#include <unistd.h>

unsigned int
alarm(unsigned int seconds);
```

## 描述

> **注意** 此接口已被 setitimer(2) 取代。

`alarm` 函数设置一个定时器，在指定的 `seconds` 秒后向调用进程传递信号 `SIGALRM`。如果已通过 `alarm` 设置了警报但尚未传递，另一次 `alarm` 调用将取代先前的调用。请求 `alarm(0)` 会取消当前警报，且不会传递 SIGALRM 信号。

由于 setitimer(2) 的限制，允许的 `seconds` 最大值为 100,000,000。

## 返回值

`alarm` 的返回值是先前调用 `alarm` 时定时器上的剩余时间。如果当前未设置警报，返回值为 0。

## 参见

setitimer(2), [sigaction(2)](../sys/sigaction.2.md), [sigsuspend(2)](../sys/sigsuspend.2.md), [signal(3)](signal.3.md), [sleep(3)](sleep.3.md), [ualarm(3)](ualarm.3.md), [usleep(3)](usleep.3.md)

## 历史

`alarm` 系统调用出现于 Programmer's Workbench (PWB/UNIX)，并被移植到 Version 7 AT&T UNIX。在 4.1cBSD 中，它被重新实现为 setitimer(2) 系统调用的封装。
