# bwn.4

`bwn` — Broadcom BCM43xx SoftMAC IEEE 802.11 无线网络驱动

## 名称

`bwn`

## 概要

要将此驱动编译进内核，请将以下行加入内核配置文件：

> device bwn
> device bhnd
> device bhndb
> device bhndb_pci
> device bcma
> device siba
> device gpio
> device wlan
> device wlan_amrr
> device firmware

要在引导时以模块形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行：

```sh
if_bwn_load="YES"
```

## 描述

`bwn` 驱动为基于 Broadcom BCM43xx 的 PCI/CardBus 网络适配器提供支持。

它支持 `station` 和 `monitor` 模式操作。任何时刻只能配置一个虚拟接口。有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

此驱动需要先加载固件才能工作。在 [ifconfig(8)](../man8/ifconfig.8.md) 工作之前，需要安装 `ports/net/bwn-firmware-kmod` port。在大多数情况下，应使用该 port 中的 `bwn_v4_ucode` 内核模块。但如果使用的是 LP（低功耗）PHY，则应使用 `bwn_v4_lp_ucode` 模块。

## 硬件

`bwn` 驱动支持基于 Broadcom BCM43xx 的无线设备，包括：

| *卡* | *芯片* | *总线* | *标准* |
| ---- | ------ | ------ | ------ |
| Apple Airport Extreme | BCM4318 | PCI | b/g |
| ASUS WL-138g | BCM4318 | PCI | b/g |
| Buffalo WLI-CB-G54S | BCM4318 | CardBus | b/g |
| Dell Wireless 1390 | BCM4311 | Mini PCI | b/g |
| Dell Wireless 1470 | BCM4318 | Mini PCI | b/g |
| Dell Truemobile 1400 | BCM4309 | Mini PCI | b/g |
| HP Compaq 6715b | BCM4312 | PCI | b/g |
| HP nx6125 | BCM4319 | PCI | b/g |
| Linksys WPC54G Ver 3 | BCM4318 | CardBus | b/g |
| Linksys WPC54GS Ver 2 | BCM4318 | CardBus | b/g |
| US Robotics 5411 | BCM4318 | CardBus | b/g |

较旧 Broadcom 芯片组（BCM4301、BCM4303 和 BCM4306 rev 2）的用户必须使用 [bwi(4)](bwi.4.md)，因为 v4 版本的固件不支持这些芯片。较新的固件太大，无法容纳这些旧芯片。

## 实例

加入现有 BSS 网络（即连接到接入点）：

```sh
ifconfig wlan create wlandev bwn0 inet 192.168.0.20 e
    netmask 0xffffff00
```

加入网络名为“`my_net`”的特定 BSS 网络：

```sh
ifconfig wlan create wlandev bwn0 ssid my_net up
```

加入使用 64 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev bwn0 ssid my_net e
        wepmode on wepkey 0x1234567890 weptxkey 1 up
```

## 加载器可调参数

可调参数可在 [loader(8)](../man8/loader.8.md) 提示符下引导内核前设置，或存储在 loader.conf(5) 中。

**`hw.bwn.usedma`** 此可调参数在硬件上启用 DMA 操作。如果值为 0，将使用 PIO 模式。默认值为 1。

## 参见

arp(4), [bcma(4)](bcma.4.md), [bhnd(4)](bhnd.4.md), [bhndb(4)](bhndb.4.md), [bwi(4)](bwi.4.md), [cardbus(4)](cardbus.4.md), [intro(4)](intro.4.md), [pci(4)](pci.4.md), [siba(4)](siba.4.md), [wlan(4)](wlan.4.md), [wlan_amrr(4)](wlan_amrr.4.md), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 历史

`bwn` 驱动首次出现于 FreeBSD 8.1。该驱动在 FreeBSD 12.0 中更新以支持通用的 Broadcom [bhnd(4)](bhnd.4.md) 总线接口。

## 作者

`bwn` 驱动由 Weongyo Jeong <weongyo@FreeBSD.org> 编写。[bhnd(4)](bhnd.4.md) 的支持由 Landon Fuller <landonf@FreeBSD.org> 添加。

## 注意事项

某些 LP PHY 设备存在 DMA 操作问题，在这种情况下尝试使用 PIO 模式。
