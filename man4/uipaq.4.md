# uipaq(4)

`uipaq` — iPAQ 设备的 USB 支持

## 名称

`uipaq`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device usb
> device ucom
> device uipaq

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
uipaq_load="YES"
```

## 描述

`uipaq` 驱动为 iPAQ 设备提供的 USB 串口仿真提供支持。

该设备通过 [ucom(4)](ucom.4.md) 驱动访问，使其行为类似 [tty(4)](tty.4.md)。

## 硬件

`uipaq` 驱动支持以下 iPAQ 设备：

- ASUS P535 PDA
- Casio BE300 PDA
- Compaq IPaq PocketPC
- HP Jornada 568
- HP iPAQ 22xx/Jornada 548
- HTC PPC6700 调制解调器
- HTC 智能手机
- HTC Winmobile
- Sharp W-ZERO3 ES 智能手机
- 大多数基于 Windows CE 的手机

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

FreeBSD 的支持从 NetBSD 引入，用于 FreeBSD 7.0。NetBSD 在 NetBSD 4.0 中加入支持，该支持从 OpenBSD 3.8 引入。
