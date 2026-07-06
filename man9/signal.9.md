# signal.9

`signal` — 内核信号函数

## 名称

`signal`, `SIGADDSET`, `SIGDELSET`, `SETEMPTYSET`, `SIGFILLSET`, `SIGISMEMBER`, `SIGISEMPTY`, `SIGNOTEMPTY`, `SIGSETEQ`, `SIGSETNEQ`, `SIGSETOR`, `SIGSETAND`, `SIGSETNAND`, `SIGSETCANTMASK`, `SIG_STOPSIGMASK`, `SIG_CONTSIGMASK`, `SIGPENDING`, `cursig`, `execsigs`, `issignal`, `killproc`, `pgsigio`, `postsig`, `sigexit`, `siginit`, `signotify`, `trapsignal`

## 概要

`#include <sys/param.h>`

`#include <sys/proc.h>`

`#include <sys/signalvar.h>`

`Ft void Fn SIGADDSET sigset_t set int signo Ft void Fn SIGDELSET sigset_t set int signo Ft void Fn SIGEMPTYSET sigset_t set Ft void Fn SIGFILLSET sigset_t set Ft int Fn SIGISMEMBER sigset_t set int signo Ft int Fn SIGISEMPTY sigset_t set Ft int Fn SIGNOTEMPTY sigset_t set Ft int Fn SIGSETEQ sigset_t set1 sigset_t set2 Ft int Fn SIGSETNEQ sigset_t set1 sigset_t set2 Ft void Fn SIGSETOR sigset_t set1 sigset_t set2 Ft void Fn SIGSETAND sigset_t set1 sigset_t set2 Ft void Fn SIGSETNAND sigset_t set1 sigset_t set2 Ft void Fn SIG_CANTMASK sigset_t set Ft void Fn SIG_STOPSIGMASK sigset_t set Ft void Fn SIG_CONTSIGMASK sigset_t set Ft int Fn SIGPENDING struct proc *p Ft int Fn cursig struct thread *td Ft void Fn execsigs struct proc *p Ft int Fn issignal struct thread *td Ft void Fn killproc struct proc *p char *why Ft void Fn pgsigio struct sigio **sigiop int sig int checkctty Ft void Fn postsig int sig Ft void Fn sigexit struct thread *td int signum Ft void Fn siginit struct proc *p Ft void Fn signotify struct thread *td Ft void Fn trapsignal struct thread *td int sig u_long code`

## 描述

`SIGADDSET` 宏将 `signo` 添加到 `set` 中。不确保 `signo` 是有效的信号编号。

`SIGDELSET` 宏从 `set` 中删除 `signo`。不确保 `signo` 是有效的信号编号。

`SIGEMPTYSET` 宏清除 `set` 中的所有信号。

`SIGFILLSET` 宏设置 `set` 中的所有信号。

`SIGISMEMBER` 宏确定 `signo` 是否在 `set` 中设置。

`SIGISEMPTY` 宏确定 `set` 是否未设置任何信号。

`SIGNOTEMPTY` 宏确定 `set` 是否设置了任何信号。

`SIGSETEQ` 宏确定两个信号集是否相等；即两者中设置了相同的信号。

`SIGSETNEQ` 宏确定两个信号集是否不同；即如果一个信号集中设置的信号在另一个信号集中未设置。

`SIGSETOR` 宏将 `set2` 中设置的信号或运算到 `set1` 中。

`SIGSETAND` 宏将 `set2` 中设置的信号与运算到 `set1` 中。

`SIGSETNAND` 宏将 `set2` 中设置的信号与非运算到 `set1` 中。

`SIG_CANTMASK` 宏从 `set` 中清除 `SIGKILL` 和 `SIGSTOP` 信号。这两个信号不能被阻塞或捕获，在操作信号的代码中使用 `SIG_CANTMASK` 来确保此策略得到执行。

`SIG_STOPSIGMASK` 宏从 `set` 中清除 `SIGSTOP`、`SIGTSTP`、`SIGTTIN` 和 `SIGTTOU` 信号。当进程等待子进程退出或执行 exec 时，以及进程在被挂起后继续时，使用 `SIG_STOPSIGMASK` 清除停止信号。

