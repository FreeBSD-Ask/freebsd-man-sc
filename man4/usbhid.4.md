# usbhid(4)

`usbhid` — USB HID 传输驱动

## 名称

`usbhid`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device usbhid

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
usbhid_load="YES"
```

## 描述

`usbhid` 驱动为 USB 人机接口设备（HID）提供接口。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`hw.usb.usbhid.enable`** 启用 `usbhid` 并使其优先级高于其他 USB HID 驱动，例如 [ukbd(4)](ukbd.4.md)、[ums(4)](ums.4.md) 和 [uhid(4)](uhid.4.md)。默认为 1。

**`hw.usb.usbhid.debug`** 调试输出级别，0 表示禁用调试，更大的值增加调试消息的详细程度。默认为 0。调试消息会打印在系统控制台上，可使用 [dmesg(8)](../man8/dmesg.8.md) 查看。

## 参见

[ehci(4)](ehci.4.md), [hkbd(4)](hkbd.4.md), [hms(4)](hms.4.md), [ohci(4)](ohci.4.md), [uhci(4)](uhci.4.md), [usb(4)](usb.4.md), [xhci(4)](xhci.4.md), usbconfig(8)

## 历史

`usbhid` 驱动首次出现于 FreeBSD 13.0。在 FreeBSD 15.0 中默认启用。

## 作者

`usbhid` 驱动由 Vladimir Kondratyev <wulf@FreeBSD.org> 编写。
