# pthread_mutex_trylock.3

`pthread_mutex_trylock` — 尝试锁定 mutex 且不阻塞

## 名称

`pthread_mutex_trylock`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_mutex_trylock(pthread_mutex_t *mutex);
```

## 描述

`pthread_mutex_trylock` 函数锁定 `mutex`。如果 mutex 已被锁定，`pthread_mutex_trylock` 不会阻塞等待 mutex，而是返回一个错误状态。

## 返回值

如果成功，`pthread_mutex_trylock` 将返回零，否则返回一个错误编号以指示错误。

## 错误

`pthread_mutex_trylock` 函数在以下情况下将失败：

**`[EINVAL]`** 由 `mutex` 指定的值无效。

**`[EBUSY]`** mutex 已被锁定。

**`[EOWNERDEAD]`** `mutex` 参数指向一个 robust mutex，且持有该 mutex 锁的前一线程所在进程在持有锁时终止。锁已授予调用者，由新所有者负责将状态恢复一致。

**`[ENOTRECOVERABLE]`** 由 `mutex` 保护的状态不可恢复。

## 参见

[pthread_mutex_consistent(3)](pthread_mutex_consistent.3.md), [pthread_mutex_destroy(3)](pthread_mutex_destroy.3.md), [pthread_mutex_init(3)](pthread_mutex_init.3.md), [pthread_mutex_lock(3)](pthread_mutex_lock.3.md), [pthread_mutex_unlock(3)](pthread_mutex_unlock.3.md)

## 标准

`pthread_mutex_trylock` 函数遵循 ISO/IEC 9945-1:1996 (“POSIX.1”) 标准。
