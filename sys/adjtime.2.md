# adjtime(2)

`adjtime` — 校正时间以同步系统时钟

## 名称

`adjtime`

## 库

Lb libc

## 概要

`#include <sys/time.h>`

```c
int
adjtime(const struct timeval *delta, struct timeval *olddelta);
```

## 描述

`adjtime()` 系统调用对系统时间（即 [gettimeofday(2)](gettimeofday.2.md) 所返回的时间）进行小幅调整，按 timeval 结构体 `delta` 指定的时间值向前或向后推进。

如果 `delta` 为负，时钟会通过比正常更慢地递增来减速，直至校正完成。如果 `delta` 为正，则使用比正常更大的递增量。`delta` 也可以是 `NULL` 指针，用于获取 `olddelta` 而不作任何调整。

用于执行校正的偏移量通常小于百分之一。因此，时间始终是单调递增的函数。前一次 `adjtime()` 调用发起的时间校正可能在再次调用 `adjtime()` 时尚未完成。如果 `olddelta` 不是 `NULL` 指针，则其指向的结构体在返回时将包含前一次调用中尚未校正的微秒数。

该调用可供在局域网中同步各台计算机时钟的时间服务器使用。此类时间服务器会放慢某些机器的时钟，加快其他机器的时钟，使它们趋于平均网络时间。

`adjtime()` 系统调用仅限超级用户使用。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 errno 以指示错误。

## 错误

`adjtime()` 系统调用在以下情况下会失败：

**[EFAULT]** 参数指向进程分配地址空间之外。

**[EPERM]** 进程的有效用户 ID 不是超级用户。

## 参见

[date(1)](../man1/date.1.md), [gettimeofday(2)](gettimeofday.2.md)

> R. Gusella, S. Zatti, "TSP: The Time Synchronization Protocol for UNIX 4.3BSD".

## 历史

`adjtime()` 系统调用首次出现于 4.3BSD。
