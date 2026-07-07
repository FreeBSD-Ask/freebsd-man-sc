# usb(4)

`usb` — 通用串行总线

## 名称

`usb`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device usb

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
usb_load="YES"
```

## 用户空间编程

USB 功能可通过 libusb 库从用户空间访问。更多信息请参见 libusb(3)。

## 描述

FreeBSD 为 USB 设备在主机端和设备端模式下提供与机器无关的总线支持和驱动。

`usb` 驱动分为三层：

**USB** 控制器（总线）

**USB** 设备

**USB** 驱动

控制器附加到物理总线（如 [pci(4)](pci.4.md)）。USB 总线附加到控制器，根集线器附加到控制器。连接到总线的任何设备会附加到根集线器或连接到 USB 总线的其他集线器。

`uhub` 设备始终存在，因为根集线器需要它。

## USB 简介

USB 是一种可将外部设备连接到 PC 的系统。最常见的 USB 速度为：

**Low** Speed（低速，1.5 MBit/sec）

**Full** Speed（全速，12 MBit/sec）

**High** Speed（高速，480 MBit/sec）

**SuperSpeed**（5 GBit/sec）

每个 USB 都有一个 USB 控制器，它是总线的主设备。物理通信是单工的，这意味着主机控制器一次只与一个 USB 设备通信。

USB 集线器树最多可连接 127 个设备。地址在设备附加到总线时由主机动态分配。

每个设备内最多可有 16 个端点。每个端点单独寻址，且地址是静态的。这些端点以四种不同模式之一通信：*control（控制）、isochronous（同步）、bulk（批量）* 或 *interrupt（中断）*。设备始终至少有一个端点。此端点地址为 0，是控制端点，用于向设备发出命令和从设备提取基本数据（如描述符）。除控制端点外，每个端点都是单向的。

设备中的端点按接口分组。接口是设备内的逻辑单元，例如同时具有键盘和轨迹球的复合设备会为每个功能分别呈现一个接口。接口有时可设置为不同模式，称为备用设置，这会影响其操作方式。不同的备用设置可具有不同的端点。

设备可在不同配置下运行。依据配置，设备可呈现不同的端点和接口集。

USB 总线的总线枚举分几个步骤进行：

- 任何接口特定驱动都可附加到设备。
- 如果未找到，则可附加通用接口类驱动。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`hw.usb.debug`** 调试输出级别，0 表示禁用调试，更大的值增加调试消息的详细程度。默认为 0。

## 参见

USB 规范可在以下地址找到：

> `https://www.usb.org/documents`

libusb(3), [aue(4)](aue.4.md), [axe(4)](axe.4.md), [axge(4)](axge.4.md), [cue(4)](cue.4.md), [ehci(4)](ehci.4.md), [kue(4)](kue.4.md), [mos(4)](mos.4.md), [ohci(4)](ohci.4.md), [pci(4)](pci.4.md), [rue(4)](rue.4.md), [ucom(4)](ucom.4.md), [udav(4)](udav.4.md), [uhci(4)](uhci.4.md), [uhid(4)](uhid.4.md), [ukbd(4)](ukbd.4.md), [ulpt(4)](ulpt.4.md), [umass(4)](umass.4.md), [ums(4)](ums.4.md), [uplcom(4)](uplcom.4.md), [urio(4)](urio.4.md), [uvscom(4)](uvscom.4.md), [xhci(4)](xhci.4.md) usbconfig(8), [usbdi(9)](../man9/usbdi.9.md)

## 标准

`uhub` 模块符合 USB 3.0 标准。

## 历史

`uhub` 模块受 Lennart Augustsson 最初编写的 NetBSD USB 协议栈启发。`uhub` 模块由 Hans Petter Selasky <hselasky@FreeBSD.org> 编写。
