# run.4

`run` — Ralink Technology USB IEEE 802.11a/g/n 无线网络驱动

## 名称

`run`

## 概要

若要将此驱动程序编译进内核，请在你的内核配置文件中加入以下行：

> device ehci
> device uhci
> device ohci
> device usb
> device run
> device wlan
> device wlan_amrr

`还需要固件，由以下提供：`

> device runfw

`或者，若要在引导时以模块方式加载驱动程序，在 loader.conf(5) 中加入以下行：`

```sh
if_run_load="YES"
runfw_load="YES"
```

## 描述

`run` 驱动支持基于 Ralink RT2700U、RT2800U、RT3000U 和 RT3900E 芯片组的 USB 2.0 无线适配器。

RT2700U 芯片组由两块集成芯片组成：一块 RT2770 MAC/BBP 和一块 RT2720（1T2R）或 RT2750（双频 1T2R）无线电收发器。

RT2800U 芯片组由两块集成芯片组成：一块 RT2870 MAC/BBP 和一块 RT2820（2T3R）或 RT2850（双频 2T3R）无线电收发器。

RT3000U 是基于 RT3070 MAC/BBP 和 RT3020（1T1R）、RT3021（1T2R）或 RT3022（2T2R）单频无线电收发器的单芯片解决方案。

RT3900E 是单芯片 USB 2.0 802.11n 解决方案。MAC/基带处理器可以是 RT3593、RT5390、RT5392 或 RT5592。无线电可以是 RT3053、RT5370、RT5372 或 RT5572。RT3053 芯片在 2GHz 和 5GHz 频段工作，支持最多 3 条发射路径和 3 条接收路径（3T3R）。RT5370 芯片在 2GHz 频段工作，支持 1 条发射路径和 1 条接收路径（1T1R）。RT5372 芯片在 2GHz 频段工作，支持最多 2 条发射路径和 2 条接收路径（2T2R）。RT5572 芯片在 2GHz 和 5GHz 频段工作，支持最多 2 条发射路径和 2 条接收路径（2T2R）。

`run` 驱动可在以下模式中操作：

**BSS** 模式 也称为 *infrastructure*（基础设施）模式，用于关联到接入点，所有流量都通过接入点传输。此模式为默认模式。

**Host AP** 模式 在此模式下，驱动充当其他卡片的接入点（基站）。

**monitor** 模式 在此模式下，驱动能够无需关联到接入点就接收数据包。这会禁用内部接收过滤器，使卡片能够从通常无法访问的网络捕获数据包，或扫描接入点。

可以将 `run` 驱动配置为使用有线等效加密（WEP）或 Wi-Fi 保护访问（WPA-PSK 和 WPA2-PSK）。WPA 是无线网络事实上的加密标准。由于 WEP 存在严重弱点，强烈建议不要将 WEP 作为保障无线通信安全的唯一机制。`run` 驱动将 WEP40、WEP104、TKIP（+MIC）和 CCMP 密码的数据帧加密和解密都卸载到硬件执行。

`run` 驱动可在运行时通过 [ifconfig(8)](../man8/ifconfig.8.md) 进行配置。

## 硬件

`run` 驱动支持以下无线适配器：

- Airlink101 AWLL6090
- ASUS USB-N11
- ASUS USB-N13 ver. A1
- ASUS USB-N14
- ASUS USB-N66
- ASUS WL-160N
- Belkin F5D8051 ver 3000
- Belkin F5D8053
- Belkin F5D8055
- Belkin F6D4050 ver 1
- Belkin F9L1103
- Buffalo WLI-UC-AG300N
- Buffalo WLI-UC-G300HP
- Buffalo WLI-UC-G300N
- Buffalo WLI-UC-G301N
- Buffalo WLI-UC-GN
- Buffalo WLI-UC-GNM
- Buffalo WLI-UC-GNM2
- Corega CG-WLUSB2GNL
- Corega CG-WLUSB2GNR
- Corega CG-WLUSB300AGN
- Corega CG-WLUSB300GNM
- D-Link DWA-130 rev B1
- D-Link DWA-130 rev F1
- D-Link DWA-140 rev B1, B2, B3, D1
- D-Link DWA-160 rev B2
- D-Link DWA-162
- DrayTek Vigor N61
- Edimax EW-7711UAn
- Edimax EW-7711UTn
- Edimax EW-7717Un
- Edimax EW-7718Un
- Edimax EW-7733UnD
- Gigabyte GN-WB30N
- Gigabyte GN-WB31N
- Gigabyte GN-WB32L
- Hawking HWDN1
- Hawking HWUN1
- Hawking HWUN2
- Hercules HWNU-300
- Linksys WUSB54GC v3
- Linksys WUSB600N
- Logitec LAN-W150N/U2
- Mvix Nubbin MS-811N
- Panda Wireless PAU06
- Planex GW-USMicroN
- Planex GW-US300MiniS
- Sitecom WL-182
- Sitecom WL-188
- Sitecom WL-301
- Sitecom WL-302
- Sitecom WL-315
- Sitecom WL-364
- SMC SMCWUSBS-N2
- Sweex LW303
- Sweex LW313
- TP-LINK TL-WDN3200
- TP-LINK TL-WN321G v4
- TP-LINK TL-WN727N v3
- Unex DNUR-81
- Unex DNUR-82
- ZyXEL NWD2705
- ZyXEL NWD210N
- ZyXEL NWD270N

## 实例

加入现有的 BSS 网络（即连接到接入点）：

```sh
ifconfig wlan create wlandev run0 inet 192.0.2.20/24
```

加入网络名为 `my_net` 的特定 BSS 网络：

```sh
ifconfig wlan create wlandev run0 ssid my_net up
```

加入使用 64 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev run0 ssid my_net e
    wepmode on wepkey 0x1234567890 weptxkey 1 up
```

加入使用 128 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev run0 wlanmode adhoc ssid my_net e
    wepmode on wepkey 0x01020304050607080910111213 weptxkey 1
```

## 诊断

- run%d: failed load firmware of file runfw 由于某种原因，驱动无法从文件系统读取微代码文件。文件可能缺失或损坏。
- run%d: could not load 8051 microcode 尝试向板载 8051 微控制器单元上传微代码时发生错误。
- run%d: device timeout 派发到硬件进行发送的帧未能在时间内完成。驱动将重置硬件。这不应发生。

## 参见

[intro(4)](intro.4.md), [netintro(4)](netintro.4.md), [runfw(4)](runfw.4.md), [usb(4)](usb.4.md), [wlan(4)](wlan.4.md), [wlan_amrr(4)](wlan_amrr.4.md), [wlan_ccmp(4)](wlan_ccmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md), [wlan_wep(4)](wlan_wep.4.md), [wlan_xauth(4)](wlan_xauth.4.md), [networking(7)](../man7/networking.7.md), hostapd(8), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 历史

`run` 驱动最早出现于 OpenBSD 4.5。

## 作者

`run` 驱动由 Damien Bergamini <damien@openbsd.org> 编写。

## 注意事项

`run` 驱动支持 RT2800、RT3000 和 RT3900 芯片组中的部分 11n 功能。
