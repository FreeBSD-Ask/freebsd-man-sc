# siginfo(3)

`siginfo` — 信号生成信息

## 名称

`siginfo`

## 概要

`#include <signal.h>`

## 描述

进程在捕获信号时可以请求信号信息。该信息指明系统生成该信号的原因。要在信号处理程序中请求信号信息，用户可以在调用 sigaction(2) 之前在 `sa_flags` 中设置 `SA_SIGINFO`，否则可以使用 sigwaitinfo(2) 和 sigtimedwait(2) 获取信号信息。无论哪种情况，系统都在 `siginfo_t` 类型的结构中返回信息，该结构包含以下信息：

信号编号

错误编号

信号代码

信号值

发送进程 ID

发送进程的实际用户 ID

虚拟地址

退出值或信号

`SIGPOLL` 的频带事件

机器陷阱代码

POSIX 定时器 ID

POSIX 定时器溢出计数

POSIX 消息队列 ID

被 Capsicum 阻塞的系统调用的系统调用号

| **类型** | **成员** | **描述** |
| --- | --- | --- |
| `int` | `si_signo` |  |
| `int` | `si_errno` |  |
| `int` | `si_code` |  |
| `union sigval` | `si_value` |  |
| `pid_t` | `si_pid` |  |
| `uid_t` | `si_uid` |  |
| `void` | `*si_addr` |  |
| `int` | `si_status` |  |
| `long` | `si_band` |  |
| `int` | `si_trapno` |  |
| `int` | `si_timerid` |  |
| `int` | `si_overrun` |  |
| `int` | `si_mqd` |  |
| `int` | `si_syscall` |  |

`si_signo` 成员包含信号编号。

`si_errno` 成员包含在以下文件中定义的错误编号：

```c
#include <errno.h>
```

`si_code` 成员包含描述信号原因的代码。下表 **代码** 列中指定的宏定义为 `si_code` 的值而定义，这些值是信号特定的或非信号特定的生成信号的原因：

非法操作码

非法操作数

非法寻址模式

非法陷阱

非法特权操作码

非法特权寄存器

协处理器错误

内部栈错误

整数除以零

整数溢出

浮点除以零

浮点溢出

浮点下溢

浮点不精确结果

无效浮点操作

下标越界

地址未映射到对象

映射对象的权限无效

无效地址对齐

不存在的物理地址

对象特定的硬件错误

无法分配页面以在缺页时映射

进程断点

进程跟踪陷阱

DTrace 引发的陷阱

能力保护陷阱

子进程已退出

子进程异常终止且未创建核心文件

子进程异常终止并创建了核心文件

被跟踪的子进程已陷入陷阱

子进程已停止

已停止的子进程已继续

数据输入可用

输出缓冲区可用

输入消息可用

I/O 错误

高优先级输入可用

设备已断开

只有 `si_signo` 成员有意义；所有其他成员的值未指定。

由 kill(2) 发送的信号

由 sigqueue(2) 发送的信号

由 timer_settime(2) 设置的定时器到期生成的信号

异步 I/O 请求完成生成的信号

空消息队列上到达消息生成的信号

由内核各部分生成的信号

由 [pthread_kill(3)](pthread_kill.3.md) 发送的信号

| **信号** | **代码** | **原因** |
| --- | --- | --- |
| `SIGILL` | `ILL_ILLOPC` | 非法操作码 |
|  | `ILL_ILLOPN` | 非法操作数 |
|  | `ILL_ILLADR` | 非法寻址模式 |
|  | `ILL_ILLTRP` | 非法陷阱 |
|  | `ILL_PRVOPC` | 非法特权操作码 |
|  | `ILL_PRVREG` | 非法特权寄存器 |
|  | `ILL_COPROC` | 协处理器错误 |
|  | `ILL_BADSTK` | 内部栈错误 |
| `SIGFPE` | `FPE_INTDIV` | 整数除以零 |
|  | `FPE_INTOVF` | 整数溢出 |
|  | `FPE_FLTDIV` | 浮点除以零 |
|  | `FPE_FLTOVF` | 浮点溢出 |
|  | `FPE_FLTUND` | 浮点下溢 |
|  | `FPE_FLTRES` | 浮点不精确结果 |
|  | `FPE_FLTINV` | 无效浮点操作 |
|  | `FPE_FLTSUB` | 下标越界 |
| `SIGSEGV` | `SEGV_MAPERR` | 地址未映射到对象 |
|  | `SEGV_ACCERR` | 映射对象的权限无效 |
| `SIGBUS` | `BUS_ADRALN` | 无效地址对齐 |
|  | `BUS_ADRERR` | 不存在的物理地址 |
|  | `BUS_OBJERR` | 对象特定的硬件错误 |
|  | `BUS_OOMERR` | 无法分配页面以在缺页时映射 |
| `SIGTRAP` | `TRAP_BRKPT` | 进程断点 |
|  | `TRAP_TRACE` | 进程跟踪陷阱 |
|  | `TRAP_DTRACE` | DTrace 引发的陷阱 |
|  | `TRAP_CAP` | 能力保护陷阱 |
| `SIGCHLD` | `CLD_EXITED` | 子进程已退出 |
|  | `CLD_KILLED` | 子进程异常终止且未创建核心文件 |
|  | `CLD_DUMPED` | 子进程异常终止并创建了核心文件 |
|  | `CLD_TRAPPED` | 被跟踪的子进程已陷入陷阱 |
|  | `CLD_STOPPED` | 子进程已停止 |
|  | `CLD_CONTINUED` | 已停止的子进程已继续 |
| `SIGPOLL` | `POLL_IN` | 数据输入可用 |
|  | `POLL_OUT` | 输出缓冲区可用 |
|  | `POLL_MSG` | 输入消息可用 |
|  | `POLL_ERR` | I/O 错误 |
|  | `POLL_PRI` | 高优先级输入可用 |
|  | `POLL_HUP` | 设备已断开 |
| Any | `SI_NOINFO` | 只有 `si_signo` 成员有意义；所有其他成员的值未指定 |
|  | `SI_USER` | 由 kill(2) 发送的信号 |
|  | `SI_QUEUE` | 由 sigqueue(2) 发送的信号 |
|  | `SI_TIMER` | 由 timer_settime(2) 设置的定时器到期生成的信号 |
|  | `SI_ASYNCIO` | 异步 I/O 请求完成生成的信号 |
|  | `SI_MESGQ` | 空消息队列上到达消息生成的信号 |
|  | `SI_KERNEL` | 由内核各部分生成的信号 |
|  | `SI_LWP` | 由 pthread_kill(3) 发送的信号 |

