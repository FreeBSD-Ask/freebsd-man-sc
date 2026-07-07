# sigsuspend.2

`sigsuspend` — 原子地释放被屏蔽的信号并等待中断

## 名称

`sigsuspend`

## 库

Lb libc

## 概要

`#include <signal.h>`

```c
int
sigsuspend(const sigset_t *sigmask)
```

## 描述

`sigsuspend()` 系统调用临时将屏蔽信号集更改为 `sigmask` 所指向的集合，然后等待信号到达；返回时恢复先前的屏蔽信号集。信号掩码集通常为空，表示在调用期间所有信号都被解除屏蔽。

在正常使用中，使用 [sigprocmask(2)](sigprocmask.2.md) 屏蔽一个信号以开始临界区，检查在信号发生时修改的变量以确定没有工作要做，然后使用 `sigsuspend()` 与 [sigprocmask(2)](sigprocmask.2.md) 返回的先前掩码来暂停进程等待工作。

## 返回值

`sigsuspend()` 系统调用总是因被中断而终止，返回 -1，并将 `errno` 设置为 `EINTR`。

## 参见

[pselect(2)](pselect.2.md), [sigaction(2)](sigaction.2.md), [sigpending(2)](sigpending.2.md), [sigprocmask(2)](sigprocmask.2.md), sigtimedwait(2), [sigwait(2)](sigwait.2.md), [sigwaitinfo(2)](sigwaitinfo.2.md), [sigsetops(3)](../gen/sigsetops.3.md)

## 标准

`sigsuspend()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1")。
