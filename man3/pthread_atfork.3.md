# pthread_atfork.3

`pthread_atfork` — 注册 fork 处理程序

## 名称

`pthread_atfork`

## 库

Lb libpthread

## 概要

`#include <pthread.h>`

`Ft int Fo pthread_atfork void *preparevoid void *parentvoid void *childvoid Fc`

## 描述

`Fn pthread_atfork` 函数声明在 fork(2) 之前和之后调用的 fork 处理程序，这些处理程序在调用 fork(2) 的线程上下文中执行。

通过 `Fn pthread_atfork` 注册的处理程序会在以下时机被调用：

**`prepare`** 在父进程中开始 fork(2) 处理之前。如果注册了多个 `prepare` 处理程序，它们将按注册顺序的相反顺序被调用。

**`parent`** 在父进程中 fork(2) 完成之后。如果注册了多个 `parent` 处理程序，它们将按注册顺序被调用。

**`child`** 在子进程中 fork(2) 处理完成之后。如果注册了多个 `child` 处理程序，它们将按注册顺序被调用。

如果在上述三个时机中的一个或多个不需要任何处理，可以传入空指针作为对应的 fork 处理程序。

## 返回值

若成功，`Fn pthread_atfork` 函数将返回零。否则将返回一个错误号以指示错误。

## 错误

`Fn pthread_atfork` 函数在以下情况下会失败：

**[Er** ENOMEM] 没有足够的表空间来记录 fork 处理程序地址。

## 参见

fork(2), [pthread(3)](pthread.3.md)

## 标准

`Fn pthread_atfork` 函数预期遵循 IEEE Std 1003.1 ("POSIX.1") 标准。

## 作者

本手册页由 Alex Vasylenko <lxv@omut.org> 编写。
