  KILL(1)  

KILL(1)

FreeBSD General Commands Manual

KILL(1)

[名称](#__u540D___u79F0_)
=======================

`kill` —

终止或向进程发出信号

[概要](#__u6982___u8981_)
=======================

`kill` \[`-s` signal\_name\] pid ... `kill` `-l` \[exit\_status\] `kill` `-`signal\_name pid ... `kill` `-`signal\_number pid ...

[描述](#__u63CF___u8FF0_)
=======================

`kill` 实用程序向 pid 操作数指定的进程发送信号。

只有超级用户可以向其他用户的进程发送信号。

选项如下：

[`-s`](#s) signal\_name

一个符号信号名称，指定要发送的信号，而不是默认的 `TERM` 。

[`-l`](#l) \[exit\_status\]

如果没有给出操作数，列出信号名称；否则，写出 exit\_status 对应的信号名称。

`-`signal\_name

一个符号信号名称，指定要发送的信号，而不是默认的 `TERM` 。

`-`signal\_number

一个非负十进制整数，指定要发送的信号而不是默认的 `TERM` 。

以下 PID 具有特殊含义：

\-1

如果是超级用户，向所有进程广播信号；否则广播到属于用户的所有进程。

一些比较常用的信号：

1

HUP (挂断)

2

INT (中断)

3

QUIT (退出)

6

ABRT (中止)

9

KILL (不可捕获，不可忽略的杀戮)

14

ALRM (闹钟)

15

TERM (软件终止信号)

某些 shell 可能提供与此实用程序相似或相同的内置 `kill` 命令。 请参阅 builtin(1) 手册页。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `kill` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

终止 PID 为 142 和 157 的进程：

`kill 142 157`

向 PID 507 的进程发送挂断信号 (`SIGHUP`) :

`kill -s HUP 507`

使用 PGID 117 终止进程组：

`kill -- -117`

[参见](#__u53C2___u89C1_)
=======================

builtin(1), csh(1), killall(1), ps(1), sh(1), kill(2), sigaction(2)

[标准](#__u6807___u51C6_)
=======================

`kill` 实用程序预计与 IEEE Std 1003.2 (“POSIX.2”) 兼容。

[历史](#__u5386___u53F2_)
=======================

`kill` 命令出现在 Version 3 AT&T UNIX 手册的第 8 节中。

[缺陷](#__u7F3A___u9677_)
=======================

应该为 csh(1) 用户提供命令 “`kill 0`” 的替代品。

October 3, 2016

FreeBSD 13.1-RELEASE