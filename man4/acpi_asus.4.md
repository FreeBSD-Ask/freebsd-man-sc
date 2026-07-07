# acpi_asus(4)

`acpi_asus` — Asus 笔记本附加功能

## 名称

`acpi_asus`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device acpi_asus

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
acpi_asus_load="YES"
```

## 描述

`acpi_asus` 驱动提供对近期 Asus（和 Medion）笔记本上由 ACPI 控制的附加设备（如热键和指示灯）的支持。它允许通过 [sysctl(8)](../man8/sysctl.8.md) 接口来调节 LCD 面板的亮度和显示输出状态。热键事件会传递给 devd(8)，以便通过 **`/etc/devd/asus.conf`** 中的默认配置在用户态中轻松处理。

目前，以下 Asus 笔记本受到完全支持：

- xxN
- A1x
- A2x
- A3N
- A4D
- A6VM
- D1x
- J1x
- L2B
- L2D
- L2E
- L3C
- L3D
- L3H
- L4E
- L4R
- L5x
- L8x
- M1A
- M2E
- M6N
- M6R
- S1x
- S2x
- V6V
- W5A
- Eee PC

此外，`acpi_asus` 还支持在 *Samsung P30/P35* 笔记本中发现的 Asus 兼容 *ATK0100* 接口。

## SYSCTL 变量

目前实现了以下 sysctl：

**`0`** 无显示

**`1`** LCD

**`2`** CRT

**`4`** TV-Out

**`hw.acpi.asus.lcd_brightness`** 使 LCD 背光更亮或更暗（值越大越亮）。

**`hw.acpi.asus.lcd_backlight`** 打开或关闭 LCD 背光。

**`hw.acpi.asus.video_output`** 根据以下值的按位 OR 来设置要使用的活动显示：某些型号还支持通过通用 [acpi_video(4)](acpi_video.4.md) 驱动进行视频切换。但大多数型号不支持。

这些变量的默认值可在 [sysctl.conf(5)](../man5/sysctl.conf.5.md) 中设置，该文件在引导时解析。

## 参见

[acpi(4)](acpi.4.md), [acpi_asus_wmi(4)](acpi_asus_wmi.4.md), [acpi_video(4)](acpi_video.4.md), [sysctl.conf(5)](../man5/sysctl.conf.5.md), [sysctl(8)](../man8/sysctl.8.md)

> "The acpi4asus Project".

## 历史

`acpi_asus` 驱动首次出现于 FreeBSD 5.3。

## 作者

`acpi_asus` 驱动及本手册页由 Philip Paeps <philip@FreeBSD.org> 编写。

灵感来自 Julien Lerouge 发起的 *acpi4asus project*，该项目维护了一个在 Linux 内核中实现此功能的驱动。
