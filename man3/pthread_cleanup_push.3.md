# pthread_cleanup_push.3

`pthread_cleanup_push` — 为线程退出添加清理函数

## 名称

`pthread_cleanup_push`

## 库

Lb libpthread

## 概要

`#include <pthread.h>`

`Ft void Fn pthread_cleanup_push void *cleanup_routinevoid * void *arg`

## 描述

`Fn pthread_cleanup_push` 函数将 `cleanup_routine` 添加到当前线程退出时调用的清理处理程序栈的栈顶。

调用 `cleanup_routine` 时，`arg` 将作为其唯一参数传递。

`Fn pthread_cleanup_push` 函数实现为一个打开新块的宏。对此函数的调用必须作为单独语句出现，并与同一词法作用域中后续对 [pthread_cleanup_pop(3)](pthread_cleanup_pop.3.md) 的调用配对。

## 返回值

`Fn pthread_cleanup_push` 函数不返回任何值。

## 错误

无

## 参见

[pthread_cleanup_pop(3)](pthread_cleanup_pop.3.md), [pthread_exit(3)](pthread_exit.3.md)

## 标准

`Fn pthread_cleanup_push` 函数遵循 ISO/IEC 9945-1:1996 ("POSIX.1") 标准。
