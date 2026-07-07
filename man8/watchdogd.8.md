# watchdogd(8)

`watchdogd` — 看门狗守护进程

## 名称

`watchdogd`

## 概要

`watchdogd [-dnSw] [--debug] [--softtimeout] [--softtimeout-action action] [--pretimeout timeout] [--pretimeout-action action] [-e cmd] [-I file] [-s sleep] [-t timeout] [-T script_timeout] [-x exit_timeout]`

## 描述

`watchdogd` 工具与内核的看门狗功能交互，以确保系统处于工作状态。如果 `watchdogd` 在特定超时时间内无法与内核交互，内核将采取行动以协助调试或重启计算机。

如果指定了 `-e` `cmd`，`watchdogd` 将尝试用 system(3) 执行此命令，仅当命令以零退出码返回时才会重置看门狗。如果未指定 `-e` `cmd`，守护进程将执行简单的文件系统检查。

`-n` 参数“dry-run”会使看门狗不启用系统看门狗，而仅运行看门狗函数并报告失败。这对于开发新的 watchdogd 脚本很有用，因为如果脚本有问题，系统不会重启。

`-s` `sleep` 参数可用于控制每次检查执行之间的睡眠周期，默认为 10 秒。

`-t` `timeout` 指定所需的超时时间（以秒为单位）。默认超时为 128 秒。

可能导致看门狗超时的一种情况是中断风暴。如果发生这种情况，`watchdogd` 将不再执行，因此内核的看门狗例程将在可配置的超时后采取行动。

`-T` `script_timeout` 指定 watchdogd 抱怨其脚本运行时间过长的阈值（以秒为单位）。如果未设置，`script_timeout` 默认为 `-s` `sleep` 选项指定的值。

`-x` `exit_timeout` 参数是程序退出时生效的超时时间（以秒为单位）。使用 `-x` 并指定非零值可在软件重启未在给定超时到期前完成时触发硬件重置，从而防止重启期间死锁。

收到 `SIGTERM` 或 `SIGINT` 信号时，`watchdogd` 将终止，但会先指示内核禁用超时或将其重置为 `-x` `exit_timeout` 给定的值。

`watchdogd` 工具识别以下运行时选项：

**`-I`** `file` 将 `watchdogd` 工具的进程 ID 写入指定文件。

**`-d`**, **`--debug`** 不 fork。指定此选项时，`watchdogd` 在启动时不会 fork 到后台。

**`-S`** 当看门狗命令执行时间超过预期时不向系统日志器发送消息。默认行为是通过系统日志器以 LOG_DAEMON 设施记录警告，并向标准错误输出警告。

**`-w`** 当看门狗脚本执行时间过长时发出抱怨。此标志会使 watchdogd 在执行看门狗脚本的时间超过“sleep”选项阈值时发出抱怨。

**`--pretimeout`** `timeout` 设置“预超时”看门狗。在看门狗触发前“timeout”秒尝试执行操作。操作由 --pretimeout-action 标志设置。默认仅通过 log(9) 记录一条消息（WD_SOFT_LOG）。

**`--pretimeout-action`** `action` 设置预超时的超时操作。参见“超时操作”章节。

**`--softtimeout`** 不启用各种硬件看门狗，仅使用基本的软件看门狗。默认操作仅通过 log(9) 记录一条消息（WD_SOFT_LOG）。

**`--softtimeout-action`** `action` 设置软超时的超时操作。参见“超时操作”章节。

## 超时操作

以下超时操作可通过 `--pretimeout-action` 和 `--softtimeout-action` 标志使用：

**`panic`** 达到超时时调用 [panic(9)](../man9/panic.9.md)。

**`ddb`** 达到超时时通过 kdb_enter(9) 进入内核调试器。

**`log`** 达到超时时使用 log(9) 记录一条消息。

**`printf`** 调用内核 [printf(9)](../man9/printf.9.md) 向控制台和 [dmesg(8)](dmesg.8.md) 缓冲区显示消息。

操作可以逗号分隔列表的形式组合，例如：`log,printf` 将同时执行 [printf(9)](../man9/printf.9.md) 和 log(9)，向 [dmesg(8)](dmesg.8.md) 和内核 log(4) 设备发送消息以供 syslogd(8) 使用。

## 文件

**/var/run/watchdogd.pid**

## 实例

### 调试 watchdogd 和/或你的看门狗脚本

这是调试 `watchdogd` 和你的看门狗脚本的有用方法。

（注意 ^C 的行为有些奇怪，因为 `watchdogd` 调用 system(3)，所以第一个 ^C 会终止 "sleep" 命令。）

所用选项说明：

1. 设置调试开启（--debug）
2. 设置看门狗在 30 秒触发。（-t 30）

3. 使用软超时：
   1. 使用软超时（不启用硬件看门狗）。（--softtimeout）
   2. 设置软超时操作在触发时同时执行内核 [printf(9)](../man9/printf.9.md) 和 log(9)。（--softtimeout-action log,printf）

4. 使用预超时：
   1. 设置 15 秒的预超时（稍后将触发 panic/dump）。（--pretimeout 15）
   2. 设置操作在触发时也执行内核 [printf(9)](../man9/printf.9.md) 和 log(9)。（--pretimeout-action log,printf）

5. 使用脚本：
   1. 运行 "sleep 60" 作为充当看门狗的 shell 命令（-e 'sleep 60'）
   2. 当脚本运行时间超过 1 秒时发出警告（-w）

```sh
watchdogd --debug -t 30 \
  --softtimeout --softtimeout-action log,printf \
  --pretimeout 15 --pretimeout-action log,printf \
  -e 'sleep 60' -w
```

### 生产环境使用示例

1. 设置硬超时为 120 秒（-t 120）
2. 设置 60 秒时发生 panic（以触发 [crash(8)](crash.8.md) 进行转储分析）：
   1. 使用预超时（--pretimeout 60）
   2. 指定预超时操作（--pretimeout-action log,printf,panic ）

3. 使用脚本：
   1. 运行你的脚本（-e '/path/to/your/script 60'）
   2. 如果脚本运行时间超过 15 秒则记录日志。（-w -T 15）

```sh
watchdogd  -t 120 \
  --pretimeout 60 --pretimeout-action log,printf,panic \
  -e '/path/to/your/script 60' -w -T 15
```

## 参见

[watchdog(4)](../man4/watchdog.4.md), [watchdog(8)](watchdog.8.md), [watchdog(9)](../man9/watchdog.9.md)

## 历史

`watchdogd` 工具出现于 FreeBSD 5.1。

## 作者

`watchdogd` 工具和手册页由 Sean Kelly <smkelly@FreeBSD.org> 和 Poul-Henning Kamp <phk@FreeBSD.org> 编写。

Jeff Roberson <jeff@FreeBSD.org> 做出了一些贡献。

预超时和软超时操作系统由 Alfred Perlstein <alfred@freebsd.org> 添加。
