# dtrace_proc.4

`dtrace_proc` — 用于跟踪用户进程相关事件的 DTrace 提供者

## 名称

`dtrace_proc`

## 概要

`Fn proc:::create struct proc * struct proc * int Fn proc:::exec char * Fn proc:::exec-failure int Fn proc:::exec-success char * Fn proc:::exit int Fn proc:::signal-clear int ksiginfo_t * Fn proc:::signal-discard struct thread * struct proc * int Fn proc:::signal-send struct thread * struct proc * int`

## 描述

DTrace `proc` 提供者可洞察与用户进程相关的事件：进程和线程的创建与终止事件，以及进程信号。

Fn proc:::create 探测在通过 fork(2)、vfork(2)、pdfork(2) 或 rfork(2) 系统调用创建用户进程时触发。特别是，使用 [kproc(9)](../man9/kproc.9.md) KPI 创建的内核进程不会触发此探测。Fn proc:::create 探测的前两个参数分别是新的子进程及其父进程。第三个参数是 rfork(2) 标志的掩码，指示哪些进程资源在父进程和子进程之间共享。

Fn proc:::exec 探测在进程尝试执行文件时触发。其参数是指定的文件名。如果尝试因错误而失败，Fn proc:::exec-failure 探测将随后触发，在其第一个参数中提供相应的 errno(2) 值。否则，Fn proc:::exec-success 探测将触发。

Fn proc:::exit 探测在进程退出或被终止时触发。其参数是相应的 `SIGCHLD` 信号代码；有效值记录在 [siginfo(3)](../man3/siginfo.3.md) 手册页中并定义在 `signal.h` 中。例如，当进程正常退出时，`args[0]` 的值将为 `CLD_EXITED`。

Fn proc:::signal-send 探测在即将向进程发送信号时触发。Fn proc:::signal-discard 探测在向忽略该信号的进程发送信号时触发。此探测将在相关信号的 Fn proc:::signal-send 探测之后触发。这些探测的参数是将接收信号的线程和进程，以及信号的编号。有效信号编号定义在 signal(3) 手册页中。Fn proc:::signal-clear 探测在挂起信号已被 sigwait(2)、sigtimedwait(2) 或 sigwaitinfo(2) 系统调用之一清除时触发。其参数是已清除信号的编号，以及指向相应信号信息的指针。信号的 `siginfo_t` 可从 `args[1]->ksi_info` 获取。

## 参数

虽然 `proc` 提供者探测使用原生 FreeBSD 参数类型，但进程和线程的标准 D 类型可用。分别是 `psinfo_t` 和 `lwpsinfo_t`，定义在 **/usr/lib/dtrace/psinfo.d** 中。此文件还定义了两个全局变量 `curpsinfo` 和 `curlwpsinfo`，它们使用这些类型提供当前进程和线程的表示。

`psinfo_t` 的字段为：

**`int pr_nlwp`** 进程中的线程数。

**`pid_t pr_pid`** 进程 ID。

**`pid_t pr_ppid`** 父进程的进程 ID，如果进程没有父进程则为 0。

**`pid_t pr_pgid`** 进程组领导者的进程 ID。

**`pid_t pr_sid`** 会话 ID，如果进程不属于任何会话则为 0。

**`pid_t pr_uid`** 实际用户 ID。

**`pid_t pr_euid`** 有效用户 ID。

**`pid_t pr_gid`** 实际组 ID。

**`pid_t pr_egid`** 有效组 ID。

**`uintptr_t pr_addr`** 指向进程的 `struct proc` 的指针。

**`string pr_psargs`** 进程参数。

**`u_int pr_arglen`** 进程参数字符串的长度。

**`u_int pr_jailid`** 进程的 Jail ID。

`lwpsinfo_t` 的字段为：

**`id_t pr_lwpid`** 线程 ID。

**`int pr_flag`** 线程标志。

**`int pr_pri`** 线程的实际调度优先级。

**`char pr_state`** 当前始终为 0。

**`char pr_sname`** 当前始终为 `?`。

**`short pr_syscall`** 当前始终为 0。

**`uintptr_t pr_addr`** 指向线程的 `struct thread` 的指针。

**`uintptr_t pr_wchan`** 线程正在其上睡眠的当前等待地址。

## 文件

**`/usr/lib/dtrace/psinfo.d`** `proc` 提供者的 DTrace 类型和转换器定义。

## 实例

以下脚本在进程执行事件发生时记录：

```sh
#pragma D option quiet
proc:::exec-success
{
        printf("%s", curpsinfo->pr_psargs);
}
```

注意，`pr_psargs` 字段受 `kern.ps_arg_cache_limit` sysctl 定义的限制。特别是，参数列表长于此 sysctl 定义的值的进程无法以这种方式记录。

## 兼容性

FreeBSD 中的 `proc` 提供者与 Solaris 中的 `proc` 提供者不兼容。特别是，FreeBSD 使用原生 `struct proc` 和 `struct thread` 类型作为探测参数，而非转换后的类型。此外，Solaris 中的许多 `proc` 提供者探测目前在 FreeBSD 上不可用。

## 参见

[dtrace(1)](../man1/dtrace.1.md), errno(2), fork(2), pdfork(2), rfork(2), vfork(2), [siginfo(3)](../man3/siginfo.3.md), signal(3), [dtrace_sched(4)](dtrace_sched.4.md), [kproc(9)](../man9/kproc.9.md)

## 历史

`proc` 提供者首次出现于 FreeBSD 7.1。

## 作者

本手册页由 Mark Johnston <markj@FreeBSD.org> 编写。
