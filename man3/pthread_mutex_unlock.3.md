# pthread_mutex_unlock.3

`pthread_mutex_unlock` — 解锁 mutex

## 名称

`pthread_mutex_unlock`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_mutex_unlock(pthread_mutex_t *mutex);
```

## 描述

如果当前线程持有 `mutex` 的锁，`pthread_mutex_unlock` 函数将解锁 `mutex`。

如果 `mutex` 所指向的参数是一个处于不一致状态的 robust mutex，且在解锁前未调用 `pthread_mutex_consistent` 函数，则后续对 mutex `mutex` 的加锁尝试将被拒绝，加锁函数返回 `ENOTRECOVERABLE` 错误。

## 返回值

如果成功，`pthread_mutex_unlock` 将返回零，否则返回一个错误编号以指示错误。

## 错误

`pthread_mutex_unlock` 函数在以下情况下将失败：

**`[EINVAL]`** 由 `mutex` 指定的值无效。

**`[EPERM]`** 当前线程未持有 `mutex` 的锁。

## 参见

[pthread_mutex_destroy(3)](pthread_mutex_destroy.3.md), [pthread_mutex_init(3)](pthread_mutex_init.3.md), [pthread_mutex_lock(3)](pthread_mutex_lock.3.md), [pthread_mutex_trylock(3)](pthread_mutex_trylock.3.md)

## 标准

`pthread_mutex_unlock` 函数遵循 ISO/IEC 9945-1:1996 (“POSIX.1”) 标准。
