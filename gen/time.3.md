# time(3)

`time` — 获取当日时间

## 名称

`time`

## 库

Lb libc

## 概要

`#include <time.h>`

`Ft time_t Fn time time_t *tloc`

## 描述

`time` 函数返回自 1970 年 1 月 1 日 0 时 0 分 0 秒协调世界时（UTC）以来的秒数。若发生错误，`time` 返回值 (`time_t`)-1。

若 `tloc` 非空，返回值也存储在 *`tloc` 中。

## 错误

`time` 函数可能因 [clock_gettime(2)](../man2/clock_gettime.2.md) 中描述的任何原因而失败。

## 参见

[clock_gettime(2)](../man2/clock_gettime.2.md), [gettimeofday(2)](../man2/gettimeofday.2.md), [ctime(3)](ctime.3.md)

## 标准

`time` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。

## 历史

`time` 系统调用首次出现于 Version 1 AT&T UNIX。直到 Version 3 AT&T UNIX，它返回自偶尔变化的 Epoch 以来的 60 Hz 滴答数，因为它是 32 位值，在两年多一点就会溢出。

在 Version 4 AT&T UNIX 中，返回值的粒度降低到整秒，将上述溢出推迟到 2038 年。

Version 7 AT&T UNIX 引入了 `ftime` 系统调用，返回毫秒级时间，但保留了 `gtime` 系统调用（在用户态暴露为 `time`）。`time` 本可以实现为 `ftime` 的包装，但并未如此实现。

4.1cBSD 实现了更高精度的 time 函数 `gettimeofday` 以替代 `ftime`，并基于此重新实现了 `time`。

自 FreeBSD 9 起，出于性能原因，`time` 的实现使用 `clock_gettime` CLOCK_SECOND 而非 `gettimeofday`。

## 缺陷

ISO/IEC 9899:1999 ("ISO C99") 和 IEEE Std 1003.1-2001 ("POSIX.1") 均未要求 `time` 在失败时设置 `errno`；因此，应用程序无法区分合法的时间值 -1（表示 1969 年最后一个 UTC 秒）和错误返回值。

遵循早期 C 和 POSIX 标准版本的系统（包括 FreeBSD 的旧版本）在错误情况下不会设置 *`tloc`。
