# gettimeofday(2)

`gettimeofday` — 获取/设置日期和时间

## 名称

`gettimeofday`, `settimeofday`

## 库

Lb libc

## 概要

`#include <sys/time.h>`

```c
int
gettimeofday(struct timeval *tp, struct timezone *tzp);

int
settimeofday(const struct timeval *tp, const struct timezone *tzp);
```

## 描述

*注意：* `gettimeofday()` 函数（但不包括 `settimeofday()`）已过时。详情请参见标准章节。

系统的当前格林威治时间和当前时区通过 `gettimeofday()` 系统调用获取，通过 `settimeofday()` 系统调用设置。时间以自 1970 年 1 月 1 日午夜（0 时）起的秒数和微秒数表示。系统时钟的分辨率取决于硬件，时间可能被连续更新或以“滴答”方式更新。如果 `tp` 或 `tzp` 为 NULL，则不会返回或设置相关的时间信息。

`tp` 和 `tzp` 所指向的结构定义在

`#include <sys/time.h>`

中：

```c
struct timeval {
	time_t		tv_sec;		/* 秒 */
	suseconds_t	tv_usec;	/* 微秒 */
};
struct timezone {
	int	tz_minuteswest; /* 格林威治以西的分钟数 */
	int	tz_dsttime;	/* 夏令时校正类型 */
};
```

`timezone` 结构指示本地时区（以格林威治以西的分钟数衡量），以及一个标志，如果非零，则表示一年中适当时段本地适用夏令时。内核通常不跟踪这些值，它们通常返回为零。使用 [localtime(3)](../stdtime/ctime.3.md) 查找当前活动时区的偏移量。

只有超级用户可以设置时间或时区。如果系统运行在 securelevel >= 2（参见 [init(8)](../man8/init.8.md)），时间最多只能前进或后退一秒。此限制是为了防止恶意超级用户在文件上设置任意时间戳。即使系统处于安全模式，也可以使用 [adjtime(2)](adjtime.2.md) 系统调用无限制地向后调整系统时间。

## 返回值

`gettimeofday()` 和 `settimeofday()` 系统调用在成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

以下错误码可能被设置在 `errno` 中：

**[`EINVAL`]** 提供的 `timeval` 值无效。

**[`EPERM`]** 非超级用户试图设置时间。

## 参见

[date(1)](../man1/date.1.md), [adjtime(2)](adjtime.2.md), [clock_gettime(2)](clock_gettime.2.md), [ctime(3)](../stdtime/ctime.3.md), [timeradd(3)](../man3/timeradd.3.md), [clocks(7)](../man7/clocks.7.md)

## 标准

`gettimeofday()` 函数被认为是过时的，IEEE Std 1003.1-2008, 2017 Edition ("POSIX.1") 不鼓励使用它。应用程序应改用 [clock_gettime(2)](clock_gettime.2.md) 函数。

## 历史

`gettimeofday()` 系统调用首次出现于 4.2BSD。
