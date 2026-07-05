# urndis.4

`urndis` — USB Remote NDIS 以太网设备

## 名称

`urndis`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device ehci
> device uhci
> device ohci
> device xhci
> device usb
> device miibus
> device uether
> device urndis

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
if_urndis_load="YES"
```

## 描述

`urndis` 驱动通过 Remote NDIS (RNDIS) 提供以太网访问，允许手机和平板电脑等移动设备提供网络接入。这通常被称为 USB 网络共享，在大多数情况下需要在设备上显式启用。

`urndis` 应当能与任何 USB RNDIS 设备协同工作，例如 Android 设备上常见的那些。它不支持不同的媒体类型或选项。有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`urndis` 驱动支持许多 Android 设备的“网络共享”功能。

## 参见

arp(4), [cdce(4)](cdce.4.md), [cdceem(4)](cdceem.4.md), [ipheth(4)](ipheth.4.md), [netintro(4)](netintro.4.md), [usb(4)](usb.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`urndis` 设备驱动首次出现于 OpenBSD 4.7。首个包含它的 FreeBSD 版本是 FreeBSD 9.3。

## 作者

`urndis` 驱动由 Jonathan Armani <armani@openbsd.org>、Michael Knudsen <mk@openbsd.org> 和 Fabien Romano <fabien@openbsd.org> 编写。由 Hans Petter Selasky <hselasky@FreeBSD.org> 移植到 FreeBSD。
