# pthread_rwlock_timedrdlock.3

`pthread_rwlock_timedrdlock` — 获取读写锁用于读取或在指定时间后放弃

## 名称

`pthread_rwlock_timedrdlock`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_rwlock_timedrdlock(pthread_rwlock_t *restrict rwlock,
    const struct timespec *restrict abs_timeout)
```

## 描述

该函数获取读写锁 `rwlock` 上的读锁。然而，如果在不等待其他线程解锁的情况下无法获取锁，则当 `abs_timeout` 到期时将终止此等待。

一个线程可以同时持有多个读锁。必须为每次获取的锁调用一次 [pthread_rwlock_unlock(3)](pthread_rwlock_unlock.3.md) 函数。

如果线程被信号中断，`pthread_rwlock_timedrdlock` 函数将在该线程从信号处理函数返回后自动重启。

如果调用时线程已持有 `rwlock` 的写锁，调用线程可能死锁。如果使用未初始化的读写锁调用此函数，结果未定义。

## 实现说明

为防止写者饥饿，写者优先于读者。

## 返回值

如果成功，`pthread_rwlock_timedrdlock` 函数将返回零。否则将返回一个错误号以指示错误。

此函数不会返回 `EINTR` 错误码。

## 错误

`pthread_rwlock_timedrdlock` 函数将在以下情况失败：

**`[ETIMEDOUT]`** 在指定的超时时间到期之前无法获取锁。

`pthread_rwlock_timedrdlock` 函数可能在以下情况失败：

**`[EAGAIN]`** 无法获取读锁，因为将超过 `rwlock` 的最大读锁数量。

**`[EDEADLK]`** 调用线程已持有 `rwlock` 的写锁。

**`[EINVAL]`** 由 `rwlock` 指定的值未指向已初始化的读写锁对象，或 `abs_timeout` 的纳秒值小于零或大于等于十亿。

## 参见

[pthread_rwlock_init(3)](pthread_rwlock_init.3.md), [pthread_rwlock_timedwrlock(3)](pthread_rwlock_timedwrlock.3.md), [pthread_rwlock_unlock(3)](pthread_rwlock_unlock.3.md)

## 标准

`pthread_rwlock_timedrdlock` 函数预期符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。

## 历史

`pthread_rwlock_timedrdlock` 函数首次出现于 FreeBSD 5.2。
