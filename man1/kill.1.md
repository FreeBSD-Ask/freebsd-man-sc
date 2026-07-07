# kill(1)

`kill` — 终止或向进程发送信号

## 名称

`kill`

## 概要

`kill [-s signal_name] pid ...`

`kill -l [exit_status]`

`kill -signal_name pid ...`

`kill -signal_number pid ...`

## 描述

`kill` 实用程序向由 `pid` 操作数指定的进程发送信号。

只有超级用户才能向其他用户的进程发送信号。

选项如下：

**`-s`** `signal_name` 指定要发送的信号的符号信号名，而非默认的 `TERM`。

**`-l`** [`exit_status`] 如果没有给出操作数，列出信号名称；否则，写出与 `exit_status` 对应的信号名。

**`-signal_name`** 指定要发送的信号的符号信号名，而非默认的 `TERM`。

**`-signal_number`** 一个非负十进制整数，指定要发送的信号，而非默认的 `TERM`。

以下 PID 具有特殊含义：

**0** 信号将发送到所有组 ID 等于发送者进程组 ID 的进程，且该进程有权限发送。

**-1** 如果是超级用户，向所有进程广播信号；否则向属于该用户的所有进程广播。

**-PGID** 信号将发送到属于指定进程组 ID（PGID）的所有进程。

一些常用的信号：

**1** HUP（挂起）

**2** INT（中断）

**3** QUIT（退出）

**6** ABRT（中止）

**9** KILL（不可捕获、不可忽略的终止信号）

**14** ALRM（闹钟）

**15** TERM（软件终止信号）

某些 shell 可能提供与此实用程序类似或相同的内建 `kill` 命令。请参阅 [builtin(1)](builtin.1.md) 手册页。

## 退出状态

`kill` 实用程序成功时退出 0，发生错误时退出 >0。

## 实例

终止 PID 为 142 和 157 的进程：

```sh
kill 142 157
```

向 PID 为 507 的进程发送挂起信号（`SIGHUP`）：

```sh
kill -s HUP 507
```

终止 PGID 为 117 的进程组：

```sh
kill -- -117
```

## 参见

[builtin(1)](builtin.1.md), [csh(1)](csh.1.md), [killall(1)](killall.1.md), [ps(1)](ps.1.md), [sh(1)](sh.1.md), [kill(2)](../sys/kill.2.md), [sigaction(2)](../sys/sigaction.2.md)

## 标准

`kill` 实用程序应符合 IEEE Std 1003.2 ("POSIX.2") 标准。

## 历史

`kill` 命令首次出现于 Version 3 AT&T UNIX，位于手册的第 8 节。

## 缺陷

应该为 [csh(1)](csh.1.md) 用户提供 "`kill 0`" 命令的替代方案。
