# pthread_suspend_all_np.3

`pthread_suspend_all_np` — 挂起所有活动线程

## 名称

`pthread_suspend_all_np`

## 库

Lb libpthread

## 概要

`#include <pthread_np.h>`

```c
void
pthread_suspend_all_np(void);
```

## 描述

`pthread_suspend_all_np()` 函数会使所有活动线程挂起。唯一的例外是当前线程，即调用 `pthread_suspend_all_np()` 函数的线程。

在挂起的线程被恢复之前，`pthread_suspend_all_np()` 函数的调用者使用任何非异步信号安全函数都是不安全的，除非采取相应措施确保所有线程都在安全点挂起，但 [pthread_resume_all_np(3)](pthread_resume_all_np.3.md) 例外。

## 参见

[pthread_np(3)](pthread_np.3.md), [pthread_resume_all_np(3)](pthread_resume_all_np.3.md), [pthread_resume_np(3)](pthread_resume_np.3.md), [pthread_suspend_np(3)](pthread_suspend_np.3.md)

## 作者

本手册页由 Alexey Zelkin <phantom@FreeBSD.org> 编写。
