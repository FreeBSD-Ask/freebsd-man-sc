# truss.1

`truss` — 跟踪系统调用

## 名称

`truss`

## 概要

`truss [-facedDHS] [-o file] [-s strsize] -p pid`

`truss [-facedDHS] [-o file] [-s strsize] command [args]`

## 描述

`truss` 实用程序跟踪指定进程或程序所调用的系统调用。输出到指定输出文件，默认为标准错误。它通过 ptrace(2) 停止并重启被监视的进程来实现此功能。

选项如下：

**`-f`** 跟踪由 fork(2)、vfork(2) 等创建的原始被跟踪进程的后代。为区分进程间的事件，每次事件的输出中包含进程的进程 ID（PID）。

**`-a`** 显示每次 execve(2) 系统调用中传递的参数字符串。

**`-c`** 不显示单个系统调用或信号。而是在退出前打印摘要，包含每个系统调用的：使用的总系统时间、调用次数以及调用返回错误的次数。

**`-e`** 显示每次 execve(2) 系统调用中传递的环境字符串。

**`-d`** 在输出中包含时间戳，显示自跟踪开始以来流逝的时间。

**`-D`** 在输出中包含时间戳，显示自上次记录事件以来流逝的时间。

**`-H`** 在每次事件的输出中包含线程 ID。

**`-S`** 不显示进程接收到的信号信息。（通常，`truss` 同时显示信号和系统调用事件。）

**`-o`** `file` 将输出打印到指定的 `file` 而非标准错误。

**`-s`** `strsize` 显示字符串时最多使用 `strsize` 个字符。如果缓冲区更大，字符串末尾将显示 "..."。默认 `strsize` 为 32。

**`-p`** `pid` 跟踪由 `pid` 指定的进程，而非新命令。

**`command`** [`args`] 执行 `command` 并跟踪其系统调用。（`-p` 和 `command` 选项互斥。）

## 实例

跟踪用于回显 "hello" 的系统调用：

```sh
$ truss /bin/echo hello
```

与上例相同，但将输出写入文件：

```sh
$ truss -o /tmp/truss.out /bin/echo hello
```

跟踪一个已在运行的进程：

```sh
$ truss -p 34
```

## 参见

[dtrace(1)](dtrace.1.md), [kdump(1)](kdump.1.md), [ktrace(1)](ktrace.1.md), ptrace(2), utrace(2), sysdecode(3)

## 历史

`truss` 命令由 Sean Eric Fagan 为 FreeBSD 编写。它仿照 System V Release 4 和 SunOS 上可用的类似命令。
