# acpi_sony.4

`acpi_sony` — Sony 笔记本的 ACPI 笔记本控制器驱动

## 名称

`acpi_sony`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device acpi_sony

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
acpi_sony_load="YES"
```

## 描述

`acpi_sony` 驱动提供对 Sony 笔记本中笔记本控制器的支持。请注意，并非所有功能在所有笔记本型号上都可用。

## SYSCTL

目前实现了以下 sysctl 节点：

**`dev.acpi_sony.0.brightness`** 显示当前的亮度级别。

**`dev.acpi_sony.0.brightness_default`** 显示的默认亮度级别（重启后仍生效）。

**`dev.acpi_sony.0.contrast`** 显示当前的对比度级别。

**`dev.acpi_sony.0.bass_gain`** 启用或禁用 Bass Gain 功能。

**`dev.acpi_sony.0.cdp`** 打开或关闭 CD 电源。

**`dev.acpi_sony.0.azp`** 打开或关闭音频电源。

**`dev.acpi_sony.0.lnp`** 打开或关闭有线网络接口电源。

## 参见

[acpi(4)](acpi.4.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`acpi_sony` 驱动首次出现于 FreeBSD 6.0。

## 作者

`acpi_sony` 驱动由 Takanori Watanabe <takawata@FreeBSD.org> 编写。
