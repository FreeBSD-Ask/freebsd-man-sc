# pthread_cancel(3)

`pthread_cancel` — 取消线程的执行

## 名称

`pthread_cancel`

## 库

Lb libpthread

## 概要

`#include <pthread.h>`

`Ft int Fn pthread_cancel pthread_t thread`

## 描述

`Fn pthread_cancel` 函数请求取消 `thread`。目标线程的可取消状态和类型决定了取消何时生效。当取消操作被执行时，将调用 `thread` 的取消清理处理程序。当最后一个取消清理处理程序返回时，将为 `thread` 调用线程特定数据析构函数。当最后一个析构函数返回时，`thread` 将被终止。

目标线程中的取消处理相对于调用线程从 `Fn pthread_cancel` 返回是异步进行的。

状态 `PTHREAD_CANCELED` 会对与目标线程汇合的任何线程可见。符号常量 `PTHREAD_CANCELED` 展开为类型为 `Ft (void *)` 的常量表达式，其值不与内存中任何对象的指针匹配，也不与值 `NULL` 匹配。

## 返回值

若成功，`Fn pthread_cancel` 函数将返回零。否则将返回一个错误号以指示错误。

## 错误

`Fn pthread_cancel` 函数在以下情况下会失败：

**[Er** ESRCH] 找不到与给定线程 ID 对应的线程。

## 参见

[pthread_cleanup_pop(3)](pthread_cleanup_pop.3.md), [pthread_cleanup_push(3)](pthread_cleanup_push.3.md), [pthread_exit(3)](pthread_exit.3.md), [pthread_join(3)](pthread_join.3.md), pthread_setcancelstate(3), pthread_setcanceltype(3), [pthread_testcancel(3)](pthread_testcancel.3.md)

## 标准

`Fn pthread_cancel` 函数遵循 ISO/IEC 9945-1:1996 ("POSIX.1") 标准。

## 作者

本手册页由 David Leonard <d@openbsd.org> 为 OpenBSD 的 `Fn pthread_cancel` 实现编写。
