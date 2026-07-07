# thr_kill(2)

`thr_kill` — 向线程发送信号

## 名称

`thr_kill`

## 库

Lb libc

## 概要

`#include <sys/thr.h>`

```c
int
thr_kill(long id, int sig);

int
thr_kill2(pid_t pid, long id, int sig);
```

## 描述

`thr_kill()` 和 `thr_kill2()` 系统调用允许将 `sig` 参数指定的信号发送到进程中的某些线程。对于 `thr_kill()` 函数，被发送信号的线程始终限于当前进程。对于 `thr_kill2()` 函数，`pid` 参数指定包含要被发送信号的线程的进程。

`id` 参数指定哪些线程接收信号。如果 `id` 等于 -1，指定进程中的所有线程都会被发送信号。否则，只有线程标识符等于该参数的线程会被发送信号。

`sig` 参数定义所发送的信号。它必须是有效的信号编号或零。在后一种情况下，不会实际发送信号，该调用用于验证线程的存活状态。

信号在投递时，`siginfo` 的 `si_code` 设置为 `SI_LWP`。

## 返回值

如果成功，`thr_kill()` 和 `thr_kill2()` 将返回零，否则返回 -1，并设置 `errno` 以指示错误。

## 错误

`thr_kill()` 和 `thr_kill2()` 操作返回以下错误：

**[EINVAL]** `sig` 参数不为零且未指定有效信号。

**[ESRCH]** 找不到指定的进程或线程。

此外，`thr_kill2()` 可能返回以下错误：

**[EPERM]** 当前进程没有足够的权限来检查存在性或向指定进程发送信号。

## 参见

[_umtx_op(2)](_umtx_op.2.md), [kill(2)](kill.2.md), [thr_exit(2)](thr_exit.2.md), [thr_new(2)](thr_new.2.md), [thr_self(2)](thr_self.2.md), [thr_set_name(2)](thr_set_name.2.md), [pthread_kill(3)](../man3/pthread_kill.3.md), [signal(3)](../man3/signal.3.md)

## 标准

`thr_kill()` 和 `thr_kill2()` 系统调用是非标准的，由 Lb libthr 用于实现 IEEE Std 1003.1-2001 ("POSIX.1") 的 [pthread(3)](../man3/pthread.3.md) 功能。

## 历史

`thr_kill()` 和 `thr_kill2()` 系统调用首次出现于 FreeBSD 5.2。
