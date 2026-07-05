# wpi.4

`wpi` — Intel PRO/Wireless 3945ABG IEEE 802.11a/b/g 网络驱动

## 名称

`wpi`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device wpi
> device wpifw
> device pci
> device wlan
> device wlan_amrr
> device firmware

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_wpi_load="YES"
```

## 描述

`wpi` 驱动支持以 `station`、`adhoc`、`adhoc-demo`、`hostap` 和 `monitor` 模式运行 Intel PRO/Wireless 3945ABG 网络适配器。此驱动需要 wpifw 固件模块，可在运行时使用 [ifconfig(8)](../man8/ifconfig.8.md) 配置，或在引导时通过 [rc.conf(5)](../man5/rc.conf.5.md) 配置。任何时候只能配置一个虚拟接口。

`wpi` 驱动可配置为使用有线等效保密（WEP）或 Wi-Fi 保护访问（WPA-PSK 和 WPA2-PSK）。WPA 是无线网络事实上的加密标准。强烈建议不要将 WEP 作为保障无线通信安全的唯一机制，因为它存在严重弱点。`wpi` 驱动将 CCMP 密码的数据帧加密和解密都卸载到硬件执行。

## 硬件

`wpi` 驱动为 Intel PRO/Wireless 3945ABG Mini PCIe 网络适配器提供支持。

## 文件

**`/usr/share/doc/legal/intel_wpi.LICENSE`** `wpi` 固件许可证

## 实例

加入现有 BSS 网络（即连接到接入点）：

```sh
ifconfig wlan0 create wlandev wpi0 inet 192.168.0.20 \
    netmask 0xffffff00
```

加入具有网络名称 `my_net` 的特定 BSS 网络：

```sh
ifconfig wlan0 create wlandev wpi0 ssid my_net up
```

加入具有 64 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan0 create wlandev wpi0 ssid my_net \
	wepmode on wepkey 0x1234567890 weptxkey 1 up
```

在信道 4 上创建具有 128 位 WEP 加密的 IBSS 网络：

```sh
ifconfig wlan0 create wlandev wpi0 wlanmode adhoc ssid my_net \
	wepmode on wepkey 0x01020304050607080910111213 weptxkey 1 \
	channel 4
```

加入/创建具有网络名称 `my_net` 的 802.11b IBSS 网络：

```sh
ifconfig wlan0 create wlandev wpi0 wlanmode adhoc
ifconfig wlan0 inet 192.168.0.22 netmask 0xffffff00 ssid my_net \
	mode 11b
```

创建基于主机的 802.11g 接入点：

```sh
ifconfig wlan0 create wlandev wpi0 wlanmode hostap
ifconfig wlan0 inet 192.168.0.10 netmask 0xffffff00 ssid my_ap \
	mode 11g
```

## 诊断

- wpi%d: could not load firmware image '%s' 驱动使用 [firmware(9)](../man9/firmware.9.md) 子系统加载固件镜像失败。请验证 wpifw 固件模块是否已安装。
- wpi%d: %s: timeout waiting for adapter to initialize, error %d 板载微控制器未及时初始化。这不应发生。
- wpi%d: %s: could not load boot firmware 尝试将启动固件镜像上传到板载微控制器失败。这不应发生。
- wpi%d: device timeout 分派到硬件进行发送的帧未及时完成。驱动将重置硬件并继续。这不应发生。
- wpi%d: scan timeout 未及时收到固件扫描命令响应。驱动将重置硬件并继续。这不应发生。
- wpi%d: fatal firmware error 板载微控制器由于某种原因崩溃。驱动将重置硬件并继续。这不应发生。
- wpi%d: RF switch: radio disabled 控制射频的硬件开关当前处于关闭状态。在此状态下无法进行数据传输。
- wpi%d: can't map mem space 驱动无法将设备寄存器映射到主机地址空间。这不应发生。
- wpi%d: can't map interrupt 驱动无法为设备中断分配 IRQ。这不应发生。
- wpi%d: can't establish interrupt, error %d 驱动无法安装设备中断处理程序。这不应发生。
- wpi%d: %s: bus_dmamap_load failed, error %d 驱动无法将新分配的 mbuf 映射到设备可见的地址空间。当前接收帧的内容将丢失。这不应发生。

## 参见

[pci(4)](pci.4.md), [wlan(4)](wlan.4.md), [wlan_amrr(4)](wlan_amrr.4.md), [wlan_ccmp(4)](wlan_ccmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md), [wlan_wep(4)](wlan_wep.4.md), [wlan_xauth(4)](wlan_xauth.4.md), [networking(7)](../man7/networking.7.md), hostapd(8), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 作者

原始 `wpi` 驱动由 Damien Bergamini <damien.bergamini@free.fr> 为 OpenBSD 编写。Benjamin Close <benjsc@FreeBSD.org> 将 `wpi` 移植到 FreeBSD。

## 注意事项

设备不直接支持 `Hostap` 模式；它是通过 IBSS 模式实现的（因此在此模式下 DFS/被动信道不可用）。

在某些网络上，Powersave 可能不稳定（导致偶尔出现 **'wpi%d: device timeout'** 消息），你可以尝试禁用它以提高设备稳定性。
