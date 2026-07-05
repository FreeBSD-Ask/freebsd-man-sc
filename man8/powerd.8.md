# powerd.8

`powerd` — 系统电源控制工具

## 名称

`powerd`

## 概要

`powerd [-a mode] [-b mode] [-i percent] [-M freq] [-m freq] [-N] [-n mode] [-P pidfile] [-p ival] [-r percent] [-s source] [-v]`

## 描述

`powerd` 工具监视系统状态并相应地设置各种电源控制选项。它提供了可分别为交流电源或电池供电选择的节能模式。

**`maximum`** 选择最高性能值。可缩写为 `max`。

**`minimum`** 选择最低性能值以获得最大的节能效果。可缩写为 `min`。

**`adaptive`** 试图在系统空闲时降低性能、系统繁忙时提高性能之间寻求平衡。它在小幅性能损失与大幅节能之间提供了良好的平衡。可缩写为 `adp`。

**`hiadaptive`** 类似于 `adaptive` 模式，但针对性能和交互性比功耗更重要的系统进行了调优。它提高频率更快，降低频率不那么激进，并将更长时间地维持满频率。可缩写为 `hadp`。

默认模式为电池供电时使用 `adaptive`，其他情况使用 `hiadaptive`。

`powerd` 识别以下运行时选项：

**`-a`** `mode` 选择在交流电源供电时使用的 `mode`。

**`-b`** `mode` 选择在电池供电时使用的 `mode`。

**`-i`** `percent` 指定 adaptive 模式应开始降低性能以节省电量时的 CPU 负载百分比水平。默认为 50% 或更低。

**`-M`** `freq` 指定要提升到的最大频率。

**`-m`** `freq` 指定要降低到的最小频率。

**`-N`** 在计算负载时将“nice”时间视为空闲；即如果 CPU 仅忙于“nice”进程，则不提高 CPU 频率。

**`-n`** `mode` 选择在交流电源状态未知时通常使用的 `mode`。

**`-P`** `pidfile` 指定存储进程 ID 的替代文件。

**`-p`** `ival` 指定交流电源状态和系统空闲水平的不同轮询间隔（以毫秒为单位）。默认为 250 ms。

**`-r`** `percent` 指定 adaptive 模式应认为 CPU 正在运行并提高性能时的 CPU 负载百分比水平。默认为 75% 或更高。

**`-s`** `source` 强制指定交流电源状态刷新的方法；默认自动选择。有效方法集合为 `sysctl`、`devd` 和 `apm`（仅 i386）。

**`-v`** 详细模式。有关电源更改的消息将打印到 stdout，`powerd` 将在前台运行。

## 文件

**/var/run/powerd.pid** 默认的 PID 文件。

## 参见

[acpi(4)](../man4/acpi.4.md), [apm(4)](../man4/apm.4.i386.md), [cpufreq(4)](../man4/cpufreq.4.md), [rc.conf(5)](../man5/rc.conf.5.md)

## 历史

`powerd` 工具首次出现在 FreeBSD 6.0 中。

## 作者

Colin Percival 最初编写了 `estctrl`，`powerd` 即基于该工具。Nate Lawson 随后将其更新以适配 [cpufreq(4)](../man4/cpufreq.4.md)，添加了功能并编写了本手册页。

## 缺陷

`powerd` 工具还应降低空闲磁盘和其他组件的功耗，而不仅仅是 CPU。

如果 `powerd` 与 **/etc/rc.d/power_profile** 一起使用，它们可能会相互覆盖。

`powerd` 工具可能应该使用 [devctl(4)](../man4/devctl.4.md) 接口，而不是轮询交流电源状态。
