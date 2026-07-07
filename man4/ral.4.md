# ral(4)

`ral` — Ralink Technology IEEE 802.11a/g/n 无线网络驱动程序

## 名称

`ral`

## 概要

若要将此驱动程序编译进内核，请在你的内核配置文件中加入以下行：

> device ral
> device ralfw
> device wlan
> device wlan_amrr
> device firmware

或者，若要在引导时以模块方式加载驱动程序，在 loader.conf(5) 中加入以下行：

```sh
if_ral_load="YES"
```

## 描述

`ral` 驱动程序支持基于 Ralink RT2500、RT2501、RT2600、RT2700、RT2800、RT3090 和 RT3900E 芯片组的 PCI/PCIe/CardBus 无线适配器。

RT2500 芯片组是 Ralink 的第一代 802.11b/g 适配器。它由两块集成芯片组成：一块 RT2560 MAC/BBP 和一块 RT2525 无线电收发器。

RT2501 芯片组是 Ralink 的第二代 802.11a/b/g 适配器。它由两块集成芯片组成：一块 RT2561 MAC/BBP 和一块 RT2527 无线电收发器。此芯片组支持 IEEE 802.11e 标准的多个硬件发送队列，并允许分散/聚集以实现高效的 DMA 操作。

RT2600 芯片组由两块集成芯片组成：一块 RT2661 MAC/BBP 和一块 RT2529 无线电收发器。此芯片组使用 MIMO（多输入多输出）技术和多个无线电收发器以扩展适配器的工作范围并实现更高的吞吐量。但 RT2600 芯片组不支持任何 802.11n 特性。

RT2700 芯片组是 RT2800 芯片组的低成本版本。它支持单发射路径和双接收路径（1T2R）。它由两块集成芯片组成：一块 RT2760 或 RT2790（PCIe）MAC/BBP 和一块 RT2720（2.4GHz）或 RT2750（2.4GHz/5GHz）无线电收发器。

RT2800 芯片组是 Ralink 的第一代 802.11n 适配器。它由两块集成芯片组成：一块 RT2860 或 RT2890（PCIe）MAC/BBP 和一块 RT2820（2.4GHz）或 RT2850（2.4GHz/5GHz）无线电收发器。RT2800 芯片组支持两条发射路径和最多三条接收路径（2T2R/2T3R）。它可达到最高 144Mbps（20MHz 带宽）和 300Mbps（40MHz 带宽）的速度。

RT3090 芯片组是 Ralink 的第一代单芯片 802.11n 适配器。`ral` 支持 `station`、`adhoc`、`hostap`、`mesh`、`wds` 和 `monitor` 模式操作。同一时间只能配置一个 `hostap` 或 `mesh` 虚拟接口。任意数量的 `wds` 虚拟接口可与 `hostap` 接口一起配置。多个 `station` 接口可与 `hostap` 接口一起运行以构建无线中继设备。

RT3900E 芯片组是 Ralink 的单芯片 802.11n 适配器。MAC/基带处理器可以是 RT5390 或 RT5392。RT5390 芯片在 2GHz 频段工作，支持一条发射路径和一条接收路径（1T1R）。RT5392 芯片在 2GHz 频段工作，支持最多两条发射路径和两条接收路径（2T2R）。

发射速度可由用户选择，或由驱动程序根据硬件发送重试次数自动调整。有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`ral` 驱动程序支持基于 Ralink Technology 芯片组的 PCI/PCIe/CardBus 无线适配器，包括：

