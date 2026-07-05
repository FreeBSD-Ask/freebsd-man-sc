# cxgbe.4

`cxgbe` — 基于 Chelsio T7、T6、T5 和 T4 的 1Gb 至 400Gb 以太网驱动

## 名称

`cxgbe`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device cxgbe

`若要在引导时以模块方式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
t7fw_cfg_load="YES"
t6fw_cfg_load="YES"
t5fw_cfg_load="YES"
t4fw_cfg_load="YES"
if_cxgbe_load="YES"
```

## 描述

`cxgbe` 驱动为基于 Chelsio Terminator 7、Terminator 6、Terminator 5 和 Terminator 4 ASIC（T7、T6、T5 和 T4）的 PCI Express 以太网适配器提供支持。该驱动支持 Jumbo 帧、发送/接收校验和卸载、TCP 分段卸载（TSO）、大接收卸载（LRO）、VLAN 标签插入/提取、VLAN 校验和卸载、VLAN TSO、VXLAN 校验和卸载、VXLAN TSO 以及接收侧导向（RSS）。有关进一步的硬件信息和硬件要求相关问题，请参见 `http://www.chelsio.com/`。

`cxgbe` 驱动根据关联的 ASIC 为设备使用不同的名称：

| **ASIC** | **端口名称** | **父设备** | **虚拟接口** |
| -------- | ------------ | ---------- | ------------ |
| T7 | che | chnex | vche |
| T6 | cc | t6nex | vcc |
| T5 | cxl | t5nex | vcxl |
| T4 | cxgbe | t4nex | vcxgbe |

带有 hw.cxgbe 前缀的 loader 可调参数适用于所有网卡。该驱动使用上述名称为端口和父设备提供 sysctl MIB。例如，T5 适配器在 dev.cxl 下提供端口 MIB，在 dev.t5nex 下提供适配器范围的 MIB。本页其余部分对 sysctl MIB 的引用中，使用 dev.<port> 表示端口 MIB，使用 dev.<nexus> 表示适配器范围的 MIB。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`cxgbe` 驱动支持基于 T7 ASIC 的 400Gb、200Gb、50Gb 和 10Gb 以太网适配器：

- Chelsio S71400
- Chelsio S72200
- Chelsio S72200-OCP
- Chelsio T72200
- Chelsio T72200-DPU
- Chelsio T72200-FH
- Chelsio T72200-FH-DPU
- Chelsio T72200-OCP
- Chelsio S7450-DPU
- Chelsio S7450-OCP
- Chelsio T71200-iNIC
- Chelsio T7250
- Chelsio T7210-BT
- Chelsio T7410-BT-OCP

`cxgbe` 驱动支持基于 T6 ASIC 的 100Gb 和 25Gb 以太网适配器：

- Chelsio T6225-CR
- Chelsio T6225-SO-CR
- Chelsio T62100-LP-CR
- Chelsio T62100-SO-CR
- Chelsio T62100-CR

`cxgbe` 驱动支持基于 T5 ASIC 的 40Gb、10Gb 和 1Gb 以太网适配器：

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

`cxgbe` 驱动支持基于 T4 ASIC 的 10Gb 和 1Gb 以太网适配器：

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

可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符处设置可调参数，或将其存储在 loader.conf(5) 中。有多个可调参数控制各种类型的队列数量。此类可调参数为负值时，指示驱动在可用 CPU 核心足够的情况下创建多达该数量的队列。

**`hw.cxgbe.ntxq`** 用于端口的 NIC 发送队列数。默认为 16 或系统中的 CPU 核心数，取较小者。

**`hw.cxgbe.nrxq`** 用于端口的 NIC 接收队列数。默认为 8 或系统中的 CPU 核心数，取较小者。

**`hw.cxgbe.nofldtxq`** 用于端口的 TOE 发送队列数。默认为 8 或系统中的 CPU 核心数，取较小者。

**`hw.cxgbe.nofldrxq`** 用于端口的 TOE 接收队列数。默认为 2 或系统中的 CPU 核心数，取较小者。

**`hw.cxgbe.num_vis`** 为每个端口创建的虚拟接口（VI）数。每个虚拟接口创建一个独立的网络接口。每个端口上的第一个虚拟接口是必需的，代表该端口上的主网络接口。端口上的其他虚拟接口使用上表中的虚拟接口名称命名。额外的虚拟接口使用一对队列进行接收和发送，并使用一对额外的队列进行 TOE 接收和发送。默认为 1。

**`hw.cxgbe.holdoff_timer_idx`**

**`hw.cxgbe.holdoff_timer_idx_ofld`** 用于延迟中断的定时器索引值。holdoff 定时器列表默认具有 1、5、10、50、100 和 200 这些值（所有值均以微秒为单位），索引从该列表中选择一个值。holdoff_timer_idx_ofld 适用于 TOE 接收使用的队列。默认值为 1，即定时器值为 5us。可通过 dev.<port>.X.holdoff_tmr_idx 和 dev.<port>.X.holdoff_tmr_idx_ofld sysctl 随时为不同接口分配不同的值。

