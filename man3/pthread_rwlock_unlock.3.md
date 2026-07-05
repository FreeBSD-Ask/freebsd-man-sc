# pthread_rwlock_unlock.3

`pthread_rwlock_unlock` — 释放读写锁

## 名称

`pthread_rwlock_unlock`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_rwlock_unlock(pthread_rwlock_t *lock)
```

## 描述

`pthread_rwlock_unlock` 函数用于释放先前通过 `pthread_rwlock_rdlock`、`pthread_rwlock_wrlock`、`pthread_rwlock_tryrdlock` 或 `pthread_rwlock_trywrlock` 获取的读写锁。

## 返回值

如果成功，`pthread_rwlock_unlock` 函数将返回零。否则将返回一个错误号以指示错误。

如果 `lock` 未被调用线程持有，结果未定义。

## 错误

`pthread_rwlock_unlock` 函数可能在以下情况失败：

**`[EINVAL]`** 由 `lock` 指定的值无效。

**`[EPERM]`** 当前线程未持有该读写锁。

## 参见

[pthread_rwlock_rdlock(3)](pthread_rwlock_rdlock.3.md), [pthread_rwlock_wrlock(3)](pthread_rwlock_wrlock.3.md)

## 标准

`pthread_rwlock_unlock` 函数预期符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。

## 历史

`pthread_rwlock_unlock` 函数首次出现于 FreeBSD 3.0。
