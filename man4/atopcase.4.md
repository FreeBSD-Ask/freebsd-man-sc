# atopcase.4

`atopcase` — Apple HID-over-SPI 传输驱动

## 名称

`atopcase`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device atopcase
> device intelspi
> device spibus
> device hidbus
> device hkbd

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
atopcase_load="YES"
hkbd_load="YES"
```

## 描述

`atopcase` 驱动为 Apple Intel Mac 上 SPI（Serial Peripheral Interface，串行外设接口）总线的 HID（人机接口设备）提供支持。

## 硬件

`atopcase` 驱动支持以下在 2015-2018 年生产的 MacBook：

- Macbook8,1
- Macbook9,1
- Macbook10,1
- MacbookPro11,4
- MacbookPro12,1
- MacbookPro13,1
- MacbookPro13,2
- MacbookPro13,3
- MacbookPro14,1
- MacbookPro14,2
- MacbookPro14,3

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`hw.hid.atopcase.debug`** 调试输出级别，0 表示禁用调试，更大的值会增加调试消息的详细程度。默认为 0。

## 文件

**`/dev/backlight/atopcase0`** 键盘背光 backlight(8) 设备节点。

## 参见

[acpi(4)](acpi.4.md), loader.conf(5), backlight(8), [loader(8)](../man8/loader.8.md)

## 历史

`atopcase` 驱动首次出现于 FreeBSD 14.0。

## 作者

`atopcase` 驱动最初由 Val Packett <val@packett.cool> 编写，并由 Vladimir Kondratyev <wulf@FreeBSD.org> 做了小幅改进。

本手册页由 Vladimir Kondratyev <wulf@FreeBSD.org> 编写。

## 缺陷

某些硬件上不会确认设备中断，从而导致中断风暴。在 [acpi(4)](acpi.4.md) 驱动中安装 Darwin OSI 可修复此问题。要安装 Darwin OSI，请在 loader.conf(5) 中加入以下行：

**`hw.acpi.install_interface="Darwin"`**

**`hw.acpi.remove_interface="Windows 2009, Windows 2012"`**