**`hw.cxgbe.holdoff_pktc_idx`**

**`hw.cxgbe.holdoff_pktc_idx_ofld`** 用于延迟中断的数据包计数索引值。数据包计数列表默认具有 1、8、16 和 32 这些值，索引从该列表中选择一个值。holdoff_pktc_idx_ofld 适用于 TOE 接收使用的队列。默认值为 -1，表示禁用数据包计数，中断仅根据 holdoff 定时器值生成。可通过 dev.<port>.X.holdoff_pktc_idx 和 dev.<port>.X.holdoff_pktc_idx_ofld sysctl 为不同接口分配不同的值。这些 sysctl 仅在接口从未被标记为 up（由 ifconfig up 完成）时才有效。

**`hw.cxgbe.qsize_txq`** 发送队列描述符环中的项数。同时还会分配相同大小的 buf_ring 用于额外的软件排队。参见 [ifnet(9)](../man9/ifnet.9.md)。默认值为 1024。可通过 dev.<port>.X.qsize_txq sysctl 为不同接口分配不同的值。此 sysctl 仅在接口从未被标记为 up 时才有效。

**`hw.cxgbe.qsize_rxq`** 接收队列描述符环中的项数。默认值为 1024。可通过 dev.<port>.X.qsize_rxq sysctl 为不同接口分配不同的值。此 sysctl 仅在接口从未被标记为 up 时才有效。

**`hw.cxgbe.interrupt_types`** 允许的中断类型。位 0 表示 INTx（线中断），位 1 表示 MSI，位 2 表示 MSI-X。默认为 7（全部允许）。驱动从允许的类型中选择最佳类型。

**`hw.cxgbe.pcie_relaxed_ordering`** PCIe 宽松排序。-1 表示由驱动决定是否启用 PCIe RO。0 禁用 PCIe RO。1 启用 PCIe RO。2 表示驱动不应修改 PCIe RO 设置。默认为 -1。

**`hw.cxgbe.fw_install`** 0 禁止驱动在网卡上安装固件。1 允许驱动在内部驱动启发式方法认为新固件比网卡上已有固件更可取时安装新固件。2 指示驱动只要新固件与驱动兼容且与网卡上已有版本不同，就总是在网卡上安装新固件。默认为 1。

**`hw.cxgbe.fl_pktshift`** 在接收缓冲区中以太网帧起始之前插入的填充字节数。默认值为 0。值为 2 可确保以太网负载（通常为 IP 头）位于 4 字节对齐的地址。0-7 均为有效值。

**`hw.cxgbe.fl_pad`** 非零值确保硬件向接收缓冲区的写入填充到指定边界。默认为 -1，由驱动选择填充边界。0 完全禁用尾部填充。

**`hw.cxgbe.cong_drop`** 控制硬件对拥塞的响应。-1 禁用拥塞反馈，不推荐使用。0 指示硬件在拥塞时对其流水线进行反压。这通常会导致端口发出 PAUSE 帧。1 指示硬件丢弃发往拥塞队列的帧。2 指示硬件既对流水线反压又丢弃帧。

**`hw.cxgbe.pause_settings`** PAUSE 帧设置。位 0 为 rx_pause，位 1 为 tx_pause，位 2 为 pause_autoneg。rx_pause = 1 指示硬件遵从传入的 PAUSE 帧，0 指示忽略。tx_pause = 1 允许硬件在其接收 FIFO 达到高阈值时发出 PAUSE 帧，0 禁止硬件发出 PAUSE 帧。pause_autoneg = 1 覆盖 rx_pause 和 tx_pause 位，指示硬件与链路对端协商 PAUSE 设置。默认为 7（三者均为 1）。此可调参数为所有端口建立默认 PAUSE 设置。可通过 dev.<port>.X.pause_settings sysctl 按端口显示和控制设置。

**`hw.cxgbe.fec`** 前向纠错设置。-1（默认）表示驱动应自动选择值。0 禁用 FEC。可通过设置单个位实现更精细的控制。位 0 启用 RS FEC，位 1 启用 BASE-R FEC（又名 Firecode FEC），位 2 启用 NO FEC，位 6 启用所插入的可插拔收发器/线缆推荐的 FEC。这些位可以任意组合一起设置。此可调参数为所有端口建立默认 FEC 设置。可通过 dev.<port>.X.requested_fec sysctl 按端口控制设置。链路启动时，正在使用的 FEC 可在 dev.<port>.X.link_fec 中查看。

