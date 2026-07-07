# wait(2)

`wait` — 等待进程状态改变

## 名称

`wait`, `waitid`, `waitpid`, `wait3`, `wait4`, `wait6`

## 库

Lb libc

## 概要

```c
#include <sys/wait.h>

pid_t
wait(int *status);

pid_t
waitpid(pid_t wpid, int *status, int options);
```

```c
#include <signal.h>

int
waitid(idtype_t idtype, id_t id, siginfo_t *info, int options);
```

```c
#include <sys/time.h>
#include <sys/resource.h>

pid_t
wait3(int *status, int options, struct rusage *rusage);

pid_t
wait4(pid_t wpid, int *status, int options, struct rusage *rusage);

pid_t
wait6(idtype_t idtype, id_t id, int *status, int options,
    struct __wrusage *wrusage, siginfo_t *infop);
```

## 描述

`wait()` 函数挂起其调用线程的执行，直到子进程的状态信息可用或收到信号。从成功的 `wait()` 调用返回时，`status` 区域包含有关报告状态改变的进程的信息，定义如下。

`wait4()` 和 `wait6()` 系统调用为需要等待特定子进程、需要子进程累积的资源使用统计或需要选项的程序提供了更通用的接口。其他 wait 函数使用 `wait4()` 或 `wait6()` 实现。

`wait6()` 函数是该家族中最通用的函数，其独特特性如下：

所有要等待的所需进程状态必须在 `options` 中显式指定。`wait()`、`waitpid()`、`wait3()` 和 `wait4()` 函数都隐式等待已退出和已陷入的进程，但 `waitid()` 和 `wait6()` 函数要求显式指定相应的 `WEXITED` 和 `WTRAPPED` 标志。这允许等待经历了其他状态改变的进程，而无需同时处理已终止进程的退出状态。

`wait6()` 函数接受一个 `wrusage` 参数，指向定义为以下的结构：

```c
struct __wrusage {
	struct rusage   wru_self;
	struct rusage   wru_children;
};
```

这允许调用进程收集来自其自身子进程以及孙进程的资源使用统计。当不需要资源使用统计时，此指针可以为 `NULL`。

最后一个参数 `infop` 必须是 `NULL` 或指向 `siginfo_t` 结构的指针。如果非 `NULL`，该结构将填充与进程状态改变时传递的 `SIGCHLD` 信号相同的数据。

要查询的子进程集合由参数 `idtype` 和 `id` 指定。分开的 `idtype` 和 `id` 参数除了进程 ID 和进程组 ID 外，还支持许多其他类型的标识符。

- 如果 `idtype` 为 `P_PID`，`waitid()` 和 `wait6()` 等待进程 ID 等于 `(pid_t)id` 的子进程。
- 如果 `idtype` 为 `P_PGID`，`waitid()` 和 `wait6()` 等待进程组 ID 等于 `(pid_t)id` 的子进程。
- 如果 `idtype` 为 `P_ALL`，`waitid()` 和 `wait6()` 等待任何子进程，`id` 被忽略。
- 如果 `idtype` 为 `P_PID` 或 `P_PGID` 且 `id` 为零，`waitid()` 和 `wait6()` 等待与调用者在同一进程组中的任何子进程。

此 `waitid()` 和 `wait6()` 实现支持的非标准标识符类型有：

**`P_UID`** 等待有效用户 ID 等于 `(uid_t)id` 的进程。

**`P_GID`** 等待有效组 ID 等于 `(gid_t)id` 的进程。

**`P_SID`** 等待会话 ID 等于 `id` 的进程。如果子进程启动了自己的会话，其会话 ID 将与其进程 ID 相同。否则，子进程的会话 ID 将与调用者的会话 ID 匹配。

**`P_JAILID`** 等待 jail 标识符等于 `id` 的 jail 内的进程。

对于 `waitpid()` 和 `wait4()` 函数，单个 `wpid` 参数指定要等待的子进程集合。

- 如果 `wpid` 为 -1，调用等待任何子进程。
- 如果 `wpid` 为 0，调用等待调用者进程组中的任何子进程。
- 如果 `wpid` 大于零，调用等待进程 ID 为 `wpid` 的进程。
- 如果 `wpid` 小于 -1，调用等待任何进程组 ID 等于 `wpid` 绝对值的进程。

`status` 参数定义如下。

`options` 参数包含以下任意选项的按位或。

