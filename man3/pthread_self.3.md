# pthread_self(3)

`pthread_self` — 获取调用线程的 ID

## 名称

`pthread_self`

## 库

libpthread

## 概要

```c
#include <pthread.h>

pthread_t
pthread_self(void)
```

## 描述

`pthread_self` 函数返回调用线程的线程 ID。

## 返回值

`pthread_self` 函数返回调用线程的线程 ID。

## 错误

无。

## 参见

[pthread_create(3)](pthread_create.3.md), [pthread_equal(3)](pthread_equal.3.md), [pthread_getthreadid_np(3)](pthread_getthreadid_np.3.md)

## 标准

`pthread_self` 函数符合 ISO/IEC 9945-1:1996 ("POSIX.1") 规范。
