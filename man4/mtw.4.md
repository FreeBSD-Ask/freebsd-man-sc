# mtw(4)

`mtw` — MediaTek MT7601U USB IEEE 802.11n 无线网络驱动

## 名称

`mtw`

## 概要

`device usb device mtw device wlan`

`在 rc.conf(5) 中：kld_list="if_mtw"`

## 描述

此模块提供对 MediaTek MT7601U USB 无线网络适配器的支持。如果检测到相应硬件，驱动会通过 [devmatch(8)](../man8/devmatch.8.md) 自动加载。如果显式禁用了驱动自动加载，请在 [rc.conf(5)](../man5/rc.conf.5.md) 中启用该模块。可以在运行时使用 [ifconfig(8)](../man8/ifconfig.8.md) 配置 `mtw` 驱动，或在引导时通过 [rc.conf(5)](../man5/rc.conf.5.md) 配置。

## 硬件

`mtw` 驱动支持基于 MediaTek MT7601U 的 USB 无线网络适配器，包括（但并非全部经过测试）：

- ASUS USB-N10 v2
- D-Link DWA-127 rev B1
- Edimax EW-7711UAn v2
- Foxconn WFU03
- Tenda U2
- Tenda W311MI v2
- TP-LINK TL-WN727N v4（已测试可用）
- Yealink WF40

## 文件

`mtw` 驱动需要来自 `ports/net/wifi-firmware-mt7601u-kmod` 的固件。如果在安装或运行时检测到相应硬件，此固件包会通过 fwget(8) 自动安装。

## 参见

[usb(4)](usb.4.md), [wlan(4)](wlan.4.md), [networking(7)](../man7/networking.7.md), fwget(8), wpa_supplicant(8)

## 历史

`mtw` 驱动首次出现于 OpenBSD 7.1 和 FreeBSD 15.0。

## 作者

`mtw` 驱动由 James Hastings <hastings@openbsd.org> 编写，并由 Jesper Schmitz Mouridsen <jsm@FreeBSD.org> 移植到 FreeBSD。

## 缺陷

`mtw` 仅在 `station` 模式和 `monitor` 模式下工作。在重新加载模块或重启时，如果不先拔下设备，固件并不总是会重新初始化。
