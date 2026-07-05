# pthread_key_create.3

`pthread_key_create` — 创建线程特定数据键

## 名称

`pthread_key_create`

## 库

libpthread

## 概要

```c
#include <pthread.h>

int
pthread_key_create(pthread_key_t *key, void (*destructor)(void *));
```

## 描述

`pthread_key_create` 函数创建一个对进程中所有线程可见的线程特定数据键。pthread_key_create 提供的键值是不透明对象，用于定位线程特定数据。虽然不同的线程可以使用相同的键值，但通过 [pthread_setspecific(3)](pthread_setspecific.3.md) 绑定到该键的值是按线程维护的，并在调用线程的生命周期内持续存在。

键创建时，所有活动线程中该新键关联的值为 NULL。线程创建时，新线程中所有已定义键关联的值为 NULL。

每个键值可选择关联一个析构函数。线程退出时，如果某个键值具有非 NULL 的析构函数指针，且该线程具有与该键关联的非 NULL 值，则以当前关联的值作为其唯一参数调用该指针所指向的函数。如果一个线程退出时有多个析构函数，析构函数的调用顺序未定义。

如果在为所有具有关联析构函数的非 NULL 值调用完所有析构函数之后，仍然存在一些具有关联析构函数的非 NULL 值，则重复该过程。如果在为未处理的非 NULL 值进行至少 `PTHREAD_DESTRUCTOR_ITERATIONS` 次析构函数调用迭代之后，仍然存在一些具有关联析构函数的非 NULL 值，实现将停止调用析构函数。

## 返回值

如果成功，`pthread_key_create` 函数会将新创建的键值存储在 `key` 指定的位置，并返回零；否则将返回一个错误号以指示错误。

## 错误

`pthread_key_create` 函数将在以下情况失败：

**`[EAGAIN]`** 系统缺乏必要的资源来创建另一个线程特定数据键，或超出系统对单个进程键总数 `PTHREAD_KEYS_MAX` 的限制。

**`[ENOMEM]`** 内存不足，无法创建键。

## 参见

[pthread_getspecific(3)](pthread_getspecific.3.md), [pthread_key_delete(3)](pthread_key_delete.3.md), [pthread_setspecific(3)](pthread_setspecific.3.md)

## 标准

`pthread_key_create` 函数符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。
