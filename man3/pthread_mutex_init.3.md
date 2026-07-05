# pthread_mutex_init.3

`pthread_mutex_init` — 创建 mutex

## 名称

`pthread_mutex_init`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_mutex_init(pthread_mutex_t *restrict mutex,
    const pthread_mutexattr_t *restrict attr);
```

## 描述

`pthread_mutex_init` 函数创建一个新的 mutex，其属性由 `attr` 指定。如果 `attr` 为 NULL，则使用默认属性。

## 返回值

如果成功，`pthread_mutex_init` 将返回零并将新的 mutex ID 存入 `mutex`，否则返回一个错误编号以指示错误。

## 错误

`pthread_mutex_init` 函数在以下情况下将失败：

**`[EINVAL]`** 由 `attr` 指定的值无效。

**`[ENOMEM]`** 进程无法分配足够的内存来创建另一个 mutex。

## 参见

[pthread_mutex_destroy(3)](pthread_mutex_destroy.3.md), [pthread_mutex_lock(3)](pthread_mutex_lock.3.md), [pthread_mutex_trylock(3)](pthread_mutex_trylock.3.md), [pthread_mutex_unlock(3)](pthread_mutex_unlock.3.md), [pthread_mutexattr(3)](pthread_mutexattr.3.md)

## 标准

`pthread_mutex_init` 函数遵循 ISO/IEC 9945-1:1996 (“POSIX.1”) 标准。
