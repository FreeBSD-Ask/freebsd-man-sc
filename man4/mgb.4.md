# mgb.4

`mgb` — Microchip LAN743x PCIe 千兆以太网驱动

## 名称

`mgb`

## 概要

要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_mgb_load="YES"
```

## 描述

`mgb` 驱动是实验性的，存在许多限制和注意事项。它目前仅作为内核模块提供。

`mgb` 设备驱动提供对基于 Microchip LAN7430 和 LAN7431 的 PCIe 千兆以太网适配器的支持。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`mgb` 驱动支持 Microchip PCIe 千兆以太网接口，包括：

- 带有 PHY 的 Microchip LAN7430 PCIe 千兆以太网控制器
- 带有 RGMII 接口的 Microchip LAN7431 PCIe 千兆以太网控制器

## 参见

arp(4), [miibus(4)](miibus.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 注意事项

此驱动尚未实现对许多硬件功能的支持，包括：

- 多 RX 队列支持
- RX 和 TX 校验和卸载
- 硬件 VLAN 标记添加或去除
- 多播接收数据包过滤
- 局域网唤醒（WoL）
- LSO
- RSS

LAN7431 支持完全未经测试。
