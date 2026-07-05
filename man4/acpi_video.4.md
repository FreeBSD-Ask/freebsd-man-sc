# acpi_video.4

`acpi_video` — ACPI 视频扩展驱动

## 名称

`acpi_video`

## 概要

`device acpi_video`

## 描述

此驱动使用 ACPI 视频扩展来控制显示切换和背光亮度。[sysctl(8)](../man8/sysctl.8.md) 变量的可用性取决于主机的 ACPI 实现所提供的功能。

## SYSCTL 变量

目前实现了以下 sysctl，其中 <`device`> 为 `crt`、`lcd` 或 `tv`：

**`hw.acpi.video.`** <`device`>`.active` 输出设备的当前状态。

**`hw.acpi.video.`** <`device`>`.levels` 支持的亮度级别列表。

**`hw.acpi.video.`** <`device`>`.brightness` 设备当前的亮度级别。

**`hw.acpi.video.`** <`device`>`.fullpower` 全功率模式下使用的预设亮度级别。

**`hw.acpi.video.`** <`device`>`.economy` 经济模式下使用的预设亮度级别。

这些变量的默认值可在 [sysctl.conf(5)](../man5/sysctl.conf.5.md) 中设置，该文件在引导时解析。

## 兼容性

为使 `acpi_video` 正确附加，`acpi_video` 应在任何 DRM 内核模块之后加载。这可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中使用 kld_list 指令设置正确的顺序来实现。

## 参见

[acpi(4)](acpi.4.md), loader.conf(5), [sysctl.conf(5)](../man5/sysctl.conf.5.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`acpi_video` 驱动首次出现于 FreeBSD 5.3。

## 作者

`acpi_video` 驱动由 Taku YAMAMOTO <taku@cent.saitama-u.ac.jp> 编写。本手册页由 Mark Santcroos <marks@ripe.net> 编写。

## 缺陷

某些系统尽管通过 ACPI 导出了正确的信息，但仅通过 SMM 执行输出切换。在此类系统上，必须改用相应的热键或 OEM 驱动（例如 [acpi_toshiba(4)](acpi_toshiba.4.md)）。
