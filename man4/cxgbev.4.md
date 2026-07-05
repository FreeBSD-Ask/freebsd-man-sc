# cxgbev.4

`cxgbev` — 基于 Chelsio T4、T5 和 T6 的 100Gb、40Gb、25Gb、10Gb 和 1Gb 以太网 VF 驱动

## 名称

`cxgbev`

## 概要

`若要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device cxgbe
> device cxgbev

`若要在引导时以模块方式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_cxgbev_load="YES"
```

## 描述

`cxgbev` 驱动为基于 Chelsio Terminator 4、Terminator 5 和 Terminator 6 ASIC（T4、T5 和 T6）的 PCI Express 以太网适配器上的虚拟功能（Virtual Function）提供支持。该驱动支持 Jumbo 帧、发送/接收校验和卸载、TCP 分段卸载（TSO）、大接收卸载（LRO）、VLAN 标签插入/提取、VLAN 校验和卸载、VLAN TSO 以及接收侧导向（RSS）。有关进一步的硬件信息和硬件要求相关问题，请参见 `http://www.chelsio.com/`。

`cxgbev` 驱动根据关联的 ASIC 为设备使用不同的名称：

| **ASIC** | **端口名称** | **父设备** |
| -------- | ------------ | ---------- |
| T4 | cxgbev | t4vf |
| T5 | cxlv | t5vf |
| T6 | ccv | t6vf |

带有 hw.cxgbe 前缀的 loader 可调参数适用于所有网卡的 VF。Chelsio Terminator 适配器的物理功能（Physical Function）驱动共享这些可调参数。该驱动使用上述名称为端口和父设备提供 sysctl MIB。例如，T5 VF 在 dev.cxlv 下提供端口 MIB，在 dev.t5vf 下提供父设备 MIB。本页其余部分对 sysctl MIB 的引用中，使用 dev.<port> 表示端口 MIB，使用 dev.<nexus> 表示父设备 MIB。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`cxgbev` 驱动支持基于 T6 ASIC 的 100Gb 和 25Gb 以太网适配器上的虚拟功能：

- Chelsio T6225-CR
- Chelsio T6225-SO-CR
- Chelsio T62100-LP-CR
- Chelsio T62100-SO-CR
- Chelsio T62100-CR

`cxgbev` 驱动支持基于 T5 ASIC 的 40Gb、10Gb 和 1Gb 以太网适配器上的虚拟功能：

- Chelsio T580-CR
- Chelsio T580-LP-CR
- Chelsio T580-LP-SO-CR
- Chelsio T560-CR
- Chelsio T540-CR
- Chelsio T540-LP-CR
- Chelsio T522-CR
- Chelsio T520-LL-CR
- Chelsio T520-CR
- Chelsio T520-SO
- Chelsio T520-BT
- Chelsio T504-BT

`cxgbev` 驱动支持基于 T4 ASIC 的 10Gb 和 1Gb 以太网适配器上的虚拟功能：

- Chelsio T420-CR
- Chelsio T422-CR
- Chelsio T440-CR
- Chelsio T420-BCH
- Chelsio T440-BCH
- Chelsio T440-CH
- Chelsio T420-SO
- Chelsio T420-CX
- Chelsio T420-BT
- Chelsio T404-BT

## LOADER 可调参数

可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符处设置可调参数，或将其存储在 loader.conf(5) 中。

**`hw.cxgbe.ntxq`** 用于端口的发送队列数。默认为 16 或系统中的 CPU 核心数，取较小者。

**`hw.cxgbe.nrxq`** 用于端口的接收队列数。默认为 8 或系统中的 CPU 核心数，取较小者。

**`hw.cxgbe.holdoff_timer_idx`** 用于延迟中断的定时器索引值。holdoff 定时器列表默认具有 1、5、10、50、100 和 200 这些值（所有值均以微秒为单位），索引从该列表中选择一个值。默认值为 1，即定时器值为 5us。可通过 dev.<port>.X.holdoff_tmr_idx sysctl 随时为不同接口分配不同的值。

