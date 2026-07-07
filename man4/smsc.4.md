# smsc(4)

`smsc` — USB Microchip LAN9xxx 快速以太网驱动

## 名称

`smsc`

## 概要

`要在引导时以模块形式加载此驱动，请将以下行添加到 loader.conf(5) 中：`

```sh
if_smsc_load="YES"
```

`或者，要将此驱动编译进内核，请将以下行添加到你的内核配置文件中：`

> device uhci
> device ohci
> device usb
> device miibus
> device uether
> device smsc

## 描述

`smsc` 设备驱动为基于 Microchip（前身为 SMSC）LAN9xxx 芯片组的 USB 快速以太网适配器提供支持。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

以下设备受 `smsc` 驱动支持：

- 基于 LAN9500、LAN9500A、LAN9505 和 LAN9505A 的以太网适配器
- 基于 LAN89530、LAN9530 和 LAN9730 的以太网适配器
- 带集成 USB 集线器的 LAN951x 以太网适配器

## 参见

arp(4), [intro(4)](intro.4.md), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [usb(4)](usb.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`smsc` 设备驱动最早出现于 FreeBSD 10.0。

## 作者

`smsc` 驱动由 Ben Gray <bgray@FreeBSD.org> 编写。
