# xhci.4

`xhci` — USB eXtensible 主机控制器驱动

## 名称

`xhci`

## 概要

`options USB_DEBUG device xhci`

## 描述

`xhci` 驱动为 USB eXtensible 主机控制器接口提供支持，允许在同一个 USB 端口上使用 USB 1.0、2.0 和 3.0 设备。

使用 USB 3.x 兼容设备时，XHCI 控制器支持 5.0Gbps 及以上的 USB 连接速度。

## 硬件

`xhci` 驱动支持具有 PCI 类 12（串行总线）、子类 3（USB）和编程接口 48（XHCI）的 XHCI 兼容控制器。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`hw.usb.xhci.debug`** 设置调试输出级别，其中 0 表示禁用调试，更大的值增加调试消息的详细程度。默认值为 0。

**`hw.usb.xhci.dcepquirk`** 设置以启用端点取消配置的怪癖。默认值为 0。

**`hw.usb.xhci.ctlquirk`** 设置以将完整 USB 控制请求作为单个作业提交，最多 64kBytes。否则 USB 控制请求将被拆分为多个较小的请求。默认值为 1。

**`hw.usb.xhci.streams`** 设置以启用 USB 流支持。默认值为 0。

**`hw.usb.xhci.route`** 设置用于将 EHCI 端口切换到 XHCI 控制器的位图。默认值为 0。

**`hw.usb.xhci.polling`** 设置以使用定时器轮询中断处理程序。默认值为 0。

**`hw.usb.xhci.dma32`** 设置以仅对 XHCI 控制器使用 32 位 DMA。默认值为 0。

**`hw.usb.xhci.ctlstep`** 设置以启用控制端点状态状态步进。默认值为 0。

## 参见

[ehci(4)](ehci.4.md), [ohci(4)](ohci.4.md), [uhci(4)](uhci.4.md) [usb(4)](usb.4.md)

## 历史

`xhci` 设备驱动首次出现于 FreeBSD 8.2。
