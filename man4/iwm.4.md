# iwm.4

`iwm` — Intel IEEE 802.11ac 无线网络驱动

## 名称

`iwm`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device iwm
> device pci
> device wlan
> device firmware

`你还需要为设备选择固件。从以下选项中选择：`

> device iwm3160fw
> device iwm3168fw
> device iwm7260fw
> device iwm7265fw
> device iwm7265Dfw
> device iwm8000Cfw
> device iwm8265fw
> device iwm9000fw
> device iwm9260fw

`或者你可以使用`

> device iwmfw

`来包含全部。`

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_iwm_load="YES"
iwm3160fw_load="YES"
iwm3168fw_load="YES"
iwm7260fw_load="YES"
iwm7265fw_load="YES"
iwm7265Dfw_load="YES"
iwm8000Cfw_load="YES"
iwm8265fw_load="YES"
iwm9000fw_load="YES"
iwm9260fw_load="YES"
```

## 描述

`iwm` 驱动支持以 `station` 模式运行大多数 Intel Wireless AC 系列网络设备。任何时候只能配置一个虚拟接口。此驱动需要使用 [iwmfw(4)](iwmfw.4.md) 模块构建的固件才能工作。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`iwm` 驱动支持以下 PCIe Wi-Fi 设备：

- Intel Dual Band Wireless AC 3160
- Intel Dual Band Wireless AC 3165
- Intel Dual Band Wireless AC 3168
- Intel Dual Band Wireless AC 7260
- Intel Dual Band Wireless AC 7265
- Intel Dual Band Wireless AC 8260
- Intel Dual Band Wireless AC 8265
- Intel Dual Band Wireless AC 9260
- Intel Dual Band Wireless AC 9270
- Intel Dual Band Wireless AC 946X
- Intel Dual Band Wireless AC 9560

## 实例

加入现有 BSS 网络（即连接到接入点）：

```sh
ifconfig wlan create wlandev iwm0 inet 192.0.2.20/24
```

加入网络名称为 `my_net` 的特定 BSS 网络：

```sh
ifconfig wlan create wlandev iwm0 ssid my_net up
```

加入使用 64 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev iwm0 ssid my_net e
    wepmode on wepkey 0x1234567890 weptxkey 1 up
```

加入使用 128 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev iwm0 wlanmode adhoc ssid my_net e
    wepmode on wepkey 0x01020304050607080910111213 weptxkey 1
```

## 诊断

- iwm%d: device timeout 驱动将重置硬件。这不应发生。
- iwm%d: firmware error 板载微控制器因某种原因崩溃。驱动将重置硬件。这不应发生。
- iwm%d: timeout waiting for firmware initialization to complete 板载微控制器未能及时初始化。这不应发生。
- iwm%d: could not load firmware image '%s' 驱动无法使用 [firmware(9)](../man9/firmware.9.md) 子系统加载固件映像。请验证 [iwmfw(4)](iwmfw.4.md) 固件模块存在。
- iwm%d: could not load boot firmware 尝试将引导固件映像上传到板载微控制器失败。这不应发生。
- iwm%d: could not load microcode 尝试将微代码映像上传到板载微控制器失败。这不应发生。
- iwm%d: could not load main firmware 尝试将主固件映像上传到板载微控制器失败。这不应发生。

## 参见

[iwlwifi(4)](iwlwifi.4.md), [iwmfw(4)](iwmfw.4.md), [pci(4)](pci.4.md), [wlan(4)](wlan.4.md), [wlan_ccmp(4)](wlan_ccmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md), [wlan_wep(4)](wlan_wep.4.md), [networking(7)](../man7/networking.7.md), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 缺陷

目前，`iwm` 仅支持 802.11a/b/g 模式。它不会关联到配置为仅在 802.11n/ac 模式下操作的接入点。
