# rtwn_usb.4

`rtwn_usb` — Realtek 无线 rtwn 网络驱动程序的 USB 支持

## 名称

`rtwn_usb`

## 概要

若要将此驱动程序编译进内核，请在你的内核配置文件中加入以下行：

> device xhci
> device ehci
> device uhci
> device ohci
> device usb
> device rtwn
> device rtwn_usb
> device wlan

## 描述

`rtwn_usb` 驱动为 [rtwn(4)](rtwn.4.md) 驱动提供对 USB 无线网络设备的支持。

## 硬件

`rtwn_usb` 驱动支持基于特定 Realtek RTL 8188/8192/8812 和 8821 芯片组的 USB 无线网络适配器，包括：

| *Card* | *Chip* | *Bus* |
| --- | --- | --- |
| Alfa AWUS036NHR v2 | RTL8188RU | USB 2.0 |
| ASUS USB-AC56 | RTL8812AU | USB 3.0 |
| ASUS USB-N10 NANO | RTL8188CUS | USB 2.0 |
| ASUS USB-N10 NANO rev B1 | RTL8188EUS | USB 2.0 |
| Asus USB-N13, rev. B1 | RTL8192CU | USB 2.0 |
| Belkin F7D1102 Surf Wireless Micro | RTL8188CUS | USB 2.0 |
| Buffalo WI-U2-433DHP | RTL8821AU | USB 2.0 |
| Buffalo WI-U2-433DM | RTL8821AU | USB 2.0 |
| Buffalo WI-U3-866D | RTL8812AU | USB 3.0 |
| D-Link DWA-121 rev C1A (N150 Nano) | RTL8188EU | USB 2.0 |
| D-Link DWA-123 rev D1 | RTL8188EU | USB 2.0 |
| D-Link DWA-125 rev D1 | RTL8188EU | USB 2.0 |
| D-Link DWA-131 | RTL8192CU | USB 2.0 |
| D-Link DWA-131 rev E1 | RTL8192EU | USB 2.0 |
| D-Link DWA-171 rev A1 | RTL8821AU | USB 2.0 |
| D-Link DWA-172 rev A1 | RTL8821AU | USB 2.0 |
| D-Link DWA-180 rev A1 | RTL8812AU | USB 2.0 |
| D-Link DWA-182 rev C1 | RTL8812AU | USB 3.0 |
| Edimax EW-7811Un | RTL8188CUS | USB 2.0 |
| Edimax EW-7811UTC | RTL8821AU | USB 2.0 |
| Edimax EW-7822UAC | RTL8812AU | USB 3.0 |
| EDUP EP-AC1620 | RTL8821AU | USB 2.0 |
| Elecom WDC-150SU2M | RTL8188EU | USB 2.0 |
| EnGenius EUB1200AC | RTL8812AU | USB 3.0 |
| Foxconn WFUR6 | RTL8812AU | USB 2.0 |
| Hawking HD65U | RTL8821AU | USB 2.0 |
| Hercules Wireless N USB Pico | RTL8188CUS | USB 2.0 |
| I-O Data WN-AC867U | RTL8812AU | USB 3.0 |
| Linksys WUSB6300 | RTL8812AU | USB 3.0 |
| NEC AtermWL900U PA-WL900U | RTL8812AU | USB 3.0 |
| Netgear A6100 | RTL8821AU | USB 2.0 |
| Netgear WNA1000M | RTL8188CUS | USB 2.0 |
| Mercusys MW150US | RTL8188EU | USB 2.0 |
| Planex GW-900D | RTL8812AU | USB 3.0 |
| Realtek RTL8192CU | RTL8192CU | USB 2.0 |
| Realtek RTL8188CUS | RTL8188CUS | USB 2.0 |
| Sitecom WLA-7100 | RTL8812AU | USB 3.0 |
| TP-Link Archer T2U Nano | RTL8821AU | USB 2.0 |
| TP-Link Archer T2U Plus | RTL8821AU | USB 2.0 |
| TP-Link Archer T2U v3 | RTL8821AU | USB 2.0 |
| TP-Link Archer T4U | RTL8812AU | USB 3.0 |
| TP-Link Archer T4U v2 | RTL8812AU | USB 3.0 |
| TP-Link Archer T4UH v1 | RTL8812AU | USB 3.0 |
| TP-Link Archer T4UH v2 | RTL8812AU | USB 3.0 |
| TP-Link TL-WN722N v2 | RTL8188EU | USB 2.0 |
| TP-LINK TL-WN723N v3 | RTL8188EU | USB 2.0 |
| TP-LINK TL-WN725N v2 | RTL8188EU | USB 2.0 |
| TP-LINK TL-WN727N v5 | RTL8188EU | USB 2.0 |
| TP-LINK TL-WN821N v4 | RTL8192CU | USB 2.0 |
| TP-LINK TL-WN821N v5 | RTL8192EU | USB 2.0 |
| TP-LINK TL-WN822N v4 | RTL8192EU | USB 2.0 |
| TP-LINK TL-WN823N v1 | RTL8192CU | USB 2.0 |
| TP-LINK TL-WN823N v2 | RTL8192EU | USB 2.0 |
| TRENDnet TEW-805UB | RTL8812AU | USB 3.0 |
| ZyXEL NWD6605 | RTL8812AU | USB 3.0 |

## 参见

[rtwn(4)](rtwn.4.md), [rtwn_pci(4)](rtwn_pci.4.md), [rtwnfw(4)](rtwnfw.4.md), [usb(4)](usb.4.md)

## 缺陷

`rtwn_usb` 驱动不支持这些适配器提供的任何 802.11ac 功能。在支持这些功能之前，还需要在 [ieee80211(9)](../man9/ieee80211.9.md) 中进行额外工作。
