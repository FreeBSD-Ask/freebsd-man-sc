# urtw(4)

`urtw` — Realtek RTL8187B/L USB IEEE 802.11b/g 无线网络驱动

## 名称

`urtw`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device ehci
> device uhci
> device ohci
> device usb
> device urtw
> device wlan

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
if_urtw_load="YES"
```

## 描述

`urtw` 驱动支持基于 Realtek RTL8187B/L 的 USB 802.11b/g 无线适配器。

`urtw` 支持 `station` 和 `monitor` 模式操作。任一时刻只能配置一个虚拟接口。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`urtw` 驱动支持基于 Realtek RTL8187B/L 的无线网络设备，包括：

| *Card* | *Radio* | *Bus* |
| ------ | ------- | ----- |
| Belkin F5D7050E | RTL8225 | USB |
| Linksys WUSB54GCv2 | RTL8225 | USB |
| Netgear WG111v2 | RTL8225 | USB |
| Netgear WG111v3 | RTL8225 | USB |
| Safehome WLG-1500SMA5 | RTL8225 | USB |
| Shuttle XPC Accessory PN20 | RTL8225 | USB |
| Sitecom WL168v1 | RTL8225 | USB |
| Sitecom WL168v4 | RTL8225 | USB |
| SureCom EP-9001-g(2A) | RTL8225 | USB |
| TRENDnet TEW-424UB V3.xR | RTL8225 | USB |

## 实例

加入现有的 BSS 网络（即连接到接入点）：

```sh
ifconfig wlan create wlandev urtw0 inet 192.0.2.20/24
```

加入网络名为 `my_net` 的特定 BSS 网络：

```sh
ifconfig wlan create wlandev urtw0 ssid my_net up
```

加入使用 64 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev urtw0 ssid my_net e
    wepmode on wepkey 0x1234567890 weptxkey 1 up
```

## 参见

[intro(4)](intro.4.md), [netintro(4)](netintro.4.md), [usb(4)](usb.4.md), [wlan(4)](wlan.4.md), [wlan_ccmp(4)](wlan_ccmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md), [wlan_wep(4)](wlan_wep.4.md), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

> "Realtek".

## 历史

`urtw` 设备驱动首次出现于 FreeBSD 8.0。

## 作者

`urtw` 驱动由 Weongyo Jeong <weongyo@FreeBSD.org> 编写。
