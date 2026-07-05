# ehci.4

`ehci` — USB 增强型主控制器驱动

## 名称

`ehci`

## 概要

`device ehci`

## 描述

`ehci` 驱动为 USB 增强型主控制器接口（USB Enhanced Host Controller Interface）提供支持，该接口由 USB 2.0 控制器使用。

EHCI 控制器的特殊之处在于它们只能处理 USB 2.0 协议。这意味着它们通常需要一个或多个伴随控制器（即 [ohci(4)](ohci.4.md) 或 [uhci(4)](uhci.4.md)）来处理 USB 1.x 设备。因此，每个 USB 连接器在电气上连接到两个 USB 控制器。此过程完全自动处理，但可以注意到：插入同一连接器的 USB 1.x 和 USB 2.0 设备会显示为连接到不同的 USB 总线。

## 加载器可调参数

当内核以 `options USB_DEBUG` 编译时，将提供一些影响 `ehci` 行为的可调参数。这些可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`hw.usb.ehci.lostintrbug`** 此可调参数启用丢失中断 quirks。默认值为 0（关闭）。

**`hw.usb.ehci.iaadbug`** 此可调参数启用 EHCI doorbell quirks。默认值为 0（关闭）。

**`hw.usb.ehci.no_hs`** 此可调参数禁用 USB 设备以高速（HIGH-speed）方式挂载，并强制所有已挂载设备以全速（FULL）或低速（LOW）挂载到伴随控制器。默认值为 0（关闭）。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`hw.usb.ehci.debug`** 调试输出级别，0 表示禁用调试，更大的值会增加调试消息的详细程度。默认值为 0。

## 参见

[ohci(4)](ohci.4.md), [uhci(4)](uhci.4.md), [usb(4)](usb.4.md), [xhci(4)](xhci.4.md)

## 历史

`ehci` 设备驱动首次出现于 FreeBSD 5.1。
