# bwi.4

`bwi` — Broadcom BCM43xx IEEE 802.11b/g 无线网络驱动

## 名称

`bwi`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> device bwi
> device wlan
> device wlan_amrr
> device firmware

或者，要在引导时以模块形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行：

```sh
if_bwi_load="YES"
```

## 描述

`bwi` 驱动为基于 Broadcom BCM43xx 的 PCI/CardBus 网络适配器提供支持。

它支持 `station` 和 `monitor` 模式操作。任何时候只能配置一个虚拟接口。有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

此驱动要求先加载固件才能工作。在 [ifconfig(8)](../man8/ifconfig.8.md) 工作之前需要安装 `ports/net/bwi-firmware-kmod` port。

## 硬件

`bwi` 驱动支持基于 Broadcom BCM43xx 的无线设备，包括：

| 卡片 | 芯片 | 总线 | 标准 |
| --- | --- | --- | --- |
| Apple Airport Extreme | BCM4306 | PCI | b/g |
| Apple Airport Extreme | BCM4318 | PCI | b/g |
| ASUS WL-100g | BCM4306 | CardBus | b/g |
| ASUS WL-138g | BCM4318 | PCI | b/g |
| Buffalo WLI-CB-G54S | BCM4318 | CardBus | b/g |
| Buffalo WLI-PCI-G54S | BCM4306 | PCI | b/g |
| Compaq R4035 onboard | BCM4306 | PCI | b/g |
| Dell Wireless 1390 | BCM4311 | Mini PCI | b/g |
| Dell Wireless 1470 | BCM4318 | Mini PCI | b/g |
| Dell Truemobile 1300 r2 | BCM4306 | Mini PCI | b/g |
| Dell Truemobile 1400 | BCM4309 | Mini PCI | b/g |
| HP nx6125 | BCM4319 | PCI | b/g |
| Linksys WPC54G Ver 3 | BCM4318 | CardBus | b/g |
| Linksys WPC54GS Ver 2 | BCM4318 | CardBus | b/g |
| TRENDnet TEW-401PCplus | BCM4306 | CardBus | b/g |
| US Robotics 5411 | BCM4318 | CardBus | b/g |

`bwi` 驱动使用较旧的 v3 版本 Broadcom 固件。虽然此较旧固件支持大多数 BCM43xx 部件，但 [bwn(4)](bwn.4.md) 驱动在其支持的较新芯片上工作得更好。如果使用较旧的 Broadcom 芯片组（BCM4301、BCM4303 和 BCM4306 rev 2），则必须使用 `bwi` 驱动。[bwn(4)](bwn.4.md) 使用的 v4 版本固件不支持这些芯片。

## 实例

加入现有 BSS 网络（即连接到接入点）：

```sh
ifconfig wlan create wlandev bwi0 inet 192.168.0.20 \
    netmask 0xffffff00
```

加入网络名称为“`my_net`”的指定 BSS 网络：

```sh
ifconfig wlan create wlandev bwi0 ssid my_net up
```

加入使用 64 位 WEP 加密的指定 BSS 网络：

```sh
ifconfig wlan create wlandev bwi0 ssid my_net \
        wepmode on wepkey 0x1234567890 weptxkey 1 up
```

## 参见

arp(4), [cardbus(4)](cardbus.4.md), [intro(4)](intro.4.md), [pci(4)](pci.4.md), [wlan(4)](wlan.4.md), [wlan_amrr(4)](wlan_amrr.4.md), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 历史

`bwi` 驱动首次出现于 FreeBSD 8.0。

## 作者

`bwi` 驱动由 Sepherosa Ziehau 为 Dx 编写，随后移植到 FreeBSD。

## 缺陷

某些基于 BCM4306 和 BCM4309 芯片的卡在信道 1、2 和 3 上无法正常工作。
