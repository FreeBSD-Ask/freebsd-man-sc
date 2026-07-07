# igc(4)

`igc` — Intel Ethernet Controller I225 2.5GbE 驱动

## 名称

`igc`

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device iflib
> device igc

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_igc_load="YES"
```

## 描述

`igc` 驱动为基于 Intel I225 Multi Gigabit 控制器的任何 PCI Express 适配器或 LOM（LAN On Motherboard）提供支持。该驱动支持发送/接收校验和卸载、Jumbo Frames、MSI/MSI-X、TSO 和 RSS。

通过接口 MTU 设置提供对 Jumbo Frames 的支持。使用 [ifconfig(8)](../man8/ifconfig.8.md) 实用程序选择大于 1500 字节的 MTU 可配置适配器收发 Jumbo Frames。Jumbo Frames 的最大 MTU 大小为 9216 字节。

此驱动版本支持 VLAN 硬件插入/提取以及 VLAN 校验和卸载。有关启用 VLAN 的信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。`igc` 驱动支持以下介质类型：

**`autoselect`** 启用速度和双工的自动协商。

**`10baseT/UTP`** 设置 10Mbps 操作。使用 `mediaopt` 选项选择 `half-duplex` 模式。

**`100baseTX`** 设置 100Mbps 操作。使用 `mediaopt` 选项选择 `half-duplex` 模式。

**`1000baseT`** 设置 1000Mbps 操作。此速度下仅支持 `full-duplex` 模式。

**`2500baseT`** 设置 2500Mbps 操作。此速度下仅支持 `full-duplex` 模式。

## 硬件

`igc` 驱动支持以下 2.5Gb 以太网控制器：

- I220-V
- I221-V
- I225-LM
- I225-LMvP(2)
- I225-V
- I225-IT, I225-IT(2)
- I225-K, I225-K(2)
- I226-LM
- I226-LMvP
- I226-V
- I226-IT
- I226-K

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`hw.igc.igc_disable_crc_stripping`** 禁用或启用硬件剥离 CRC 字段。这在 BMC/IPMI 共享接口上特别有用，因为剥离 CRC 会导致通过 IPMI 的远程访问失败。默认为 0（启用）。

**`hw.igc.sbp`** 在混杂模式下显示坏包。默认为 false。

**`hw.igc.eee_setting`** 禁用或启用 Energy Efficient Ethernet。默认为 1（禁用）。

**`hw.igc.max_interrupt_rate`** 每秒最大设备中断数。默认为 8000。

## 诊断

- igc%d: Hardware Initialization Failed 发生了致命的初始化错误。
- igc%d: Unable to allocate bus resource: memory 发生了致命的初始化错误。
- igc%d: Invalid MAC address 烧录到 EEPROM 中的 MAC 地址为空或为多播/广播地址。

## 参见

[altq(4)](altq.4.md), arp(4), [iflib(4)](iflib.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`igc` 设备驱动最早出现于 FreeBSD 13.1。

## 作者

`igc` 最初由 Intel Corporation 编写，并由 Netgate 转换为 [iflib(4)](iflib.4.md) 框架。
