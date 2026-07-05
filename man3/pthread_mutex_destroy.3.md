# pthread_mutex_destroy.3

`pthread_mutex_destroy` — 释放为 mutex 分配的资源

## 名称

`pthread_mutex_destroy`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_mutex_destroy(pthread_mutex_t *mutex);
```

## 描述

`pthread_mutex_destroy` 函数释放为 `mutex` 分配的资源。

## 返回值

如果成功，`pthread_mutex_destroy` 将返回零，否则返回一个错误编号以指示错误。

## 错误

`pthread_mutex_destroy` 函数在以下情况下将失败：

**`[EINVAL]`** 由 `mutex` 指定的值无效。

**`[EBUSY]`** mutex 已被其他线程锁定。

## 参见

[pthread_mutex_init(3)](pthread_mutex_init.3.md), [pthread_mutex_lock(3)](pthread_mutex_lock.3.md), [pthread_mutex_trylock(3)](pthread_mutex_trylock.3.md), [pthread_mutex_unlock(3)](pthread_mutex_unlock.3.md)

## 标准

`pthread_mutex_destroy` 函数遵循 ISO/IEC 9945-1:1996 (“POSIX.1”) 标准。
