# vtnet(4)

`vtnet` — VirtIO 以太网驱动

## 名称

`vtnet`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device vtnet

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_vtnet_load="YES"
```

## 描述

`vtnet` 设备驱动为 VirtIO 以太网设备提供支持。

如果 hypervisor 通告了相应的功能，`vtnet` 驱动支持发送和接收的 TCP/UDP 校验和卸载、TCP 分段卸载（TSO）、TCP 大接收卸载（LRO）、硬件 VLAN 标签剥离/插入功能、多播哈希过滤器以及 Jumbo Frames（最大 9216 字节），可通过接口 MTU 设置进行配置。

支持两种 TCP LRO：硬件 TCP LRO，由主机向客户机提供大于 MTU 的 TCP 段来执行；软件 TCP LRO，由客户机的网络栈以优化方式处理 TCP 段来执行。只能使用一种 TCP LRO。由于硬件 TCP LRO 可能与 IP 转发产生不良交互，而软件 TCP LRO 缓解了硬件 TCP LRO 的若干缺陷，默认设置为禁用硬件 TCP LRO。参见加载器可调参数 `hw.vtnet.X.lro_disable`。

TCP/UDP 接收校验和卸载无法为 IPv4 和 IPv6 独立配置。通过 [ifconfig(8)](../man8/ifconfig.8.md) 实用程序选择大于 1500 字节的 MTU 可配置适配器收发 Jumbo Frames。

有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`hw.vtnet.csum_disable`**

**`hw.vtnet.X.csum_disable`** 此可调参数禁用 TCP 和 UDP 的接收和发送校验和卸载。这也意味着禁用 TCP 分段卸载和大接收卸载。默认值为 0。

**`hw.vtnet.tso_disable`**

**`hw.vtnet.X.tso_disable`** 此可调参数禁用 TCP 分段卸载。默认值为 0。

**`hw.vtnet.lro_disable`**

**`hw.vtnet.X.lro_disable`** 此可调参数禁用硬件 TCP LRO。默认值为 1。

**`hw.vtnet.mq_disable`**

**`hw.vtnet.X.mq_disable`** 此可调参数禁用多队列。默认值为 0。

**`hw.vtnet.mq_max_pairs`**

**`hw.vtnet.X.mq_max_pairs`** 此可调参数设置发送和接收队列对的最大数量。仅在协商了多队列功能时才支持多队列。此驱动最多支持 8 个队列对。使用的队列对数为驱动和 hypervisor 支持的最大值、客户机中存在的 CPU 数以及此可调参数（如果非零）中的较小值。默认值为 0。

**`hw.vtnet.tso_maxlen`**

**`hw.vtnet.X.tso_maxlen`** 此可调参数设置 TSO 突发限制。默认值为 65535。

**`hw.vtnet.rx_process_limit`**

**`hw.vtnet.X.rx_process_limit`** 此可调参数设置一次处理的 RX 段数。默认值为 1024。

**`hw.vtnet.lro_entry_count`**

**`hw.vtnet.X.lro_entry_count`** 此可调参数设置软件 TCP LRO 条目数。默认值为 128，最小值为 8。

**`hw.vtnet.lro_mbufq_depth`**

**`hw.vtnet.X.lro_mbufq_depth`** 此可调参数设置软件 TCP LRO mbuf 队列的深度。默认值为 0。

**`hw.vtnet.altq_disable`** 此可调参数禁用 ALTQ 支持，允许改用多队列。此选项适用于所有接口。默认值为 0。

## 发送队列统计

为每个接口的每个发送队列提供以下只读统计信息：

**`dev.vtnet.X.txqY.rescheduled`** 发送中断处理程序被重新调度的次数。

**`dev.vtnet.X.txqY.tso`** 执行 TCP 分段卸载的次数。

**`dev.vtnet.X.txqY.csum`** 执行 UDP 或 TCP 发送校验和卸载的次数。

**`dev.vtnet.X.txqY.omcasts`** 已发送的多播数据包数。

**`dev.vtnet.X.txqY.obytes`** 已发送的字节数（基于以太网帧）。

**`dev.vtnet.X.txqY.opackets`** 已发送的数据包数（以太网帧）。

## 接收队列统计

为每个接口的每个接收队列提供以下只读统计信息：

**`dev.vtnet.X.rxqY.rescheduled`** 接收中断处理程序被重新调度的次数。

**`dev.vtnet.X.rxqY.host_lro`** 执行 TCP 大接收卸载的次数。

**`dev.vtnet.X.rxqY.csum_failed`** 接收到带有接收或发送校验和卸载请求的数据包但该请求失败的次数。失败的不同原因由 `dev.vtnet.X.rx_csum_inaccessible_ipproto`、`dev.vtnet.X.rx_csum_bad_ipproto` 和 `dev.vtnet.X.rx_csum_bad_ethtype` 计数。

**`dev.vtnet.X.rxqY.csum`** 执行 UDP 或 TCP 接收校验和卸载的次数。

**`dev.vtnet.X.rxqY.ierrors`** 输入处理期间发生错误的次数。

**`dev.vtnet.X.rxqY.iqdrops`** 输入处理期间丢弃数据包的次数。

**`dev.vtnet.X.rxqY.ibytes`** 已接收的字节数（基于以太网帧）。

**`dev.vtnet.X.rxqY.ipackets`** 已接收的数据包数（以太网帧）。

## 接口发送统计

为每个接口提供以下只读发送统计信息：

**`dev.vtnet.X.tx_task_rescheduled`** 该接口所有发送队列的 `dev.vtnet.X.txqY.rescheduled` 之和。

**`dev.vtnet.X.tx_tso_offloaded`** 该接口所有发送队列的 `dev.vtnet.X.txqY.tso` 之和。

**`dev.vtnet.X.tx_csum_offloaded`** 该接口所有发送队列的 `dev.vtnet.X.txqY.csum` 之和。

**`dev.vtnet.X.tx_defrag_failed`** 发送操作期间尝试对 mbuf 链进行碎片整理失败的次数。

**`dev.vtnet.X.tx_defragged`** 发送操作期间对 mbuf 链进行碎片整理的次数。

**`dev.vtnet.X.tx_tso_without_csum`** 在未执行发送校验和卸载的情况下尝试 TCP 分段卸载的次数。

**`dev.vtnet.X.tx_tso_not_tcp`** 对非 TCP 数据包尝试 TCP 分段卸载的次数。

**`dev.vtnet.X.tx_csum_proto_mismatch`** 发送校验和卸载请求的 IP 协议版本与数据包的 IP 协议版本不匹配的次数。

**`dev.vtnet.X.tx_csum_unknown_ethtype`** 对 EtherType 既非 IPv4 也非 IPv6（考虑简单 VLAN 标记）的以太网帧请求发送卸载操作的次数。

## 接口接收统计

为每个接口提供以下只读接收统计信息：

**`dev.vtnet.X.rx_task_rescheduled`** 该接口所有接收队列的 `dev.vtnet.X.rxqY.rescheduled` 之和。

**`dev.vtnet.X.rx_csum_offloaded`** 该接口所有接收队列的 `dev.vtnet.X.rxqY.csum` 之和。

**`dev.vtnet.X.rx_csum_failed`** 该接口所有接收队列的 `dev.vtnet.X.rxqY.csum_failed` 之和。

**`dev.vtnet.X.rx_csum_inaccessible_ipproto`** 接收到带有接收或发送校验和卸载请求的数据包但 IP 协议不可访问的次数。

**`dev.vtnet.X.rx_csum_bad_ipproto`** 接收到带有接收或发送校验和卸载请求的数据包但 IP 协议既非 TCP 也非 UDP 的次数。

**`dev.vtnet.X.rx_csum_bad_ethtype`** 接收到带有接收或发送校验和卸载请求的数据包但 EtherType 既非 IPv4 也非 IPv6 的次数。

**`dev.vtnet.X.rx_mergeable_failed`** 接收可合并缓冲区失败的次数。

**`dev.vtnet.X.rx_enq_replacement_failed`** 替换接收 mbuf 链入队失败的次数。

**`dev.vtnet.X.rx_frame_too_large`** 在不使用可合并缓冲区的大接收卸载期间，帧长于 mbuf 链的次数。

**`dev.vtnet.X.mbuf_alloc_failed`** 为接收缓冲区分配 mbuf 簇失败的次数。

## 接口配置参数

为每个接口提供以下只读配置参数：

**`dev.vtnet.X.act_vq_pairs`** 活动 virtqueue 对数。

**`dev.vtnet.X.req_vq_pairs`** 请求的 virtqueue 对数。

**`dev.vtnet.X.max_vq_pairs`** 支持的最大 virtqueue 对数。

**`dev.vtnet.X.flags`** 接口的标志。主要用于调试。

**`dev.vtnet.X.features`** 由 virtio 规范定义的接口功能。

## 参见

arp(4), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [virtio(4)](virtio.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`vtnet` 驱动由 Bryan Venteicher <bryanv@FreeBSD.org> 编写。最早出现在 FreeBSD 9.0 中。

## 注意事项

`vtnet` 驱动仅在 hypervisor 通告可合并缓冲区功能时支持 LRO。
