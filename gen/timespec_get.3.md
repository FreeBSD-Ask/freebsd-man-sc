# timespec_get(3)

`timespec_get` — 获取当前日历时间

## 名称

`timespec_get`

## 库

Lb libc

## 概要

```c
#include <time.h>

int
timespec_get(struct timespec *ts, int base);
```

## 描述

`timespec_get` 函数将 `ts` 所指向的区间设置为基于 `base` 中指定时间基准的当前日历时间。

`TIME_UTC` 基准返回自纪元以来的时间。该时间以自 1970 年 1 月 1 日午夜（0 时）以来的秒和纳秒表示。在 FreeBSD 中，这对应于 `CLOCK_REALTIME`。

`TIME_MONOTONIC` 基准返回自过去某个未指定时间点起单调递增的时间。在 FreeBSD 中，这对应于 `CLOCK_MONOTONIC`。

## 返回值

`timespec_get` 函数成功时返回所传递的 `base` 值，失败时返回 `0`。

## 参见

[clock_gettime(2)](../sys/clock_gettime.2.md), [gettimeofday(2)](../sys/gettimeofday.2.md), [time(3)](time.3.md), [timespec_getres(3)](timespec_getres.3.md)

## 标准

带有 `TIME_UTC` 基准的 `timespec_get` 函数遵循 ISO/IEC 9899:2011 ("ISO C11")。`TIME_MONOTONIC` 基准遵循 ISO/IEC 9899:2023 ("ISO C23")。

## 历史

此接口首次出现于 FreeBSD 12。

## 作者

Kamil Rytarowski <kamil@NetBSD.org> Warner Losh <imp@FreeBSD.org>
