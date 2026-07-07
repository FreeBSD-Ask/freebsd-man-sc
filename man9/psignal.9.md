# psignal(9)

`psignal` — 向线程、进程或进程组发送信号

## 名称

`psignal`, `kern_psignal`, `pgsignal`, `tdsignal`

## 概要

```c
#include <sys/types.h>
```

```c
#include <sys/signalvar.h>
```

```c
void
kern_psignal(struct proc *p, int signum)

void
pgsignal(struct pgrp *pgrp, int signum, int checkctty)

void
tdsignal(struct thread *td, int signum)
```

## 描述

这些函数向线程或一个/多个进程发送信号。所有三个函数共有的参数 `signum` 应在 [1-`NSIG`] 范围内。

`kern_psignal` 函数向由进程结构 `p` 表示的进程发送信号 `signum`。`kern_psignal` 函数曾被称为 `psignal`，但为了消除与同名 libc 函数的名称冲突并促进代码重用而被重命名。除下面注明的少数例外，目标进程的信号处置会被更新，并被标记为可运行，因此信号的后续处理在上下文切换后在目标进程的上下文中完成。注意，`kern_psignal` 本身不会导致上下文切换。

在以下情况下，目标进程不会被标记为可运行：

- 目标进程正在不可中断地休眠。当进程从系统调用或陷阱返回时，将注意到该信号。
- 目标进程当前正在忽略该信号。
- 如果向采用默认操作的休眠进程发送停止信号（参见 sigaction(2)），进程将被停止而不被唤醒。
- `SIGCONT` 重启已停止的进程（或使其重新休眠），而不管信号操作如何（例如，被阻塞或忽略）。

如果目标进程正被跟踪，`kern_psignal` 的行为就像目标进程对 `signum` 采取默认操作。这允许跟踪进程被通知该信号。

`pgsignal` 函数向由 `pgrp` 描述的进程组中的每个成员发送信号 `signum`。如果 `checkctty` 非零，则仅向具有控制终端的进程发送信号。`pgsignal` 通过遍历由 `pgrp` 所指向的进程组结构中 `pg_members` 字段为首的进程列表，并适当地调用 `kern_psignal` 来实现。如果 `pgrp` 为 `NULL`，则不采取任何操作。

`tdsignal` 函数向由线程结构 `td` 表示的线程发送信号 `signum`。

## 参见

[sigaction(2)](../sys/sigaction.2.md), [signal(9)](signal.9.md), [tsleep(9)](sleep.9.md)

## 历史

`psignal` 函数在 FreeBSD 9.0 中被重命名为 `kern_psignal`。
