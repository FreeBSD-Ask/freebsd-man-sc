# sleep(1)

`sleep` — 暂停执行一段时间

## 名称

`sleep`

## 概要

`sleep number[unit] [...]`

## 描述

`sleep` 命令暂停执行至少 `number` 秒（默认，或单位 `s`）、分钟（单位 `m`）、小时（单位 `h`）或天（单位 `d`）。间隔可以用 [strtod(3)](../stdlib/strtod.3.md) 允许的任何形式编写。如果指定了多个间隔，它们将相加。如果最终总和为零或负数，`sleep` 立即退出。

如果 `sleep` 命令收到信号，它采取标准动作。当收到 `SIGINFO` 信号时，在标准输出上打印剩余睡眠秒数的估计值。

## 实现说明

此实现不对 `SIGALRM` 信号进行特殊处理。

## 退出状态

`sleep` 实用程序成功时退出 0，发生错误时退出 >0。

## 实例

在半小时后运行命令：

```sh
(sleep 0.5h; sh command_file >out 2>err)&
```

此命令会等待半小时再运行脚本 `command_file`。参见 [at(1)](at.1.md) 实用程序了解另一种实现方式。

反复运行命令：

```sh
while :; do
	if ! [ -r zzz.rawdata ] ; then
		sleep 5m
	else
		for i in *.rawdata ; do
			sleep 70
			awk -f collapse_data "$i"
		done >results
		break
	fi
done
```

此类脚本的应用场景可能是：当前正在运行的程序处理一系列文件所需的时间比预期的长，而希望另一个程序在第一个程序完成后（即创建 `zzz.rawdata` 时）尽快开始处理第一个程序创建的文件。脚本每五分钟检查一次文件 `zzz.rawdata`，找到文件后，在每个 [awk(1)](awk.1.md) 作业之间礼貌地等待 70 秒来进行另一部分处理。

## 参见

[nanosleep(2)](../sys/nanosleep.2.md), [sleep(3)](../sys-1/sleep.3.md)

## 标准

`sleep` 命令预期与 IEEE Std 1003.2 ("POSIX.2") 兼容。

对非整数间隔、秒以外的单位以及相加的多个间隔的支持是不可移植的扩展，首次引入于 GNU sh-utils 2.0a（2002 年发布）。

## 历史

`sleep` 命令出现在 Version 4 AT&T UNIX 中。
