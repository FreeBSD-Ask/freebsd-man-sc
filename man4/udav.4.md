# udav(4)

`udav` — Davicom DM9601 USB 以太网驱动

## 名称

`udav`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device ehci
> device uhci
> device ohci
> device usb
> device miibus
> device uether
> device udav

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_udav_load="YES"
```

## 硬件

`udav` 驱动支持以下适配器：

- Corega FEther USB-TXC
- ShanTou ST268 USB NIC

## 描述

`udav` 驱动提供对基于 Davicom DM9601 芯片组的 USB 以太网适配器的支持。

有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [usb(4)](usb.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

> "Davicom DM9601 data sheet".

## 历史

`udav` 设备驱动首次出现于 NetBSD 2.0。

## 作者

`udav` 驱动由 Shingo WATANABE <nabe@nabechan.org> 编写。
