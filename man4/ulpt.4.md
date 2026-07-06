# ulpt.4

`ulpt` — USB 打印机支持

## 名称

`ulpt`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device ulpt

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
ulpt_load="YES"
```

## 描述

`ulpt` 驱动为遵循打印机双向或单向协议的 USB 打印机提供支持。次设备号中的位选择驱动的各项功能。

| *次设备号位* | *功能* |
| --- | --- |
| 64 | 不初始化（重置）端口上的设备。 |

某些打印机无法处理打开时的重置；如遇问题，请尝试 `unlpt` 设备。

## 硬件

`ulpt` 驱动为 USB 打印机和并口打印机转换电缆提供支持，包括以下设备：

- ATen 并口打印机适配器
- Belkin F5U002 并口打印机适配器
- Canon BJ F850, S600
- Canon LBP-1310, 350
- Entrega USB 转并口打印机适配器
- Hewlett-Packard HP Deskjet 3420 (P/N: C8947A #ABJ)
- Oki Data MICROLINE ML660PS
- Seiko Epson PM-900C, 880C, 820C, 730C

## 文件

**`/dev/ulpt?`** 带重置的设备
**`/dev/unlpt?`** 不带重置的设备

## 参见

[lpt(4)](lpt.4.md), [usb(4)](usb.4.md)

## 历史

`ulpt` 驱动出现于 NetBSD 1.4。本手册页由 Tom Rhodes <trhodes@FreeBSD.org> 于 2002 年 4 月从 NetBSD 引入。
