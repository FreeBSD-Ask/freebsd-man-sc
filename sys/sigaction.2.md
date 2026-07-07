# sigaction(2)

`sigaction` — 软件信号设施

## 名称

`sigaction`

## 库

Lb libc

## 概要

```c
#include <signal.h>

struct  sigaction {
        void    (*sa_handler)(int);
        void    (*sa_sigaction)(int, siginfo_t *, void *);
        int     sa_flags;               /* 参见下方的信号选项 */
        sigset_t sa_mask;               /* 要应用的信号掩码 */
};

int
sigaction(int sig, const struct sigaction * restrict act,
    struct sigaction * restrict oact);
```

## 描述

系统定义了一组可传递给进程的信号。信号传递类似于硬件中断的发生：信号通常被阻止进一步发生，当前线程上下文被保存，并构建新的上下文。进程可以指定一个向其传递信号的*处理程序*（handler），或指定信号要被*忽略*。进程还可以指定在信号发生时由系统采取默认动作。信号也可以对线程*阻塞*，在这种情况下，它不会被传递到该线程，直到被*解除阻塞*。传递时采取的动作在传递时确定。通常，信号处理程序在线程的当前栈上执行。这可以按每个处理程序进行更改，以便在特殊的*信号栈*上接收信号。

信号例程通常在导致其调用的信号被*阻塞*的状态下执行，但其他信号仍可能发生。全局*信号掩码*定义了当前阻止传递到线程的信号集合。线程的信号掩码从其父进程初始化（通常为空）。可以通过 [sigprocmask(2)](sigprocmask.2.md) 或 [pthread_sigmask(3)](../man3/pthread_sigmask.3.md) 调用，或在信号传递到线程时更改。

当进程或线程出现信号条件时，该信号被添加到进程或线程的待处理信号集合中。信号是指向进程整体还是特定线程取决于其生成方式。对于指向特定线程的信号，如果该信号当前未被线程*阻塞*，则传递到该线程。对于指向进程的信号，如果该信号当前未被所有线程*阻塞*，则传递到一个未阻塞它的线程（选择哪个未指定）。每当线程进入操作系统时（例如，在系统调用、缺页或陷阱期间，或时钟中断时），信号都可能被传递。如果多个信号同时准备传递，任何可能由陷阱引起的信号将首先传递。其他信号可能同时被处理，每个信号看起来都在前一个信号处理程序的第一条指令之前中断其处理程序。待处理信号集合由 [sigpending(2)](sigpending.2.md) 系统调用返回。当捕获的信号被传递时，线程的当前状态被保存，计算新的信号掩码（如下所述），并调用信号处理程序。对处理程序的调用安排为：如果信号处理例程正常返回，线程将在信号传递之前的上下文中恢复执行。如果线程希望在不同的上下文中恢复，则必须自行安排恢复先前的上下文。

当信号传递到线程时，在进程的信号处理程序执行期间（或直到进行 [sigprocmask(2)](sigprocmask.2.md) 系统调用）安装新的信号掩码。此掩码由当前信号掩码集、要传递的信号和要调用的处理程序关联的信号掩码取并集形成。

`sigaction()` 系统调用为 `sig` 指定的信号分配一个动作。如果 `act` 非 NULL，它指定了传递指定信号时要使用的动作（`SIG_DFL`、`SIG_IGN` 或处理程序例程）和掩码。如果 `oact` 非 NULL，该信号先前的处理信息将返回给用户。

上面 `struct sigaction` 的声明并非字面意义。它仅用于列出可访问的成员。实际定义参见

```c
#include <sys/signal.h>
```

特别地，`sa_handler` 和 `sa_sigaction` 占用的存储空间重叠，应用程序尝试同时使用两者是无意义的。

一旦安装了信号处理程序，它通常保持安装状态，直到进行另一次 `sigaction()` 系统调用或执行 [execve(2)](execve.2.md)。可以通过将 `sa_handler` 设置为 `SIG_DFL` 来重置特定信号的默认动作。默认动作包括：终止进程（可能附带核心转储）、无动作、停止进程或继续进程。有关每个信号的默认动作，参见下方的信号列表。如果 `sa_handler` 为 `SIG_DFL`，信号的默认动作是丢弃该信号，如果信号处于待处理状态，即使信号被屏蔽，待处理的信号也会被丢弃。如果 `sa_handler` 设置为 `SIG_IGN`，信号的当前和待处理实例都将被忽略并丢弃。

可以通过设置 `sa_flags` 来指定选项。各个位的含义如下：

**`SA_NOCLDSTOP`** 如果在为 `SIGCHLD` 信号安装捕获函数时设置了此位，则 `SIGCHLD` 信号仅在子进程退出时生成，而非子进程停止时。

