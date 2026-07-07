# uark(4)

`uark` — 基于 Arkmicro Technologies ARK3116 的 USB 串行适配器

## 名称

`uark`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device usb
> device ucom
> device uark

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
uark_load="YES"
```

## 描述

`uark` 驱动支持基于 Arkmicro Technologies ARK3116 的串行适配器。

## 硬件

`uark` 驱动支持以下适配器：

- HL USB-RS232
- HugePine USB-UART
- KQ-U8A Data Cable
- Skymaster USB to RS232

## 文件

**`/dev/ttyU*`** 用于呼入端口
**`/dev/ttyU*.init`**
**`/dev/ttyU*.lock`** 相应的呼入初始状态和锁定状态设备
**`/dev/cuaU*`** 用于呼出端口
**`/dev/cuaU*.init`**
**`/dev/cuaU*.lock`** 相应的呼出初始状态和锁定状态设备

## 参见

[tty(4)](tty.4.md), [ucom(4)](ucom.4.md), [usb(4)](usb.4.md)

## 历史

`uark` 设备驱动首次出现于 OpenBSD 4.0。首次包含它的 FreeBSD 版本是 FreeBSD 7.0。

## 作者

`uark` 驱动由 Jonathan Gray <jsg@openbsd.org> 编写。

## 注意事项

目前不支持设置硬件流控制。尚不知道如何让硬件发送 break。

Arkmicro Technologies 不回复有关其产品文档的请求。
