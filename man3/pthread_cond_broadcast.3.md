# pthread_cond_broadcast.3

`pthread_cond_broadcast` — 唤醒所有等待条件变量的线程

## 名称

`pthread_cond_broadcast`

## 库

Lb libpthread

## 概要

`#include <pthread.h>`

`Ft int Fn pthread_cond_broadcast pthread_cond_t *cond`

## 描述

`Fn pthread_cond_broadcast` 函数唤醒所有等待条件变量 `cond` 的线程。

## 返回值

若成功，`Fn pthread_cond_broadcast` 函数将返回零，否则将返回一个错误号以指示错误。

## 错误

`Fn pthread_cond_broadcast` 函数在以下情况下会失败：

**[Er** EINVAL] `cond` 指定的值无效。

## 参见

[pthread_cond_destroy(3)](pthread_cond_destroy.3.md), [pthread_cond_init(3)](pthread_cond_init.3.md), [pthread_cond_signal(3)](pthread_cond_signal.3.md), [pthread_cond_timedwait(3)](pthread_cond_timedwait.3.md), [pthread_cond_wait(3)](pthread_cond_wait.3.md)

## 标准

`Fn pthread_cond_broadcast` 函数遵循 ISO/IEC 9945-1:1996 ("POSIX.1") 标准。
