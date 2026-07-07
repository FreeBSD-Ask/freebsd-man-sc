# pthread_rwlockattr_setpshared(3)

`pthread_rwlockattr_setpshared` — 设置进程共享属性

## 名称

`pthread_rwlockattr_setpshared`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_rwlockattr_setpshared(pthread_rwlockattr_t *attr, int pshared)
```

## 描述

`pthread_rwlockattr_setpshared` 函数将 `attr` 的进程共享属性设置为 `pshared` 所引用的值。`pshared` 参数可能为以下两个值之一：

**`PTHREAD_PROCESS_SHARED`** 任何进程的任何线程，只要能访问读写锁所在的内存，都可以操作该锁。

**`PTHREAD_PROCESS_PRIVATE`** 只有在与初始化读写锁的线程同一进程内创建的线程才能操作该锁。此为默认值。

## 返回值

如果成功，`pthread_rwlockattr_setpshared` 函数将返回零。否则将返回一个错误号以指示错误。

## 错误

`pthread_rwlockattr_setpshared` 函数将在以下情况失败：

**`[EINVAL]`** 由 `attr` 或 `pshared` 指定的值无效。

## 参见

[pthread_rwlock_init(3)](pthread_rwlock_init.3.md), [pthread_rwlockattr_getpshared(3)](pthread_rwlockattr_getpshared.3.md), [pthread_rwlockattr_init(3)](pthread_rwlockattr_init.3.md)

## 标准

`pthread_rwlockattr_setpshared` 函数预期符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。

## 历史

`pthread_rwlockattr_setpshared` 函数首次出现于 FreeBSD 3.0。对进程共享读写锁的支持出现于 FreeBSD 11.0。
