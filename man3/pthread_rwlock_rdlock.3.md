# pthread_rwlock_rdlock(3)

`pthread_rwlock_rdlock` — 获取读写锁用于读取

## 名称

`pthread_rwlock_rdlock`, `pthread_rwlock_tryrdlock`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_rwlock_rdlock(pthread_rwlock_t *lock)

int
pthread_rwlock_tryrdlock(pthread_rwlock_t *lock)
```

## 描述

`pthread_rwlock_rdlock` 函数获取 `lock` 上的读锁，前提是 `lock` 当前未被持有用于写入，且没有写者线程当前在该锁上阻塞。如果无法立即获取读锁，调用线程将阻塞直到能够获取该锁。

`pthread_rwlock_tryrdlock` 函数执行相同操作，但如果无法立即获取锁（即锁已被持有用于写入或有等待的写者），则不会阻塞。

一个线程可以同时持有多个读锁。若如此，必须为每次获取的锁调用一次 `pthread_rwlock_unlock`。

当调用线程已持有写锁时获取读锁，其结果未定义。

## 实现说明

为防止写者饥饿，写者优先于读者。

## 返回值

如果成功，`pthread_rwlock_rdlock` 和 `pthread_rwlock_tryrdlock` 函数将返回零。否则将返回一个错误号以指示错误。

## 错误

`pthread_rwlock_tryrdlock` 函数将在以下情况失败：

**`[EBUSY]`** 无法获取锁，因为写者持有该锁或正在该锁上阻塞。

`pthread_rwlock_rdlock` 和 `pthread_rwlock_tryrdlock` 函数可能在以下情况失败：

**`[EAGAIN]`** 无法获取锁，因为已超过 `lock` 的最大读锁数量。

**`[EDEADLK]`** 当前线程已持有 `lock` 用于写入。

**`[EINVAL]`** 由 `lock` 指定的值无效。

**`[ENOMEM]`** 内存不足，无法初始化锁（仅适用于静态初始化的锁）。

## 参见

[pthread_rwlock_init(3)](pthread_rwlock_init.3.md), pthread_rwlock_trywrlock(3), [pthread_rwlock_unlock(3)](pthread_rwlock_unlock.3.md), [pthread_rwlock_wrlock(3)](pthread_rwlock_wrlock.3.md)

## 标准

`pthread_rwlock_rdlock` 和 `pthread_rwlock_tryrdlock` 函数预期符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。

## 历史

`pthread_rwlock_rdlock` 函数首次出现于 FreeBSD 3.0。
