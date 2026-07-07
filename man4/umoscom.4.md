# umoscom(4)

`umoscom` — 基于 MOSCHIP 芯片的串口适配器的 USB 支持

## 名称

`umoscom`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device usb
> device ucom
> device umoscom

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
umoscom_load="YES"
```

## 描述

`umoscom` 驱动为基于 MOSCHIP 芯片的各种串口适配器提供支持。

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

`umoscom` 驱动出现于 OpenBSD，并被移植到 FreeBSD。
