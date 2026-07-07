# uvscom(4)

`uvscom` — SUNTAC Slipper U VS-10U 串口适配器的 USB 支持驱动

## 名称

`uvscom`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device usb
> device ucom
> device uvscom

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
uvscom_load="YES"
```

## 硬件

`uvscom` 驱动支持以下适配器：

- DDI Pocket Air H" C@rd
- DDI Pocket Air H" C@rd 64
- NTT P-in
- NTT P-in m@ster

## 描述

`uvscom` 驱动为 SUNTAC Slipper U VS-10U 芯片提供支持。Slipper U 是一种用于数据通信卡适配器的 PC 卡转 USB 转换器。

该设备通过 [ucom(4)](ucom.4.md) 驱动访问，使其行为类似 [tty(4)](tty.4.md)。

## 文件

**`/dev/ttyU*`** 用于呼入端口
**`/dev/ttyU*.init`**
**`/dev/ttyU*.lock`** 对应的呼入初始状态和锁定状态设备
**`/dev/cuaU*`** 用于呼出端口
**`/dev/cuaU*.init`**
**`/dev/cuaU*.lock`** 对应的呼出初始状态和锁定状态设备

## 参见

[tty(4)](tty.4.md), [ucom(4)](ucom.4.md), [usb(4)](usb.4.md)

## 历史

`uvscom` 驱动首次出现于 FreeBSD，后来出现于 NetBSD 1.6。本手册页由 Tom Rhodes <trhodes@FreeBSD.org> 于 2002 年 4 月从 NetBSD 引入。
