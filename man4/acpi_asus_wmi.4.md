# acpi_asus_wmi(4)

`acpi_asus_wmi` — Asus 笔记本 WMI 附加功能

## 名称

`acpi_asus_wmi`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device acpi_asus_wmi

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
acpi_asus_wmi_load="YES"
```

## 描述

`acpi_asus_wmi` 驱动为 Asus 笔记本上由 WMI 控制的附加设备（如热键和 LED）提供支持。它允许使用 [sysctl(8)](../man8/sysctl.8.md) 接口调节 LCD 面板和键盘背光的亮度、开启或关闭 WiFi、蓝牙、摄像头、读卡器等内部组件，以及读取某些传感器。热键事件会传递给 devd(8)，以便在用户空间中借助 **`/etc/devd/asus.conf`** 中的默认配置轻松处理。一些热键事件，例如键盘背光和触摸板控制，由驱动内部处理。

## SYSCTL 变量

当前实现了以下 sysctl：

**`dev.acpi_asus_wmi.0.handle_keys`** 指定驱动是否应在内部处理某些硬件按键，例如键盘背光。

同一 sysctl 分支下的其他许多变量与具体型号相关。

这些变量的默认值可在 [sysctl.conf(5)](../man5/sysctl.conf.5.md) 中设置，该文件在引导时解析。

## 文件

**`/dev/backlight/acpi_asus_wmi0`** 键盘 backlight(8) 设备节点。

## 参见

[acpi(4)](acpi.4.md), [acpi_asus(4)](acpi_asus.4.md), [acpi_video(4)](acpi_video.4.md), [sysctl.conf(5)](../man5/sysctl.conf.5.md), backlight(8), devd(8), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`acpi_asus_wmi` 驱动最早出现在 FreeBSD 10.0 中。

## 作者

Alexander Motin <mav@FreeBSD.org>
