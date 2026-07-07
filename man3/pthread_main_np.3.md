# pthread_main_np(3)

`pthread_main_np` — 标识初始线程

## 名称

`pthread_main_np`

## 库

libpthread

## 概要

```c
#include <pthread_np.h>

int
pthread_main_np(void);
```

## 描述

`pthread_main_np` 函数用于在用户态线程环境中标识初始线程。其语义类似于 Solaris 的 `thr_main` 函数。

## 返回值

`pthread_main_np` 函数在调用线程为初始线程时返回 1，在调用线程不是初始线程时返回 0，在线程初始化尚未完成时返回 -1。

## 参见

[pthread_create(3)](pthread_create.3.md), [pthread_equal(3)](pthread_equal.3.md), [pthread_np(3)](pthread_np.3.md), [pthread_self(3)](pthread_self.3.md)

## 作者

本手册页由 Alexey Zelkin <phantom@FreeBSD.org> 编写。
