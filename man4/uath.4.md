# uath.4

`uath` — Atheros USB IEEE 802.11a/b/g 无线网络驱动

## 名称

`uath`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device ehci
> device uhci
> device ohci
> device usb
> device uath
> device wlan

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_uath_load="YES"
```

## 描述

`uath` 驱动支持基于 Atheros Communications 第五代 AR5005UG 和 AR5005UX 芯片组的 USB 2.0 无线网络设备。

AR5005UG 芯片组由 AR5523 多协议 MAC/基带处理器和可在 2300 至 2500 MHz 之间工作的 AR2112 单片射频组成（802.11b/g）。

AR5005UX 芯片组由 AR5523 多协议 MAC/基带处理器和可在 2300 至 2500 MHz（802.11b/g）或 4900 至 5850 MHz（802.11a）之间工作的 AR5112 双频段单片射频组成。

AR5005UG 和 AR5005UX 芯片组都集成了 32 位 MIPS R4000 类处理器，运行固件并管理传输速率的自动控制和射频校准等事务。

`uath` 支持 `station` 和 `monitor` 模式操作。任何时候只能配置一个虚拟接口。有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 固件

`uath` 需要下载到设备的固件。这通常由 uathload(8) 实用程序完成，该程序在设备插入时由 devd(8) 启动。uathload(8) 将固件包含在二进制程序中。此固件经授权可供通用使用，并包含在基本系统中。

## 硬件

`uath` 驱动应与以下适配器配合工作：

| *适配器* | *芯片组* |
| -------- | -------- |
| `Compex WLU108AG` | AR5005UX |
| `Compex WLU108G` | AR5005UG |
| `D-Link DWL-G132` | AR5005UG |
| `IODATA WN-G54/US` | AR5005UG |
| `MELCO WLI-U2-KAMG54` | AR5005UX |
| `Netgear WG111T` | AR5005UG |
| `Netgear WG111U` | AR5005UX |
| `Netgear WPN111` | AR5005UG |
| `Olitec 000544` | AR5005UG |
| `PLANET WDL-U357` | AR5005UX |
| `Siemens Gigaset 108` | AR5005UG |
| `SMC SMCWUSBT-G` | AR5005UG |
| `SMC SMCWUSBT-G2` | AR5005UG |
| `SparkLAN WL-785A` | AR5005UX |
| `TP-Link TL-WN620G` | AR5005UG |
| `TRENDware International TEW-444UB` | AR5005UG |
| `TRENDware International TEW-504UB` | AR5005UX |
| `Unex Technology UR054ag` | AR5005UX |
| `ZyXEL XtremeMIMO M-202` | AR5005UX |

## 实例

加入现有 BSS 网络（即连接到接入点）：

```sh
ifconfig wlan create wlandev uath0 inet 192.168.0.20 e
    netmask 0xffffff00
```

加入网络名称为“`my_net`”的特定 BSS 网络：

```sh
ifconfig wlan create wlandev uath0 ssid my_net up
```

加入使用 64 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev uath0 ssid my_net e
	wepmode on wepkey 0x1234567890 weptxkey 1 up
```

加入使用 128 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev uath0 wlanmode adhoc ssid my_net e
    wepmode on wepkey 0x01020304050607080910111213 weptxkey 1
```

## 诊断

- uath%d: could not send command (error=%s) 向固件发送命令的尝试失败。
- uath%d: timeout waiting for command reply 向固件发送了读取命令，但固件未及时回复。
- uath%d: device timeout 分派到硬件进行传输的帧未及时完成。驱动将重置硬件。这不应发生。

## 参见

[netintro(4)](netintro.4.md), [usb(4)](usb.4.md), [wlan(4)](wlan.4.md), [wlan_ccmp(4)](wlan_ccmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md), [wlan_wep(4)](wlan_wep.4.md), devd(8), [ifconfig(8)](../man8/ifconfig.8.md), uathload(8), wpa_supplicant(8)

## 历史

`uath` 驱动首次出现于 OpenBSD 4.0。

## 作者

`uath` 驱动由 Weongyo Jeong <weongyo@FreeBSD.org> 和 Sam Leffler <sam@FreeBSD.org> 编写。它与 Damien Bergamini <damien@openbsd.org> 编写的驱动有远亲关系。

## 注意事项

不支持 Atheros 专有的 108 Mbps 模式（又名 Super AG 模式）。

双频适配器目前无法工作；解决方法是将操作限制在 2.4GHz 信道。
