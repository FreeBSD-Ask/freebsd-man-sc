# signal(3)

`signal` — 简化的软件信号设施

## 名称

`signal` — 简化的软件信号设施

## 库

Lb libc

## 概要

```c
#include <signal.h>

void
(*signal(int sig, void (*func)(int)))(int);

或者在 FreeBSD 的等效但更易读的 typedef 版本中：

typedef void (*sig_t)(int);

sig_t
signal(int sig, sig_t func);
```

## 描述

`signal` 设施是更通用的 [sigaction(2)](../sys/sigaction.2.md) 设施的简化接口。

信号允许从进程外部操纵进程，也允许进程操纵自身或自身的副本（子进程）。信号有两种一般类型：导致进程终止的和不导致进程终止的。导致程序终止的信号可能源于不可恢复的错误，也可能是用户在终端上键入 `interrupt' 字符的结果。当进程因希望在后台访问其控制终端而被停止时，会使用信号（参见 [tty(4)](../man4/tty.4.md)）。当进程在停止后恢复、子进程状态改变或控制终端有输入就绪时，可选地产生信号。如果不采取任何操作，大多数信号会导致接收它们的进程终止；某些信号则使接收它们的进程停止，或者如果进程未另行请求则简单地被丢弃。除 `SIGKILL` 和 `SIGSTOP` 信号外，`signal` 函数允许信号被捕获、被忽略或产生中断。这些信号定义在文件 `signal.h` 中：

| **编号** | **名称** | **默认动作** | **描述** |
| --- | --- | --- | --- |
| 1 | `SIGHUP` | 终止进程 | 终端线路挂起 |
| 2 | `SIGINT` | 终止进程 | 中断程序 |
| 3 | `SIGQUIT` | 创建核心转储 | 退出程序 |
| 4 | `SIGILL` | 创建核心转储 | 非法指令 |
| 5 | `SIGTRAP` | 创建核心转储 | 跟踪陷阱 |
| 6 | `SIGABRT` | 创建核心转储 | 中止程序（原为 `SIGIOT`） |
| 7 | `SIGEMT` | 创建核心转储 | 执行仿真指令 |
| 8 | `SIGFPE` | 创建核心转储 | 浮点异常 |
| 9 | `SIGKILL` | 终止进程 | 终止程序 |
| 10 | `SIGBUS` | 创建核心转储 | 总线错误 |
| 11 | `SIGSEGV` | 创建核心转储 | 段违例 |
| 12 | `SIGSYS` | 创建核心转储 | 调用不存在的系统调用 |
| 13 | `SIGPIPE` | 终止进程 | 向无读取者的管道写入 |
| 14 | `SIGALRM` | 终止进程 | 实时定时器到期 |
| 15 | `SIGTERM` | 终止进程 | 软件终止信号 |
| 16 | `SIGURG` | 丢弃信号 | 套接字上存在紧急条件 |
| 17 | `SIGSTOP` | 停止进程 | 停止（无法捕获或忽略） |
| 18 | `SIGTSTP` | 停止进程 | 键盘产生的停止信号 |
| 19 | `SIGCONT` | 丢弃信号 | 停止后继续 |
| 20 | `SIGCHLD` | 丢弃信号 | 子进程状态已改变 |
| 21 | `SIGTTIN` | 停止进程 | 尝试从控制终端后台读取 |
| 22 | `SIGTTOU` | 停止进程 | 尝试向控制终端后台写入 |
| 23 | `SIGIO` | 丢弃信号 | 描述符上可能进行 I/O（参见 [fcntl(2)](../sys/fcntl.2.md)） |
| 24 | `SIGXCPU` | 终止进程 | 超出 CPU 时间限制（参见 [setrlimit(2)](../sys/getrlimit.2.md)） |
| 25 | `SIGXFSZ` | 终止进程 | 超出文件大小限制（参见 [setrlimit(2)](../sys/getrlimit.2.md)） |
| 26 | `SIGVTALRM` | 终止进程 | 虚拟时间警报（参见 [setitimer(2)](../sys/getitimer.2.md)） |
| 27 | `SIGPROF` | 终止进程 | 性能分析定时器警报（参见 [setitimer(2)](../sys/getitimer.2.md)） |
| 28 | `SIGWINCH` | 丢弃信号 | 窗口大小改变 |
| 29 | `SIGINFO` | 丢弃信号 | 键盘的状态请求 |
| 30 | `SIGUSR1` | 终止进程 | 用户定义信号 1 |
| 31 | `SIGUSR2` | 终止进程 | 用户定义信号 2 |
| 32 | `SIGTHR` | 终止进程 | 线程中断 |
| 33 | `SIGLIBRT` | 终止进程 | 实时库中断 |

`sig` 参数指定接收到的信号。`func` 过程允许用户选择接收到信号时的动作。要将信号的默认动作设置为如上所列，`func` 应为 `SIG_DFL`。`SIG_DFL` 重置为默认动作。要忽略信号，`func` 应为 `SIG_IGN`。这将导致后续的信号实例被忽略，挂起的实例被丢弃。如果不使用 `SIG_IGN`，信号的后续出现将自动被阻塞，并调用 `func`。

当函数返回时，被处理的信号解除阻塞，进程从信号发生时中断处继续执行。**与先前的信号设施不同，处理函数 func() 在信号传递后仍然保持安装状态。**

对于某些系统调用，如果在调用执行期间捕获到信号且调用被提前终止，该调用将自动重启。使用 [signal(3)](signal.3.md) 安装的任何处理程序都将设置 `SA_RESTART` 标志，这意味着任何可重启的系统调用在收到信号时都不会返回。受影响的系统调用包括在通信通道或低速设备上的 [read(2)](../sys/read.2.md)、[write(2)](../sys/write.2.md)、sendto(2)、recvfrom(2)、sendmsg(2) 和 recvmsg(2)，以及在 [ioctl(2)](../sys/ioctl.2.md) 或 [wait(2)](../sys/wait.2.md) 期间。但是，已经提交的调用不会重启，而是返回部分成功（例如，较短的读取计数）。这些语义可以通过 [siginterrupt(3)](siginterrupt.3.md) 更改。

当安装了信号处理程序的进程 fork 时，子进程继承这些信号。所有被捕获的信号可以通过调用 [execve(2)](../sys/execve.2.md) 函数重置为默认动作；被忽略的信号保持忽略状态。

如果进程显式指定 `SIG_IGN` 作为信号 `SIGCHLD` 的动作，系统将不会在调用进程的子进程退出时创建僵尸进程。因此，系统将丢弃子进程的退出状态。如果调用进程随后调用 [wait(2)](../sys/wait.2.md) 或等效函数，它将阻塞直到调用进程的所有子进程终止，然后返回 -1，`errno` 设置为 `ECHILD`。

参见 [sigaction(2)](../sys/sigaction.2.md) 获取可在信号处理程序中安全使用的函数列表。

## 返回值

成功调用时返回先前的动作。否则返回 SIG_ERR，并设置全局变量 `errno` 以指示错误。

## 错误

如果发生以下情况之一，`signal` 函数将失败且不执行任何动作：

**[`EINVAL`]** `sig` 参数不是有效的信号编号。

**[`EINVAL`]** 试图忽略 `SIGKILL` 或 `SIGSTOP`，或为其提供处理程序。

## 参见

[kill(1)](../man1/kill.1.md), [kill(2)](../sys/kill.2.md), [ptrace(2)](../sys/ptrace.2.md), [sigaction(2)](../sys/sigaction.2.md), [sigaltstack(2)](../sys/sigaltstack.2.md), [sigprocmask(2)](../sys/sigprocmask.2.md), [sigsuspend(2)](../sys/sigsuspend.2.md), [wait(2)](../sys/wait.2.md), fpsetmask(3), [setjmp(3)](setjmp.3.md), [siginterrupt(3)](siginterrupt.3.md), [tty(4)](../man4/tty.4.md)

## 历史

`signal` 函数出现于 Version 4 AT&T UNIX。当前的 `signal` 设施出现于 4.0BSD。通过忽略 `SIGCHLD` 来避免创建子进程僵尸的选项出现于 FreeBSD 5.0。

