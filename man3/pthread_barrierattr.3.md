# pthread_barrierattr.3

`pthread_barrierattr_destroy` — 操作屏障属性对象

## 名称

`pthread_barrierattr_destroy`, `pthread_barrierattr_init`

## 库

Lb libpthread

## 概要

`#include <pthread.h>`

`Ft int Fn pthread_barrierattr_destroy pthread_barrierattr_t *attr Ft int Fo pthread_barrierattr_getpshared const pthread_barrierattr_t *restrict attr int *restrict pshared Fc Ft int Fn pthread_barrierattr_init pthread_barrierattr_t *attr Ft int Fo pthread_barrierattr_setpshared pthread_barrierattr_t *attr int pshared Fc`

## 描述

`Fn pthread_barrierattr_init` 函数将以默认属性初始化 `attr`。`Fn pthread_barrierattr_destroy` 函数将销毁 `attr` 并释放可能为其分配的任何资源。

`Fn pthread_barrierattr_getpshared` 函数将 `attr` 中进程共享属性的值放入 `pshared` 所指向的内存区域。`Fn pthread_barrierattr_setpshared` 函数将 `attr` 的进程共享属性设置为 `pshared` 中指定的值。参数 `pshared` 可取以下值之一：

**`PTHREAD_PROCESS_PRIVATE`** 其所附加的屏障对象只能由与创建该对象的进程相同的进程中的线程访问。

**`PTHREAD_PROCESS_SHARED`** 其所附加的屏障对象可由创建该对象的进程以外的进程中的线程访问。

## 返回值

若成功，所有这些函数都将返回零。否则将返回一个错误号以指示错误。

这些函数都不会返回 Er EINTR 。

## 错误

`Fn pthread_barrierattr_destroy`、`Fn pthread_barrierattr_getpshared` 和 `Fn pthread_barrierattr_setpshared` 函数可能因以下原因失败：

**[Er** EINVAL] `attr` 指定的值无效。

`Fn pthread_barrierattr_init` 函数在以下情况下会失败：

**[Er** ENOMEM] 没有足够的内存来初始化屏障属性对象 `attr`。

`Fn pthread_barrierattr_setpshared` 函数在以下情况下会失败：

**[Er** EINVAL] `pshared` 中指定的值不是允许的值之一。

## 参见

[pthread_barrier_destroy(3)](pthread_barrier_destroy.3.md), pthread_barrier_init(3), pthread_barrier_wait(3)

## 历史

`Fn pthread_barrierattr_*` 系列函数首次出现于 FreeBSD 5.2 的 Lb libkse 中，并在 FreeBSD 5.3 的 Lb libthr 中出现。对进程共享屏障的支持出现于 FreeBSD 11.0。
