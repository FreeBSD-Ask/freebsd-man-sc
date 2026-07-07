# microuptime(9)

`binuptime` — 获取自启动以来经过的时间

## 名称

`binuptime`, `getbinuptime`, `microuptime`, `getmicrouptime`, `nanouptime`, `getnanouptime`, `sbinuptime`, `getsbinuptime`

## 概要

```c
#include <sys/time.h>
```

```c
void
binuptime(struct bintime *bt)

void
getbinuptime(struct bintime *bt)

void
microuptime(struct timeval *tv)

void
getmicrouptime(struct timeval *tv)

void
nanouptime(struct timespec *ts)

void
getnanouptime(struct timespec *tsp)

sbintime_t
sbinuptime(void)

sbintime_t
getsbinuptime(void)
```

## 描述

`binuptime` 和 `getbinuptime` 函数将自启动以来经过的时间以 `struct bintime` 的形式存储在 `bt` 所指定的地址处。`microuptime` 和 `getmicrouptime` 函数执行相同的功能，但将经过的时间记录为 `struct timeval`。类似地，`nanouptime` 和 `getnanouptime` 函数将经过的时间存储为 `struct timespec`。`sbinuptime` 和 `getsbinuptime` 函数以 `sbintime_t` 的形式返回自启动以来经过的时间。

`binuptime`、`microuptime`、`nanouptime` 和 `sbinuptime` 函数总是查询 timecounter 以尽可能精确地返回当前时间。而 `getbinuptime`、`getmicrouptime`、`getnanouptime` 和 `getsbinuptime` 函数是抽象层，返回精度较低但获取速度更快的时间。

`getbinuptime`、`getmicrouptime`、`getnanouptime` 和 `getsbinuptime` 函数的设计意图是在定时器精度与执行时间之间贯彻用户的偏好。

## 参见

bintime(9), [get_cyclecount(9)](get_cyclecount.9.md), getbintime(9), getmicrotime(9), getnanotime(9), [microtime(9)](microtime.9.md), nanotime(9), [tvtohz(9)](tvtohz.9.md)

## 作者

本手册页由 Kelly Yancey <kbyanc@posi.net> 编写。