**`hw.cxgbe.holdoff_pktc_idx`** 用于延迟中断的数据包计数索引值。数据包计数列表默认具有 1、8、16 和 32 这些值，索引从该列表中选择一个值。默认值为 -1，表示禁用数据包计数，中断仅根据 holdoff 定时器值生成。可通过 dev.<port>.X.holdoff_pktc_idx sysctl 为不同接口分配不同的值。此 sysctl 仅在接口从未被标记为 up（由 ifconfig up 完成）时才有效。

**`hw.cxgbe.qsize_txq`** 发送队列描述符环中的项数。同时还会分配相同大小的 buf_ring 用于额外的软件排队。参见 [ifnet(9)](../man9/ifnet.9.md)。默认值为 1024。可通过 dev.<port>.X.qsize_txq sysctl 为不同接口分配不同的值。此 sysctl 仅在接口从未被标记为 up 时才有效。

**`hw.cxgbe.qsize_rxq`** 接收队列描述符环中的项数。默认值为 1024。可通过 dev.<port>.X.qsize_rxq sysctl 为不同接口分配不同的值。此 sysctl 仅在接口从未被标记为 up 时才有效。

**`hw.cxgbe.interrupt_types`** 允许的中断类型。位 0 表示 INTx（线中断），位 1 表示 MSI，位 2 表示 MSI-X。默认为 7（全部允许）。驱动从允许的类型中选择最佳类型。注意，虚拟功能不支持 INTx 中断，如果 MSI 和 MSI-X 均未启用，则附加失败。

**`hw.cxgbe.fl_pktshift`** 在接收缓冲区中以太网帧起始之前插入的填充字节数。默认值为 2，可确保以太网负载（通常为 IP 头）位于 4 字节对齐的地址。0-7 均为有效值。

**`hw.cxgbe.fl_pad`** 非零值确保硬件向接收缓冲区的写入填充到指定边界。默认为 -1，由驱动选择填充边界。0 完全禁用尾部填充。

**`hw.cxgbe.buffer_packing`** 允许硬件机会性地在同一接收缓冲区中交付多个帧。默认为 -1，由驱动决定。0 或 1 显式禁用或启用此功能。

**`hw.cxgbe.allow_mbufs_in_cluster`** 设为 1 允许驱动机会性地在接收缓冲区中放置一个或多个 mbuf。这是默认行为。0 禁止驱动这样做。

**`hw.cxgbe.largest_rx_cluster`**

**`hw.cxgbe.safest_rx_cluster`** 接收簇的大小。每个都必须设置为可用大小之一（通常为 2048、4096、9216 和 16384），且 largest_rx_cluster 必须大于或等于 safest_rx_cluster。默认分别为 16384 和 4096。驱动从不尝试分配大于 largest_rx_cluster 的接收缓冲区，如果分配大于 safest_rx_cluster 的缓冲区失败，则回退到分配 safest_rx_cluster 大小的缓冲区。注意 largest_rx_cluster 仅设定上限——允许驱动分配更小大小的缓冲区。

虚拟功能的某些设置和资源由父物理功能驱动决定。例如，物理功能驱动限制虚拟功能可用的队列数。其中一些限制可在与物理功能驱动一起使用的固件配置文件中调整。

虚拟功能端口的 PAUSE 设置继承自物理功能上同一端口的设置。虚拟功能无法修改该设置，但会跟踪物理功能驱动对关联端口设置所做的更改。

虚拟功能上的接收队列在响应拥塞时总是丢弃数据包（等效于将 `hw.cxgbe.cong_drop` 设为 1）。

VF 驱动当前依赖于 PF 驱动。因此，加载 VF 驱动时也会作为依赖项加载 PF 驱动。

## 支持

有关一般信息和支持，请访问 Chelsio 支持网站：`http://www.chelsio.com/`。

如果在使用受支持适配器时发现此驱动的问题，请将与该问题相关的所有具体信息通过电子邮件发送至 <support@chelsio.com>。

## 参见

arp(4), [cxgbe(4)](cxgbe.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`cxgbev` 设备驱动首次出现于 FreeBSD 11.1 和 FreeBSD 11.1。

## 作者

`cxgbev` 驱动由 Navdeep Parhar <np@FreeBSD.org> 和 John Baldwin <jhb@FreeBSD.org> 编写。
