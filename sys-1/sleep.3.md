# sleep(3)

`sleep` — 挂起线程执行，挂起时间以秒为单位

## 名称

`sleep`

## 库

Lb libc

## 概要

```c
#include <unistd.h>

unsigned int
sleep(unsigned int seconds);
```

## 描述

`sleep` 函数挂起调用线程的执行，直到经过 `seconds` 秒或有信号投递到线程且其动作为调用信号捕获函数、终止线程或进程。系统活动可能使挂起时间延长不确定的量。

该函数通过 [nanosleep(2)](../sys/nanosleep.2.md) 实现，暂停 `seconds` 秒或直到信号发生。因此在本实现中，挂起不会影响进程定时器的状态，对 SIGALRM 也没有特殊处理。

## 返回值

若 `sleep` 函数因请求的时间已过而返回，返回值为零。若因信号投递而返回，返回值为未睡完的时间（请求时间减去实际睡眠时间），单位为秒。

## 参见

[nanosleep(2)](../sys/nanosleep.2.md), [usleep(3)](usleep.3.md)

## 标准

`sleep` 函数遵循 IEEE Std 1003.1-1990 ("POSIX.1")。

## 历史

`sleep` 函数首次出现于 Version 7 AT&T UNIX。
