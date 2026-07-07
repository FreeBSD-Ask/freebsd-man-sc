# iwn(4)

`iwn` — Intel IEEE 802.11n 无线网络驱动

## 名称

`iwn`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device iwn
> device pci
> device wlan
> device firmware

`你还需要为设备选择固件。从以下选项中选择：`

> device iwn1000fw
> device iwn100fw
> device iwn105fw
> device iwn135fw
> device iwn2000fw
> device iwn2030fw
> device iwn4965fw
> device iwn5000fw
> device iwn5150fw
> device iwn6000fw
> device iwn6000g2afw
> device iwn6000g2bfw
> device iwn6050fw

`或者你可以使用`

> device iwnfw

`来包含全部。`

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_iwn_load="YES"
iwn1000fw_load="YES"
iwn100fw_load="YES"
iwn105fw_load="YES"
iwn135fw_load="YES"
iwn2000fw_load="YES"
iwn2030fw_load="YES"
iwn4965fw_load="YES"
iwn5000fw_load="YES"
iwn5150fw_load="YES"
iwn6000fw_load="YES"
iwn6000g2afw_load="YES"
iwn6000g2bfw_load="YES"
iwn6050fw_load="YES"
```

## 描述

`iwn` 驱动支持 `station` 和 `monitor` 模式操作。任何时候只能配置一个虚拟接口。有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

此驱动需要使用 `iwnfw` 模块构建的固件才能工作。

## 硬件

`iwnfw` 驱动为以下设备提供支持：

- Intel Centrino Advanced-N 6200
- Intel Centrino Advanced-N 6205
- Intel Centrino Advanced-N 6230
- Intel Centrino Advanced-N 6235
- Intel Centrino Advanced-N + WiMAX 6250
- Intel Centrino Ultimate-N 6300
- Intel Centrino Wireless-N 100
- Intel Centrino Wireless-N 105
- Intel Centrino Wireless-N 130
- Intel Centrino Wireless-N 135
- Intel Centrino Wireless-N 1000
- Intel Centrino Wireless-N 1030
- Intel Centrino Wireless-N 2200
- Intel Centrino Wireless-N 2230
- Intel Centrino Wireless-N 4965
- Intel Centrino Wireless-N 5100
- Intel Centrino Wireless-N 6150
- Intel Centrino Wireless-N 6200
- Intel Centrino Wireless-N 6250
- Intel Centrino Wireless-N + WiMAX 6150
- Intel Ultimate N WiFi Link 5300
- Intel Wireless WiFi Link 4965
- Intel WiFi Link 5100
- Intel WiMAX/WiFi Link 5150
- Intel WiMAX/WiFi Link 5350

## 实例

加入现有 BSS 网络（即连接到接入点）：

```sh
# ifconfig wlan create wlandev iwn0 inet 192.168.0.20 e
    netmask 0xffffff00
```

加入网络名称为 `my_net` 的特定 BSS 网络：

```sh
# ifconfig wlan create wlandev iwn0 ssid my_net up
```

加入使用 64 位 WEP 加密的特定 BSS 网络：

```sh
# ifconfig wlan create wlandev iwn0 ssid my_net e
	wepmode on wepkey 0x1234567890 weptxkey 1 up
```

加入使用 128 位 WEP 加密的特定 BSS 网络：

```sh
# ifconfig wlan create wlandev iwn0 wlanmode adhoc ssid my_net e
    wepmode on wepkey 0x01020304050607080910111213 weptxkey 1
```

## 诊断

- iwn%d: device timeout 驱动将重置硬件。这不应发生。
- iwn%d: firmware error 板载微控制器因某种原因崩溃。驱动将重置硬件。这不应发生。
- iwn%d: timeout waiting for firmware initialization to complete 板载微控制器未能及时初始化。这不应发生。
- iwn%d: could not load firmware image '%s' 驱动无法使用 [firmware(9)](../man9/firmware.9.md) 子系统加载固件映像。请验证 [iwnfw(4)](iwnfw.4.md) 固件模块存在。
- iwn%d: could not load boot firmware 尝试将引导固件映像上传到板载微控制器失败。这不应发生。
- iwn%d: could not load microcode 尝试将微代码映像上传到板载微控制器失败。这不应发生。
- iwn%d: could not load main firmware 尝试将主固件映像上传到板载微控制器失败。这不应发生。

## 参见

[iwnfw(4)](iwnfw.4.md), [pci(4)](pci.4.md), [wlan(4)](wlan.4.md), [wlan_ccmp(4)](wlan_ccmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md), [wlan_wep(4)](wlan_wep.4.md), [networking(7)](../man7/networking.7.md), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 作者

原始 `iwnfw` 驱动由 Damien Bergamini <damien.bergamini@free.fr> 编写。
