# iwi(4)

`iwi` — Intel PRO/Wireless 2200BG/2225BG/2915ABG IEEE 802.11 网络驱动

## 名称

`iwi`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device iwi
> device iwifw
> device pci
> device wlan
> device firmware

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_iwi_load="YES"
```

`无论哪种情况，都需在 loader.conf(5) 中加入以下行以确认接受固件许可（见下文）：`

```sh
legal.intel_iwi.license_ack=1
```

## 描述

`iwi` 驱动为 Intel PRO/Wireless 2200BG/2225BG/2915ABG IEEE 802.11a/b/g 无线网络设备提供支持，支持 `station`、`adhoc` 和 `monitor` 模式操作。任何时候只能配置一个虚拟接口。

此驱动需要使用 `iwifw` 模块构建的固件才能工作。要使加载的固件可供使用，必须在 loader.conf(5) 中加入以下行，表示同意 **/usr/share/doc/legal/intel_iwi.LICENSE** 中的许可：

```sh
legal.intel_iwi.license_ack=1
```

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`iwifw` 驱动支持以下无线网络设备：

- Intel PRO/Wireless 2200BG MiniPCI Network Connection
- Intel PRO/Wireless 2225BG PCI Network Connection
- Intel PRO/Wireless 2915ABG MiniPCI Network Connection

## 文件

**/usr/share/doc/legal/intel_iwi.LICENSE** `iwifw` 固件许可

## 实例

加入现有 BSS 网络（即连接到接入点）：

```sh
ifconfig wlan create wlandev iwi0 inet 192.0.2.20/24
```

加入网络名称为 `my_net` 的特定 BSS 网络：

```sh
ifconfig wlan create wlandev iwi0 ssid my_net up
```

加入使用 64 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev iwi0 ssid my_net e
    wepmode on wepkey 0x1234567890 weptxkey 1 up
```

加入使用 128 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev iwi0 wlanmode adhoc ssid my_net e
    wepmode on wepkey 0x01020304050607080910111213 weptxkey 1
```

## 诊断

- iwi%d: device timeout 驱动将重置硬件。这不应发生。
- iwi%d: firmware error 板载微控制器因某种原因崩溃。驱动将重置硬件。这不应发生。
- iwi%d: timeout waiting for firmware initialization to complete 板载微控制器未能及时初始化。这不应发生。
- iwi%d: could not load firmware image '%s' 驱动无法使用 [firmware(9)](../man9/firmware.9.md) 子系统加载固件映像。请验证 [iwifw(4)](iwifw.4.md) 固件模块已安装，且已设置许可协议的 [loader(8)](../man8/loader.8.md) 可调参数。
- iwi%d: could not load boot firmware 尝试将引导固件映像上传到板载微控制器失败。这不应发生。
- iwi%d: could not load microcode 尝试将微代码映像上传到板载微控制器失败。这不应发生。
- iwi%d: could not load main firmware 尝试将主固件映像上传到板载微控制器失败。这不应发生。

## 参见

[iwifw(4)](iwifw.4.md), [pci(4)](pci.4.md), [wlan(4)](wlan.4.md), [wlan_ccmp(4)](wlan_ccmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md), [wlan_wep(4)](wlan_wep.4.md), [networking(7)](../man7/networking.7.md), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 作者

原始 `iwifw` 驱动由 Damien Bergamini <damien.bergamini@free.fr> 编写。
