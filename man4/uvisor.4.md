# uvisor(4)

`uvisor` — 基于 PalmOS 的 PDA 的 USB 支持

## 名称

`uvisor`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device usb
> device ucom
> device uvisor

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
uvisor_load="YES"
```

## 描述

`uvisor` 驱动为基于 USB 的 PalmOS PDA 提供支持，例如 Handspring Visor、Palm Mxxx 系列和 Sony Clie。

该设备通过 [ucom(4)](ucom.4.md) 驱动访问，使其行为类似 [tty(4)](tty.4.md)。该设备具有多个用于不同目的的端口，每个端口都有自己的 [ucom(4)](ucom.4.md) 设备。附加消息描述了每个端口的用途。

可使用常规的 Pilot 工具在 HotSync 端口上访问附加的设备。

## 硬件

`uvisor` 驱动支持以下设备：

- Aceeca Mez1000 RDA
- Handspring Treo
- Handspring Treo 600
- Handspring Visor
- Palm I705
- Palm M125
- Palm M130
- Palm M500
- Palm M505
- Palm M515
- Palm Tungsten T
- Palm Tungsten Z
- Palm Zire
- Palm Zire 31
- Sony Clie 4.0
- Sony Clie 4.1
- Sony Clie 5.0
- Sony Clie PEG-S500C
- Sony Clie NX60
- Sony Clie S360
- Sony Clie TJ37

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

`uvisor` 驱动于 2002 年 8 月从 NetBSD 1.5 引入。本手册页当时由 Tom Rhodes <trhodes@FreeBSD.org> 从 NetBSD 引入。

## 缺陷

提供多个 [ucom(4)](ucom.4.md) 实例的代码尚未从 NetBSD 移植。此驱动在当前状态下是否能正常工作尚不明确。
