# pthread_attr_setcreatesuspend_np(3)

`pthread_attr_setcreatesuspend_np` — 为创建挂起线程准备属性

## 名称

`pthread_attr_setcreatesuspend_np`

## 库

Lb libpthread

## 概要

`#include <pthread_np.h>`

`Ft int Fn pthread_attr_setcreatesuspend_np pthread_attr_t *attr`

## 描述

`Fn pthread_attr_setcreatesuspend_np` 指示 [pthread_create(3)](pthread_create.3.md)，使用 `attr` 属性创建的线程应以挂起状态创建，直到通过调用 `Fn pthread_resume_np` 或 `Fn pthread_resume_all_np` 显式恢复。

## 返回值

Rv -std pthread_attr_setcreatesuspend_np

## 错误

`Fn pthread_attr_setcreatesuspend_np` 函数在以下情况下会失败：

**[Er** EINVAL] `attr` 指定的值无效。

## 参见

pthread_attr_destroy(3), pthread_attr_init(3), [pthread_create(3)](pthread_create.3.md), [pthread_np(3)](pthread_np.3.md), [pthread_resume_all_np(3)](pthread_resume_all_np.3.md), [pthread_resume_np(3)](pthread_resume_np.3.md)

## 作者

本手册页由 Alexey Zelkin <phantom@FreeBSD.org> 编写。