对于同步信号，`si_addr` 通常设置为故障指令的地址。但是，由内存访问故障（如 `SIGSEGV` 和 `SIGBUS`）引发的同步信号可能在 `si_addr` 中报告故障内存访问的地址（如果可用）。此外，由硬件观察点异常引发的 `SIGTRAP` 可能在 `si_addr` 中报告触发观察点的数据地址。

同步信号将 `si_trapno` 设置为与机器相关的陷阱编号。

此外，还提供以下信号特定的信息：

子进程 ID

退出值或信号；如果 `si_code` 等于 `CLD_EXITED`，则等于子进程的退出值，否则等于导致子进程状态改变的信号。

`POLL_IN`、`POLL_OUT` 或 `POLL_MSG`

| **信号** | **成员** | **值** |
| --- | --- | --- |
| `SIGCHLD` | `si_pid` | 子进程 ID |
|  | `si_status` | 退出值或信号 |
|  | `si_uid` | 发送信号的进程的实际用户 ID |
| `SIGPOLL` | `si_band` | 频带事件 |

最后，还提供以下代码特定的信息：

发送信号的进程 ID

发送信号的进程的实际用户 ID

传递给 sigqueue(2) 系统调用的值

发送信号的进程 ID

发送信号的进程的实际用户 ID

传递给 timer_create(2) 系统调用的值

由 timer_create(2) 系统调用返回的定时器 ID

对应于该信号的定时器溢出计数

如果定时器溢出将达到 {`DELAYTIMER_MAX`}，则设置在以下文件中定义的错误代码：

```c
#include <errno.h>
```

传递给 aio 系统调用的值

传递给 mq_notify(2) 系统调用的值

生成该信号的消息队列 ID

发送信号的进程 ID

发送信号的进程的实际用户 ID

| **代码** | **成员** | **值** |
| --- | --- | --- |
| `SI_USER` | `si_pid` | 发送信号的进程 ID |
|  | `si_uid` | 发送信号的进程的实际用户 ID |
| `SI_QUEUE` | `si_value` | 传递给 sigqueue(2) 系统调用的值 |
|  | `si_pid` | 发送信号的进程 ID |
|  | `si_uid` | 发送信号的进程的实际用户 ID |
| `SI_TIMER` | `si_value` | 传递给 timer_create(2) 系统调用的值 |
|  | `si_timerid` | 由 timer_create(2) 系统调用返回的定时器 ID |
|  | `si_overrun` | 对应于该信号的定时器溢出计数 |
|  | `si_errno` | 错误代码 |
| `SI_ASYNCIO` | `si_value` | 传递给 aio 系统调用的值 |
| `SI_MESGQ` | `si_value` | 传递给 mq_notify(2) 系统调用的值 |
|  | `si_mqd` | 生成该信号的消息队列 ID |
| `SI_LWP` | `si_pid` | 发送信号的进程 ID |
|  | `si_uid` | 发送信号的进程的实际用户 ID |

## 注释

目前，内核从不生成 `SIGPOLL` 信号。当进程更改其状态或退出时，`SIGCHLD` 信号被排队。POSIX 实时扩展（如 aio、定时器和消息队列）也会对信号进行排队。代码为 `SI_USER`、`SI_KERNEL` 或 `SI_LWP` 的信号仅在资源充足时才排队；否则，结果为 `SI_NOINFO`。对于某些硬件架构，`si_addr` 的确切值可能不可用。

## 参见

aio_read(2), kill(2), mq_notify(2), sigaction(2), sigqueue(2), sigwaitinfo(2), timer_create(2), timer_settime(2), waitpid(2), [pthread_kill(3)](pthread_kill.3.md)

## 标准

`siginfo_t` 类型遵循 IEEE Std 1003.1-2004 ("POSIX.1") 标准。

## 历史

对 POSIX 信号信息的完整支持首次出现于 FreeBSD 7.0。代码 `SI_USER` 和 `SI_KERNEL` 可从 FreeBSD 8.1 起生成。代码 `SI_LWP` 可从 FreeBSD 9.0 起生成。

## 作者

本手册页由 David Xu <davidxu@FreeBSD.org> 编写。
