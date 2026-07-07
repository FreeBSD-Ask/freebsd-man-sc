# fwget(8)

`fwget` — 为运行中的系统安装固件包

## 名称

`fwget`

## 概要

`fwget [-n] [-v] [subsystem]`

## 描述

`fwget` 工具可用于检测并为运行中系统上存在的设备安装固件包。

选项如下：

**`-n`** 干运行，仅显示所需的包。

**`-v`** 输出更详细的信息。

**`subsystem`** 硬件子系统，默认为所有支持的子系统。多个硬件子系统以空格分隔，接受 `pci` 和 `usb`。

## 参见

[firmware(9)](../man9/firmware.9.md)

## 历史

`fwget` 工具首次出现在 FreeBSD 14.0 中。

## 作者

`fwget` 工具及本手册页由 Emmanuel Vadot <manu@FreeBSD.org> 为 Beckhoff Automation GmbH & Co. KG 编写。

## 注意事项

此工具目前仅支持 [pci(4)](../man4/pci.4.md) 和 [usb(4)](../man4/usb.4.md) 子系统。
