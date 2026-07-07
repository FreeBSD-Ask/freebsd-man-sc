# pthread_mutexattr_getkind_np(3)

`pthread_mutexattr_getkind_np` — mutex 属性操作（遗留）

## 名称

`pthread_mutexattr_getkind_np`, `pthread_mutexattr_setkind_np`

## 库

libpthread

## 概要

```c
#include <pthread_np.h>

int
pthread_mutexattr_getkind_np(pthread_mutexattr_t attr);

int
pthread_mutexattr_setkind_np(pthread_mutexattr_t *attr, int kind);
```

## 描述

*这些函数是 mutex 类型操作的已弃用且不可移植的实现。*

建议改用 pthread_mutexattr_gettype(3) 和 pthread_mutexattr_settype(3) 函数。

## 返回值

`pthread_mutexattr_getkind_np` 函数在成功时返回一个表示 mutex 属性 `attr` “类型”的正值；否则返回 -1，并设置全局变量 `errno` 以指示错误。

`pthread_mutexattr_setkind_np` 函数在成功时返回 0，否则返回一个错误编号以指示错误。

## 错误

`pthread_mutexattr_getkind_np` 和 `pthread_mutexattr_setkind_np` 函数在以下情况下将失败：

**`[EINVAL]`** 由 `attr` 指定的值无效。

## 参见

[pthread_mutex_destroy(3)](pthread_mutex_destroy.3.md), [pthread_mutex_init(3)](pthread_mutex_init.3.md), pthread_mutexattr_gettype(3), pthread_mutexattr_settype(3), [pthread_np(3)](pthread_np.3.md)
