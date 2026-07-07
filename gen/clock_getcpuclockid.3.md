# clock_getcpuclockid(3)

`clock_getcpuclockid` — 访问进程 CPU 时间时钟

## 名称

`clock_getcpuclockid`

## 库

Lb libc

## 概要

`#include <time.h>`

```c
int
clock_getcpuclockid(pid_t pid, clockid_t *clock_id)
```

## 描述

`clock_getcpuclockid` 返回由 `pid` 指定的进程的 CPU 时间时钟的时钟 ID。如果 `pid` 所描述的进程存在且调用进程具有权限，该时钟的时钟 ID 将通过 `clock_id` 返回。

如果 `pid` 为零，`clock_getcpuclockid` 函数通过 `clock_id` 返回发起调用的进程的 CPU 时间时钟的时钟 ID。

## 返回值

成功完成时，`clock_getcpuclockid` 返回零；否则返回一个错误号以指示错误。

## 错误

`clock_getcpuclockid` 函数在以下情况将失败：

**[`EPERM`]** 请求进程没有权限访问该进程的 CPU 时间时钟。

**[`ESRCH`]** 找不到与 `pid` 指定的进程相对应的进程。

## 参见

[clock_gettime(2)](../sys/clock_gettime.2.md)

## 标准

`clock_getcpuclockid` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

`clock_getcpuclockid` 函数首次出现于 FreeBSD 10.0。

## 作者

David Xu <davidxu@FreeBSD.org>
