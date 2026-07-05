# pthread_getcpuclockid.3

`pthread_getcpuclockid` — 访问线程 CPU 时间时钟

## 名称

`pthread_getcpuclockid`

## 库

libpthread

## 概要

```c
#include <pthread.h>
#include <time.h>

int
pthread_getcpuclockid(pthread_t thread_id, clockid_t *clock_id);
```

## 描述

如果 `thread_id` 所描述的线程存在，`pthread_getcpuclockid` 函数返回该线程的 CPU 时间时钟的时钟 ID。

## 返回值

成功完成后，`pthread_getcpuclockid` 返回零；否则返回一个错误号以指示错误。

## 错误

`pthread_getcpuclockid` 函数将在以下情况失败：

**`[ESRCH]`** `thread_id` 指定的值不引用一个存在的线程。

## 参见

clock_gettime(2)

## 标准

`pthread_getcpuclockid` 函数符合 IEEE Std 1003.1-2004 ("POSIX.1") 规范。

## 历史

`pthread_getcpuclockid` 函数首次出现于 FreeBSD 10.0。

## 作者

David Xu <davidxu@FreeBSD.org>
