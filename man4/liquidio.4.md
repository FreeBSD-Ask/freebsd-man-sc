# liquidio.4

`liquidio` — Cavium 10Gb/25Gb 以太网驱动

## 名称

`liquidio`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device lio

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_lio_load="YES"
```

## 描述

`liquidio` 驱动提供对 23XX 10Gb/25Gb 以太网适配器的支持。该驱动支持 Jumbo 帧、发送/接收校验和卸载、TCP 分段卸载（TSO）、大接收卸载（LRO）、VLAN 标签插入/提取、VLAN 校验和卸载、VLAN TSO 以及接收侧引导（RSS）。

通过接口 MTU 设置提供对 Jumbo 帧的支持。使用 [ifconfig(8)](../man8/ifconfig.8.md) 工具选择大于 1500 字节的 MTU 时，将配置适配器收发 Jumbo 帧。Jumbo 帧的最大 MTU 为 16000。

有关此设备配置的更多信息，请参见 ifconfig(8)。

## 硬件

`liquidio` 驱动支持以下网卡：

- LiquidIO II CN2350 210SV/225SV
- LiquidIO II CN2360 210SV/225SV

## 加载器可调参数

可在引导内核前在 [loader(8)](../man8/loader.8.md) 提示符处设置可调参数，或将其存储在 loader.conf(5) 中。

**`hw.lio.fw_type`** 字符串，指定要加载的固件类型。默认为 "nic"。使用 "none" 则从闪存加载固件。

**`hw.lio.num_queues_per_pf0`** 无符号整数，指定每个 PF0 的队列数。有效范围为 0 到 64。设为 0 表示根据 CPU 数量自动配置，最大为 8。

**`hw.lio.num_queues_per_pf1`** 无符号整数，指定每个 PF1 的队列数。有效范围为 0 到 64。设为 0 表示根据 CPU 数量自动配置，最大为 8。

**`hw.lio.console_bitmask`** 位掩码，指示哪些控制台的调试输出重定向到 syslog。

**`hw.lio.rss`** 启用/禁用驱动 RSS 支持。

**`hw.lio.hwlro`** 启用/禁用硬件 LRO。

## 支持

获取一般信息和支持，请访问 Cavium 支持网站：`http://support.cavium.com`。

## 参见

[altq(4)](altq.4.md), arp(4), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`liquidio` 设备驱动首次出现于 FreeBSD 12.0。

## 作者

`liquidio` 驱动由 Derek Chickles <derek.chickles@cavium.com> 编写。
