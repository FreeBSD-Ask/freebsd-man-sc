# kue(4)

`kue` — Kawasaki LSI KL5KUSB101B USB 以太网驱动

## 名称

`kue`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device uhci
> device ohci
> device usb
> device miibus
> device uether
> device kue

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_kue_load="YES"
```

## 描述

`kue` 驱动为基于 Kawasaki LSI KL5KLUSB101B 芯片组的 USB 以太网适配器提供支持。

KL5KLUSB101B 支持 128 条目多播过滤器、用于站地址的单个完美过滤条目和混杂模式。数据包通过单独的 USB 批量传输端点接收和发送。

Kawasaki 芯片组仅支持 10Mbps 半双工模式，因此没有可选的 Fn ifmedia 模式。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`kue` 驱动支持基于 Kawasaki LSI KL5KLUSB101B 的 USB 以太网适配器，包括：

- 3Com 3c19250
- 3Com 3c460 HomeConnect Ethernet USB Adapter
- ADS Technologies USB-10BT
- AOX USB101
- ATen UC10T
- Abocom URE 450
- Corega USB-T
- D-Link DSB-650C
- Entrega NET-USB-E45, NET-HUB-3U1E
- I/O Data USB ETT
- Kawasaki DU-H3E
- LinkSys USB10T
- Netgear EA101
- Peracom USB Ethernet Adapter
- Psion Gold Port USB Ethernet adapter
- SMC 2102USB, 2104USB

## 诊断

- kue%d: watchdog timeout 数据包已排队等待传输并发出传输命令，但设备未能在超时到期前确认传输。

- kue%d: no memory for rx list 驱动无法为接收环分配 mbuf。

## 参见

arp(4), netintro(4), ng_ether(4), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`kue` 设备驱动最早出现于 FreeBSD 4.0。

## 作者

`kue` 驱动由 Bill Paul <wpaul@ee.columbia.edu> 编写。

## 缺陷

`kue` 驱动不会累计以太网冲突统计信息，因为 Kawasaki 固件似乎不维护任何内部统计信息。
