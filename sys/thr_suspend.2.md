# thr_suspend(2)

`thr_suspend` — 挂起调用线程

## 名称

`thr_suspend`

## 库

Lb libc

## 概要

`#include <sys/thr.h>`

```c
int
thr_suspend(struct timespec *timeout);
```

## 描述

*此函数用于实现线程功能。普通应用程序应改用 [pthread_cond_timedwait(3)](../man3/pthread_cond_timedwait.3.md) 配合 [pthread_cond_broadcast(3)](../man3/pthread_cond_broadcast.3.md) 来实现典型的、在被挂起线程配合下的安全挂起，或在某些特定情况下使用 [pthread_suspend_np(3)](../man3/pthread_suspend_np.3.md) 和 [pthread_resume_np(3)](../man3/pthread_resume_np.3.md)。*

`thr_suspend` 系统调用将调用线程置于挂起状态，此时它不具备获得 CPU 时间的资格。此状态可在另一线程调用 [thr_wake(2)](thr_wake.2.md) 时、由 `timeout` 指定的时间间隔已过时、或通过向被挂起线程交付信号时退出。

如果 `timeout` 参数为 `NULL`，挂起状态只能通过显式的 `thr_wake` 或信号来终止。

如果在 `thr_suspend` 调用之前已交付了来自 [thr_wake(2)](thr_wake.2.md) 的唤醒，则线程不会进入挂起状态。相反，该调用会立即返回而不报错。

如果某线程先前以其自身的线程标识符调用了 [thr_wake(2)](thr_wake.2.md)，导致设置了内部内核标志以立即中止可中断睡眠并返回 `EINTR` 错误（参见 [thr_wake(2)](thr_wake.2.md)），则该标志会被清除。与从另一线程调用 [thr_wake(2)](thr_wake.2.md) 一样，下一次 `thr_suspend` 调用不会导致挂起。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置 `errno` 以指示错误。

## 错误

`thr_suspend` 操作返回以下错误：

**[`EFAULT`]** `timeout` 参数所指向的内存无效。

**[`ETIMEDOUT`]** 指定的超时时间已过。

**[`ETIMEDOUT`]** `timeout` 参数指定了零时间间隔。

**[`EINTR`]** 睡眠被信号中断。

## 参见

[ps(1)](../man1/ps.1.md), [thr_wake(2)](thr_wake.2.md), [pthread_resume_np(3)](../man3/pthread_resume_np.3.md), [pthread_suspend_np(3)](../man3/pthread_suspend_np.3.md)

## 标准

`thr_suspend` 系统调用是非标准的。

## 历史

`thr_suspend` 系统调用首次出现于 FreeBSD 5.2。
