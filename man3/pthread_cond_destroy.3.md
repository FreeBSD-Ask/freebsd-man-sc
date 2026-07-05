# pthread_cond_destroy.3

`pthread_cond_destroy` — 销毁条件变量

## 名称

`pthread_cond_destroy`

## 库

Lb libpthread

## 概要

`#include <pthread.h>`

`Ft int Fn pthread_cond_destroy pthread_cond_t *cond`

## 描述

`Fn pthread_cond_destroy` 函数释放条件变量 `cond` 所分配的资源。

## 实现说明

在所有阻塞于条件变量上的线程被唤醒后，可以立即销毁该条件变量。

## 返回值

若成功，`Fn pthread_cond_destroy` 函数将返回零，否则将返回一个错误号以指示错误。

## 错误

`Fn pthread_cond_destroy` 函数在以下情况下会失败：

**[Er** EINVAL] `cond` 指定的值无效。

**[Er** EBUSY] 变量 `cond` 已被其他线程锁定。

## 参见

[pthread_cond_broadcast(3)](pthread_cond_broadcast.3.md), [pthread_cond_init(3)](pthread_cond_init.3.md), [pthread_cond_signal(3)](pthread_cond_signal.3.md), [pthread_cond_timedwait(3)](pthread_cond_timedwait.3.md), [pthread_cond_wait(3)](pthread_cond_wait.3.md)

## 标准

`Fn pthread_cond_destroy` 函数遵循 ISO/IEC 9945-1:1996 ("POSIX.1") 标准。
