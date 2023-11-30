  TRUSS(1)  

TRUSS(1)

FreeBSD General Commands Manual

TRUSS(1)

[NAME](#NAME)
=============

`truss` —

跟踪系统调用

[概要](#__u6982___u8981_)
=======================

`truss` \[`-facedDHS`\] \[`-o` file\] \[`-s` strsize\] `-p` pid `truss` \[`-facedDHS`\] \[`-o` file\] \[`-s` strsize\] command \[args\]

[描述](#__u63CF___u8FF0_)
=======================

`truss` 实用程序跟踪指定进程或程序调用的系统调用。输出到指定的输出文件，默认为标准错误。 它通过停止并重新启动通过 ptrace(2) 监视的进程来实现这一点。

选项如下：

[`-f`](#f)

跟踪由 fork(2) 、 vfork(2) 等创建的原始跟踪进程的后代。 为了区分进程之间的事件，进程的进程 (PID) 包含在每个事件的输出中。

[`-a`](#a)

显示在每个 execve(2) 系统调用中传递的参数字符串。

[`-c`](#c)

不显示单个系统调用或信号。 相反，在退出之前，打印包含每个系统调用的摘要： 使用的总系统时间、调用调用的次数以及调用返回错误的次数。

[`-e`](#e)

显示在每个 execve(2) 系统调用中传递的环境字符串。

[`-d`](#d)

在输出中包含时间戳，显示自跟踪开始以来经过的时间。

[`-D`](#D)

在输出中包含时间戳，显示自上次记录事件以来经过的时间。

[`-H`](#H)

在每个事件的输出中包含线程 ID。

[`-S`](#S)

不显示有关进程接收到的信号的信息。 （通常， `truss` 会显示信号以及系统调用事件。）

[`-o`](#o) file

将输出打印到指定 file 而不是标准错误。

[`-s`](#s) strsize

最多使用 strsize 个字符显示字符串。 如果缓冲区较大， “`...`” 将显示在字符串的末尾。 默认 strsize 为 32。

[`-p`](#p) pid

遵循 pid 指定的进程而不是新命令。

command \[args\]

执行 command 并跟踪它的系统调用。 （ `-p` 和 command 选项是互斥的。）

[实例](#__u5B9E___u4F8B_)
=======================

遵循用于回显 "hello" 的系统调用：

`$ truss /bin/echo hello`

做同样的事情，但是把输出放到一个文件中：

`$ truss -o /tmp/truss.out /bin/echo hello`

遵循已经运行的进程：

`$ truss -p 34`

[参见](#__u53C2___u89C1_)
=======================

dtrace(1), kdump(1), ktrace(1), ptrace(2), utrace(2)

[历史](#__u5386___u53F2_)
=======================

`truss` 命令由 Sean Eric Fagan 为 FreeBSD 编写。 它是根据 System V Release 4 和 SunOS 可用的类似命令建模的。

July 24, 2017

FreeBSD 13.1-RELEASE