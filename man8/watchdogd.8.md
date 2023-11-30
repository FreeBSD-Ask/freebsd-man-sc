  WATCHDOGD(8)  

WATCHDOGD(8)

FreeBSD System Manager's Manual

WATCHDOGD(8)

[名称](#__u540D___u79F0_)
=======================

`watchdogd` —

看门狗守护进程

[概要](#__u6982___u8981_)
=======================

`watchdogd` \[`-dnSw`\] \[`--debug`\] \[`--softtimeout`\] \[`--softtimeout-action` action\] \[`--pretimeout` timeout\] \[`--pretimeout-action` action\] \[`-e` cmd\] \[`-I` file\] \[`-s` sleep\] \[`-t` timeout\] \[`-T` script\_timeout\] \[`-x` exit\_timeout\]

[描述](#__u63CF___u8FF0_)
=======================

`watchdogd` 实用程序与内核的看门狗设施接口，以确保系统处于工作状态。 如果 `watchdogd` 在特定超时后无法与内核交互，内核将采取措施帮助调试或重新启动计算机。

如果指定了 `-e` cmd , `watchdogd` 将尝试使用 system(3) 执行此命令，并且只有当命令返回零退出代码时才会重置 watchdog。 如果未指定 `-e` cmd ，则守护程序将改为执行简单的文件系统检查。

`-n` 参数 'dry-run' 将导致看门狗不武装系统看门狗，而只运行看门狗功能并报告故障。 这对于开发新的 watchdogd 脚本很有用，因为如果脚本出现问题，系统将不会重新启动。

`-s` sleep 参数可用于控制每次执行检查之间的睡眠时间，默认为 10 秒。

`-t` timeout 以秒为单位指定所需的超时时间。 默认超时为 128 秒。

导致看门狗超时的一种可能情况是中断风暴。 如果发生这种情况， `watchdogd` 将不再执行，因此内核的看门狗例程将在可配置的超时后采取行动。

`-T` script\_timeout 指定看门狗将抱怨其脚本运行时间过长的阈值（以秒为单位）。 如果未设置 script\_timeout 默认为 `-s` sleep 选项指定的值。

`-x` exit\_timeout 参数是程序退出时保持有效的超时时间（以秒为单位）。 如果在给定的超时到期之前软件重新启动未完成，则将 `-x` 与非零值一起使用可通过触发硬件重置来防止重新启动期间锁定。

在收到 `SIGTERM` 和 `SIGINT` 信号后， `watchdogd` 将在首先指示内核禁用超时或将其重置为 `-x` exit\_timeout 给出的值之后终止。

`watchdogd` 实用程序可识别以下运行时选项：

[`-I`](#I) file

在指定文件中写入 `watchdogd` 实用程序的进程 ID。

[`-d`](#d) `--debug`

不要分叉。 指定此选项后， `watchdogd` 将不会在启动时分叉到后台。

[`-S`](#S)

当看门狗命令的执行时间比预期的要长时，不要向系统记录器发送消息。 默认行为是使用 LOG\_DAEMON 工具通过系统记录器记录警告，并将警告输出到标准错误。

[`-w`](#w)

当看门狗脚本花费太长时间时抱怨。 当执行 watchdog 脚本的时间超过 'sleep' 选项的阈值时，此标志将导致 watchdogd 抱怨。

[`--pretimeout`](#-pretimeout) timeout

设置 "pretimeout" 设置“pretimeout”看门狗。 在看门狗将触发尝试动作之前的 "timeout" 秒。 该操作由 --pretimeout-action 标志设置。 默认只是通过 log(9) 记录消息 (WD\_SOFT\_LOG)。

[`--pretimeout-action`](#-pretimeout-action) action

设置 pretimeout 的超时操作。 请参阅 [超时操作](#__u8D85___u65F6___u64CD___u4F5C_) 部分。

[`--softtimeout`](#-softtimeout)

而不是武装各种硬件看门狗，只使用一个基本的软件看门狗。 默认操作只是 log(9) 一条消息 (WD\_SOFT\_LOG)。

[`--softtimeout-action`](#-softtimeout-action) action

设置 softtimeout 的超时操作。 请参阅 [超时操作](#__u8D85___u65F6___u64CD___u4F5C_) 部分。

[超时操作](#__u8D85___u65F6___u64CD___u4F5C_)
=========================================

通过 `--pretimeout-action` 和 `--softtimeout-action` 标志可以使用以下超时操作：

panic

达到超时时调用 panic(9) 。

ddb

达到超时时，通过 kdb\_enter(9) 进入内核调试器。

log

达到超时时使用 log(9) 记录消息。

printf

调用内核 printf(9) 向控制台和 dmesg(8) 缓冲区显示一条消息。

可以将操作组合在一个逗号分隔的列表中，如下所示： log,printf 将同时将 printf(9) 和 log(9) 发送到 dmesg(8) 和 syslogd(8) 的内核 log(4) 设备。

[文件](#__u6587___u4EF6_)
=======================

/var/run/watchdogd.pid

[实例](#__u5B9E___u4F8B_)
=======================

[调试 watchdogd 和/或你的 watchdog 脚本。](#__u8C03___u8BD5__watchdogd___u548C_/__u6216___u4F60___u7684__watchdog___u811A___u672C___u3002_)
----------------------------------------------------------------------------------------------------------------------------------

这是调试 `watchdogd` 和看门狗脚本的有用方法。

（注意 ^C 的工作很奇怪，因为 `watchdogd` 调用 system(3) 所以第一个 ^C 将终止 "sleep" 命令。）

使用的选项说明：

1.  设置调试 (--debug)
2.  将看门狗设置为在 30 秒时跳闸。 (-t 30)
3.  使用软超时
    1.  使用软超时（不要武装硬件看门狗） (--softtimeout)
    2.  设置 softtimeout 操作以在它跳闸时同时执行内核 printf(9) 和 log(9) 。 (--softtimeout-action log,printf)
4.  使用预超时：
    1.  设置 15 秒的预超时（这将在稍后触发恐慌/转储）。 (--pretimeout 15)
    2.  跳闸时将操作设置为内核 printf(9) 和 log(9) 。 (--pretimeout-action log,printf)
5.  脚本的使用：
    1.  作为看门狗的 shell 命令运行 "sleep 60" (-e 'sleep 60')
    2.  当脚本运行时间超过 1 秒时警告我们 (-w)

watchdogd --debug -t 30 \\ --softtimeout --softtimeout-action log,printf \\ --pretimeout 15 --pretimeout-action log,printf \\ -e 'sleep 60' -w 

[示例的生产使用](#__u793A___u4F8B___u7684___u751F___u4EA7___u4F7F___u7528_)
--------------------------------------------------------------------

1.  将硬超时设置为 120 秒 (-t 120)
2.  将恐慌设置为在 60 秒发生（触发 crash(8) 以进行转储分析）：
    1.  使用预超时 (--pretimeout 60)
    2.  指定超时前操作 (--pretimeout-action log,printf,panic )
3.  脚本的使用：
    1.  运行你的脚本 (-e '/path/to/your/script 60')
    2.  记录您的脚本运行时间是否超过 15 秒。 (-w -T 15)

watchdogd -t 120 \\ --pretimeout 60 --pretimeout-action log,printf,panic \\ -e '/path/to/your/script 60' -w -T 15 

[参见](#__u53C2___u89C1_)
=======================

watchdog(4), watchdog(8), watchdog(9)

[历史](#__u5386___u53F2_)
=======================

`watchdogd` 实用程序出现在 FreeBSD 5.1 中。

[作者](#__u4F5C___u8005_)
=======================

`watchdogd` 实用程序和手册页由 Sean Kelly <[smkelly@FreeBSD.org](mailto:smkelly@FreeBSD.org)\> 和 Poul-Henning Kamp <[phk@FreeBSD.org](mailto:phk@FreeBSD.org)\> 编写。

Jeff Roberson <[jeff@FreeBSD.org](mailto:jeff@FreeBSD.org)\> 做出的一些贡献。

Alfred Perlstein <[alfred@freebsd.org](mailto:alfred@freebsd.org)\> 添加了 pretimeout 和 softtimeout 操作系统。

May 11, 2015

FreeBSD 13.1-RELEASE