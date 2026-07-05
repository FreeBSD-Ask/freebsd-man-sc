# gve.4

`gve` — Google 虚拟网卡 (gVNIC) 以太网驱动

## 名称

`gve`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device gve

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_gve_load="YES"
```

## 描述

gVNIC 是为 Google Compute Engine (GCE) 专门设计的虚拟网络接口。它用于支持每 VM 的 Tier-1 网络性能，以及在 GCE 上使用某些 VM 形状。

`gve` 是 gVNIC 的驱动。它支持以下特性：

- RX 校验和卸载
- TX 校验和卸载
- TCP 分段卸载 (TSO)
- 软件大接收卸载 (LRO)
- Jumbo 帧
- 接收端缩放 (RSS)

关于配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`gve` 绑定到 gVNIC 呈现的单一 PCI 设备 ID：

- 0x1AE0:0x0042

## 实例

将 gve0 接口的 TX 队列数更改为 4：

> sysctl dev.gve.0.num_tx_queues=4

将 gve0 接口的 RX 队列数更改为 4：

> sysctl dev.gve.0.num_rx_queues=4

将 gve0 接口的 TX 环大小更改为 512：

> sysctl dev.gve.0.tx_ring_size=512

将 gve0 接口的 RX 环大小更改为 512：

> sysctl dev.gve.0.rx_ring_size=512

## 诊断

驱动初始化期间会记录以下消息：

- Enabled MSIX with %d vectors
- Configured device resources
- Successfully attached %s
- Deconfigured device resources

驱动初始化失败时会看到这些消息。全局（跨队列）分配失败：

- Failed to configure device resources: err=%d
- No compatible queue formats
- Failed to allocate ifnet struct
- Failed to allocate admin queue mem
- Failed to alloc DMA mem for DescribeDevice
- Failed to allocate QPL page

irq 和 BAR 分配失败：

- Failed to acquire any msix vectors
- Tried to acquire %d msix vectors, got only %d
- Failed to setup irq %d for Tx queue %d
- Failed to setup irq %d for Rx queue %d
- Failed to allocate irq %d for mgmnt queue
- Failed to setup irq %d for mgmnt queue, err: %d
- Failed to allocate BAR0
- Failed to allocate BAR2
- Failed to allocate msix table

Rx 队列特定分配失败：

- No QPL left for rx ring %d
- Failed to alloc queue resources for rx ring %d
- Failed to alloc desc ring for rx ring %d
- Failed to alloc data ring for rx ring %d

Tx 队列特定分配失败：

- No QPL left for tx ring %d
- Failed to alloc queue resources for tx ring %d
- Failed to alloc desc ring for tx ring %d
- Failed to vmap fifo, qpl_id = %d

接口分离失败时会记录以下消息：

- Failed to deconfigure device resources: err=%d

如果启用了 bootverbose，在接口启动时会记录以下消息：

- Created %d rx queues
- Created %d tx queues
- MTU set to %d

在接口关闭时会记录以下消息：

- Destroyed %d rx queues
- Destroyed %d tx queues

在启动或关闭接口时遇到错误会看到这些消息：

- Failed to destroy rxq %d, err: %d
- Failed to destroy txq %d, err: %d
- Failed to create rxq %d, err: %d
- Failed to create txq %d, err: %d
- Failed to set MTU to %d
- Invalid new MTU setting. new mtu: %d max mtu: %d min mtu: %d
- Cannot bring the iface up when detached
- Reached max number of registered pages %lu > %lu
- Failed to init lro for rx ring %d

任何管理队列命令失败时会看到这些消息：

- AQ command(%u): failed with status %d
- AQ command(%u): unknown status code %d
- AQ commands timed out, need to reset AQ
- Unknown AQ command opcode %d

检测到 TX 超时时会显示这些消息：

- Found %d timed out packet(s) on txq%d, kicking it for completions
- Found %d timed out packet(s) on txq%d with its last kick %ld sec ago which is less than the cooldown period %d. Resetting device

由于错误而重置设备时会记录以下消息：

- Scheduling reset task!
- Waiting until admin queue is released.
- Admin queue released

如果是 NIC 请求重置，会记录此消息：

- Device requested reset

如果重置在重新初始化阶段失败，会记录此消息：

- Restore failed!

这两条消息对应于 NIC 向驱动告警链路状态变化：

- Device link is up.
- Device link is down.

除这些消息外，驱动还按队列公开数据包和错误计数器作为 sysctl 节点。全局（跨队列）计数器可使用 [netstat(1)](../man1/netstat.1.md) 读取。

## SYSCTL 变量

`gve` 公开以下 [sysctl(8)](../man8/sysctl.8.md) 变量：

**`hw.gve.driver_version`** 驱动版本号。只读。

**`hw.gve.queue_format`** 使用中的队列格式。只读。

**`hw.gve.disable_hw_lro`** 将此引导时可调参数设置为 1 可禁用 NIC 中的大接收卸载 (LRO)。默认值为 0，表示硬件 LRO 默认启用。内核中的软件 LRO 栈始终使用。此 sysctl 变量需在加载驱动之前使用 loader.conf(5) 设置。

**`hw.gve.allow_4k_rx_buffers`** 将此引导时可调参数设置为 1 可启用 4K RX 缓冲区支持。默认值为 0，表示将使用 2K RX 缓冲区。4K RX 缓冲区仅在 DQO_RDA 和 DQO_QPL 队列格式上受支持。启用后，将在启用 HW LRO 或 mtu 大于 2048 时使用 4K RX 缓冲区。此 sysctl 变量需在加载驱动之前使用 loader.conf(5) 设置。

**`dev.gve.X.num_rx_queues and dev.gve.X.num_tx_queues`** 运行时可调参数，表示当前使用的 RX/TX 队列数。默认值为设备可支持的最大 RX/TX 队列数。此调用会在设置新队列时关闭接口，可能导致任何新数据包被丢弃。如果系统无法为驱动提供足够资源，此调用可能失败。在这种情况下，驱动将恢复到之前的 RX/TX 队列数。如果这也失败，将触发设备重置。注意：即使队列被移除，队列统计的 sysctl 节点仍可用。

**`dev.gve.X.rx_ring_size and dev.gve.X.tx_ring_size`** 运行时可调参数，表示 RX/TX 队列的当前环大小。默认值设为设备环大小的默认值。此调用会在以新环大小设置队列时关闭接口，可能导致任何新数据包被丢弃。如果系统无法为驱动提供足够资源，此调用可能失败。在这种情况下，驱动将尝试恢复 RX/TX 队列的之前环大小。如果这也失败，设备将处于不健康状态，需要重新加载。此值必须是 2 的幂且在定义范围内。

## 限制

`gve` 不支持发送带 VLAN 标记的数据包。所有带 VLAN 标记的流量都会被丢弃。

## 队列格式

`gve` 具有不同的数据路径模式，称为队列格式：

- GQI_QPL：“QPL”代表“Queue Page List”，指硬件期望固定 bounce buffer 且无法访问任意内存。GQI 是较旧的描述符格式。“GQI”中的 G 指较旧的硬件代，“QI”代表“Queue In-order”，指 NIC 发送 Tx 和 Rx 完成的顺序与驱动投递相应描述符的顺序相同。
- DQO_RDA：DQO 是为充分利用下一代 VM 形状所需的描述符格式。“RDA”代表“Raw DMA Addressing”，指硬件可处理 DMA 的数据包且不期望将其复制进出固定 bounce buffer。“DQO”中的 D 指较新的硬件代，“QO”代表“Queue Out-of-order”，指 NIC 可能以与驱动投递相应描述符不同的顺序发送 Tx 和 Rx 完成。
- DQO_QPL：“QPL”模式下的下一代描述符格式。

## 支持

请发送邮件至 <gvnic-drivers@google.com> 描述所遇到问题的具体情况。

## 参见

[netstat(1)](../man1/netstat.1.md), loader.conf(5), [ifconfig(8)](../man8/ifconfig.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`gve` 设备驱动首次出现于 FreeBSD 13.3。

## 作者

`gve` 驱动由 Google 编写。
