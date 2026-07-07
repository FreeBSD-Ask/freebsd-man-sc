# microtime(9)

`bintime` — 获取当前时间

## 名称

`bintime`, `getbintime`, `microtime`, `getmicrotime`, `nanotime`, `getnanotime`

## 概要

```c
#include <sys/time.h>
```

```c
void
bintime(struct bintime *bt)

void
getbintime(struct bintime *bt)

void
microtime(struct timeval *tv)

void
getmicrotime(struct timeval *tv)

void
nanotime(struct timespec *ts)

void
getnanotime(struct timespec *tsp)
```

## 描述

`bintime` 和 `getbintime` 函数将系统时间以 `struct bintime` 的形式存储在 `bt` 所指定的地址处。`microtime` 和 `getmicrotime` 函数执行相同的功能，但将时间记录为 `struct timeval`。类似地，`nanotime` 和 `getnanotime` 函数将时间存储为 `struct timespec`。

`bintime`、`microtime` 和 `nanotime` 函数总是查询 timecounter 以尽可能精确地返回当前时间。而 `getbintime`、`getmicrotime` 和 `getnanotime` 函数是抽象层，返回精度较低但获取速度更快的时间。

`getbintime`、`getmicrotime` 和 `getnanotime` 函数的设计意图是在定时器精度与执行时间之间贯彻用户的偏好。

## 参见

binuptime(9), getbinuptime(9), getmicrouptime(9), getnanouptime(9), [microuptime(9)](microuptime.9.md), nanouptime(9), [tvtohz(9)](tvtohz.9.md)

## 历史

`bintime` 函数首次出现于 FreeBSD 5.0。`microtime` 和 `nanotime` 函数首次出现于 FreeBSD 3.0，但自 4.4BSD 起就以其他形式存在。

## 作者

本手册页由 Kelly Yancey <kbyanc@posi.net> 编写。
