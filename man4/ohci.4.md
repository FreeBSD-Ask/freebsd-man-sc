# ohci.4

`ohci` — OHCI USB 主控制器驱动

## 名称

`ohci`

## 概要

`device ohci`

## 描述

`ohci` 驱动为基于 PCI 的 OHCI 类型 USB 控制器提供支持。

## 硬件

`ohci` 驱动支持所有符合 OHCI v1.0 的控制器，包括：

- AcerLabs M5237 (Aladdin-V)
- AMD-756
- OPTi 82C861 (FireLink)
- NEC uPD 9210
- CMD Tech 670 (USB0670)
- CMD Tech 673 (USB0673)
- NVIDIA nForce3

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`hw.usb.ohci.debug`** 调试输出级别，0 表示禁用调试，更大的值会增加调试消息的详细程度。默认值为 0。

## 参见

[ehci(4)](ehci.4.md), [uhci(4)](uhci.4.md), [xhci(4)](xhci.4.md)

## 历史

`ohci` 设备驱动最早出现于 FreeBSD 3.0。

## 作者

`ohci` 驱动由 Lennart Augustsson <augustss@carlstedt.se> 为 NetBSD 项目编写。
