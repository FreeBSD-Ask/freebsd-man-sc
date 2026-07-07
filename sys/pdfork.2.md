# pdfork(2)

`pdfork` — 管理进程描述符的系统调用

## 名称

`pdfork`, `pdrfork`, `pdgetpid`, `pdkill`, `pdwait`

## 库

Lb libc

## 概要

`#include <sys/procdesc.h>`

```c
pid_t
pdfork(int *fdp, int pdflags);
```

```c
pid_t
pdrfork(int *fdp, int pdflags, int rfflags);
```

```c
int
pdgetpid(int fd, pid_t *pidp);
```

```c
int
pdkill(int fd, int signum);
```

```c
int
pdwait(int fd, int *status, int options,
    struct __wrusage *wrusage, struct __siginfo *info);
```

## 描述

进程描述符是表示进程的特殊文件描述符，使用 `pdfork`（[fork(2)](fork.2.md) 的一个变体）创建，如果成功，将在 `fdp` 所指向的整数中返回一个进程描述符。通过 `pdfork` 创建的进程在终止时不会产生 `SIGCHLD`。`pdfork` 可接受以下 `pdflags`：

**`PD_DAEMON`** 不使用默认的关闭即终止行为，而是允许进程继续存活，直到通过 [kill(2)](kill.2.md) 显式终止。此选项在 [capsicum(4)](../man4/capsicum.4.md) 能力模式下不允许（参见 [cap_enter(2)](cap_enter.2.md)）。

**`PD_CLOEXEC`** 在进程描述符上设置执行时关闭标志。

`pdrfork` 系统调用是 `pdfork` 的一个变体，它还接受 `rfflags` 参数来控制调用者与新进程之间进程资源的共享。与 `pdfork` 一样，该函数将引用所创建进程的进程描述符写入 `fdp` 参数所指向的位置。有关可能的 `rfflag` 标志的描述，参见 [rfork(2)](rfork.2.md)。`pdrfork` 系统调用要求同时指定 `RFPROC` 和 `RFPROCDESC` 标志，或指定 `RFSPAWN` 标志。

`pdgetpid` 查询进程描述符 `fd` 中的进程 ID (PID)。

`pdkill` 在功能上与 [kill(2)](kill.2.md) 相同，区别在于它接受的是进程描述符 `fd`，而非 PID。

`pdwait` 系统调用允许调用线程等待并检索由 `fd` 进程描述符所引用进程的状态信息。行为规范参见 wait6 系统调用的描述。

以下系统调用也具有特定于进程描述符的效应：

[fstat(2)](stat.2.md) 查询进程描述符的状态；当前仅定义了 `st_mode`、`st_birthtime`、`st_atime`、`st_ctime` 和 `st_mtime` 字段。如果属主的读、写和执行位被设置，则由进程描述符表示的进程仍然存活。

[poll(2)](poll.2.md) 和 [select(2)](select.2.md) 允许等待进程状态转换；当前仅定义了 `POLLHUP`，并在进程死亡时引发。进程状态转换也可使用 [kqueue(2)](kqueue.2.md) 过滤器 `EVFILT_PROCDESC` 监控；当前仅实现了 `NOTE_EXIT`。

[close(2)](close.2.md) 将关闭进程描述符，除非设置了 `PD_DAEMON`；如果进程仍然存活且这是对进程描述符的最后一次引用，该进程将以信号 `SIGKILL` 终止。所引用进程的 PID 在进程描述符关闭之前不会被重用，无论僵尸进程是否通过 `pdwait`、wait6 或类似系统调用被回收。

## 返回值

`pdfork` 和 `pdrfork` 返回一个 PID、0 或 -1，如同 [fork(2)](fork.2.md) 那样。

`pdgetpid`、`pdkill` 和 `pdwait` 成功时返回 0，失败时返回 -1。

## 错误

这些函数可能返回与其基于 PID 的等价物相同的错误号（例如 `pdfork` 可能返回与 [fork(2)](fork.2.md) 相同的错误号），并有以下附加项：

**[`EFAULT`]** 将结果文件描述符值复制到 `fdp` 所指向内存的 copyout 失败。注意，检测到此条件时子进程已被创建，且子进程继续执行，与父进程相同。如果必须处理此错误，建议在调用 `pdfork` 或 `pdrfork` 之前记住 `getpid` 的结果，并在之后将其与 `getpid` 返回的值进行比较，以查看代码是在父进程还是子进程中执行。

**[`EINVAL`]** 给定给 `pdkill` 的信号编号无效。

**[`ENOTCAPABLE`]** 所操作的进程描述符权限不足（例如 `pdkill` 需要 `CAP_PDKILL`）。

## 参见

[close(2)](close.2.md), [fork(2)](fork.2.md), [fstat(2)](stat.2.md), [kill(2)](kill.2.md), [kqueue(2)](kqueue.2.md), [poll(2)](poll.2.md), [wait4(2)](wait.2.md), [capsicum(4)](../man4/capsicum.4.md), [procdesc(4)](../man4/procdesc.4.md)

## 历史

`pdfork`、`pdgetpid` 和 `pdkill` 系统调用首次出现于 FreeBSD 9.0。`pdrfork` 和 `pdwait` 系统调用首次出现于 FreeBSD 15.1。

对进程描述符模式的支持是作为 TrustedBSD 项目的一部分开发的。

## 作者

这些函数和能力设施由 Robert N. M. Watson <rwatson@FreeBSD.org> 和 Jonathan Anderson <jonathan@FreeBSD.org> 在 University of Cambridge Computer Laboratory 创建，并得到了 Google, Inc. 的资助支持。`pdrfork` 和 `pdwait` 函数由 Konstantin Belousov <kib@FreeBSD.org> 在 Alan Somers <asomers@FreeBSD.org> 的输入下开发。
