# ural.4

`ural` — Ralink RT2500USB IEEE 802.11a/b/g 无线网络驱动

## 名称

`ural`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device ehci
> device uhci
> device ohci
> device usb
> device ural
> device wlan
> device wlan_amrr

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
if_ural_load="YES"
```

## 描述

`ural` 驱动支持基于 RT2500USB 芯片组的 USB 2.0 无线适配器。

RT2500USB 芯片组由两块集成芯片组成：一块 RT2570 MAC/BBP 和一块无线电收发器（型号取决于网卡修订版本）。

RT2522、RT2523、RT2524、RT2525、RT2525e 和 RT2526 无线电收发器工作在 2.4GHz 频段（802.11b/g），而 RT5222 是双频无线电收发器，可工作在 2.4GHz 和 5.2GHz 频段（802.11a）。

`ural` 支持 `station`、`adhoc`、`hostap` 和 `monitor` 模式操作。任一时刻只能配置一个虚拟接口。有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`ural` 驱动支持基于 Ralink Technology RT2500USB 芯片组的 USB 2.0 无线适配器，包括：

| *Card* | *Bus* |
| --- | --- |
| AMIT WL532U | USB |
| ASUS WL-167g | USB |
| Belkin F5D7050 v2000 | USB |
| Buffalo WLI-U2-KG54-AI | USB |
| CNet CWD-854 | USB |
| Compex WLU54G 2A1100 | USB |
| Conceptronic C54RU | USB |
| D-Link DWL-G122 b1 | USB |
| Dynalink WLG25USB | USB |
| E-Tech WGUS02 | USB |
| Gigabyte GN-WBKG | USB |
| Hercules HWGUSB2-54 | USB |
| KCORP LifeStyle KLS-685 | USB |
| Linksys WUSB54G v4 | USB |
| Linksys WUSB54GP v4 | USB |
| MSI MS-6861 | USB |
| MSI MS-6865 | USB |
| MSI MS-6869 | USB |
| NovaTech NV-902 | USB |
| OvisLink Evo-W54USB | USB |
| SerComm UB801R | USB |
| SparkLAN WL-685R | USB |
| Surecom EP-9001-g | USB |
| Sweex LC100060 | USB |
| Tonze UW-6200C | USB |
| Zinwell ZWX-G261 | USB |
| Zonet ZEW2500P | USB |

最新列表可在 `http://ralink.rapla.net/` 找到。

## 实例

加入现有的 BSS 网络（即连接到接入点）：

```sh
ifconfig wlan create wlandev ural0 inet 192.0.2.20/24
```

加入网络名为 `my_net` 的特定 BSS 网络：

```sh
ifconfig wlan create wlandev ural0 ssid my_net up
```

加入使用 64 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev ural0 ssid my_net e
    wepmode on wepkey 0x1234567890 weptxkey 1 up
```

加入使用 128 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev ural0 wlanmode adhoc ssid my_net e
    wepmode on wepkey 0x01020304050607080910111213 weptxkey 1
```

## 诊断

- ural%d: device timeout 驱动将重置硬件。这种情况不应发生。

## 参见

[intro(4)](intro.4.md), [netintro(4)](netintro.4.md), [usb(4)](usb.4.md), [wlan(4)](wlan.4.md), [wlan_amrr(4)](wlan_amrr.4.md), [wlan_ccmp(4)](wlan_ccmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md), [wlan_wep(4)](wlan_wep.4.md), [wlan_xauth(4)](wlan_xauth.4.md), [networking(7)](../man7/networking.7.md), hostapd(8), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 历史

`ural` 驱动首次出现于 OpenBSD 3.7 和 FreeBSD 6.0。

## 作者

原始 `ural` 驱动由 Damien Bergamini <damien.bergamini@free.fr> 编写。

## 缺陷

Host AP 模式不支持客户端省电。使用省电模式的客户端会出现丢包（在客户端禁用省电可解决此问题）。
