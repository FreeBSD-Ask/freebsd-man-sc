# pthread_mutex_consistent.3

`pthread_mutex_consistent` — 将 robust mutex 所保护的状态标记为一致

## 名称

`pthread_mutex_consistent`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_mutex_consistent(pthread_mutex_t *mutex);
```

## 描述

如果持有 robust mutex 的线程所在进程在持有该 mutex 时终止，mutex 将进入不一致状态，下一个获取该 mutex 锁的线程会通过返回值 `EOWNERDEAD` 收到该状态的通知。此时，在状态被标记为一致之前，mutex 无法正常使用。

`pthread_mutex_consistent` 在 `mutex` 参数指向处于不一致状态的已初始化 robust mutex 时调用，会将该 mutex 重新标记为一致。随后通过 `pthread_mutex_unlock` 或其他方式解锁该 mutex，将允许其他等待者加锁。

如果处于不一致状态的 mutex 在解锁前未通过调用 `pthread_mutex_consistent` 标记为一致，后续尝试加锁 `mutex` 的操作将由加锁函数返回 `ENOTRECOVERABLE` 错误。

## 返回值

如果成功，`pthread_mutex_consistent` 将返回零，否则返回一个错误编号以指示错误。

## 错误

`pthread_mutex_lock` 函数在以下情况下将失败：

**`[EINVAL]`** 由 `mutex` 参数指向的 mutex 不是 robust mutex，或者未处于不一致状态。

## 参见

[pthread_mutex_init(3)](pthread_mutex_init.3.md), [pthread_mutex_lock(3)](pthread_mutex_lock.3.md), [pthread_mutex_unlock(3)](pthread_mutex_unlock.3.md), pthread_mutexattr_setrobust(3)

## 标准

`pthread_mutex_consistent` 函数遵循 IEEE Std 1003.1-2008 (“POSIX.1”) 标准。
