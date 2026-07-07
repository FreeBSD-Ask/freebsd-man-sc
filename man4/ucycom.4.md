# ucycom(4)

`ucycom` — Cypress CY7C63743 和 CY7C64013 USB 转 RS232 桥接器设备驱动

## 名称

`ucycom`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device usb
> device hid
> device ucom
> device ucycom

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
ucycom_load="YES"
```

## 描述

`ucycom` 驱动提供对 Cypress CY7C63743 和 CY7C64013 桥接芯片的支持。这些芯片旨在为现有 RS232 设备提供低成本的 USB 过渡路径，能力相当有限。

`ucycom` 驱动的行为类似 [tty(4)](tty.4.md)。

## 硬件

`ucycom` 驱动目前支持以下采用 Cypress USB 转 RS232 桥接芯片的设备：

- DeLorme Earthmate USB GPS 接收器

## 文件

**`/dev/ttyU*`** 用于呼入端口
**`/dev/ttyU*.init`**
**`/dev/ttyU*.lock`** 相应的呼入初始状态和锁定状态设备
**`/dev/cuaU*`** 用于呼出端口
**`/dev/cuaU*.init`**
**`/dev/cuaU*.lock`** 相应的呼入初始状态和锁定状态设备

## 参见

[tty(4)](tty.4.md), [ucom(4)](ucom.4.md), [usb(4)](usb.4.md)

## 历史

`ucycom` 驱动首次出现于 FreeBSD 5.3。

## 作者

`ucycom` 驱动和本 man 页面由 Dag-Erling Smørgrav <des@FreeBSD.org> 编写。
