# pthread_key_delete.3

`pthread_key_delete` — 删除线程特定数据键

## 名称

`pthread_key_delete`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_key_delete(pthread_key_t key);
```

## 描述

`pthread_key_delete` 函数删除先前由 [pthread_key_create(3)](pthread_key_create.3.md) 返回的线程特定数据键。在调用 `pthread_key_delete` 时，与 `key` 关联的线程特定数据值不必为 NULL。应用程序有责任释放任何应用存储，或对与被删除的键或任何线程中关联的线程特定数据相关的数据结构执行任何清理操作；这种清理可以在调用 `pthread_key_delete` 之前或之后进行。在调用 `pthread_key_delete` 之后任何试图使用 `key` 的行为都将导致未定义行为。

`pthread_key_delete` 函数可从析构函数中调用。`pthread_key_delete` 不会调用析构函数。先前可能与 `key` 关联的任何析构函数将不再在线程退出时被调用。

## 返回值

如果成功，`pthread_key_delete` 函数将返回零；否则将返回一个错误号以指示错误。

## 错误

`pthread_key_delete` 函数将在以下情况失败：

**`[EINVAL]`** `key` 值无效。

## 参见

[pthread_getspecific(3)](pthread_getspecific.3.md), [pthread_key_create(3)](pthread_key_create.3.md), [pthread_setspecific(3)](pthread_setspecific.3.md)

## 标准

`pthread_key_delete` 函数符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。
