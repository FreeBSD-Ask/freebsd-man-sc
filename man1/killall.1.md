# killall(1)

`killall` — 按名称终止进程

## 名称

`killall`

## 概要

`killall [-delmsvz] [-help] [-I] [-j jail] [-u user] [-t tty] [-c procname] [-SIGNAL] [procname ...]`

## 描述

`killall` 实用程序按名称选择并终止进程，与 [kill(1)](kill.1.md) 按 PID 选择进程的方式不同。默认情况下，它会向所有真实 UID 与 `killall` 调用者相同且匹配 `procname` 名称的进程发送 `TERM` 信号。超级用户可以终止任何进程。

选项如下：

**`-d`** 更详细地显示将要执行的操作，但不发送任何信号。显示用户进程总数和真实用户 ID。将打印将要发送信号的进程列表，或显示一条表示未找到匹配进程的消息。

**`-e`** 对 `-u` 选项指定的匹配进程，使用有效用户 ID 而非（默认的）真实用户 ID。

**`-help`** 显示命令用法帮助并退出。

**`-I`** 在尝试向每个进程发送信号前请求确认。

**`-l`** 列出可用信号的名称并退出，与 [kill(1)](kill.1.md) 类似。

**`-m`** 将参数 `procname` 作为（区分大小写的）正则表达式与找到的进程名称进行匹配。注意！这很危险，单个点号就会匹配调用者真实 UID 下运行的任何进程。

**`-v`** 详细显示将要执行的操作。

**`-s`** 与 `-v` 相同，但不发送任何信号。

**`-SIGNAL`** 发送不同的信号而非默认的 `TERM`。信号可以指定为名称（带有或不带前导 "`SIG`"）或数字。

**`-j`** `jail` 终止指定 `jail` 中的进程。

**`-u`** `user` 将潜在匹配进程限制为属于指定 `user` 的进程。

**`-t`** `tty` 将潜在匹配进程限制为在指定 `tty` 上运行的进程。

**`-c`** `procname` 将潜在匹配进程限制为匹配指定 `procname` 的进程。

**`-q`** 如果没有匹配的进程，则抑制错误消息。

**`-z`** 不跳过僵尸进程。除了在存在匹配指定模式的僵尸进程时打印几条错误消息外，这不应有任何影响。

## 所有进程

向给定 UID 的所有进程发送信号已经由 [kill(1)](kill.1.md) 支持。因此，使用 [kill(1)](kill.1.md) 来完成这项工作（例如 "`kill -TERM -1`" 或以 root 身份执行 "`echo kill -TERM -1 | su -m <user>`"）。

## 实现说明

FreeBSD 的 `killall` 实现与传统 UNIX System V 的 `killall` 行为语义完全不同。后者会终止当前用户能够终止的所有进程，仅用于系统关机过程。

## 退出状态

如果找到并成功向某些进程发送信号，`killall` 实用程序退出 0。否则，返回状态码 1。

## 实例

向所有 firefox 进程发送 `SIGTERM`：

```sh
killall firefox
```

向属于 `USER` 的 firefox 进程发送 `SIGTERM`：

```sh
killall -u ${USER} firefox
```

停止所有 firefox 进程：

```sh
killall -SIGSTOP firefox
```

恢复 firefox 进程：

```sh
killall -SIGCONT firefox
```

显示将对 firefox 进程执行的操作，但不实际发送信号：

```sh
killall -s firefox
```

向 jail ID 282 中运行的 csh 进程发送 `SIGKILL`：

```sh
killall -9 -j282 csh
```

向匹配指定模式的所有进程发送 `SIGTERM`（如 vim 和 vimdiff）：

```sh
killall -m 'vim*'
```

## 诊断

仅在使用 `-d` 标志时才会打印诊断消息。

## 参见

[kill(1)](kill.1.md), pkill(1), [sysctl(3)](../gen/sysctl.3.md), [jail(8)](../man8/jail.8.md)

## 历史

`killall` 命令首次出现于 FreeBSD 2.1。它是模仿其他平台上可用的 `killall` 命令而创建的。

## 作者

`killall` 程序最初由 Perl 编写，由 Wolfram Schneider 贡献，本手册页由 Jörg Wunsch 编写。当前版本的 `killall` 由 Peter Wemm 使用 sysctl(3) 用 C 重写。
