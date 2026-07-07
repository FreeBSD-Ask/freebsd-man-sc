# ichwd(4)

`ichwd` — Intel ICH 看门狗中断定时器设备驱动

## 名称

`ichwd`

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device ichwd

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
ichwd_load="YES"
```

## 描述

`ichwd` 驱动为所有 Intel ICH 主板芯片组上存在的看门狗中断定时器提供 [watchdog(4)](watchdog.4.md) 支持。

ICH WDT 以约 0.6 秒的滴答倒数计时；具体值取决于硬件质量和环境因素。支持的看门狗间隔范围为 2 到 63 个滴答。

在 QEMU 中，有一种基于 Intel 6300ESB 控制器 hub 的 x86 系统专用看门狗实现。该内核模块提供了对此看门狗的支持。

可选地，将 `hw.i6300esbwd.x.locked=1` [sysctl(8)](../man8/sysctl.8.md) 设置为 1，可防止用户在看门狗超时检查启用后将其禁用。

注意，在某些基于 ICH 的系统上，WDT 可能存在但被禁用（在硬件中或由 BIOS 禁用）。`ichwd` 驱动会尝试检测此状况，并在认为 WDT 已禁用时拒绝附着。

## 参见

[watchdog(4)](watchdog.4.md), [watchdog(8)](../man8/watchdog.8.md), [watchdogd(8)](../man8/watchdogd.8.md), [watchdog(9)](../man9/watchdog.9.md)

> "Using the Intel ICH Family Watchdog Timer (WDT)", Document Number 292273-001.

## 历史

`ichwd` 驱动最早出现于 FreeBSD 5.3。

## 作者

`ichwd` 驱动由 Texas A&M University 的 Wm. Daryl Hawkins <dhawkins@tamu.edu> 和 Dag-Erling Smørgrav <des@FreeBSD.org> 编写。本手册页由 Dag-Erling Smørgrav <des@FreeBSD.org> 编写。