**`WCONTINUED`** 报告通过接收 `SIGCONT` 信号而从作业控制停止状态继续的选定进程的状态。[ptrace(2)](ptrace.2.md) 也可以使进程继续，当发出 `PT_DETACH` 请求以分离调试器时。

**`WNOHANG`** 当没有进程希望报告状态时不阻塞。

**`WUNTRACED`** 报告由于 `SIGTTIN`、`SIGTTOU`、`SIGTSTP` 或 `SIGSTOP` 信号而停止的选定进程的状态。

**`WSTOPPED`** `WUNTRACED` 的别名。

**`WTRAPPED`** 报告通过 [ptrace(2)](ptrace.2.md) 跟踪并已陷入或到达断点的选定进程的状态。此标志对于 `wait()`、`waitpid()`、`wait3()` 和 `wait4()` 函数隐式设置。对于 `waitid()` 和 `wait6()` 函数，如果期望来自已陷入进程的状态报告，则必须显式在 `options` 中包含此标志。

**`WEXITED`** 报告已终止的选定进程的状态。此标志对于 `wait()`、`waitpid()`、`wait3()` 和 `wait4()` 函数隐式设置。对于 `waitid()` 和 `wait6()` 函数，如果期望来自已终止进程的状态报告，则必须显式在 `options` 中包含此标志。

**`WNOWAIT`** 使返回状态的进程保持可等待状态。该进程可以在此次调用完成后再次被等待。

对于 `waitid()` 和 `wait6()` 函数，必须至少指定 `WEXITED`、`WUNTRACED`、`WSTOPPED`、`WTRAPPED` 或 `WCONTINUED` 选项中的一个。否则，调用将没有事件可报告。为避免在这种情况下无限期挂起，这些函数返回 -1 并将 `errno` 设置为 `EINVAL`。

如果 `rusage` 非 NULL，则返回已终止进程及其所有子进程使用的资源摘要。

如果 `wrusage` 非 NULL，则分别返回已终止进程使用的资源和其所有子进程使用的资源的摘要。

如果 `infop` 非 NULL，则返回一个 `siginfo_t` 结构，其中 `si_signo` 字段设置为 `SIGCHLD`，`si_pid` 字段设置为报告状态的进程的进程 ID。对于已退出的进程，`siginfo_t` 结构的 `si_status` 字段包含传递给 [_exit(2)](_exit.2.md) 的完整 32 位退出状态；其他调用的 `status` 参数仅返回退出状态的最低 8 位。

当指定 `WNOHANG` 选项且没有进程希望报告状态时，`waitid()` 将 `infop` 中的 `si_signo` 和 `si_pid` 字段设置为零。检查这些字段是了解是否报告了状态改变的唯一方式。

当指定 `WNOHANG` 选项且没有进程希望报告状态时，`wait4()` 和 `wait6()` 返回进程 ID 0。

`wait()` 调用与 `wpid` 值为 -1、`options` 值为零且 `rusage` 值为 `NULL` 的 `wait4()` 相同。`waitpid()` 函数与 `rusage` 值为 `NULL` 的 `wait4()` 相同。较旧的 `wait3()` 调用与 `wpid` 值为 -1 的 `wait4()` 相同。`wait4()` 函数与在 `options` 中设置 `WEXITED` 和 `WTRAPPED` 标志且 `infop` 设置为 `NULL` 的 `wait6()` 相同。

以下宏可用于测试进程的当前状态。以下四个宏中恰好有一个将求值为非零（真）值：

**`WIFCONTINUED(status)`** 如果进程未终止，并且在作业控制停止或调试器分离后已继续，则为真。仅当 wait 调用指定了 `WCONTINUED` 选项时，此宏才可能为真。

**`WIFEXITED(status)`** 如果进程通过调用 [_exit(2)](_exit.2.md) 或 [exit(3)](../stdlib/exit.3.md) 正常终止，则为真。

**`WIFSIGNALED(status)`** 如果进程由于接收到信号而终止，则为真。

**`WIFSTOPPED(status)`** 如果进程未终止，但已停止且可以重新启动，则为真。仅当 wait 调用指定了 `WUNTRACED` 选项或子进程正在被跟踪（参见 [ptrace(2)](ptrace.2.md)）时，此宏才可能为真。

根据这些宏的值，以下宏产生关于子进程的其余状态信息：

**`WEXITSTATUS(status)`** 如果 `WIFEXITED(status)` 为真，求值为子进程传递给 [_exit(2)](_exit.2.md) 或 [exit(3)](../stdlib/exit.3.md) 的参数的低 8 位。

