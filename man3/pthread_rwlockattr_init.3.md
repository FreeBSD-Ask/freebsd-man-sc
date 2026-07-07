# pthread_rwlockattr_init(3)

`pthread_rwlockattr_init` — 初始化读写锁属性对象

## 名称

`pthread_rwlockattr_init`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_rwlockattr_init(pthread_rwlockattr_t *attr)
```

## 描述

`pthread_rwlockattr_init` 函数用于初始化读写锁属性对象。

## 返回值

如果成功，`pthread_rwlockattr_init` 函数将返回零。否则将返回一个错误号以指示错误。

## 错误

`pthread_rwlockattr_init` 函数将在以下情况失败：

**`[ENOMEM]`** 内存不足，无法初始化属性对象。

## 参见

[pthread_rwlock_init(3)](pthread_rwlock_init.3.md), [pthread_rwlockattr_destroy(3)](pthread_rwlockattr_destroy.3.md), [pthread_rwlockattr_getpshared(3)](pthread_rwlockattr_getpshared.3.md), [pthread_rwlockattr_setpshared(3)](pthread_rwlockattr_setpshared.3.md)

## 标准

`pthread_rwlockattr_init` 函数预期符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。

## 历史

`pthread_rwlockattr_init` 函数首次出现于 FreeBSD 3.0。
