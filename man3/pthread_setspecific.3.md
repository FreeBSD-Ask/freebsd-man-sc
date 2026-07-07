# pthread_setspecific(3)

`pthread_setspecific` — 设置线程特定数据值

## 名称

`pthread_setspecific`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_setspecific(pthread_key_t key, const void *value)
```

## 描述

`pthread_setspecific` 函数将线程特定值与先前通过调用 `pthread_key_create` 获取的 `key` 关联。不同线程可以将不同的值绑定到同一个键。这些值通常是指向为调用线程保留使用的动态分配内存块的指针。

使用非 `pthread_key_create` 获取的键值调用 `pthread_setspecific`，或在 `key` 已被 `pthread_key_delete` 删除后调用，其效果未定义。

`pthread_setspecific` 函数可以从线程特定数据析构函数中调用，但如果这样做导致在 `PTHREAD_DESTRUCTOR_ITERATIONS` 次析构函数调用后仍有非 NULL 的键值残留，可能导致存储丢失或无限循环。

## 返回值

如果成功，`pthread_setspecific` 函数将返回零。否则将返回一个错误号以指示错误。

## 错误

`pthread_setspecific` 函数将在以下情况失败：

**`[ENOMEM]`** 内存不足，无法将值与 `key` 关联。

**`[EINVAL]`** `key` 的值无效。

## 参见

[pthread_getspecific(3)](pthread_getspecific.3.md), [pthread_key_create(3)](pthread_key_create.3.md), [pthread_key_delete(3)](pthread_key_delete.3.md)

## 标准

`pthread_setspecific` 函数符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。
