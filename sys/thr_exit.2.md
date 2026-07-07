# thr_exit(2)

`thr_exit` — 终止当前线程

## 名称

`thr_exit`

## 库

Lb libc

## 概要

`#include <sys/thr.h>`

```c
void
thr_exit(long *state);
```

## 描述

*此函数用于实现线程功能。普通应用程序应改用 [pthread_exit(3)](../man3/pthread_exit.3.md)。*

`thr_exit` 系统调用终止当前内核调度线程。

如果 `state` 参数不为 `NULL`，该参数所指向的位置会被更新为一个任意的非零值，并随后对该位置执行 [_umtx_op(2)](_umtx_op.2.md) `UMTX_OP_WAKE` 操作。

终止进程中最后一个线程的尝试会被静默忽略。请使用 [_exit(2)](_exit.2.md) 系统调用来终止进程。

## 返回值

该函数不返回值。从该函数返回表示调用线程是进程中的最后一个线程。

## 参见

[_exit(2)](_exit.2.md), [_umtx_op(2)](_umtx_op.2.md), [thr_kill(2)](thr_kill.2.md), [thr_kill2(2)](thr_kill.2.md), [thr_new(2)](thr_new.2.md), [thr_self(2)](thr_self.2.md), [thr_set_name(2)](thr_set_name.2.md), [pthread_exit(3)](../man3/pthread_exit.3.md)

## 标准

`thr_exit` 系统调用是非标准的，由 Lb libthr 用于实现 IEEE Std 1003.1-2001 ("POSIX.1") [pthread(3)](../man3/pthread.3.md) 功能。

## 历史

`thr_exit` 系统调用首次出现于 FreeBSD 5.2。
