# malo.4

`malo` — Marvell Libertas IEEE 802.11b/g 无线网络驱动

## 名称

`malo`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device malo
> device pci
> device wlan
> device firmware

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_malo_load="YES"
```

## 描述

`malo` 驱动提供对基于 Marvell Libertas 88W8335 的 PCI 和 Cardbus 网络适配器的支持。`malo` 支持 `station` 和 `monitor` 模式操作。任何时候只能配置一个虚拟接口。有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

此驱动在运行前需要先加载固件。在 [ifconfig(8)](../man8/ifconfig.8.md) 工作之前，需要安装 `ports/net/malo-firmware-kmod` port。

## 硬件

以下网卡属于 `malo` 驱动支持的网卡：

| 网卡 | 芯片 | 总线 | 标准 |
| --- | --- | --- | --- |
| Netgear WG311v3 | 88W8335 | PCI | b/g |
| Tenda TWL542P | 88W8335 | PCI | b/g |
| U-Khan UW-2054i | 88W8335 | PCI | b/g |

## 实例

加入现有的 BSS 网络（即连接到接入点）：

```sh
ifconfig wlan create wlandev malo0 inet 192.168.0.20 e
    netmask 0xffffff00
```

加入网络名为“`my_net`”的特定 BSS 网络：

```sh
ifconfig wlan create wlandev malo0 ssid my_net up
```

加入使用 64 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev malo0 ssid my_net e
	wepmode on wepkey 0x1234567890 weptxkey 1 up
```

## 参见

[cardbus(4)](cardbus.4.md), [pci(4)](pci.4.md), [wlan(4)](wlan.4.md), [wlan_ccmp(4)](wlan_ccmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md), [wlan_wep(4)](wlan_wep.4.md), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 历史

`malo` 设备驱动首次出现于 FreeBSD 7.1。
