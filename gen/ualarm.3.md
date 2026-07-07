# ualarm(3)

`ualarm` — 在指定时间后调度信号

## 名称

`ualarm` — 在指定时间后调度信号

## 库

Lb libc

## 概要

```c
#include <unistd.h>

useconds_t
ualarm(useconds_t microseconds, useconds_t interval);
```

## 描述

> **注意** 这是 [setitimer(2)](../sys/setitimer.2.md) 的简化接口。

`ualarm` 函数在等待 `microseconds` 微秒后发出终止信号 `SIGALRM`。系统活动或处理调用所花费的时间可能导致轻微延迟。

如果 `interval` 参数非零，则在定时器到期后（即经过 `microseconds` 微秒后），每隔 `interval` 微秒向进程发送一次 `SIGALRM` 信号。

由于 [setitimer(2)](../sys/setitimer.2.md) 的限制，`microseconds` 和 `interval` 的最大值限定为 100,000,000,000,000（前提是该值能装入无符号整数）。

## 返回值

当信号成功被捕获时，`ualarm` 返回时钟上剩余的时间量。

## 注释

一微秒等于 0.000001 秒。

## 参见

[getitimer(2)](../sys/getitimer.2.md), [setitimer(2)](../sys/setitimer.2.md), [sigaction(2)](../sys/sigaction.2.md), [sigsuspend(2)](../sys/sigsuspend.2.md), [alarm(3)](alarm.3.md), [signal(3)](signal.3.md), [sleep(3)](sleep.3.md), [usleep(3)](usleep.3.md)

## 历史

`ualarm` 函数出现于 4.3BSD。
