# uhci.4

`uhci` — UHCI USB 主机控制器驱动

## 名称

`uhci`

## 概要

`device uhci`

## 描述

`uhci` 驱动为基于 PCI 的 UHCI 类型 USB 控制器提供支持。

## 硬件

`uhci` 驱动支持所有兼容 UHCI v1.1 的控制器，包括：

- Intel 82371AB/EB (PIIX4)
- Intel 82371SB (PIIX3)
- VIA 83C572

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`hw.usb.uhci.debug`** 调试输出级别，0 表示禁用调试，更大的值增加调试消息的详细程度。默认为 0。

## 参见

[ehci(4)](ehci.4.md), [ohci(4)](ohci.4.md), [xhci(4)](xhci.4.md)

## 历史

`uhci` 设备驱动首次出现于 FreeBSD 3.0。

## 作者

`uhci` 驱动由 Lennart Augustsson <augustss@carlstedt.se> 为 NetBSD 项目编写。
