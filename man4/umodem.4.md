# umodem(4)

`umodem` — USB 通信设备类串口（CDC ACM）驱动

## 名称

`umodem`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device usb
> device ucom
> device umodem

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
umodem_load="YES"
```

## 描述

`umodem` 驱动为实现通信设备类抽象控制模型（CDC ACM）的 USB 调制解调器和串口设备提供支持。它还提供设备端的 CDC ACM 支持。所支持的调制解调器基本上是标准串口线调制解调器，只是通过 USB 访问。它们支持常规 AT 命令集。命令可与数据流复用，也可通过独立管道处理。在后一种情况下，AT 命令必须在独立于数据设备的设备上发出。

该设备通过 [ucom(4)](ucom.4.md) 驱动访问，使其行为类似 [tty(4)](tty.4.md)。

## 硬件

`umodem` 驱动支持的设备包括：

- 3Com 5605
- Curitel PC5740 无线调制解调器
- Kyocera AH-K3001V 移动电话（WILLCOM）
- Kyocera WX320K 移动电话（WILLCOM）
- Metricom Ricochet GS USB 无线调制解调器
- Sierra MC5720 无线调制解调器
- Yamaha 宽带无线路由器 RTW65b
- ELSA MicroLink 56k USB 调制解调器
- Sony Ericsson W810i 手机
- Sonim XP5300 Force

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

`umodem` 驱动出现于 NetBSD 1.5。本手册页由 Tom Rhodes <trhodes@FreeBSD.org> 于 2002 年 4 月从 NetBSD 引入。

## 缺陷

目前仅支持命令与数据复用的调制解调器。
