# timeradd(3)

`timeradd` — 对 timeval 和 timespec 的操作

## 名称

`timeradd`, `timersub`, `timerclear`, `timerisset`, `timercmp`, `timespecadd`, `timespecsub`, `timespecclear`, `timespecisset`, `timespeccmp`

## 概要

```c
#include <sys/time.h>
```

```c
void
timeradd(struct timeval *a, struct timeval *b, struct timeval *res);

void
timersub(struct timeval *a, struct timeval *b, struct timeval *res);

void
timerclear(struct timeval *tvp);

int
timerisset(struct timeval *tvp);

int
timercmp(struct timeval *a, struct timeval *b, CMP);

void
timespecadd(struct timespec *a, struct timespec *b, struct timespec *res);

void
timespecsub(struct timespec *a, struct timespec *b, struct timespec *res);

void
timespecclear(struct timespec *ts);

int
timespecisset(struct timespec *ts);

int
timespeccmp(struct timespec *a, struct timespec *b, CMP);
```

## 描述

这些宏用于操作 `timeval` 和 `timespec` 结构，以便与 clock_gettime(2)、clock_settime(2)、gettimeofday(2) 和 settimeofday(2) 调用一起使用。`timeval` 结构定义在

```c
#include <sys/time.h>
```

中，如下：

```c
struct timeval {
	long	tv_sec;		/* 自 1970 年 1 月 1 日以来的秒数 */
	long	tv_usec;	/* 以及微秒 */
};
```

`timespec` 结构定义在

```c
#include <time.h>
```

中，如下：

```c
struct timespec {
	time_t tv_sec;		/* 秒 */
	long   tv_nsec;		/* 以及纳秒 */
};
```

`timeradd()` 和 `timespecadd()` 将存储在 `a` 中的时间信息与 `b` 相加，并将结果存储在 `res` 中。结果经过简化，使 `res->tv_usec` 或 `res->tv_nsec` 的值始终小于 1 秒。

`timersub()` 和 `timespecsub()` 从 `a` 中减去存储在 `b` 中的时间信息，并将结果存储在 `res` 中。

`timerclear()` 和 `timespecclear()` 将其参数初始化为 1970 年 1 月 1 日午夜（0 时）（即 Epoch）。

`timerisset()` 和 `timespecisset()` 在其参数设置为 Epoch 以外的任何时间值时返回真。

`timercmp()` 和 `timespeccmp()` 使用 `CMP` 中给定的比较运算符比较 `a` 和 `b`，并返回该比较的结果。

## 参见

clock_gettime(2), gettimeofday(2)

## 历史

`timeradd()` 系列宏从 NetBSD 1.1 导入，出现于 FreeBSD 2.2.6。`timespecadd()` 系列宏从 NetBSD 1.3 导入到 FreeBSD 3.0，但直到 FreeBSD 12.0 才暴露给用户空间。
