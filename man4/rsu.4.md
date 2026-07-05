# rsu.4

`rsu` — Realtek RTL8188SU/RTL8192SU USB IEEE 802.11b/g/n 无线网络驱动

## 名称

`rsu`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device ehci
> device uhci
> device ohci
> device usb
> device rsu
> device rsufw
> device wlan

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_rsu_load="YES"
rsu-rtl8712fw_load="YES"
```

## 描述

`rsu` 驱动支持基于 Realtek RTL8188SU、RTL8191SU 和 RTL8192SU 芯片组的 USB 2.0 无线网络设备。

RTL8188SU 是一款高度集成的 802.11n 适配器，将 MAC、支持 1T1R 的基带和 RF 集成在单芯片中。它仅在 2GHz 频段工作。

RTL8191SU 是一款高度集成的多入单出（MISO）802.11n 适配器，将 MAC、支持 1T2R 的基带和 RF 集成在单芯片中。它仅在 2GHz 频段工作。

RTL8192SU 是一款高度集成的多入多出（MIMO）802.11n 适配器，将 MAC、支持 2T2R 的基带和 RF 集成在单芯片中。它仅在 2GHz 频段工作。

`rsu` 驱动可在以下模式下运行：

**BSS** 模式 也称为*基础结构*模式，用于与接入点关联，所有流量都通过接入点传递。此模式为默认模式。

**monitor** 模式 在此模式下，驱动无需与接入点关联即可接收数据包。这会禁用内部接收过滤器，使网卡能够捕获通常无法访问的网络数据包，或扫描接入点。

`rsu` 驱动可配置为使用有线等效保密（WEP）或 Wi-Fi 保护访问（WPA-PSK 和 WPA2-PSK）。WPA 是无线网络事实上的加密标准。由于 WEP 存在严重弱点，强烈建议不要将其作为保障无线通信安全的唯一机制。

`rsu` 驱动可在运行时通过 [ifconfig(8)](../man8/ifconfig.8.md) 进行配置。

## 硬件

`rsu` 驱动为 Realtek RTL8188SU/RTL8192SU USB IEEE 802.11b/g/n 无线网络适配器提供支持，包括：

- ASUS USB-N10
- ASUS WL-167G V3
- Belkin F7D1101 v1
- D-Link DWA-131 A1
- EDUP EP-MS150N(W)
- Edimax EW-7622UMN
- Hercules HWGUn-54
- Hercules HWNUm-300
- Planex GW-USNano
- Sitecom WL-349 v1
- Sitecom WL-353
- Sitecom WLA-1100 v1001
- Sweex LW154
- TRENDnet TEW-646UBH
- TRENDnet TEW-648UB
- TRENDnet TEW-649UB

## 文件

**`/usr/share/doc/legal/realtek.LICENSE`** `rsu` 固件许可证

驱动需要以下固件文件的至少 1.2 版本，在接口附加时加载：

**`/boot/kernel/rsu-rtl8712fw.ko`**

## 实例

加入现有的 BSS 网络（即连接到接入点）：

```sh
ifconfig wlan create wlandev rsu0 inet 192.0.2.20/24
```

加入网络名称为 `my_net` 的特定 BSS 网络：

```sh
ifconfig wlan create wlandev rsu0 ssid my_net up
```

加入采用 64 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev rsu0 ssid my_net e
    wepmode on wepkey 0x1234567890 weptxkey 1 up
```

## 诊断

- %s: failed load firmware of file rsu-rtl8712fw 由于某种原因，驱动无法从文件系统读取微代码文件。该文件可能缺失或已损坏。
- device timeout 派遣到硬件进行发送的帧未及时完成。驱动将重置硬件。这不应发生。

## 参见

[intro(1)](../man1/intro.1.md), [netintro(4)](netintro.4.md), [rsufw(4)](rsufw.4.md), [usb(4)](usb.4.md), [wlan(4)](wlan.4.md), [networking(7)](../man7/networking.7.md), arp(8), hostapd(8), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 历史

`rsu` 驱动最早出现在 OpenBSD 4.9 和 FreeBSD 10.0 中。

## 作者

`rsu` 驱动由 Damien Bergamini <damien@openbsd.org> 编写，由 Rui Paulo <rpaulo@freebsd.org> 移植。802.11n 支持由 Adrian Chadd <adrian@freebsd.org> 添加。

## 注意事项

`rsu` 驱动目前不支持 802.11n 发送聚合，无论是 A-MSDU 还是 A-MPDU。

`rsu` 驱动在非 monitor 模式下不捕获管理帧；如果不加此限制，某些固件功能（例如 'join bss'）将无法正常工作。
