  TIMEOUT(1)  

TIMEOUT(1)

FreeBSD General Commands Manual

TIMEOUT(1)

[名称](#__u540D___u79F0_)
=======================

`timeout` —

运行有时间限制的命令

[概要](#__u6982___u8981_)
=======================

`timeout` \[`--signal` sig | `-s` sig\] \[`--preserve-status`\] \[`--kill-after` time | `-k` time\] \[`--foreground`\] duration command \[args ...\]

[描述](#__u63CF___u8FF0_)
=======================

`timeout` 用它的 args 启动 command 。如果该 command 在 duration 时间后仍在运行，则将其杀死。默认情况下，发送 `SIGTERM` 。特殊 duration 时间为零，表示没有限制。因此，如果 duration 时间为 0，则永远不会发送信号。

选项如下：

[`--preserve-status`](#-preserve-status)

以与 command 相同的状态退出，即使它超时并被杀死。

[`--foreground`](#-foreground)

不要将超时传播给 command 的孩子。

[`-s`](#s) sig, `--signal` sig

指定超时时发送的信号。 默认情况下，发送 `SIGTERM` 。

[`-k`](#k) time, `--kill-after` time

如果在发送第一个信号后的一段 time 后 command 仍在运行，则发送 `SIGKILL` 信号。

[持续时间格式](#__u6301___u7EED___u65F6___u95F4___u683C___u5F0F_)
===========================================================

duration 时间和 time 是非负整数或实数（十进制），带有可选的单位指定后缀。 没有明确单位的值被解释为秒。

支持的单位符号有：

[`s`](#s_2)

秒

[`m`](#m)

分钟

[`h`](#h)

小时

[`d`](#d)

天

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

如果未达到超时，则返回 command 的退出状态。

如果达到超时并设置了 `--preserve-status` ，则返回 command 的退出状态。 如果 `--preserve-status` 未设置，则返回退出状态 124。

如果 command 收到信号后退出，返回的退出状态为信号号加 128。

如果 command 引用了一个不存在的程序，则返回的退出状态为 127。

如果 command 是其他无效程序，则返回的退出状态为 126。

如果将无效参数传递给 `-s` 或 `-k`, 则返回的退出状态为 125。

[实例](#__u5B9E___u4F8B_)
=======================

以 4 秒的时间限制运行 sleep(1) 。 由于命令在 2 秒内完成，因此退出状态为 0：

$ timeout 4 sleep 2 $ echo $? 0 

运行 sleep(1) 4 秒并在 2 秒后终止进程。 因为没有使用 `--preserve-status` ，所以返回 124：

$ timeout 2 sleep 4 $ echo $? 124 

与上述相同，但保留状态。 退出状态为 128 + 信号编号（ SIGTERM 为 15）

$ timeout --preserve-status 2 sleep 4 $ echo $? 143 

与上述相同，但发送 SIGALRM （信号编号 14）而不是 SIGTERM

$ timeout --preserve-status -s SIGALRM 2 sleep 4 $ echo $? 142 

尝试 fetch(1) FreeBSD 手册的单页版本。 如果进程拒绝停止，则在 1 分钟后发送 SIGTERM 信号，并在 5 秒后发送 SIGKILL 信号：

timeout -k 5s 1m fetch \\ https://www.freebsd.org/doc/en\_US.ISO8859-1/books/handbook/book.html 

[参见](#__u53C2___u89C1_)
=======================

kill(1), signal(3)

[历史](#__u5386___u53F2_)
=======================

`timeout` 命令最早出现在 FreeBSD 10.3 中。

[作者](#__u4F5C___u8005_)
=======================

Baptiste Daroussin <[bapt@FreeBSD.org](mailto:bapt@FreeBSD.org)\> 和 Vsevolod Stakhov <[vsevolod@FreeBSD.org](mailto:vsevolod@FreeBSD.org)\>

July 7, 2020

FreeBSD 13.1-RELEASE