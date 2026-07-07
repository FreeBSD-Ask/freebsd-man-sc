# ath(4)

`ath` — Atheros IEEE 802.11 无线网络驱动

## 名称

`ath`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> device ath
> device ath_hal
> device ath_rate_sample
> device wlan

或者，要在引导时以模块形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行：

```sh
if_ath_load="YES"
```

## 描述

`ath` 驱动为基于 Atheros AR5210、AR5211、AR5212、AR5416 和 AR9300 编程 API 的无线网络适配器提供支持。这些 API 被多种芯片采用；几乎所有带 PCI、PCIe 和/或 CardBus 接口的芯片均受支持。

支持的功能包括 802.11 和 802.3 帧、电源管理、BSS、IBSS、MBSS、WDS/DWDS TDMA 以及基于主机接入点的工作模式。所有主机/设备交互通过 DMA 完成。

`ath` 驱动将所有 IP 和 ARP 流量封装为 802.11 帧，但可接收 802.11 或 802.3 帧。发射速率和工作模式可选，具体取决于芯片组。基于 AR5210 的设备支持 802.11a 操作，发射速率为 6 Mbps、9 Mbps、12 Mbps、18 Mbps、24 Mbps、36 Mbps、48 Mbps 和 54 Mbps。基于 AR5211 的设备支持 802.11a 和 802.11b 操作，802.11a 速率同上，802.11b 速率为 1Mbps、2Mbps、5.5 Mbps 和 11Mbps。基于 AR5212 的设备支持 802.11a、802.11b 和 802.11g 操作，各有相应速率。基于 AR5416 及更高类别的设备可进行 802.11n 操作。大多数芯片还支持 Atheros Turbo 模式（TM），该模式在 5GHz 频段运行，发射速率为两倍。部分芯片还支持在 2.4GHz 频段配合 802.11g 的 Turbo 模式，但由于法规要求，目前未提供此支持。（注意，Turbo 模式仅能与其他基于 Atheros 的设备互操作。）基于 AR5212 和 AR5416 的设备还支持半宽（10MHz）和四分之一宽（5MHz）信道。实际使用的发射速率取决于信号质量和驱动采用的“速率控制”算法。所有芯片均支持 WEP 加密。AR5212、AR5416 及更高版本的部件具有 WPA 所需的 AES-CCM、TKIP 和 Michael 加密操作的硬件支持。要启用加密，请按如下所示使用 [ifconfig(8)](../man8/ifconfig.8.md)。

该驱动支持 `station`、`adhoc`、`adhoc-demo`、`hostap`、`mesh`、`wds` 和 `monitor` 模式操作。对于使用 5212 或更高版本部件的卡，可配置多个 `hostap` 虚拟接口以同时使用。当配置多个接口时，每个接口可有独立的 MAC 地址，该地址通过设置底层设备所分配 MAC 地址中的 U/L 位形成。任意数量的 `wds` 虚拟接口可与 `hostap` 接口一同配置。多个 `station` 接口可与 `hostap` 接口一起运行，以构建无线中继设备。当编译时启用 `options IEEE80211_SUPPORT_TDMA`（同时启用所需的 802.11 支持）时，该驱动还支持 `tdma` 操作。有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

`ath` 驱动支持的设备有 Cardbus、ExpressCard、Mini-PCI 和 Mini-PCIe 封装形式。Cardbus 和 ExpressCard 插槽中的无线卡可即时插入和弹出。

## 硬件

`ath` 驱动支持所有 Atheros Cardbus、ExpressCard、PCI 和 PCIe 卡，但基于 AR5005VL 芯片组的卡除外。

## 实例

加入使用 WEP 加密的指定 BSS 网络：

```sh
ifconfig wlan0 create wlandev ath0
ifconfig wlan0 inet 192.168.0.20 netmask 0xffffff00 ssid my_net \
	wepmode on wepkey 0x8736639624
```

加入/创建网络名称为“`my_net`”的 802.11b IBSS 网络：

```sh
ifconfig wlan0 create wlandev ath0 wlanmode adhoc
ifconfig wlan0 inet 192.168.0.22 netmask 0xffffff00 ssid my_net \
	mode 11b
```

创建 802.11g 基于主机的接入点：

```sh
ifconfig wlan0 create wlandev ath0 wlanmode hostap
ifconfig wlan0 inet 192.168.0.10 netmask 0xffffff00 ssid my_ap \
	mode 11g
```