**`WTERMSIG(status)`** 如果 `WIFSIGNALED(status)` 为真，求值为导致进程终止的信号编号。

**`WCOREDUMP(status)`** 如果 `WIFSIGNALED(status)` 为真，当进程终止伴随创建了包含信号接收时进程映像的核心文件时，求值为真。

**`WSTOPSIG(status)`** 如果 `WIFSTOPPED(status)` 为真，求值为导致进程停止的信号编号。

## 注释

参见 [sigaction(2)](sigaction.2.md) 获取终止信号列表。状态 0 表示正常终止。

如果父进程终止时未等待其所有子进程终止，剩余的子进程将重新分配给退出进程的 reaper 作为父进程，参见 [procctl(2)](procctl.2.md) `PROC_REAP_ACQUIRE`。如果未分配特定 reaper，则 ID 为 1 的进程（init 进程）默认成为孤儿子进程的父进程。

如果在任何 `wait()` 调用挂起时捕获到信号，调用可能会被中断或在信号捕获例程返回时重启，取决于该信号的有效选项；参见 [sigaction(2)](sigaction.2.md) 中关于 `SA_RESTART` 的讨论。

实现对每个状态已改变的子进程排队一个 `SIGCHLD` 信号；如果 `wait()` 因子进程状态可用而返回，与该子进程 ID 关联的待处理 SIGCHLD 信号将被丢弃。任何其他待处理的 `SIGCHLD` 信号保持待处理。

如果 `SIGCHLD` 被阻塞且 `wait()` 因子进程状态可用而返回，除非该子进程有其他状态可用，否则待处理的 `SIGCHLD` 信号将被清除。

## 返回值

如果 `wait()` 由于停止、继续或终止的子进程而返回，子进程的进程 ID 将返回给调用进程。否则，返回 -1 并设置 `errno` 以指示错误。

如果 `wait6()`、`wait4()`、`wait3()` 或 `waitpid()` 由于停止、继续或终止的子进程而返回，子进程的进程 ID 将返回给调用进程。如果没有先前未等待的子进程，返回 -1 并将 `errno` 设置为 `ECHILD`。否则，如果指定了 `WNOHANG` 且没有停止、继续或退出的子进程，返回 0。如果检测到错误或捕获的信号中止了调用，返回 -1 并设置 `errno` 以指示错误。

如果 `waitid()` 由于一个或多个进程有状态改变要报告而返回，返回 0。如果检测到错误，返回 -1 并设置 `errno` 以指示错误。如果指定了 `WNOHANG` 且没有停止、继续或退出的子进程，返回 0。必须检查 `infop` 的 `si_signo` 和 `si_pid` 字段是否为零，以确定是否有进程报告了状态。

`wait()` 函数家族仅在调用进程不在 [capsicum(4)](../man4/capsicum.4.md) capability 模式下，且 `wait6()` 已被显式给予子进程的进程 ID 时，才会返回由 [pdfork(2)](pdfork.2.md) 创建的子进程。

## 错误

`wait()` 函数在以下情况下将失败并立即返回：

**[`ECHILD`]** 调用进程没有现有的未等待子进程。

**[`ECHILD`]** 没有来自已终止子进程的状态可用，因为调用进程通过忽略信号 `SIGCHLD` 或为该信号设置 `SA_NOCLDWAIT` 标志，要求系统丢弃此类状态。

**[`EFAULT`]** `status` 或 `rusage` 参数指向非法地址。（可能不会在子进程退出前检测到。）

**[`EINTR`]** 调用被捕获的信号中断，或该信号未设置 `SA_RESTART` 标志。

**[`EINVAL`]** 为 `options` 指定了无效值，或 `idtype` 和 `id` 未指定有效的进程集合。

## 参见

[_exit(2)](_exit.2.md), pdwait(2), [procctl(2)](procctl.2.md), [ptrace(2)](ptrace.2.md), [sigaction(2)](sigaction.2.md), [exit(3)](../stdlib/exit.3.md), [siginfo(3)](../man3/siginfo.3.md)

## 标准

`wait()`、`waitpid()` 和 `waitid()` 函数由 POSIX 定义；`wait6()`、`wait4()` 和 `wait3()` 未由 POSIX 指定。`WCOREDUMP()` 宏是 POSIX 接口的扩展。

将 `WNOWAIT` 标志与 `waitpid()` 一起使用的能力是一种扩展；POSIX 仅允许将此标志与 `waitid()` 一起使用。

## 历史

`wait()` 函数出现于 Version 1 AT&T UNIX。
