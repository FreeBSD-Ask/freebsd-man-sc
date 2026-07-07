# cue(4)

`cue` — CATC USB-EL1210A USB 以太网驱动

## 名称

`cue`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device uhci
> device ohci
> device usb
> device miibus
> device uether
> device cue

`或者，若要在引导时以模块方式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_cue_load="YES"
```

## 描述

`cue` 驱动为基于 Computer Access Technology Corporation USB-EL1210A 芯片组的 USB 以太网适配器提供支持。

USB-EL1210A 支持 512 位多播哈希过滤器、用于站点地址的单个完美过滤项以及混杂模式。数据包通过独立的 USB 批量传输端点进行接收和发送。

CATC 芯片组仅支持 10Mbps 半双工模式，因此没有可选择的 Fn ifmedia 模式。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`cue` 驱动支持基于 CATC USB-EL1210A 的 USB 以太网适配器，包括：

- Belkin F5U011/F5U111
- CATC Netmate
- CATC Netmate II
- SmartBridges SmartLink

## 诊断

- cue%d: watchdog timeout 一个数据包已排队等待传输并且已发出传输命令，但设备在超时之前未能确认传输。
- cue%d: no memory for rx list 驱动未能为接收环分配一个 mbuf。

## 参见

arp(4), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`cue` 设备驱动首次出现于 FreeBSD 4.0。

## 作者

`cue` 驱动由 Bill Paul <wpaul@ee.columbia.edu> 编写。
