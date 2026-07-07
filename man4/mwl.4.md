# mwl(4)

`mwl` — Marvell 88W8363 IEEE 802.11n 无线网络驱动

## 名称

`mwl`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device mwl
> device mwlfw
> device wlan
> device firmware

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_mwl_load="YES"
```

## 描述

`mwl` 驱动提供对基于 Marvell 88W8363 部件的 IEEE 802.11n 无线网络适配器的支持。支持 PCI 和/或 CardBus 接口。

此驱动需要使用 `mwlfw` 模块构建的固件才能工作。通常此模块由驱动按需加载，但也可以编译进内核。

支持的功能包括 802.11n、电源管理、BSS、MBSS 和基于主机的接入点操作模式。所有主机/设备交互都通过 DMA 进行。

`mwlfw` 驱动将 IP 和 ARP 流量封装为 802.11 帧，但可以接收 802.11 或 802.3 帧。设备支持 802.11n、802.11a、802.11g 和 802.11b 操作，传输速率与各自相适应。实际使用的传输速率取决于信号质量和固件中实现的“速率控制”算法。所有芯片都有硬件支持 WEP、AES-CCM、TKIP 和 Michael 加密操作。

该驱动支持 `station`、`hostap`、`mesh` 和 `wds` 模式操作。可以配置多个 `hostap` 虚拟接口以同时使用。配置多个接口时，每个接口可以有一个单独的 mac 地址，该地址通过设置分配给底层设备的 mac 地址中的 U/L 位来形成。任意数量的 `wds` 虚拟接口可与 `hostap` 接口一起配置。多个 `station` 接口可与 `hostap` 接口一起操作，以构建无线中继设备。有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

`mwlfw` 驱动支持的设备有 Cardbus 或 mini-PCI 封装。Cardbus 插槽中的无线卡可以即时插入和弹出。

## 实例

加入现有的 BSS 网络（即连接到接入点）：

```sh
ifconfig wlan create wlandev mwl0 inet 192.168.0.20 e
	netmask 0xffffff00"
```

加入网络名为“`my_net`”的特定 BSS 网络：

```sh
ifconfig wlan create wlandev mwl0 inet 192.168.0.20 e
	netmask 0xffffff00 ssid my_net"
```

加入使用 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan0 create wlandev mwl0
ifconfig wlan0 inet 192.168.0.20 netmask 0xffffff00 ssid my_net e
	wepmode on wepkey 0x8736639624
```

创建 802.11g 基于主机的接入点：

```sh
ifconfig wlan0 create wlandev mwl0 wlanmode hostap
ifconfig wlan0 inet 192.168.0.10 netmask 0xffffff00 ssid my_ap e
	mode 11g
```

创建 802.11a mesh 站点：

```sh
ifconfig wlan0 create wlandev mwl0 wlanmode mesh
ifconfig wlan0 meshid my_mesh mode 11a inet 192.168.0.10/24
```

创建两个虚拟 802.11a 基于主机的接入点，一个启用 WEP，一个无安全，并将它们桥接到 fxp0（有线）设备：

```sh
ifconfig wlan0 create wlandev mwl0 wlanmode hostap e
	ssid paying-customers wepmode on wepkey 0x1234567890 e
	mode 11a up
ifconfig wlan1 create wlandev mwl0 wlanmode hostap bssid e
	ssid freeloaders up
ifconfig bridge0 create addm wlan0 addm wlan1 addm fxp0 up
```

## 诊断

- mwl%d: unable to setup builtin firmware 下载和/或设置固件时出现问题。设备不可用。
- mwl%d: failed to setup descriptors: %d 设置 DMA 数据结构时出现问题。这通常是由于无法分配连续内存引起的。
- mwl%d: transmit timeout 分派到硬件进行传输的帧未及时完成。这不应发生。
- mwl%d: device not present 活动时弹出了 cardbus 设备；对固件的请求未完成。

## 参见

[cardbus(4)](cardbus.4.md), [intro(4)](intro.4.md), [mwlfw(4)](mwlfw.4.md), [pci(4)](pci.4.md), [wlan(4)](wlan.4.md), [wlan_ccmp(4)](wlan_ccmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md), [wlan_wep(4)](wlan_wep.4.md), [wlan_xauth(4)](wlan_xauth.4.md), hostapd(8), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 历史

`mwlfw` 设备驱动首次出现于 FreeBSD 8.0。

## 缺陷

该驱动在 station 模式下不支持省电操作；因此功耗不理想（例如在笔记本电脑上）。
