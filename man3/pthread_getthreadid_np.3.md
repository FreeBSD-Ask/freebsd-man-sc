# pthread_getthreadid_np.3

`pthread_getthreadid_np` — 获取调用线程的整数 ID

## 名称

`pthread_getthreadid_np`

## 库

libpthread

## 概要

```c
#include <pthread_np.h>

int
pthread_getthreadid_np(void);
```

## 描述

`pthread_getthreadid_np` 函数返回调用线程的唯一整数 ID。其语义类似于 AIX 的 `pthread_getthreadid_np` 函数。

## 返回值

`pthread_getthreadid_np` 函数返回调用线程的线程整数 ID。

## 错误

无。

## 参见

[pthread_np(3)](pthread_np.3.md), [pthread_self(3)](pthread_self.3.md)

## 作者

本手册页由 Jung-uk Kim <jkim@FreeBSD.org> 编写。
