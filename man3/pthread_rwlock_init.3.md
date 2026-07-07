# pthread_rwlock_init(3)

`pthread_rwlock_init` — 初始化读写锁

## 名称

`pthread_rwlock_init`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_rwlock_init(pthread_rwlock_t *restrict lock,
    const pthread_rwlockattr_t *restrict attr);
```

## 描述

`pthread_rwlock_init` 函数用于初始化一个读写锁，其属性由 `attr` 指定。如果 `attr` 为 NULL，则使用默认的读写锁属性。

对已初始化的锁再次调用 `pthread_rwlock_init` 的结果是未定义的。

## 返回值

如果成功，`pthread_rwlock_init` 函数将返回零。否则返回一个错误编号以指示错误。

## 错误

`pthread_rwlock_init` 函数在以下情况下将失败：

**`[EAGAIN]`** 系统缺少初始化该锁所需的必要资源（除内存外）。

**`[ENOMEM]`** 内存不足，无法初始化该锁。

**`[EPERM]`** 调用者没有足够的权限执行该操作。

`pthread_rwlock_init` 函数在以下情况下可能失败：

**`[EBUSY]`** 系统检测到试图重新初始化由 `lock` 引用的对象，该对象是一个此前已初始化但尚未销毁的读写锁。

**`[EINVAL]`** 由 `attr` 指定的值无效。

## 参见

[pthread_rwlock_destroy(3)](pthread_rwlock_destroy.3.md), [pthread_rwlockattr_init(3)](pthread_rwlockattr_init.3.md), [pthread_rwlockattr_setpshared(3)](pthread_rwlockattr_setpshared.3.md)

## 标准

`pthread_rwlock_init` 函数预期遵循 Version 2 of the Single UNIX Specification (“SUSv2”) 标准。

## 历史

`pthread_rwlock_init` 函数首次出现于 FreeBSD 3.0。
