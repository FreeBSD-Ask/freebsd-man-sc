# pthread_cleanup_pop.3

`pthread_cleanup_pop` — 调用首个清理例程

## 名称

`pthread_cleanup_pop`

## 库

Lb libpthread

## 概要

`#include <pthread.h>`

`Ft void Fn pthread_cleanup_pop int execute`

## 描述

`Fn pthread_cleanup_pop` 函数从当前线程的清理例程栈中弹出栈顶清理例程；如果 `execute` 非零，则执行该函数。如果没有清理例程，则 `Fn pthread_cleanup_pop` 不做任何操作。

`Fn pthread_cleanup_pop` 函数实现为一个关闭一个块的宏。对此函数的调用必须作为单独语句出现，并与同一词法作用域中先前对 [pthread_cleanup_push(3)](pthread_cleanup_push.3.md) 的调用配对。

## 返回值

`Fn pthread_cleanup_pop` 函数不返回任何值。

## 错误

无

## 参见

[pthread_cleanup_push(3)](pthread_cleanup_push.3.md), [pthread_exit(3)](pthread_exit.3.md)

## 标准

`Fn pthread_cleanup_pop` 函数遵循 ISO/IEC 9945-1:1996 ("POSIX.1") 标准。
