# otus.4

`otus` — Atheros AR9170 USB IEEE 802.11a/b/g/n 无线网络驱动

## 名称

`otus`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device ehci
> device uhci
> device ohci
> device usb
> device otus
> device wlan

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_otus_load="YES"
```

## 描述

`otus` 驱动支持基于 Atheros AR9170 芯片组的 USB 2.0 无线网络设备。

Atheros AR9170 是一个草案 802.11n 适配器，使用外部无线电在仅 2.4GHz 或 2.4GHz 和 5GHz 模式下工作。

AR9101 无线电支持仅 2GHz 的 1T1R 操作。

AR9102 无线电支持仅 2GHz 的 2T2R 操作。

AR9104 无线电支持 2GHz 和 5GHz 的 2T2R 操作。

以下是 `otus` 驱动可以操作的模式：

**BSS** 模式 也称为 *infrastructure* 模式，用于与接入点关联，所有流量都通过接入点传递。此模式为默认模式。

`otus` 驱动可配置为使用有线等效保密（WEP）或 Wi-Fi 保护访问（WPA-PSK 和 WPA2-PSK）。WPA 是无线网络事实上的加密标准。由于 WEP 存在严重缺陷，强烈建议不要将其作为保障无线通信安全的唯一机制。

`otus` 驱动可在运行时通过 [ifconfig(8)](../man8/ifconfig.8.md) 进行配置。

## 硬件

`otus` 驱动为 Atheros AR9170 USB IEEE 802.11b/g/n 无线网络适配器提供支持，包括：

- 3Com 3CRUSBN275
- Arcadyan WN7512
- CACE AirPcap Nx
- D-Link DWA-130 rev D1
- D-Link DWA-160 rev A1
- D-Link DWA-160 rev A2
- IO-Data WN-GDN/US2
- NEC Aterm WL300NU-G
- Netgear WNDA3100
- Netgear WN111 v2
- Planex GW-US300
- SMC Networks SMCWUSB-N2
- TP-Link TL-WN821N v1, v2
- Ubiquiti SR71 USB
- Unex DNUA-81
- Z-Com UB81
- Z-Com UB82
- ZyXEL NWD-271N

## 文件

驱动需要以下固件文件的至少 1.0 版本，这些文件在接口附加时加载：

**`/boot/kernel/otusfw-init.ko`**
**`/boot/kernel/otusfw-main.ko`**

## 实例

加入现有的 BSS 网络（即连接到接入点）：

```sh
ifconfig wlan create wlandev otus0 inet 192.0.2.20/24
```

加入网络名称为 `my_net` 的特定 BSS 网络：

```sh
ifconfig wlan create wlandev otus0 ssid my_net up
```

加入使用 64 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev otus0 ssid my_net e
    wepmode on wepkey 0x1234567890 weptxkey 1 up
```

## 诊断

- %s: failed load firmware of file otusfw-main 由于某种原因，驱动无法从文件系统读取微代码文件。该文件可能缺失或已损坏。

## 参见

[intro(1)](../man1/intro.1.md), [netintro(4)](netintro.4.md), [otusfw(4)](otusfw.4.md), [usb(4)](usb.4.md), [wlan(4)](wlan.4.md), arp(8), hostapd(8), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 历史

`otus` 驱动最早出现于 OpenBSD 4.6 和 FreeBSD 11。

## 作者

`otus` 驱动由 Damien Bergamini <damien@openbsd.org> 编写，并由 Adrian Chadd <adrian@freebsd.org> 移植。

## 注意事项

`otus` 驱动仅支持 802.11a/b/g 操作。目前不支持 802.11n 操作。
