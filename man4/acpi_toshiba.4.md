# acpi_toshiba.4

`acpi_toshiba` — Toshiba HCI 接口

## 名称

`acpi_toshiba`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device acpi_toshiba

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
acpi_toshiba_load="YES"
```

## 描述

HCI 是 Toshiba 的 *Hardware Control Interface*，在其各型号间较为统一。`acpi_toshiba` 驱动允许用户使用若干 [sysctl(8)](../man8/sysctl.8.md) 变量来操作由 HCI 控制的硬件。

## SYSCTL 变量

目前实现了以下 sysctl：

**`0`** 无显示

**`1`** LCD

**`2`** CRT

**`4`** TV-Out

**`hw.acpi.toshiba.force_fan`** 无论当前温度如何，强制启用（`1`）或禁用（`0`）主动散热。

**`hw.acpi.toshiba.video_output`** 根据以下值的按位 OR 来设置要使用的活动显示：仅某些系统（即 Libretto L5）支持通过此硬件专用驱动进行视频切换。请使用 [acpi_video(4)](acpi_video.4.md) 驱动以获得通用的视频输出支持。

**`hw.acpi.toshiba.lcd_brightness`** 使 LCD 背光更亮或更暗（值越大越亮）。

**`hw.acpi.toshiba.lcd_backlight`** 打开和关闭 LCD 背光。

**`hw.acpi.toshiba.cpu_speed`** 将 CPU 速度设置为指定速度。这提供与 `hw.acpi.cpu.throttle_state` 变量类似的功能。sysctl 值越大表示 CPU 速度越低。

这些变量的默认值可在 [sysctl.conf(5)](../man5/sysctl.conf.5.md) 中设置，该文件在引导时解析。

## 加载器可调参数

`hw.acpi.toshiba.enable_fn_keys` 可调参数启用或禁用键盘上的功能键。默认启用功能键。

此行为可在 [loader(8)](../man8/loader.8.md) 提示符下或 loader.conf(5) 中更改。

## 参见

[acpi(4)](acpi.4.md), [acpi_video(4)](acpi_video.4.md), loader.conf(5), [sysctl.conf(5)](../man5/sysctl.conf.5.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`acpi_toshiba` 驱动首次出现于 FreeBSD 5.1。

## 作者

`acpi_toshiba` 驱动由 Hiroyuki Aizu <aizu@navi.org> 编写。本手册页由 Philip Paeps <philip@FreeBSD.org> 编写。
