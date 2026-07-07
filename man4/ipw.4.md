# ipw(4)

`ipw` — Intel PRO/Wireless 2100 IEEE 802.11a/b 驱动

## 名称

`ipw`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device ipw
> device ipwfw
> device pci
> device wlan
> device firmware

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_ipw_load="YES"
```

无论哪种情况，请在 loader.conf(5) 中加入以下行以确认接受固件许可（见下文）：

```sh
legal.intel_ipw.license_ack=1
```

## 描述

`ipw` 驱动为 Intel PRO/Wireless 2100 802.11a/b 无线网络设备提供支持，可在 `station`、`adhoc` 和 `monitor` 模式下运行。任何时候只能配置一个虚拟接口。

此驱动需要使用 `ipwfw` 模块构建的固件才能工作。要启用已加载固件的使用，必须通过在 loader.conf(5) 中加入以下行来同意 **/usr/share/doc/legal/intel_ipw.LICENSE** 中的许可：

```sh
legal.intel_ipw.license_ack=1
```

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`ipwfw` 驱动支持 Intel PRO/Wireless 2100a/b MiniPCI 网络适配器。

## 文件

**`/usr/share/doc/legal/intel_ipw.LICENSE`** `ipwfw` 固件许可

## 实例

加入现有 BSS 网络（即连接到接入点）：

```sh
ifconfig wlan create wlandev ipw0 inet 192.0.2.20/24
```

加入网络名称为 `my_net` 的特定 BSS 网络：

```sh
ifconfig wlan create wlandev ipw0 ssid my_net up
```

加入使用 64 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev ipw0 ssid my_net e
    wepmode on wepkey 0x1234567890 weptxkey 1 up
```

加入使用 128 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev ipw0 wlanmode adhoc ssid my_net e
    wepmode on wepkey 0x01020304050607080910111213 weptxkey 1
```

## 诊断

- ipw%d: device timeout 驱动将重置硬件。这不应发生。
- ipw%d: firmware error 板载微控制器因某种原因崩溃。驱动将重置硬件。这不应发生。
- ipw%d: timeout waiting for firmware initialization to complete 板载微控制器未能在时间内初始化。这不应发生。
- ipw%d: could not load firmware image '%s' 驱动无法使用 [firmware(9)](../man9/firmware.9.md) 子系统加载固件映像。验证 [ipwfw(4)](ipwfw.4.md) 固件模块已安装且许可协议 [loader(8)](../man8/loader.8.md) 可调参数已设置。
- ipw%d: could not load microcode 尝试将微代码映像上传到板载微控制器失败。这不应发生。
- ipw%d: could not load firmware 尝试将固件映像上传到板载微控制器失败。这不应发生。

## 参见

[ipwfw(4)](ipwfw.4.md), [pci(4)](pci.4.md), [wlan(4)](wlan.4.md), [wlan_ccmp(4)](wlan_ccmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md), [wlan_wep(4)](wlan_wep.4.md), [networking(7)](../man7/networking.7.md), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 作者

原始 `ipwfw` 驱动由 Damien Bergamini <damien.bergamini@free.fr> 编写。