**`SA_NOCLDWAIT`** 如果在为 `SIGCHLD` 信号调用 `sigaction()` 时设置了此位，系统在调用进程的子进程退出时不会创建僵尸进程。如果调用进程随后发出 [wait(2)](wait.2.md)（或等效调用），它将阻塞直到调用进程的所有子进程终止，然后返回 -1 并将 `errno` 设置为 `ECHILD`。通过将 `SIGCHLD` 的 `sa_handler` 设置为 `SIG_IGN` 也可以达到避免创建僵尸进程的相同效果。

**`SA_ONSTACK`** 如果设置了此位，系统将在每个线程通过 [sigaltstack(2)](sigaltstack.2.md) 指定的*信号栈*上向进程传递信号。

**`SA_NODEFER`** 如果设置了此位，在处理程序执行期间不会屏蔽所传递信号的后续发生。

**`SA_RESETHAND`** 如果设置了此位，处理程序在信号传递时被重置为 `SIG_DFL`。

**`SA_RESTART`** 参见下文段落。

**`SA_SIGINFO`** 如果设置了此位，假定处理程序函数由 `struct sigaction` 的 `sa_sigaction` 成员指向，并应与上面所示或下方[实例](#实例)中的原型匹配。在分配 `SIG_DFL` 或 `SIG_IGN` 时不应设置此位。

如果在下方列出的系统调用期间捕获了信号，调用可能被强制以 `EINTR` 错误终止，调用可能返回比请求更短的数据传输，或者调用可能被重启。通过在 `sa_flags` 中设置 `SA_RESTART` 位来请求重启待处理调用。受影响的系统调用包括在通信通道或慢速设备（如终端，但非普通文件）上的 [open(2)](open.2.md)、[read(2)](read.2.md)、[write(2)](write.2.md)、sendto(2)、recvfrom(2)、sendmsg(2) 和 recvmsg(2)，以及在 [wait(2)](wait.2.md) 或 [ioctl(2)](ioctl.2.md) 期间。然而，已经提交的调用不会重启，而是返回部分成功（例如，较短的读取计数）。

在 [pthread_create(3)](../man3/pthread_create.3.md) 之后，信号掩码被新线程继承，新线程的待处理信号集合和信号栈为空。

在 [fork(2)](fork.2.md) 或 [vfork(2)](vfork.2.md) 之后，所有信号、信号掩码、信号栈以及重启/中断标志都被子进程继承。

[execve(2)](execve.2.md) 系统调用恢复所有被捕获信号的默认动作，并将所有信号重置为在用户栈上捕获。被忽略的信号保持被忽略；信号掩码保持不变；重启待处理系统调用的信号继续如此。

以下是所有信号的列表，名称与包含文件

```c
#include <signal.h>
```

中的一致：

| **名称** | **默认动作** | **描述** |
| --- | --- | --- |
| `SIGHUP` | 终止进程 | 终端线路挂起 |
| `SIGINT` | 终止进程 | 中断程序 |
| `SIGQUIT` | 创建核心转储 | 退出程序 |
| `SIGILL` | 创建核心转储 | 非法指令 |
| `SIGTRAP` | 创建核心转储 | 跟踪陷阱 |
| `SIGABRT` | 创建核心转储 | [abort(3)](../stdlib/abort.3.md) 调用（原 `SIGIOT`） |
| `SIGEMT` | 创建核心转储 | 模拟指令执行 |
| `SIGFPE` | 创建核心转储 | 浮点异常 |
| `SIGKILL` | 终止进程 | 杀死程序 |
| `SIGBUS` | 创建核心转储 | 总线错误 |
| `SIGSEGV` | 创建核心转储 | 段违规 |
| `SIGSYS` | 创建核心转储 | 调用了不存在的系统调用 |
| `SIGPIPE` | 终止进程 | 向无读取者的管道写入 |
| `SIGALRM` | 终止进程 | 实时计时器到期 |
| `SIGTERM` | 终止进程 | 软件终止信号 |
| `SIGURG` | 丢弃信号 | 套接字上存在紧急条件 |
| `SIGSTOP` | 停止进程 | 停止（无法被捕获或忽略） |
| `SIGTSTP` | 停止进程 | 从键盘生成的停止信号 |
| `SIGCONT` | 丢弃信号 | 停止后继续 |
| `SIGCHLD` | 丢弃信号 | 子进程状态已改变 |
| `SIGTTIN` | 停止进程 | 尝试从控制终端后台读取 |
| `SIGTTOU` | 停止进程 | 尝试向控制终端后台写入 |
| `SIGIO` | 丢弃信号 | 描述符上可能进行 I/O（参见 [fcntl(2)](fcntl.2.md)） |
| `SIGXCPU` | 终止进程 | 超过 CPU 时间限制（参见 setrlimit(2)） |
| `SIGXFSZ` | 终止进程 | 超过文件大小限制（参见 setrlimit(2)） |
| `SIGVTALRM` | 终止进程 | 虚拟时间告警（参见 setitimer(2)） |
| `SIGPROF` | 终止进程 | 性能分析计时器告警（参见 setitimer(2)） |
| `SIGWINCH` | 丢弃信号 | 窗口大小改变 |
| `SIGINFO` | 丢弃信号 | 来自键盘的状态请求 |
| `SIGUSR1` | 终止进程 | 用户定义信号 1 |
| `SIGUSR2` | 终止进程 | 用户定义信号 2 |

## 注意

`act` 中指定的 `sa_mask` 字段不允许阻塞 `SIGKILL` 或 `SIGSTOP`。任何此类尝试都将被静默忽略。

以下函数要么是可重入的，要么不被信号中断，是异步信号安全的。因此，应用程序可以从信号捕获函数中，或在多线程进程中调用 [fork(2)](fork.2.md) 之后的子进程中无限制地调用它们：

基本接口：

`_Exit()` , `_exit()` , `accept()` , `access()` , `alarm()` , `bind()` , `cfgetispeed()` , `cfgetospeed()` , `cfsetispeed()` , `cfsetospeed()` , `chdir()` , `chmod()` , `chown()` , `close()` , `connect()` , `creat()` , `dup()` , `dup2()` , `execl()` , `execle()` , `execv()` , `execve()` , `faccessat()` , `fchdir()` , `fchmod()` , `fchmodat()` , `fchown()` , `fchownat()` , `fcntl()` , `_Fork()` , `fstat()` , `fstatat()` , `fsync()` , `ftruncate()` , `getegid()` , `geteuid()` , `getgid()` , `getgroups()` , `getpeername()` , `getpgrp()` , `getpid()` , `getppid()` , `getsockname()` , `getsockopt()` , `getuid()` , `kill()` , `link()` , `linkat()` , `listen()` , `lseek()` , `lstat()` , `mkdir()` , `mkdirat()` , `mkfifo()` , `mkfifoat()` , `mknod()` , `mknodat()` , `open()` , `openat()` , `pause()` , `pipe()` , `poll()` , `pselect()` , `pthread_sigmask()` , `raise()` , `read()` , `readlink()` , `readlinkat()` , `recv()` , `recvfrom()` , `recvmsg()` , `rename()` , `renameat()` , `rmdir()` , `select()` , `send()` , `sendmsg()` , `sendto()` , `setgid()` , `setpgid()` , `setsid()` , `setsockopt()` , `setuid()` , `shutdown()` , `sigaction()` , `sigaddset()` , `sigdelset()` , `sigemptyset()` , `sigfillset()` , `sigismember()` , `signal()` , `sigpending()` , `sigprocmask()` , `sigsuspend()` , `sleep()` , `sockatmark()` , `socket()` , `socketpair()` , `stat()` , `symlink()` , `symlinkat()` , `tcdrain()` , `tcflow()` , `tcflush()` , `tcgetattr()` , `tcgetpgrp()` , `tcsendbreak()` , `tcsetattr()` , `tcsetpgrp()` , `time()` , `times()` , `umask()` , `uname()` , `unlink()` , `unlinkat()` , `utime()` , `wait()` , `waitpid()` , `write()` 。

X/Open 系统接口：

`sigpause()` , `sigset()` , `utimes()` 。

实时接口：

`aio_error()` , `clock_gettime()` , `timer_getoverrun()` , `aio_return()` , `fdatasync()` , `sigqueue()` , `timer_gettime()` , `aio_suspend()` , `sem_post()` , `timer_settime()` 。

POSIX 未指定为异步信号安全的基本接口：

`fpathconf()` , `pathconf()` , `sysconf()` 。

POSIX 未指定为异步信号安全、但计划如此的基本接口：

`ffs()` , `htonl()` , `htons()` , `memccpy()` , `memchr()` , `memcmp()` , `memcpy()` , `memmove()` , `memset()` , `ntohl()` , `ntohs()` , `stpcpy()` , `stpncpy()` , `strcat()` , `strchr()` , `strcmp()` , `strcpy()` , `strcspn()` , `strlen()` , `strncat()` , `strncmp()` , `strncpy()` , `strnlen()` , `strpbrk()` , `strrchr()` , `strspn()` , `strstr()` , `strtok_r()` , `wcpcpy()` , `wcpncpy()` , `wcscat()` , `wcschr()` , `wcscmp()` , `wcscpy()` , `wcscspn()` , `wcslen()` , `wcsncat()` , `wcsncmp()` , `wcsncpy()` , `wcsnlen()` , `wcspbrk()` , `wcsrchr()` , `wcsspn()` , `wcsstr()` , `wcstok()` , `wmemchr()` , `wmemcmp()` , `wmemcpy()` , `wmemmove()` , `wmemset()` 。

扩展接口：

`accept4()` , `bindat()` , `close_range()` , `closefrom()` , `connectat()` , `eaccess()` , `ffsl()` , `ffsll()` , `flock()` , `fls()` , `flsl()` , `flsll()` , `futimesat()` , `pipe2()` , `strlcat()` , `strlcpy()` , `strsep()` 。

此外，读写 `errno` 是异步信号安全的。

不在上述列表中的所有函数都被认为在信号方面是不安全的。也就是说，当此类函数从中断了不安全函数的信号处理程序中调用时，其行为是未定义的。但一般而言，信号处理程序应仅设置一个标志；大多数其他操作都不安全。

此外，良好的做法是复制全局变量 `errno`，并在从信号处理程序返回之前恢复它。这可以防止 `errno` 被信号处理程序内部调用的函数设置的副作用。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 实例

处理程序可能匹配的原型有三种：

**ANSI** C：`void handler(int);`

**传统** BSD 风格：`void handler(int, int code, struct sigcontext *scp);`

**POSIX** `SA_SIGINFO`：`void handler(int, siginfo_t *info, ucontext_t *uap);`

如果在 `sa_flags` 中设置了 `SA_SIGINFO` 位，处理程序函数应匹配 `SA_SIGINFO` 原型。然后它应由 `struct sigaction` 的 `sa_sigaction` 成员指向。注意，不应以这种方式分配 `SIG_DFL` 或 `SIG_IGN`。

如果未设置 `SA_SIGINFO` 标志，处理程序函数应匹配 ANSI C 或传统 BSD 原型，并由 `struct sigaction` 的 `sa_handler` 成员指向。实际上，FreeBSD 总是发送后者的三个参数，由于 ANSI C 原型是其子集，两者都能工作。FreeBSD 包含文件中的 `sa_handler` 成员声明是 ANSI C 的（如 POSIX 所要求），因此 BSD 风格函数的函数指针需要强制转换才能编译时不产生警告。传统 BSD 风格不可移植，且由于其功能是 `SA_SIGINFO` 处理程序的完整子集，其使用已被弃用。

`sig` 参数是信号编号，即

```c
#include <signal.h>
```

中的某个 `SIG...` 值。

BSD 风格处理程序的 `code` 参数和 `SA_SIGINFO` 处理程序的 `info` 参数的 `si_code` 成员包含解释信号原因的数字代码，通常是

```c
#include <sys/signal.h>
```

中的某个 `SI_...` 值，或特定于信号的代码，即 `SIGFPE` 的某个 `FPE_...` 值。

BSD 风格处理程序的 `scp` 参数指向 `struct sigcontext` 的实例。

POSIX `SA_SIGINFO` 处理程序的 `uap` 参数指向 ucontext_t 的实例。

## 错误

如果发生以下任一情况，`sigaction()` 系统调用将失败，且不会安装新的信号处理程序：

**[`EINVAL`]** `sig` 参数不是有效的信号编号。

**[`EINVAL`]** 尝试忽略或为 `SIGKILL` 或 `SIGSTOP` 提供处理程序。

## 参见

[kill(1)](../man1/kill.1.md), [kill(2)](kill.2.md), [ptrace(2)](ptrace.2.md), setitimer(2), setrlimit(2), [sigaltstack(2)](sigaltstack.2.md), [sigpending(2)](sigpending.2.md), [sigprocmask(2)](sigprocmask.2.md), [sigsuspend(2)](sigsuspend.2.md), [wait(2)](wait.2.md), fpsetmask(3), [setjmp(3)](../gen/setjmp.3.md), [siginfo(3)](../man3/siginfo.3.md), [siginterrupt(3)](../gen/siginterrupt.3.md), [sigsetops(3)](../gen/sigsetops.3.md), [ucontext(3)](../gen/ucontext.3.md), [tty(4)](../man4/tty.4.md)

## 标准

`sigaction()` 系统调用预计符合 IEEE Std 1003.1-1990 ("POSIX.1")。`SA_ONSTACK` 和 `SA_RESTART` 标志是 Berkeley 扩展，信号 `SIGTRAP`、`SIGEMT`、`SIGBUS`、`SIGSYS`、`SIGURG`、`SIGIO`、`SIGXCPU`、`SIGXFSZ`、`SIGVTALRM`、`SIGPROF`、`SIGWINCH` 和 `SIGINFO` 也是如此。这些信号在大多数 BSD 派生系统上可用。`SA_NODEFER` 和 `SA_RESETHAND` 标志旨在与其他操作系统向后兼容。`SA_NOCLDSTOP` 和 `SA_NOCLDWAIT` 标志提供了其他操作系统中常见的选项特性。这些标志被 -susv2 批准，同时批准的还有通过忽略 `SIGCHLD` 来避免创建僵尸进程的选项。
