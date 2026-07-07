# pthread_resume_np(3)

`pthread_resume_np` — 恢复被挂起的线程

## 名称

`pthread_resume_np`

## 库

libpthread

## 概要

```c
#include <pthread_np.h>

int
pthread_resume_np(pthread_t tid);
```

## 描述

`pthread_resume_np` 函数在被挂起的线程上调用时，将使其恢复执行。如果由 `tid` 参数指定的线程未被挂起，则不执行任何操作。

## 返回值

如果成功，`pthread_resume_np` 函数返回 0。否则返回一个错误编号以指示错误。

## 错误

`pthread_resume_np` 函数在以下情况下将失败：

**`[EINVAL]`** 由 `tid` 参数指定的值无效。

**`[ESRCH]`** 找不到与 `tid` 参数指定的线程 ID 对应的线程。

## 参见

[pthread_attr_setcreatesuspend_np(3)](pthread_attr_setcreatesuspend_np.3.md), [pthread_np(3)](pthread_np.3.md), [pthread_resume_all_np(3)](pthread_resume_all_np.3.md), [pthread_suspend_all_np(3)](pthread_suspend_all_np.3.md), [pthread_suspend_np(3)](pthread_suspend_np.3.md)

## 作者

本手册页由 Alexey Zelkin <phantom@FreeBSD.org> 编写。
