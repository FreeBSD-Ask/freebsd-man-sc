# pthread_multi_np(3)

`pthread_multi_np` — 在多线程与单线程调度模式之间切换

## 名称

`pthread_multi_np`, `pthread_single_np`

## 库

libpthread

## 概要

```c
#include <pthread_np.h>

int
pthread_multi_np(void);

int
pthread_single_np(void);
```

## 描述

`pthread_single_np` 函数将进程切换到单线程模式，即挂起除当前线程以外的所有线程。此函数的语义类似于 [pthread_suspend_all_np(3)](pthread_suspend_all_np.3.md)。

`pthread_multi_np` 函数将进程切换到多线程模式。此函数的语义类似于 [pthread_resume_all_np(3)](pthread_resume_all_np.3.md)。

## 返回值

`pthread_multi_np` 和 `pthread_single_np` 函数始终返回 0。

## 参见

[pthread_np(3)](pthread_np.3.md), [pthread_resume_all_np(3)](pthread_resume_all_np.3.md), [pthread_suspend_all_np(3)](pthread_suspend_all_np.3.md)

## 作者

本手册页由 Alexey Zelkin <phantom@FreeBSD.org> 编写。
