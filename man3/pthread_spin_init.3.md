# pthread_spin_init(3)

`pthread_spin_init` — 初始化或销毁自旋锁

## 名称

`pthread_spin_init`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_spin_init(pthread_spinlock_t *lock, int pshared)

int
pthread_spin_destroy(pthread_spinlock_t *lock)
```

## 描述

`pthread_spin_init` 函数将 `lock` 初始化为未锁定状态，并分配开始使用它所需的任何资源。如果 `pshared` 设置为 `PTHREAD_PROCESS_SHARED`，任何线程，无论是否属于创建自旋锁的进程，只要能访问 `lock` 所在的内存区域，都可以使用 `lock`。如果设置为 `PTHREAD_PROCESS_PRIVATE`，则只能被同一进程内的线程使用。

`pthread_spin_destroy` 函数将销毁 `lock` 并释放为其分配的任何资源。

## 返回值

如果成功，`pthread_spin_init` 和 `pthread_spin_destroy` 都将返回零。否则将返回一个错误号以指示错误。

这两个函数都不会返回 `EINTR`。

## 错误

`pthread_spin_init` 和 `pthread_spin_destroy` 函数将在以下情况失败：

**`[EBUSY]`** 尝试在 `lock` 正在使用时初始化或销毁它。

**`[EINVAL]`** 由 `lock` 指定的值无效。

`pthread_spin_init` 函数将在以下情况失败：

**`[EAGAIN]`** 除内存外资源不足，无法初始化 `lock`。

**`[ENOMEM]`** 内存不足，无法初始化 `lock`。

## 参见

[pthread_spin_lock(3)](pthread_spin_lock.3.md), pthread_spin_unlock(3)

## 历史

`pthread_spin_init` 和 `pthread_spin_destroy` 函数首次出现于 FreeBSD 5.2 的 libkse 中，以及 FreeBSD 5.3 的 libthr 中。对进程共享自旋锁的支持出现于 FreeBSD 11.0。
