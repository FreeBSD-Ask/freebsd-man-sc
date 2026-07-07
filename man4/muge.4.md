# muge(4)

`muge` — Microchip LAN78xx USB 千兆以太网驱动

## 名称

`muge`

## 概要

要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_muge_load="YES"
```

## 描述

`muge` 设备驱动提供对基于 Microchip LAN78xx 和 LAN7515 芯片组的 USB 千兆以太网适配器的支持。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`muge` 驱动支持 Microchip USB 千兆以太网接口，包括：

- Microchip LAN7800 USB 3.1 千兆以太网控制器（带 PHY）
- Microchip LAN7850 USB 2.0 千兆以太网控制器（带 PHY）
- Microchip LAN7515 USB 2 集线器和千兆以太网控制器（带 PHY）

## 参见

arp(4), [miibus(4)](miibus.4.md), [usb(4)](usb.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`muge` 设备驱动首次出现于 FreeBSD 12.0。
