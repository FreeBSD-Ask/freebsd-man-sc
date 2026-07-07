# pthread_suspend_np(3)

`pthread_suspend_np` — 挂起一个线程

## 名称

`pthread_suspend_np`

## 库

Lb libpthread

## 概要

`#include <pthread_np.h>`

```c
int
pthread_suspend_np(pthread_t tid);
```

## 描述

`pthread_suspend_np()` 函数作用于一个活动线程时，会使其挂起。

在挂起的线程被恢复之前，`pthread_suspend_np()` 函数的调用者使用任何非异步信号安全函数都是不安全的，除非采取相应措施确保该线程在安全点挂起，但 [pthread_resume_np(3)](pthread_resume_np.3.md) 例外。

## 返回值

如果成功，`pthread_suspend_np()` 函数返回 0。否则，返回一个错误号以指示错误。

## 错误

`pthread_suspend_np()` 函数在以下情况下会失败：

**[`EDEADLK`]** 试图挂起当前线程。

**[`EINVAL`]** `tid` 参数指定的值无效。

**[`ESRCH`]** 找不到与 `tid` 参数指定的线程 ID 对应的线程。

## 参见

[pthread_np(3)](pthread_np.3.md), [pthread_resume_all_np(3)](pthread_resume_all_np.3.md), [pthread_resume_np(3)](pthread_resume_np.3.md), [pthread_suspend_all_np(3)](pthread_suspend_all_np.3.md)

## 作者

本手册页由 Alexey Zelkin <phantom@FreeBSD.org> 编写。
