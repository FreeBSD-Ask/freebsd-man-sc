# ipheth(4)

`ipheth` — USB Apple iPhone/iPad 网络共享以太网驱动

## 名称

`ipheth`

## 概要

要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_ipheth_load="YES"
```

或者，要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device uhci
> device ohci
> device usb
> device miibus
> device uether
> device ipheth

## 描述

`ipheth` 驱动提供通过 Apple iPhone 和 iPad 设备进行网络访问的支持，通常称为 USB 网络共享。

`ipheth` 应能与任何 Apple iPhone 或 iPad 设备一起工作。在大多数情况下，必须先在设备上显式启用此功能。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。该设备不支持不同的介质类型或选项。

## 硬件

以下设备受 `ipheth` 驱动支持：

- Apple iPhone 网络共享（所有型号）
- Apple iPad 网络共享（所有型号）

## 实例

```sh
`#` `kldload ipheth`
`#` `usbconfig | grep Apple`
ugen0.2: <Apple Inc. iPhone> at usbus0, cfg=0 md=HOST spd=HIGH (480Mbps) pwr=ON (500mA)
```

```sh
`#` `usbconfig -d 0.2 dump_all_config_desc | grep -E '(^ Conf|iConf)'`
 Configuration index 0
    iConfiguration = 0x0005  <PTP>
 Configuration index 1
    iConfiguration = 0x0006  <iPod USB Interface>
 Configuration index 2
    iConfiguration = 0x0007  <PTP + Apple Mobile Device>
 Configuration index 3
    iConfiguration = 0x0008  <PTP + Apple Mobile Device + Apple USB Ethernet>
```

```sh
`#` `usbconfig -d 0.2 set_config 3`
`#` `usbconfig | grep 'Apple.*cfg=3'`
ugen0.2: <Apple Inc. iPhone> at usbus0, cfg=3 md=HOST spd=HIGH (480Mbps) pwr=ON (500mA)
```

```sh
`#` `dmesg | grep 'ue[0-9]'`
ue0: <USB Ethernet> on ipheth0
ue0: bpf attached
ue0: Ethernet address: 4e:7c:5f:2c:5f:7a
```

```sh
`#` `usbmuxd --enable-exit --foreground --user root --verbose`
```

```sh
`#` `sysrc ifconfig_ue0="SYNCDHCP"`
ifconfig_ue0:  -> SYNCDHCP
`#` `service netif restart ue0`
```

**实例 1：** 手动配置 以下示例展示如何手动配置未被自动识别的设备的网络访问。首先，加载驱动并找出 USB Apple 设备的单元号和地址：在此示例中，设备的单元号和地址为 0.2（“`ugen0.2`”），其配置索引为 0（“`cfg=0`”）。其次，检查设备的其他可用配置：在此示例中，有 4 种不同的可用配置。索引为 3 的配置似乎与以太网相关。现在配置设备：此时 Apple 设备应询问是否信任 FreeBSD 机器（必须开启“Mobile Data”）。应会出现一个新的 *ue* USB 以太网接口：此时可能需要运行 usbmuxd(1)（在 [ports(7)](../man7/ports.7.md) 的 `comms/usbmuxd` 中可用）。现在配置网络接口：完成。机器现在应通过 USB 网络共享连接到网络。

## 参见

arp(4), [cdce(4)](cdce.4.md), [cdceem(4)](cdceem.4.md), [intro(4)](intro.4.md), [netintro(4)](netintro.4.md), [urndis(4)](urndis.4.md), [usb(4)](usb.4.md), [ifconfig(8)](../man8/ifconfig.8.md), usbconfig(8)

## 历史

`ipheth` 设备驱动首次出现于 FreeBSD 8.2。

## 作者

`ipheth` 驱动由 Hans Petter Selasky <hselasky@FreeBSD.org> 编写。

## 缺陷

某些设备不会被自动识别，可能需要使用 usbconfig(8) 实用程序手动配置以使用备用配置。变通方法见“实例”小节。
