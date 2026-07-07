# pthread_rwlock_wrlock(3)

`pthread_rwlock_wrlock` — 获取读写锁用于写入

## 名称

`pthread_rwlock_wrlock`, `pthread_rwlock_trywrlock`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_rwlock_wrlock(pthread_rwlock_t *lock)

int
pthread_rwlock_trywrlock(pthread_rwlock_t *lock)
```

## 描述

`pthread_rwlock_wrlock` 函数阻塞直到能够获取 `lock` 上的写锁。`pthread_rwlock_trywrlock` 函数执行相同操作，但如果无法立即获取锁则不会阻塞。

如果调用时调用线程已持有该锁，结果未定义。

## 实现说明

为防止写者饥饿，写者优先于读者。

## 返回值

如果成功，`pthread_rwlock_wrlock` 和 `pthread_rwlock_trywrlock` 函数将返回零。否则将返回一个错误号以指示错误。

## 错误

`pthread_rwlock_trywrlock` 函数将在以下情况失败：

**`[EBUSY]`** 调用线程无法在不阻塞的情况下获取锁。

`pthread_rwlock_wrlock` 和 `pthread_rwlock_trywrlock` 函数可能在以下情况失败：

**`[EDEADLK]`** 调用线程已持有该读写锁（用于读取或写入）。

**`[EINVAL]`** 由 `lock` 指定的值无效。

**`[ENOMEM]`** 内存不足，无法初始化锁（仅适用于静态初始化的锁）。

## 参见

[pthread_rwlock_init(3)](pthread_rwlock_init.3.md), [pthread_rwlock_rdlock(3)](pthread_rwlock_rdlock.3.md), pthread_rwlock_tryrdlock(3), [pthread_rwlock_unlock(3)](pthread_rwlock_unlock.3.md)

## 标准

`pthread_rwlock_wrlock` 和 `pthread_rwlock_trywrlock` 函数预期符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。

## 历史

`pthread_rwlock_wrlock` 函数首次出现于 FreeBSD 3.0。
