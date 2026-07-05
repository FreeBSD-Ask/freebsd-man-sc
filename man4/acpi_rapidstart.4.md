# acpi_rapidstart.4

`acpi_rapidstart` — Intel Rapid Start 技术 ACPI 驱动

## 名称

`acpi_rapidstart`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device acpi_rapidstart

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
acpi_rapidstart_load="YES"
```

## 描述

`acpi_rapidstart` 驱动为 Intel Rapid Start 技术 ACPI 设备接口提供支持。注意此驱动仅针对 ACPI 设备接口。它具有 _CID PNP0C02，因此应在引导时加载，以避免附加到 acpi_sysresource 驱动。

## SYSCTL

当前实现了以下 [sysctl(8)](../man8/sysctl.8.md) 节点：

**`1`** 在 RTC 唤醒时进入 Fast Flash Standby。
**`2`** 在 Critical Battery 唤醒时进入 Fast Flash Standby（启用）

**`dev.acpi_rapidstart.0.ffs`** Rapid start 标志。它是以下值的按位 OR：

**`dev.acpi_rapidstart.0.ftv`** Fast Flash Standby 定时器值（分钟）。

## 参见

[acpi(4)](acpi.4.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`acpi_rapidstart` 驱动最早出现在 FreeBSD 10.0 中。

## 作者

`acpi_rapidstart` 驱动由 Takanori Watanabe <takawata@FreeBSD.org> 编写。
