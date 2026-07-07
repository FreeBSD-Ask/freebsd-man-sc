# sfxge(4)

`sfxge` — Solarflare 10Gb 以太网适配器驱动

## 名称

`sfxge`

## 概要

`要将此驱动编译进内核，请将以下行添加到你的内核配置文件中：`

> device sfxge

`要在引导时以模块形式加载此驱动，请将以下行添加到 loader.conf(5) 中：`

```sh
sfxge_load="YES"
```

## 描述

`sfxge` 驱动为基于 Solarflare SFC9000 和 XtremeScale X2 系列控制器的 10Gb 以太网适配器提供支持。该驱动支持 jumbo 帧、发送/接收校验和卸载、TCP 分段卸载（TSO）、大接收卸载（LRO）、VLAN 校验和卸载、VLAN TSO，以及使用 MSI-X 中断的接收端缩放（RSS）。

驱动为每个 CPU 分配 1 个接收队列、发送队列、事件队列和 IRQ，最多 64 个。应使用 cpuset(1) 分散 IRQ 亲和性。中断节流可通过 sysctl `dev.sfxge.%d.int_mod` 控制（单位为微秒）。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

大量 MAC、PHY 和数据路径统计信息可在 sysctl `dev.sfxge.%d.stats` 下获取。适配器的 VPD 字段（包括序列号）可在 sysctl `dev.sfxge.%d.vpd` 下获取。

## 硬件

`sfxge` 驱动支持所有基于 Solarflare SFC9000 系列控制器的 10Gb 以太网适配器。

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。实际值可使用 [sysctl(8)](../man8/sysctl.8.md) 获取。

**`hw.sfxge.rx_ring`** 接收队列环中的最大描述符数。支持的值为：512、1024、2048 和 4096。

**`hw.sfxge.tx_ring`** 发送队列环中的最大描述符数。支持的值为：512、1024、2048 和 4096。

**`hw.sfxge.tx_dpl_get_max`** 已排队发送数据包（TCP 和非 TCP）的延迟数据包"get-list"的最大长度，仅在能获取发送队列锁时使用。如果数据包被丢弃，`tx_get_overflow` 计数器会递增，本地发送方会收到 ENOBUFS。该值必须大于 0。

**`hw.sfxge.tx_dpl_get_non_tcp_max`** 延迟数据包"get-list"中非 TCP 数据包的最大数量，仅在能获取发送队列锁时使用。如果数据包被丢弃，`tx_get_non_tcp_overflow` 计数器会递增，本地发送方会收到 ENOBUFS。该值必须大于 0。

**`hw.sfxge.tx_dpl_put_max`** 已排队发送数据包的延迟数据包"put-list"的最大长度，在无法获取发送队列锁时使用。如果数据包被丢弃，`tx_put_overflow` 计数器会递增，本地发送方会收到 ENOBUFS。该值必须大于或等于 0。

**`hw.sfxge.tso_fw_assisted`** 用于启用/禁用 NIC 固件支持的 FW 辅助 TSO 版本的位掩码。支持 FATSOv1（位 0）和 FATSOv2（位 1）。默认全部启用。

**`hw.sfxge.N.max_rss_channels`** 第 N 个适配器分配的最大 RSS 通道数。如果设为 0 或未设置，通道数由 CPU 核心数决定。

**`hw.sfxge.lro.table_size`** LRO 哈希表的大小。必须是 2 的幂。更大的表意味着可以加速更多的流。

**`hw.sfxge.lro.chain_max`** 哈希链的最大长度。如果链过长，查找时间会增加，可能超过 LRO 的收益。

**`hw.sfxge.lro.idle_ticks`** 连接在丢弃其 LRO 状态前可保持空闲的最长时间（以 tick 为单位）。

**`hw.sfxge.lro.slow_start_packets`** 在连接符合 LRO 条件前，必须按序到达的带有效载荷的数据包数量。其理念是应避免在发送方处于慢启动阶段时合并段，因为降低 ACK 速率可能损害性能。

**`hw.sfxge.lro.loss_packets`** 在连接符合 LRO 条件前，发生丢失后必须按序到达的带有效载荷的数据包数量。其理念是应避免在发送方从丢失中恢复时合并段，因为降低 ACK 速率可能损害性能。

**`hw.sfxge.mcdi_logging`** 启用 MCDI 协议消息日志记录（仅在编译时启用才可用）。

**`hw.sfxge.N.mcdi_logging`** 按端口启用或禁用 MCDI 协议消息日志记录。每个端口的默认值为 `hw.sfxge.mcdi_logging` 的值。也可在驱动加载后使用 sysctl `dev.sfxge.%d.mcdi_logging` 启用或禁用日志记录。

**`hw.sfxge.stats_update_period_ms`** 从硬件刷新接口统计信息的周期（毫秒）。接受范围为 0 到 65535，默认为 1000（1 秒）。使用零值可禁用定期统计信息更新。在固件 v6.2.1.1033 及更高版本的 SFN8xxx 系列适配器以及 SFN5xxx、SFN6xxx 和 XtremeScale X2xxx 系列适配器上受支持。SFN7xxx 系列适配器和早期固件的 sfN8xxx 系列使用固定的 1000 毫秒统计信息更新周期。该周期也可在驱动加载后使用 sysctl `dev.sfxge.%d.stats_update_period_ms` 更改。

## 支持

有关一般信息和支持，请访问 Solarflare 支持网站：`https://support.solarflare.com`。

## 参见

cpuset(1), arp(4), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 作者

`sfxge` 驱动由 Philip Paeps 和 Solarflare Communications, Inc. 编写。
