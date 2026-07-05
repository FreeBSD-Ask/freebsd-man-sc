# timeout.1

`timeout` — 在时间限制内运行命令

## 名称

`timeout`

## 概要

`timeout [-f | --foreground] [-k time | --kill-after time] [-p | --preserve-status] [-s signal | --signal signal] [-v | --verbose] duration command [arg ...]`

## 描述

`timeout` 使用其 `arg` 参数列表启动 `command`。如果 `command` 在 `duration` 之后仍在运行，则通过发送 `signal` 将其杀死；如果未指定 `-s` 选项，则发送 `SIGTERM`。特殊的 `duration` 值零表示无限制。因此，当 `duration` 为 0 时永远不会发送信号。

`command` 继承的信号处置与 `timeout` 继承的处置相同，但超时后将发送的信号除外，该信号会被重置为采取默认动作，从而终止进程。

如果 `timeout` 收到 `SIGALRM` 信号，它的行为就如同时间限制已到，并向 `command` 发送指定信号。对于发送给 `timeout` 的任何其他信号，它会将其传播给 `command`，但 `SIGKILL` 和 `SIGSTOP` 除外。如果你想阻止 `command` 超时，可向 `timeout` 发送 `SIGKILL`。

选项如下：

**`-f`**, `--foreground` 仅对 `command` 自身超时，不将信号传播给其后代进程。详见“实现说明”一节。

**`-k`** `time`, `--kill-after` `time` 如果在第一次发送信号后 `time` 时间过去 `command` 仍在运行，则发送 `SIGKILL` 信号。

**`-p`**, `--preserve-status` 始终以与 `command` 相同的状态退出，即使已超时。

**`-s`** `signal`, `--signal` `signal` 指定超时时发送的信号。默认发送 `SIGTERM`。

**`-v`**, `--verbose` 向 stderr(4) 显示有关超时、待发送信号以及 `command` 退出的信息。

### 持续时间格式

`duration` 和 `time` 为非负整数或实数（十进制），可选后缀指定单位。未显式指定单位的值按秒解释。

支持的单位后缀有：

**`s`** 秒

**`m`** 分

**`h`** 小时

**`d`** 天

## 实现说明

如果未指定 `--foreground` 选项，`timeout` 将作为 `command` 及其后代进程的回收者（reaper）运行（另见 procctl(2)），并等待所有后代进程终止。如果存在后台运行的后代进程，此行为可能带来意外结果，因为它们会忽略 `SIGINT` 和 `SIGQUIT` 信号。例如，以下发送 `SIGTERM` 信号的命令将在 2 秒内完成：

```sh
$ timeout -s TERM 2 sh -c 'sleep 4 & sleep 5'
```

然而，以下发送 `SIGINT` 信号的命令将在 4 秒内完成：

```sh
$ timeout -s INT 2 sh -c 'sleep 4 & sleep 5'
```

## 退出状态

如果时间限制已到且未指定 `--preserve-status` 选项，退出状态为 124。否则，`timeout` 以与 `command` 相同的退出状态退出。例如，如果 `command` 被信号终止，`timeout` 自身也会以相同信号终止。

如果发生错误，返回以下退出值：

**125** 发生了下文所述两种情况以外的错误。例如，指定了无效的持续时间或信号。

**126** 找到了 `command` 但无法执行。

**127** 找不到 `command`。

## 实例

以 4 秒为时间限制运行 sleep(1)。由于命令在 2 秒内完成，退出状态为 0：

```sh
$ timeout 4 sleep 2
$ echo $?
0
```

运行 sleep(1) 4 秒，并在 2 秒后终止进程。由于未使用 `--preserve-status`，退出状态为 124：

```sh
$ timeout 2 sleep 4
$ echo $?
124
```

与上例相同，但保留状态。对大多数 shell 而言，退出状态为 128 + 信号编号（`SIGTERM` 为 15）：

```sh
$ timeout --preserve-status 2 sleep 4
$ echo $?
143
```

与上例相同，但发送 `SIGALRM`（信号编号 14）而非 `SIGTERM`：

```sh
$ timeout --preserve-status -s SIGALRM 2 sleep 4
$ echo $?
142
```

尝试使用 fetch(1) 获取 FreeBSD Handbook 的 PDF 版本。1 分钟后发送 `SIGTERM` 信号，如果进程拒绝停止，则在 5 秒后发送 `SIGKILL` 信号：

```sh
$ timeout -k 5s 1m fetch \
> https://download.freebsd.org/ftp/doc/en/books/handbook/book.pdf
```

## 参见

[kill(1)](kill.1.md), nohup(1), signal(3), daemon(8)

## 标准

`timeout` 实用程序预期符合 -p1003.1-2024 规范。

`-v` 选项及长选项名是该规范的扩展。

## 历史

`timeout` 命令首次出现于 FreeBSD 10.3。

最初的 FreeBSD 实现与 Padraig Brady 所写 GNU Coreutils 8.21 中的 GNU `timeout` 兼容。`timeout` 实用程序首次出现于 GNU Coreutils 7.0。

## 作者

Baptiste Daroussin <bapt@FreeBSD.org>、Vsevolod Stakhov <vsevolod@FreeBSD.org> 以及 Aaron LI <aly@aaronly.me>