| *Card* | *MAC/BBP* | *Bus* |
| ------ | --------- | ----- |
| A-Link WL54H | RT2560 | PCI |
| A-Link WL54PC | RT2560 | CardBus |
| AirLink101 AWLC5025 | RT2661 | CardBus |
| AirLink101 AWLH5025 | RT2661 | PCI |
| Amigo AWI-914W | RT2560 | CardBus |
| Amigo AWI-922W | RT2560 | mini-PCI |
| Amigo AWI-926W | RT2560 | PCI |
| AMIT WL531C | RT2560 | CardBus |
| AMIT WL531P | RT2560 | PCI |
| AOpen AOI-831 | RT2560 | PCI |
| ASUS WL-107G | RT2560 | CardBus |
| ASUS WL-130g | RT2560 | PCI |
| Atlantis Land A02-PCI-W54 | RT2560 | PCI |
| Atlantis Land A02-PCM-W54 | RT2560 | CardBus |
| Belkin F5D7000 v3 | RT2560 | PCI |
| Belkin F5D7010 v2 | RT2560 | CardBus |
| Billionton MIWLGRL | RT2560 | mini-PCI |
| Canyon CN-WF511 | RT2560 | PCI |
| Canyon CN-WF513 | RT2560 | CardBus |
| CC&C WL-2102 | RT2560 | CardBus |
| CNet CWC-854 | RT2560 | CardBus |
| CNet CWP-854 | RT2560 | PCI |
| Compex WL54G | RT2560 | CardBus |
| Compex WLP54G | RT2560 | PCI |
| Conceptronic C54RC | RT2560 | CardBus |
| Conceptronic C54Ri | RT2560 | PCI |
| D-Link DWA-525 rev A2 | RT5392 | PCI |
| Digitus DN-7001G-RA | RT2560 | CardBus |
| Digitus DN-7006G-RA | RT2560 | PCI |
| E-Tech WGPC02 | RT2560 | CardBus |
| E-Tech WGPI02 | RT2560 | PCI |
| Edimax EW-7108PCg | RT2560 | CardBus |
| Edimax EW-7128g | RT2560 | PCI |
| Eminent EM3036 | RT2560 | CardBus |
| Eminent EM3037 | RT2560 | PCI |
| Encore ENLWI-G-RLAM | RT2560 | PCI |
| Encore ENPWI-G-RLAM | RT2560 | CardBus |
| Fiberline WL-400P | RT2560 | PCI |
| Fibreline WL-400X | RT2560 | CardBus |
| Gigabyte GN-WI01GS | RT2561S | mini-PCI |
| Gigabyte GN-WIKG | RT2560 | mini-PCI |
| Gigabyte GN-WMKG | RT2560 | CardBus |
| Gigabyte GN-WP01GS | RT2561S | PCI |
| Gigabyte GN-WPKG | RT2560 | PCI |
| Hawking HWC54GR | RT2560 | CardBus |
| Hawking HWP54GR | RT2560 | PCI |
| iNexQ CR054g-009 (R03) | RT2560 | PCI |
| JAHT WN-4054P | RT2560 | CardBus |
| JAHT WN-4054PCI | RT2560 | PCI |
| LevelOne WNC-0301 v2 | RT2560 | PCI |
| LevelOne WPC-0301 v2 | RT2560 | CardBus |
| Linksys WMP54G v4 | RT2560 | PCI |
| Micronet SP906GK | RT2560 | PCI |
| Micronet SP908GK V3 | RT2560 | CardBus |
| Minitar MN54GCB-R | RT2560 | CardBus |
| Minitar MN54GPC-R | RT2560 | PCI |
| MSI CB54G2 | RT2560 | CardBus |
| MSI MP54G2 | RT2560 | mini-PCI |
| MSI PC54G2 | RT2560 | PCI |
| OvisLink EVO-W54PCI | RT2560 | PCI |
| PheeNet HWL-PCIG/RA | RT2560 | PCI |
| Planex GW-NS300N | RT2860 | CardBus |
| Pro-Nets CB80211G | RT2560 | CardBus |
| Pro-Nets PC80211G | RT2560 | PCI |
| Repotec RP-WB7108 | RT2560 | CardBus |
| Repotec RP-WP0854 | RT2560 | PCI |
| SATech SN-54C | RT2560 | CardBus |
| SATech SN-54P | RT2560 | PCI |
| Sitecom WL-112 | RT2560 | CardBus |
| Sitecom WL-115 | RT2560 | PCI |
| SMC SMCWCB-GM | RT2661 | CardBus |
| SMC SMCWPCI-GM | RT2661 | PCI |
| SparkLAN WL-685R | RT2560 | CardBus |
| Surecom EP-9321-g | RT2560 | PCI |
| Surecom EP-9321-g1 | RT2560 | PCI |
| Surecom EP-9428-g | RT2560 | CardBus |
| Sweex LC500050 | RT2560 | CardBus |
| Sweex LC700030 | RT2560 | PCI |
| TekComm NE-9321-g | RT2560 | PCI |
| TekComm NE-9428-g | RT2560 | CardBus |
| Unex CR054g-R02 | RT2560 | PCI |
| Unex MR054g-R02 | RT2560 | CardBus |
| Zinwell ZWX-G160 | RT2560 | CardBus |
| Zinwell ZWX-G360 | RT2560 | mini-PCI |
| Zinwell ZWX-G361 | RT2560 | PCI |
| Zonet ZEW1500 | RT2560 | CardBus |
| Zonet ZEW1600 | RT2560 | PCI |

## 实例

加入现有的 BSS 网络（即连接到接入点）：

```sh
ifconfig wlan create wlandev ral0 inet 192.0.2.20/24
```

加入网络名为 `my_net` 的特定 BSS 网络：

```sh
ifconfig wlan create wlandev ral0 inet 192.0.2.20/24 e
    ssid my_net
```

加入使用 40 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev ral0 inet 192.0.2.20/24 e
    ssid my_net wepmode on wepkey 0x1234567890 weptxkey 1
```

加入使用 104 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev ral0 inet 192.0.2.20/24 e
    ssid my_net e
    wepmode on wepkey 0x01020304050607080910111213 weptxkey 1
```

## 诊断

- ral%d: could not load 8051 microcode 尝试向板载 8051 微控制器单元上传微代码时发生错误。
- ral%d: timeout waiting for MCU to initialize 板载 8051 微控制器单元未能在时间内完成初始化。
- ral%d: device timeout 派发到硬件进行发送的帧未能在时间内完成。驱动程序将重置硬件。这不应发生。

## 参见

[cardbus(4)](cardbus.4.md), [intro(4)](intro.4.md), [wlan(4)](wlan.4.md), [wlan_ccmp(4)](wlan_ccmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md), [wlan_wep(4)](wlan_wep.4.md), [wlan_xauth(4)](wlan_xauth.4.md), [networking(7)](../man7/networking.7.md), hostapd(8), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 历史

`ral` 驱动程序首次出现于 OpenBSD 3.7。对 RT2501 和 RT2600 芯片组的支持添加于 OpenBSD 3.9。对 RT2800 芯片组的支持添加于 OpenBSD 4.3。对 RT2700 芯片组的支持添加于 OpenBSD 4.4。对 RT3090 芯片组的支持添加于 OpenBSD 4.9。

## 作者

原始 `ral` 驱动程序由 Damien Bergamini <damien@openbsd.org> 编写。

## 注意事项

`ral` 驱动程序不使用硬件加密引擎。

`ral` 驱动程序不支持 RT2700 和 RT2800 芯片组提供的任何 802.11n 功能。在支持这些功能之前还需要额外的工作。

Host AP 模式不支持省电。客户端尝试使用省电模式可能会遇到显著的丢包（在客户端禁用省电可解决此问题）。

某些 PCI `ral` 适配器严格要求支持 PCI 2.2 或更高版本的系统。购买网卡前请检查板卡的 PCI 版本，因为基于较早 PCI 规范修订版本的系统上这些适配器很可能无法工作。
