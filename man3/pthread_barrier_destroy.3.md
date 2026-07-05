# pthread_barrier_destroy.3

`pthread_barrier_destroy` — 销毁、初始化或等待屏障对象

## 名称

`pthread_barrier_destroy`

## 库

Lb libpthread

## 概要

`#include <pthread.h>`

`Ft int Fn pthread_barrier_destroy pthread_barrier_t *barrier Ft int Fn pthread_barrier_init pthread_barrier_t *restrict barrier const pthread_barrierattr_t *attr unsigned count Ft int Fn pthread_barrier_wait pthread_barrier_t *barrier`

## 描述

`Fn pthread_barrier_init` 函数将使用 `attr` 中指定的属性初始化 `barrier`；如果 `attr` 为 `NULL`，则使用默认属性。在任意等待线程被释放之前必须调用 `Fn pthread_barrier_wait` 的线程数量由 `count` 指定。`Fn pthread_barrier_destroy` 函数将销毁 `barrier` 并释放可能为其分配的任何资源。

`Fn pthread_barrier_wait` 函数在 `barrier` 处同步调用线程。这些线程将被阻塞，无法继续推进，直到足够数量的线程调用此函数。在任意线程被释放之前必须调用此函数的线程数量由 `Fn pthread_barrier_init` 的 `count` 参数决定。一旦这些线程被释放，屏障将被重置。

## 实现说明

在 Lb libthr 中，`PTHREAD_BARRIER_SERIAL_THREAD` 返回值总是由最后一个到达屏障的线程返回。

## 返回值

若成功，`Fn pthread_barrier_destroy` 和 `Fn pthread_barrier_init` 都将返回零。否则将返回一个错误号以指示错误。如果对 `Fn pthread_barrier_wait` 的调用成功，除其中一个线程外，所有线程都将返回零。那一个线程将返回 `PTHREAD_BARRIER_SERIAL_THREAD`。否则将返回一个错误号以指示错误。

这些函数都不会返回 Er EINTR 。

## 错误

`Fn pthread_barrier_destroy` 函数在以下情况下会失败：

**[Er** EBUSY] 试图在 `barrier` 正在使用时销毁它。

`Fn pthread_barrier_destroy` 和 `Fn pthread_barrier_wait` 函数可能因以下原因失败：

**[Er** EINVAL] `barrier` 指定的值无效。

`Fn pthread_barrier_init` 函数在以下情况下会失败：

**[Er** EAGAIN] 系统缺乏内存以外的资源来初始化 `barrier`。

**[Er** EINVAL] `count` 参数小于 1。

**[Er** ENOMEM] 没有足够的内存来初始化 `barrier`。

## 参见

[pthread_barrierattr(3)](pthread_barrierattr.3.md)

## 历史

`Fn pthread_barrier_destroy`、`Fn pthread_barrier_init` 和 `Fn pthread_barrier_wait` 函数首次出现于 FreeBSD 5.2 的 Lb libkse 中，并在 FreeBSD 5.3 的 Lb libthr 中出现。
