# pthread_cond_signal.3

`pthread_cond_signal` — 唤醒等待条件变量的线程

## 名称

`pthread_cond_signal`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_cond_signal(pthread_cond_t *cond);
```

## 描述

`pthread_cond_signal` 函数唤醒一个等待条件变量 `cond` 的线程。

## 返回值

如果成功，`pthread_cond_signal` 函数将返回零；否则将返回一个错误号以指示错误。

## 错误

`pthread_cond_signal` 函数将在以下情况失败：

**`[EINVAL]`** 由 `cond` 指定的值无效。

## 参见

[pthread_cond_broadcast(3)](pthread_cond_broadcast.3.md), [pthread_cond_destroy(3)](pthread_cond_destroy.3.md), [pthread_cond_init(3)](pthread_cond_init.3.md), [pthread_cond_timedwait(3)](pthread_cond_timedwait.3.md), [pthread_cond_wait(3)](pthread_cond_wait.3.md)

## 标准

`pthread_cond_signal` 函数符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。
