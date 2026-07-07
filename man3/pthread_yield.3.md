# pthread_yield(3)

`pthread_yield` — 让出当前线程的控制权

## 名称

`pthread_yield`

## 库

Lb libpthread

## 概要

`#include <pthread.h>`

```c
void
pthread_yield(void);
```

## 描述

`pthread_yield()` 强制正在运行的线程让出处理器，直到它再次成为其线程列表的头部。

## 参见

sched_yield(2)

## 标准

`pthread_yield()` 是对 IEEE Std 1003.1-2001 ("POSIX.1") 的非可移植（但相当常见）扩展。