**`hw.cxgbe.autoneg`** 链路自动协商设置。此可调参数为所有端口建立默认自动协商设置。可通过 dev.<port>.X.autoneg sysctl 按端口显示和控制设置。0 禁用自动协商。1 启用自动协商。默认为 -1，由驱动选择值。对于不支持自动协商的端口和模块组合，dev.<port>.X.autoneg 为 -1。

**`hw.cxgbe.buffer_packing`** 允许硬件机会性地在同一接收缓冲区中交付多个帧。默认为 -1，由驱动决定。0 或 1 显式禁用或启用此功能。

**`hw.cxgbe.largest_rx_cluster`**

**`hw.cxgbe.safest_rx_cluster`** 接收簇的大小。每个都必须设置为可用大小之一（通常为 2048、4096、9216 和 16384），且 largest_rx_cluster 必须大于或等于 safest_rx_cluster。默认分别为 16384 和 4096。驱动从不尝试分配大于 largest_rx_cluster 的接收缓冲区，如果分配大于 safest_rx_cluster 的缓冲区失败，则回退到分配 safest_rx_cluster 大小的缓冲区。注意 largest_rx_cluster 仅设定上限——允许驱动分配更小大小的缓冲区。

**`hw.cxgbe.config_file`** 选择预打包的设备配置文件。配置文件包含对网卡上的硬件资源进行分区和配置的方案。此可调参数仅用于专门的应用程序，不应在正常操作中使用。当前使用的配置文件可在 dev.<nexus>.X.cf 和 dev.<nexus>.X.cfcsum sysctl 中查看。

**`hw.cxgbe.linkcaps_allowed`**

**`hw.cxgbe.niccaps_allowed`**

**`hw.cxgbe.toecaps_allowed`**

**`hw.cxgbe.rdmacaps_allowed`**

**`hw.cxgbe.iscsicaps_allowed`**

**`hw.cxgbe.fcoecaps_allowed`** 禁止某项功能会向驱动和固件提示不要为该功能保留硬件资源。每一项都是位字段，为该功能内的每个子功能对应一位。此可调参数仅用于专门的应用程序，不应在正常操作中使用。已为其保留硬件资源的功能列在 dev.<nexus>.X.*caps sysctl 中。

**`hw.cxgbe.tx_vm_wr`** 设置为 1 指示驱动使用 VM 工作请求发送数据。这使得 PF 接口可通过 ASIC 中的内部交换机向 VF 接口发送帧。注意 [cxgbev(4)](cxgbev.4.md) VF 驱动始终使用 VM 工作请求，不受此可调参数影响。默认值为 0，仅当 PF 和 VF 接口需要相互通信时才应更改。当接口处于管理性 down 状态时，可使用 dev.<port>.X.tx_vm_wr sysctl 为不同接口分配不同的值。

**`hw.cxgbe.attack_filter`** 设置为 1 以启用"攻击过滤器"。默认为 0。当以下任何条件为真时，攻击过滤器将丢弃传入帧：源 ip/ip6 == 目的 ip/ip6；tcp 且源/目的 ip 非单播；源/目的 ip 为环回（127.x.y.z）；源 ip6 非单播；源/目的 ip6 为环回（::1/128）或未指定（::/128）；tcp 且源/目的 ip6 为多播（ff00::/8）。此功能仅在基于 T4 和 T5 的网卡上可用。

**`hw.cxgbe.drop_ip_fragments`** 设置为 1 以丢弃所有传入的 IP 分片。默认为 0。注意这会丢弃有效帧。

**`hw.cxgbe.drop_pkts_with_l2_errors`** 设置为 1 以丢弃具有第 2 层长度或校验和错误的传入帧。默认为 1。

**`hw.cxgbe.drop_pkts_with_l3_errors`** 设置为 1 以丢弃具有 IP 版本、长度或校验和错误的传入帧。仅对 TCP 或 UDP 数据包验证 IP 校验和。默认为 0。

**`hw.cxgbe.drop_pkts_with_l4_errors`** 设置为 1 以丢弃具有第 4 层（TCP 或 UDP）长度、校验和或其他错误的传入帧。默认为 0。

## 支持

有关一般信息和支持，请访问 Chelsio 支持网站：`http://www.chelsio.com/`。

如果在使用受支持适配器时发现此驱动的问题，请将与该问题相关的所有具体信息通过电子邮件发送至 <support@chelsio.com>。

## 参见

arp(4), [ccr(4)](ccr.4.md), [cxgb(4)](cxgb.4.md), [cxgbev(4)](cxgbev.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`cxgbe` 设备驱动首次出现于 FreeBSD 9.0。对 T5 网卡的支持首次出现于 FreeBSD 9.2 和 FreeBSD 10.0。对 T6 网卡的支持首次出现于 FreeBSD 11.1 和 FreeBSD 12.0。对 T7 网卡的支持首次出现于 FreeBSD 15.0。

## 作者

`cxgbe` 驱动由 Navdeep Parhar <np@FreeBSD.org> 编写。