创建 802.11a mesh 站：

```sh
ifconfig wlan0 create wlandev ath0 wlanmode mesh
ifconfig wlan0 meshid my_mesh mode 11a inet 192.168.0.10/24
```

创建两个虚拟 802.11a 基于主机的接入点，一个启用 WEP，一个无安全设置，并将它们桥接到 fxp0（有线）设备：

```sh
ifconfig wlan0 create wlandev ath0 wlanmode hostap \
	ssid paying-customers wepmode on wepkey 0x1234567890 \
	mode 11a up
ifconfig wlan1 create wlandev ath0 wlanmode hostap bssid \
	ssid freeloaders up
ifconfig bridge0 create addm wlan0 addm wlan1 addm fxp0 up
```

在配置为使用 2.5 毫秒时隙的双时隙 TDMA BSS 中创建主节点：

```sh
ifconfig wlan0 create wlandev ath0 wlanmode tdma \
	ssid tdma-test tmdaslot 0 tdmaslotlen 2500 \
	channel 36 up
```

## 诊断

- ath%d: unable to attach hardware; HAL status %u：Atheros 硬件访问层无法按请求配置硬件。状态码在 HAL 包含文件 `sys/dev/ath/ath_hal/ah.h` 中有解释。
- ath%d: failed to allocate descriptors: %d：驱动无法为发送和接收描述符分配连续内存。通常表明系统内存不足和/或碎片化。
- ath%d: unable to setup a data xmit queue!：向 HAL 设置普通数据帧发送队列的请求失败。不应发生此情况。
- ath%d: unable to setup a beacon xmit queue!：向 HAL 设置 802.11 信标帧发送队列的请求失败。不应发生此情况。
- ath%d: 802.11 address: %s：显示烧录在 EEPROM 中的 MAC 地址。
- ath%d: hardware error; resetting：硬件发生不可恢复的错误。此类错误包括不可恢复的 DMA 错误。驱动将重置硬件并继续。
- ath%d: rx FIFO overrun; resetting：硬件中的接收 FIFO 在数据传输到主机之前溢出。通常由于硬件接收描述符不足、无处存放接收数据所致。驱动将重置硬件并继续。
- ath%d: unable to reset hardware; hal status %u：Atheros 硬件访问层无法按请求重置硬件。状态码在 HAL 包含文件 `sys/dev/ath/ath_hal/ah.h` 中有解释。不应发生此情况。
- ath%d: unable to start recv logic：驱动无法重新启动帧接收。不应发生此情况。
- ath%d: device timeout：分发到硬件进行发送的帧未及时完成。驱动将重置硬件并继续。不应发生此情况。
- ath%d: bogus xmit rate 0x%x：为 outgoing 帧指定的发送速率无效。该帧被丢弃。不应发生此情况。
- ath%d: ath_chan_set: unable to reset channel %u (%u MHz)：扫描过程中切换信道时 Atheros 硬件访问层无法重置硬件。不应发生此情况。
- ath%d: failed to enable memory mapping：驱动无法启用对 PCI 设备寄存器的内存映射 I/O。不应发生此情况。
- ath%d: failed to enable bus mastering：驱动无法将设备启用为 PCI 总线主控以进行 DMA。不应发生此情况。
- ath%d: cannot map register space：驱动无法将设备寄存器映射到主机地址空间。不应发生此情况。
- ath%d: could not map interrupt：驱动无法为设备中断分配 IRQ。不应发生此情况。
- ath%d: could not establish interrupt：驱动无法安装设备中断处理程序。不应发生此情况。

## 参见

[ath_hal(4)](ath_hal.4.md), [cardbus(4)](cardbus.4.md), [intro(4)](intro.4.md), [wlan(4)](wlan.4.md), [wlan_ccmp(4)](wlan_ccmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md), [wlan_wep(4)](wlan_wep.4.md), [wlan_xauth(4)](wlan_xauth.4.md), hostapd(8), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 历史

`ath` 设备驱动首次出现于 FreeBSD 5.2。

## 注意事项

D-LINK DWL-G520 和 DWL-G650 的 A1 修订版基于 Intersil PrismGT 芯片，不受此驱动支持。

## 缺陷

该驱动支持可选的 station 模式省电操作。

AR5210 只能在硬件中执行 WEP；因此为允许 TKIP 和 CCMP 的软件实现正常运行，禁用了硬件辅助 WEP。可通过修改驱动重新启用硬件 WEP。
