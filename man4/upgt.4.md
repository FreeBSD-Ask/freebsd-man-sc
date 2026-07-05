# upgt.4

`upgt` — Conexant/Intersil PrismGT SoftMAC USB IEEE 802.11b/g 无线网络

## 名称

`upgt` 驱动

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device ehci
> device uhci
> device ohci
> device usb
> device upgt
> device wlan

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
if_upgt_load="YES"
```

## 弃用通知

`upgt` 驱动计划在 FreeBSD 16.0 中移除。

## 描述

`upgt` 驱动支持基于 GW3887 芯片组的 USB 2.0 Conexant/Intersil PrismGT 系列无线适配器。

以下是 `upgt` 驱动可运行的模式：

**BSS** 模式 又称 *infrastructure*（基础设施）模式，用于关联到接入点，所有流量都通过接入点传输。此模式为默认模式。

**monitor** 模式 在此模式下，驱动能够不关联接入点就接收数据包。这会禁用内部接收过滤器，使网卡能够捕获通常无法访问的网络中的数据包，或扫描接入点。

`upgt` 支持软件 WEP。Wired Equivalent Privacy (WEP) 是无线网络事实上的加密标准。通常可以用三种模式之一进行配置：不加密、40 位加密或 104 位加密。遗憾的是，由于 WEP 协议存在严重缺陷，强烈建议不要将其作为保护无线通信的唯一机制。默认情况下不启用 WEP。

`upgt` 驱动可在运行时通过 [ifconfig(8)](../man8/ifconfig.8.md) 进行配置。

## 文件

此驱动需要安装 `upgtfw` 固件才能工作。该固件文件未公开发布。可通过 pkg_add(1) 安装的固件包位于：

```sh
http://weongyo.org/project/upgt/upgt-firmware-2.13.1.0.tar.gz
```

## 硬件

`upgtfw` 驱动支持基于 GW3887 芯片组的 USB 2.0 Conexant/Intersil PrismGT 系列无线适配器，其中包括：

- Belkin F5D7050 (version 1000)
- Cohiba Proto Board
- D-Link DWL-G120 Cohiba
- FSC Connect2Air E-5400 USB D1700
- Gigaset USB Adapter 54
- Inventel UR045G
- Netgear WG111v1 (rev2)
- SMC EZ ConnectG SMC2862W-G
- Sagem XG703A
- Spinnaker DUT
- Spinnaker Proto Board

## 实例

加入现有的 BSS 网络（即连接到接入点）：

```sh
ifconfig wlan create wlandev upgt0 inet 192.168.0.20 e
    netmask 0xffffff00
```

加入网络名为 “`my_net`” 的特定 BSS 网络：

```sh
ifconfig wlan create wlandev upgt0 ssid my_net up
```

加入使用 64 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev upgt0 ssid my_net e
        wepmode on wepkey 0x1234567890 weptxkey 1 up
```

## 参见

arp(4), [netintro(4)](netintro.4.md), [usb(4)](usb.4.md), [wlan(4)](wlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`upgtfw` 驱动首次出现于 OpenBSD 4.3。

## 作者

`upgtfw` 驱动由 Marcus Glocker <mglocker@openbsd.org> 编写。

硬件规范由 `http://www.prism54.org` 上的人员逆向工程得出。

## 注意事项

`upgtfw` 驱动仅支持 USB 2.0 设备（GW3887 芯片组），不支持包含 NET2280、ISL3880 和 ISL3886 芯片组的 USB 1.0 设备。要在驱动中添加对 USB 1.0 的支持，还需要进一步的工作。
