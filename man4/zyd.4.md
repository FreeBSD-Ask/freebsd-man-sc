# zyd(4)

`zyd` — ZyDAS ZD1211/ZD1211B USB IEEE 802.11b/g 无线网络驱动

## 名称

`zyd`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device ehci
> device uhci
> device ohci
> device usb
> device zyd
> device wlan
> device wlan_amrr

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
if_zyd_load="YES"
```

## 描述

`zyd` 驱动为基于 ZyDAS ZD1211 和 ZD1211B USB 芯片的无线网络适配器提供支持。

`zyd` 支持 `station` 和 `monitor` 模式操作。任何时候只能配置一个虚拟接口。有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

以下设备已知受 `zyd` 驱动支持：

- 3COM 3CRUSB10075
- Acer WLAN-G-US1
- Airlink+ AWLL3025
- Airlink 101 AWLL3026
- AOpen 802.11g WL54
- Asus A9T 集成无线网卡
- Asus WL-159g
- Belkin F5D7050 v.4000
- Billion BiPAC 3011G
- Buffalo WLI-U2-KG54L
- CC&C WL-2203B
- DrayTek Vigor 550
- Edimax EW-7317UG
- Edimax EW-7317LDG
- Fiberline Networks WL-43OU
- iNexQ UR055g
- Linksys WUSBF54G
- Longshine LCS-8131G3
- MSI US54SE
- MyTek MWU-201 USB 适配器
- Philips SNU5600
- Planet WL-U356
- Planex GW-US54GZ
- Planex GW-US54GZL
- Planex GW-US54Mini
- Safecom SWMULZ-5400
- Sagem XG 760A
- Sagem XG 76NA
- Sandberg Wireless G54 USB
- Sitecom WL-113
- SMC SMCWUSB-G
- Sweex wireless USB 54 Mbps
- Tekram/Siemens USB 适配器
- Telegent TG54USB
- Trendnet TEW-424UB rev A
- Trendnet TEW-429UB
- TwinMOS G240
- Unicorn WL-54G
- US Robotics 5423
- X-Micro XWL-11GUZX
- Yakumo QuickWLAN USB
- Zonet ZEW2501
- ZyXEL ZyAIR G-202
- ZyXEL ZyAIR G-220

## 实例

以下示例将 zyd0 配置为使用 WEP 密钥“0x1deadbeef1”、信道 11 加入任意 BSS 网络：

```sh
ifconfig wlan create wlandev zyd0 channel 11 e
    wepmode on wepkey 0x1deadbeef1 weptxkey 1 e
    inet 192.0.2.20/24
```

加入现有的 BSS 网络 `my_net`：

```sh
ifconfig wlan create wlandev zyd0 192.0.2.20/24 e
    ssid my_net
```

## 诊断

- zyd%d: could not load firmware (error=%d) 尝试将固件上传到板载微控制器单元时发生错误。
- zyd%d: could not send command (error=%s) 向固件发送命令的尝试失败。
- zyd%d: sorry, radio %s is not supported yet 驱动尚未实现对指定射频芯片的支持。设备不会附加。
- zyd%d: device version mismatch: 0x%x (only >= 43.30 supported) 此驱动不支持 ZD1211 芯片组的早期修订版本。设备不会附加。
- zyd%d: device timeout 分派到硬件进行传输的帧未及时完成。驱动将重置硬件。这不应发生。

## 参见

[intro(4)](intro.4.md), [netintro(4)](netintro.4.md), [usb(4)](usb.4.md), [wlan(4)](wlan.4.md), [wlan_amrr(4)](wlan_amrr.4.md), [wlan_ccmp(4)](wlan_ccmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md), [wlan_wep(4)](wlan_wep.4.md), [networking(7)](../man7/networking.7.md), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 作者

原始 `zyd` 驱动由 Florian Stoehr <ich@florian-stoehr.de>、Damien Bergamini <damien@openbsd.org> 和 Jonathan Gray <jsg@openbsd.org> 编写。

## 注意事项

`zyd` 驱动不支持硬件中可用的大量功能。要正确支持 IBSS 和电源管理功能，还需要更多工作。
