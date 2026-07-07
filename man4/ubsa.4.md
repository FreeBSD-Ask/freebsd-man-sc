# ubsa(4)

`ubsa` — Belkin 串行适配器的 USB 支持

## 名称

`ubsa`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device usb
> device ucom
> device ubsa

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
ubsa_load="YES"
```

## 描述

`ubsa` 驱动提供对 Belkin 及其他厂商的多种串行适配器所用 USB 转 RS232 桥接芯片的支持。

该设备通过 [ucom(4)](ucom.4.md) 驱动访问，使其行为类似 [tty(4)](tty.4.md)。

## 硬件

`ubsa` 驱动支持以下适配器：

- AnyData ADU-500A EV-DO 调制解调器
- AnyData ADU-E100A（不支持 EV-DO 模式）
- Belkin F5U103
- Belkin F5U120
- e-Tek Labs Kwik232
- GoHubs GoCOM232
- Peracom 单端口串行适配器

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

`ubsa` 驱动出现于 FreeBSD 5.0。[uplcom(4)](uplcom.4.md) man 页面由 Tom Rhodes <trhodes@FreeBSD.org> 于 2002 年 4 月从 NetBSD 引入，并由 Alexander Kabaev <kan@FreeBSD.org> 于 2002 年 10 月针对 `ubsa` 驱动进行了修改。

## 作者

`ubsa` 驱动由 Alexander Kabaev <kan@FreeBSD.org> 编写。
