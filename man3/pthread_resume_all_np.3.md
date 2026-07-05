# pthread_resume_all_np.3

`pthread_resume_all_np` — 恢复所有被挂起的线程

## 名称

`pthread_resume_all_np`

## 库

libpthread

## 概要

```c
#include <pthread_np.h>

void
pthread_resume_all_np(void);
```

## 描述

`pthread_resume_all_np` 函数会扫描所有活动线程，并恢复此前被挂起的线程。

## 参见

[pthread_attr_setcreatesuspend_np(3)](pthread_attr_setcreatesuspend_np.3.md), [pthread_np(3)](pthread_np.3.md), [pthread_resume_np(3)](pthread_resume_np.3.md), [pthread_suspend_all_np(3)](pthread_suspend_all_np.3.md), [pthread_suspend_np(3)](pthread_suspend_np.3.md)

## 作者

本手册页由 Alexey Zelkin <phantom@FreeBSD.org> 编写。
