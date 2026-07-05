# wdatwd.4

`wdatwd` — 基于 ACPI WDAT 的看门狗中断定时器设备驱动

## 名称

`wdatwd`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device wdatwd

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
wdatwd_load="YES"
```

## 描述

`wdatwd` 驱动为 ACPI WDAT（看门狗动作表）中的看门狗中断定时器提供 [watchdog(4)](watchdog.4.md) 支持。

由于 WDAT 本身是真实硬件（如 ICH WDT）的抽象，需注意同一时间只能使用一个驱动，要么是真实硬件专用驱动，要么是本驱动。

## SYSCTL 变量

以下只读 [sysctl(8)](../man8/sysctl.8.md) 变量可用：

**`dev.wdatwd.%d.running`** 看门狗定时器的状态。0 表示未运行，1 表示运行中。

**`dev.wdatwd.%d.timeout`** 看门狗超时的当前值（毫秒）。在某些系统上可能为 0，零值表示使用默认超时。

**`dev.wdatwd.%d.timeout_configurable`** 超时是否可配置。0 表示可配置，任何正值表示不可配置。

**`dev.wdatwd.%d.timeout_default`** 看门狗超时的默认值（毫秒），如果有的话。

## 参见

[ichwd(4)](ichwd.4.md), [watchdog(4)](watchdog.4.md), [watchdog(8)](../man8/watchdog.8.md), [watchdogd(8)](../man8/watchdogd.8.md), [watchdog(9)](../man9/watchdog.9.md)

> Microsoft Corporation, "Hardware Watchdog Timers Design Specification", 2006.

## 作者

`wdatwd` 驱动由 MACOME 公司的 Tetsuya Uemura <t_uemura@macome.co.jp> 编写。
