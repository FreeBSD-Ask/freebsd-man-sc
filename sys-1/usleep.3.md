# usleep(3)

`usleep` — 挂起线程执行一段以微秒为单位的时间间隔

## 名称

`usleep`

## 库

libc

## 概要

```c
#include <unistd.h>

int
usleep(useconds_t microseconds);
```

## 描述

`usleep` 函数挂起调用线程的执行，直到 `microseconds` 微秒已过去，或者一个信号被传递到该线程且其动作是调用信号捕获函数或终止进程。系统活动可能使休眠时间延长一段不确定的时间。

该函数通过 nanosleep(2) 实现，暂停 `microseconds` 微秒或直到信号发生。因此，在本实现中，休眠对进程定时器的状态没有影响，且不对 `SIGALRM` 进行特殊处理。

## 返回值

如果成功，`usleep` 函数返回零；否则返回一个错误号以指示错误。

## 错误

`usleep` 函数在以下情况下将