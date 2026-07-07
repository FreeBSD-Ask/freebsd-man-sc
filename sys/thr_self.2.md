# thr_self(2)

`thr_self` — 返回调用线程的线程标识符

## 名称

`thr_self`

## 库

Lb libc

## 概要

`#include <sys/thr.h>`

```c
int
thr_self(long *id);
```

## 描述

`thr_self()` 系统调用将当前内核调度线程的系统级线程标识符存储在 `id` 参数所指向的变量中。

线程标识符是范围从 `PID_MAX + 2`（100001）到 `INT_MAX` 的整数。线程标识符在任意时刻对于系统中的每个运行线程都保证是唯一的。线程退出后，标识符可能被重用。

## 返回值

如果成功，`thr_self()` 返回零；否则返回 -1，并设置 `errno` 以指示错误。

## 错误

`thr_self()` 操作可能返回以下错误：

**[`EFAULT`]** `id` 参数所指向的内存无效。

## 参见

[_umtx_op(2)](_umtx_op.2.md), [thr_exit(2)](thr_exit.2.md), [thr_kill(2)](thr_kill.2.md), [thr_kill2(2)](thr_kill.2.md), [thr_new(2)](thr_new.2.md), [thr_set_name(2)](thr_set_name.2.md), [pthread_getthreadid_np(3)](../man3/pthread_getthreadid_np.3.md), [pthread_self(3)](../man3/pthread_self.3.md)

## 标准

`thr_self()` 系统调用是非标准的，由 `libthr` 用于实现 IEEE Std 1003.1-2001 ("POSIX.1") [pthread(3)](../man3/pthread.3.md) 功能。

## 历史

`thr_self()` 系统调用首次出现于 FreeBSD 5.2。
