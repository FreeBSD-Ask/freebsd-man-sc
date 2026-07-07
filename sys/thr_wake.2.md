# thr_wake(2)

`thr_wake` — 唤醒挂起的线程

## 名称

`thr_wake`

## 库

Lb libc

## 概要

```c
#include <sys/thr.h>

int
thr_wake(long id);
```

## 描述

*此函数用于实现线程功能。普通应用程序应改用 [pthread_cond_timedwait(3)](../man3/pthread_cond_timedwait.3.md) 配合 [pthread_cond_broadcast(3)](../man3/pthread_cond_broadcast.3.md) 来实现典型的、在被挂起线程配合下的安全挂起，或在某些特定情况下使用 [pthread_suspend_np(3)](../man3/pthread_suspend_np.3.md) 和 [pthread_resume_np(3)](../man3/pthread_resume_np.3.md)。*

将调用线程的线程标识符（参见 [thr_self(2)](thr_self.2.md)）传递给 `thr_wake()` 会设置线程标志，使该线程在内核中的下一次可信号中断的睡眠立即失败并返回 `EINTR` 错误。该标志在可中断睡眠尝试或调用 [thr_suspend(2)](thr_suspend.2.md) 时被清除。系统线程库使用此机制实现取消功能。

如果 `id` 不等于当前线程标识符，则指定线程如果已被 [thr_suspend(2)](thr_suspend.2.md) 系统调用挂起，将被唤醒。如果在 `thr_wake()` 调用时该线程未被挂起，该唤醒会被记住，线程下一次尝试通过 [thr_suspend(2)](thr_suspend.2.md) 挂起自身时将立即成功返回。仅记住一次唤醒。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`thr_wake()` 操作返回以下错误：

**[`ESRCH`]** 未找到指定的线程，或该线程不属于调用线程所在的进程。

## 参见

[ps(1)](../man1/ps.1.md), [thr_self(2)](thr_self.2.md), [thr_suspend(2)](thr_suspend.2.md), [pthread_cancel(3)](../man3/pthread_cancel.3.md), [pthread_resume_np(3)](../man3/pthread_resume_np.3.md), [pthread_suspend_np(3)](../man3/pthread_suspend_np.3.md)

## 标准

`thr_suspend()` 系统调用是非标准的，由 `libthr` 用于实现 IEEE Std 1003.1-2001 ("POSIX.1") [pthread(3)](../man3/pthread.3.md) 功能。

## 历史

`thr_suspend()` 系统调用首次出现于 FreeBSD 5.2。
