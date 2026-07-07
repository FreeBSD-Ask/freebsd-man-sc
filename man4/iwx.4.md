# iwx(4)

`iwx` — Intel Wi-Fi 6 IEEE 802.11ax 无线网络驱动

## 名称

`iwx`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device iwx
> device pci
> device wlan

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_iwx_load="YES"
```

## 描述

`iwx` 驱动支持 Intel Wi-Fi 6 系列 M.2 无线网络适配器。如果检测到相应硬件且 [iwlwifi(4)](iwlwifi.4.md) 已在 [rc.conf(5)](../man5/rc.conf.5.md) 中被列入黑名单，该驱动将通过 [devmatch(8)](../man8/devmatch.8.md) 自动加载。`iwx` 驱动可在运行时使用 [ifconfig(8)](../man8/ifconfig.8.md) 配置，或在引导时使用 [rc.conf(5)](../man5/rc.conf.5.md) 配置。

以下是 `iwx` 驱动可操作的模式：

**station** 模式 用于与接入点关联，所有流量通过接入点传输。此模式支持后台扫描，参见 [ifconfig(8)](../man8/ifconfig.8.md)。station 模式为默认。

**monitor** 模式 在此模式下，驱动可在不与接入点关联的情况下接收数据包。这会禁用内部接收过滤器，使网卡能够捕获通常无法访问的网络中的数据包，或扫描接入点。

## 硬件

`iwx` 驱动支持以下 M.2 无线网络适配器：

- Intel Wi-Fi 6 AX200
- Intel Wi-Fi 6 AX201 CNVi
- Intel Wi-Fi 6 AX210
- Intel Wi-Fi 6 AX211 CNVi

## SYSCTL 变量

`iwx` 驱动支持以下 [sysctl(8)](../man8/sysctl.8.md) 变量：

**`dev.iwx.?.debug`** 以位掩码指定调试级别。默认为 `0`。

## 文件

`iwx` 驱动需要 `ports/net/wifi-firmware-iwlwifi-kmod` 中的固件。如果安装或运行时检测到相应硬件，此固件包将通过 fwget(8) 自动安装。

## 诊断

- iwx0: device timeout 分派到硬件进行传输的帧未及时完成。驱动将重置硬件。这不应发生。
- iwx0: fatal firmware error 固件因某种原因崩溃。驱动将重置硬件。这不应发生。
- iwx0: radio is disabled by hardware switch 无线电发射器关闭，因此无法发送任何数据包。驱动将重置硬件。确保笔记本电脑无线电开关已打开。
- iwx0: could not read firmware ... (error N) 由于某种原因，驱动无法从文件系统读取固件映像。文件可能缺失或损坏。
- iwx0: firmware too short: N bytes 固件映像已损坏，无法加载到适配器。
- iwx0: could not load firmware 尝试将固件加载到适配器失败。驱动将重置硬件。

## 参见

[intro(4)](intro.4.md), [iwlwifi(4)](iwlwifi.4.md), [iwlwififw(4)](iwlwififw.4.md), [wlan(4)](wlan.4.md), [networking(7)](../man7/networking.7.md), fwget(8), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 历史

`iwx` 驱动出现于 FreeBSD 15.0。

## 注意事项

`iwx` 驱动不支持硬件加密卸载。

`iwx` 驱动不支持 802.11ax。在 [ieee80211(9)](../man9/ieee80211.9.md) 中需要额外工作才能支持这些功能。
