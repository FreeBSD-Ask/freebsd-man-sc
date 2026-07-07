# u2f(4)

`u2f` — FIDO/U2F USB 安全密钥

## 名称

`u2f`

## 概要

`device u2f`

`在 loader.conf(5) 中：u2f_load="YES"`

`在 sysctl.conf(5) 中：hw.hid.u2f.debug`

## 描述

`u2f` 驱动提供对 FIDO/U2F 兼容 USB 安全密钥的支持。它们是人机接口设备（HID），可通过 **`/dev/u2f/N`** 接口访问。

该驱动与通用 [uhid(4)](uhid.4.md) 设备的 read(2)、write(2) 和 ioctl(2) 操作兼容，但仅接受来自 u2f 组用户的可选 HID ioctl(2) 调用。

## 硬件

`u2f` 驱动支持 FIDO/U2F 兼容的 USB 安全密钥。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`hw.hid.u2f.debug`** 调试输出级别，0 为禁用调试，更大的值增加调试消息的详尽程度。默认为 0。

## 文件

**`/dev/u2f/*`**

## 参见

[uhid(4)](uhid.4.md), [usbhid(4)](usbhid.4.md), [usb(4)](usb.4.md)

## 历史

`u2f` 驱动首次出现于 FreeBSD 15.0。

## 作者

`u2f` 驱动由 Vladimir Kondratyev <wulf@FreeBSD.org> 编写。

本 man 页面由 Vladimir Kondratyev <wulf@FreeBSD.org> 基于 OpenBSD fido(4) man 页面编写。
