# pthread_getspecific.3

`pthread_getspecific` — 获取线程特定数据值

## 名称

`pthread_getspecific`

## 库

libpthread

## 概要

```c
#include <pthread.h>

void *
pthread_getspecific(pthread_key_t key);
```

## 描述

`pthread_getspecific` 函数返回当前与调用线程的指定 `key` 绑定的值。

使用并非由 [pthread_key_create(3)](pthread_key_create.3.md) 获取的 `key` 值，或在 `key` 已被 [pthread_key_delete(3)](pthread_key_delete.3.md) 删除之后调用 `pthread_getspecific`，其效果未定义。

`pthread_getspecific` 函数可从线程特定数据析构函数中调用。对正在被销毁的线程特定数据键调用 `pthread_getspecific` 将返回值 NULL，除非该值在析构函数启动后被 [pthread_setspecific(3)](pthread_setspecific.3.md) 调用所改变。

## 返回值

`pthread_getspecific` 函数将返回与给定 `key` 关联的线程特定数据值。如果没有与 `key` 关联的线程特定数据值，则返回 NULL。

## 错误

无。

## 参见

[pthread_key_create(3)](pthread_key_create.3.md), [pthread_key_delete(3)](pthread_key_delete.3.md), [pthread_setspecific(3)](pthread_setspecific.3.md)

## 标准

`pthread_getspecific` 函数符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。
