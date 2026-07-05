# rum.4

`rum` — Ralink Technology USB IEEE 802.11a/b/g 无线网络驱动

## 名称

`rum`

## 概要

若要将此驱动程序编译进内核，请在你的内核配置文件中加入以下行：

> device ehci
> device uhci
> device ohci
> device usb
> device rum
> device wlan
> device wlan_amrr

或者，若要在引导时以模块方式加载驱动程序，在 loader.conf(5) 中加入以下行：

```sh
if_rum_load="YES"
```

## 描述

`rum` 驱动支持基于 Ralink RT2501USB 和 RT2601USB 芯片组的 USB 2.0 和 PCI Express Mini Card 无线适配器。

Ralink PCI Express Mini Card 适配器显示为普通 USB 2.0 设备，因此由 `rum` 驱动处理。

RT2501USB 芯片组是 Ralink 的第二代 802.11a/b/g 适配器。它由两块集成芯片组成：一块 RT2571W MAC/BBP 和一块 RT2528 或 RT5226 无线电收发器。

RT2601USB 芯片组由两块集成芯片组成：一块 RT2671 MAC/BBP 和一块 RT2527 或 RT5225 无线电收发器。此芯片组使用 MIMO（多输入多输出）技术和多个天线扩展适配器的工作范围并实现更高的吞吐量。

所有芯片均有硬件支持 WEP、AES-CCM、TKIP 和 Michael 加密操作。

`rum` 支持 `station`、`adhoc`、`adhoc-demo`、`hostap` 和 `monitor` 模式操作。同一时间只能配置一个虚拟接口。有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`rum` 驱动支持基于 Ralink RT2501USB 和 RT2601USB 芯片组的 USB 2.0 无线适配器，包括：

| *Card* | *Bus* |
| --- | --- |
| 3Com Aolynk WUB320g | USB |
| Abocom WUG2700 Ta | USB |
| Airlink101 AWLL5025 | USB |
| ASUS WL-167g ver 2 | USB |
| Belkin F5D7050 ver 3 | USB |
| Belkin F5D9050 ver 3 | USB |
| Buffalo WLI-U2-SG54HP | USB |
| Buffalo WLI-U2-SG54HG | USB |
| Buffalo WLI-U2-G54HP | USB |
| Buffalo WLI-UC-G | USB |
| CNet CWD-854 ver F | USB |
| Conceptronic C54RU ver 2 | USB |
| Corega CG-WLUSB2GO | USB |
| D-Link DWA-110 | USB |
| D-Link DWA-111 | USB |
| D-Link DWL-G122 rev C1 | USB |
| D-Link WUA-1340 | USB |
| Digitus DN-7003GR | USB |
| Edimax EW-7318USG | USB |
| Gigabyte GN-WB01GS | USB |
| Gigabyte GN-WI05GS | USB |
| Hawking HWUG1 | USB |
| Hawking HWU54DM | USB |
| Hercules HWGUSB2-54-LB | USB |
| Hercules HWGUSB2-54V2-AP | USB |
| LevelOne WNC-0301USB v3 | USB |
| Linksys WUSB54G rev C | USB |
| Linksys WUSB54GR | USB |
| Planex GW-US54HP | USB |
| Planex GW-US54Mini2 | USB |
| Planex GW-USMM | USB |
| Senao NUB-3701 | USB |
| Sitecom WL-113 ver 2 | USB |
| Sitecom WL-172 | USB |
| Sweex LW053 | USB |
| TP-LINK TL-WN321G v1/v2/v3 | USB |

## 实例

加入现有的 BSS 网络（即连接到接入点）：

```sh
ifconfig wlan create wlandev rum0 inet 192.0.2.20/24
```

加入网络名为 `my_net` 的特定 BSS 网络：

```sh
ifconfig wlan create wlandev rum0 ssid my_net up
```

加入使用 64 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev rum0 ssid my_net e
    wepmode on wepkey 0x1234567890 weptxkey 1 up
```

加入使用 128 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev rum0 wlanmode adhoc ssid my_net e
    wepmode on wepkey 0x01020304050607080910111213 weptxkey 1
```

## 诊断

- rum%d: could not load 8051 microcode 尝试向板载 8051 微控制器单元上传微代码时发生错误。驱动将重置硬件。这不应发生。

## 参见

[intro(4)](intro.4.md), [netintro(4)](netintro.4.md), [usb(4)](usb.4.md), [wlan(4)](wlan.4.md), [wlan_amrr(4)](wlan_amrr.4.md), [wlan_ccmp(4)](wlan_ccmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md), [wlan_wep(4)](wlan_wep.4.md), [wlan_xauth(4)](wlan_xauth.4.md), [networking(7)](../man7/networking.7.md), hostapd(8), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 历史

`rum` 驱动最早出现于 OpenBSD 4.0 和 FreeBSD 7.0。

## 作者

原始 `rum` 驱动由 Niall O'Higgins <niallo@openbsd.org> 和 Damien Bergamini <damien@openbsd.org> 编写。