`SIG_CONTSIGMASK` 宏从 `set` 中清除 `SIGCONT` 信号。当进程被停止时调用 `SIG_CONTSIGMASK`。

`SIGPENDING` 宏确定给定进程是否有任何未屏蔽的挂起信号。如果进程有挂起信号且进程当前正在被跟踪，即使该信号被屏蔽，`SIGPENDING` 也将返回 true。

`cursig` 函数返回应该传递给进程 `td->td_proc` 的信号编号。如果没有挂起的信号，则返回零。

`execsigs` 函数重置进程的信号集和信号栈，为 execve(2) 做准备。在调用 `execsigs` 之前必须持有 `p` 的进程锁。

`issignal` 函数确定进程 `td->td_proc` 是否有任何应该被捕获的挂起信号，或导致此进程终止或中断其当前系统调用的挂起信号。如果进程 `td->td_proc` 当前正在被跟踪，被忽略的信号将被处理，并且进程始终被停止。停止信号由 `issignal` 立即处理并清除，除非进程是孤儿进程组的成员且停止信号源自 TTY。可能会获取和释放 `td->td_proc` 的进程自旋锁。在调用 `issignal` 之前必须锁定 `sigacts` 结构 `td->td_proc->p_sigacts`，并且可能在调用期间释放并重新获取。在调用 `issignal` 之前必须获取 `td->td_proc` 的进程锁，并且可能在调用期间释放并重新获取。系统进程和 init 不采取默认信号操作。

`killproc` 函数向 `p` 传递 `SIGKILL`。`why` 被记录为进程被杀死的原因。

`pgsigio` 函数向进程或进程组 `sigiop->sio_pgid` 发送信号 `sig`。如果 `checkctty` 为非零，则信号仅传递给进程组中具有控制终端的进程。如果 `sigiop->sio_pgid` 用于进程（> 0），则获取和释放 `sigiop->sio_proc` 的锁。如果 `sigiop->sio_pgid` 用于进程组（< 0），则获取和释放 `sigiop->sio_pgrp` 的进程组锁。获取和释放 `sigio_lock` 锁。

`postsig` 函数处理信号 `sig` 的实际传递。在内核被通知应传递信号（通过调用 `signotify`，这会设置标志 `PS_NEEDSIGCHK`）后，从 `ast` 调用 `postsig`。在调用 `postsig` 之前必须持有拥有 `curthread` 的进程的进程锁，且当前进程不能为 0。在调用 `postsig` 之前必须持有当前进程的 `p_sigacts` 字段的锁，并且可能释放并重新获取。

`sigexit` 函数使拥有 `td` 的进程以信号编号 `sig` 的返回值退出。如果需要，进程将转储核心。在调用 `sigexit` 之前必须持有拥有 `td` 的进程的进程锁。

`siginit` 函数在系统初始化期间被调用，使每个具有默认属性 `SA_IGNORE` 的信号（除 `SIGCONT` 外）被 `p` 忽略。获取和释放 `p` 的进程锁，以及 sigacts 结构 `p->p_sigacts` 的锁。`siginit` 曾经被调用的唯一进程是 `proc0`。

`signotify` 函数标记有未屏蔽的挂起信号应该由 `ast` 处理。在调用 `signotify` 之前必须持有进程 `td->td_proc` 的进程锁，并且获取和释放线程锁。

`trapsignal` 函数向进程 `td->td_proc` 发送作为陷阱结果的信号。如果进程未被跟踪且信号可以立即传递，`trapsignal` 将直接传递；否则，`trapsignal` 将调用 [psignal(9)](psignal.9.md) 来传递信号。获取和释放 `td->td_proc` 的进程锁。获取和释放 `td->td_proc` 的 `p_sigacts` 字段的锁。

## 返回值

`SIGISMEMBER`、`SIGISEMPTY`、`SIGNOTEMPTY`、`SIGSETEQ`、`SIGSETNEQ` 和 `SIGPENDING` 宏在检查的条件为真时都返回非零（true）；否则返回零（false）。

`cursig` 函数返回有效信号编号或零。

`issignal` 返回有效信号编号或零。

## 参见

pgsignal(9), [psignal(9)](psignal.9.md)

## 作者

本手册页由 Chad David <davidc@FreeBSD.org> 编写。
