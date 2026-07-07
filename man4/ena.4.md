# ena(4)

`ena` — AWS EC2 弹性网络适配器（ENA）驱动

## 名称

`ena`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device ena

`或者，若要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_ena_load="YES"
```

## 描述

ENA 是一种网络接口，设计用于充分利用现代 CPU 特性和系统架构。

ENA 设备公开一个轻量级管理接口，包含最少的内存映射寄存器集和通过管理队列（Admin Queue）扩展的命令集。

该驱动支持一系列 ENA 设备，与链路速度无关（即 10GbE、25GbE、40GbE 等使用同一驱动），并具有可协商和可扩展的功能集。

部分 ENA 设备支持 SR-IOV。此驱动同时用于 SR-IOV 物理功能（PF）和虚拟功能（VF）设备。

ENA 设备通过提供多个 Tx/Rx 队列对（最大数量由设备通过管理队列通告）、每个 Tx/Rx 队列对专用的 MSI-X 中断向量以及针对 CPU 缓存行优化的数据放置，实现高速且低开销的网络流量处理。

启用 RSS 时，每个 Tx/Rx 队列对绑定到相应的 CPU 核心及其 NUMA 域。这些绑定的顺序基于 RSS 桶映射。对于禁用 RSS 支持的构建，CPU 和 NUMA 管理由内核处理。多核扩展支持接收端扩展（RSS）。

`ena` 驱动及其对应设备实现了健康监控机制（如 watchdog），使设备和驱动能够以对应用程序透明的方式恢复，并提供调试日志。

部分 ENA 设备支持一种称为低延迟队列（Low-latency Queue，LLQ）的工作模式，可再节省数微秒。

`ena` 驱动提供对 [netmap(4)](netmap.4.md) 框架的支持。内核必须以 DEV_NETMAP 选项构建才能使用此功能。

## 硬件

`ena` 驱动支持以下 PCI 厂商 ID/设备 ID：

- 1d0f:0ec2 - ENA PF
- 1d0f:1ec2 - 带 LLQ 支持的 ENA PF
- 1d0f:ec20 - ENA VF
- 1d0f:ec21 - 带 LLQ 支持的 ENA VF

## 加载器可调参数

`ena` 驱动的行为可通过运行时或引导时 sysctl 参数更改。引导时参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。运行时参数可使用 [sysctl(8)](../man8/sysctl.8.md) 命令设置。

引导时可调参数：

**`hw.ena.enable_9k_mbufs`** 为 Rx 描述符使用 9k mbuf。默认值为 0。如果该节点值设为 1，Rx 缓冲区将使用 9k mbuf。如果设为 0，则使用页大小 mbuf。在 Rx 中使用 9k 缓冲区可提高 Rx 吞吐量，但在低内存条件下可能会增加分配时间，因为系统必须查找 3 个连续页。这进一步可能导致操作系统不稳定，伴随 ENA 驱动重置和 NVMe 超时。如果网络性能至关重要且内存容量充足，可使用 9k mbuf。

**`hw.ena.force_large_llq_header`** 强制驱动使用大型（224 字节）或常规（96 字节）LLQ 头大小。默认值为 2，将使用推荐的 LLQ 头大小。如果该节点值设为 0，将使用常规大小 LLQ 头（96B）。在某些情况下，数据包头可能大于此值（例如带多个扩展的 IPv6）。在这种情况下，应使用 224B 的大型 LLQ 头大小，可将此节点值设为 1 以强制使用。仅当设备同时支持 LLQ 和大型 LLQ 头时，使用大型 LLQ 头大小才会生效。否则，将回退到无 LLQ 模式或常规头大小。增大 LLQ 头大小会将 Tx 队列大小减半，因此可能影响 Tx 丢包数量。

运行时可调参数：

- 0 - ENA_ERR - 启用驱动错误消息和 ena_com 错误日志。
- 1 - ENA_WARN - 启用非关键错误的日志。
- 2 - ENA_INFO - 使驱动更详细地报告其操作。
- 3 - ENA_DBG - 启用调试日志。

```sh
sysctl hw.ena.log_level=1
```

```sh
sysctl dev.ena.1.io_queues_nb=2
```

```sh
sysctl dev.ena.0.rx_queue_size=8192
```

```sh
sysctl dev.ena.0.buf_ring_size=2048
```

```sh
sysctl dev.ena.1.eni_metrics.sample_interval=10
```

```sh
sysctl dev.ena.0.rss.indir_table_size
```

```sh
sysctl dev.ena.0.rss.indir_table="0:5 5:0"
```

```sh
sysctl dev.ena.0.rss.key=6d5a56da255b0ec24167253d43a38fb0d0ca2bcbae7b30b477cb2da38030f20c6a42b73bbeac01fa
```

**`hw.ena.log_level`** 控制驱动的额外日志详细程度。默认值为 2。日志级别越高，打印的日志越多。0 表示禁用所有额外日志，仅打印错误日志。默认值（2）报告错误、警告，并详细描述驱动操作。可能的标志为：注意：要在 Tx/Rx 数据路径上启用日志，驱动必须以 ENA_LOG_IO_ENABLE 编译标志编译。示例：要启用错误和警告日志，应使用以下命令：

**`dev.ena.X.io_queues_nb`** 当前分配并使用的 IO 队列数。默认值为 max_num_io_queues。控制 IO 队列对（Tx/Rx）的数量。由于此调用必须重新分配队列，它将重置接口并重启所有队列——这意味着当前在队列中持有的所有内容都将丢失，可能导致数据包丢弃。如果系统无法向驱动提供足够资源，此调用可能失败。在这种情况下，驱动将尝试还原之前的 IO 队列数。如果还原也失败，将触发设备重置。示例：要为设备 ena1 仅使用 2 个 Tx 和 Rx 队列，应使用以下命令：

**`dev.ena.X.rx_queue_size`** Rx 队列大小。默认值为 1024。控制每个 Rx 队列的 IO 描述符数。如果用户在驱动统计中观察到大量 Rx 丢弃，可能需要增大 Rx 队列大小。出于性能原因，Rx 队列大小必须是 2 的幂。如果系统无法向驱动提供足够资源，此调用可能失败。在这种情况下，驱动将尝试还原之前的描述符数。如果还原也失败，将触发设备重置。示例：要将设备 ena0 的 Rx 环大小增加到 8K 描述符，应使用以下命令：

**`dev.ena.X.buf_ring_size`** Tx 缓冲环（drbr）大小。默认值为 4096。输入必须是 2 的幂。控制 Tx 缓冲环中可容纳的 mbuf 数量。drbr 作为多生产者、单消费者无锁环，用于在 Tx 过程忙于发送数据包或 Tx 环已满时缓冲来自协议栈的额外 mbuf。增大缓冲环大小可减少在 IO 队列无法立即处理的大型 Tx 突发中丢弃的 Tx 数据包数。每个 Tx 队列都有其自己的 drbr。建议至少将 drbr 保持为默认值，但如果系统缺乏资源，可减小。如果系统无法向驱动提供足够资源，此调用可能失败。在这种情况下，驱动将尝试还原之前的 drbr 数并触发设备重置。示例：要将接口 ena0 的 drbr 大小设置为 2048，应使用以下命令：

**`dev.ena.X.eni_metrics.sample_interval`** 更新 ENI 指标的间隔（以秒为单位）。默认值为 0。确定 ENI 指标应更新的频率（如果有）。ENI 指标在定时器服务中异步更新，以避免因 sysctl 节点读取导致管理队列过载。此节点中的值控制向设备发出管理命令以更新 ENI 指标值之间的间隔。如果某些应用程序定期监视 eni_metrics，则可相应调整 ENI 指标间隔。值 0 完全关闭更新。值 1 是最小间隔，等于 1 秒。允许的最大更新间隔为 1 小时。示例：要每 10 秒更新设备 ena1 的 ENI 指标，应使用以下命令：

**`dev.ena.X.rss.indir_table_size`** RSS 间接表大小。默认值为 128。返回 RSS 间接表中的条目数。示例：要读取 RSS 间接表大小，应使用以下命令：

**`dev.ena.X.rss.indir_table`** RSS 间接表映射。默认为 indir_table_size 长度的 x:y 键值对。更新 RSS 间接表的选定索引。条目字符串由一个或多个 x:y 键值对组成，其中 x 表示表索引，y 表示其新值。不需要更新的表索引可从字符串中省略，并保留其现有值。如果某个索引输入多次，则使用最后一个值。示例：要更新 RSS 间接表中的两个选定索引（例如将索引 0 设置为队列 5，然后将索引 5 设置为队列 0），应使用以下命令：

**`dev.ena.X.rss.key`** RSS 哈希键。默认为 40 字节长的随机生成哈希键。控制 RSS Toeplitz 哈希算法的键值。仅在驱动未以内核侧 RSS 支持编译时可用。示例：要将 RSS 哈希键值更改为 0x6d, 0x5a, 0x56, 0xda, 0x25, 0x5b, 0x0e, 0xc2, br 0x41, 0x67, 0x25, 0x3d, 0x43, 0xa3, 0x8f, 0xb0, br 0xd0, 0xca, 0x2b, 0xcb, 0xae, 0x7b, 0x30, 0xb4, br 0x77, 0xcb, 0x2d, 0xa3, 0x80, 0x30, 0xf2, 0x0c, br 0x6a, 0x42, 0xb7, 0x3b, 0xbe, 0xac, 0x01, 0xfa 应使用以下命令：

## 诊断

### 设备初始化阶段

- ena%d: failed to init mmio read less 初始化 mmio 寄存器读取请求期间发生错误。
- ena%d: Can not reset device 无法重置设备。br 设备可能未响应或已在重置过程中。
- ena%d: device version is too low 控制器版本过旧，驱动不支持。
- ena%d: Invalid dma width value %d 控制器无法请求 dma 事务宽度。br 设备停止响应或要求了无效值。
- ena%d: Can not initialize ena admin queue with device 管理队列初始化失败。br 设备可能未响应，或资源初始化存在问题。
- ena%d: Cannot get attribute for ena device rc: %d 从控制器获取设备属性失败。
- ena%d: Cannot configure aenq groups rc: %d 尝试配置 AENQ 组时发生错误。

### 驱动初始化/关闭阶段

- ena%d: PCI resource allocation failed!
- ena%d: failed to pmap registers bar
- ena%d: can not allocate ifnet structure
- ena%d: Error with network interface setup
- ena%d: Failed to enable and set the admin interrupts
- ena%d: Error, MSI-X is already enabled
- ena%d: Failed to enable MSIX, vectors %d rc %d
- ena%d: Not enough number of MSI-X allocated: %d
- ena%d: Error with MSI-X enablement
- ena%d: could not allocate irq vector: %d
- ena%d: unable to allocate bus resource: registers!
- ena%d: unable to allocate bus resource: msix! 初始化设备时资源分配失败。br 驱动将不会挂载。
- ena%d: ENA device init failed (err: %d)
- ena%d: Cannot initialize device 设备初始化失败。br 驱动将不会挂载。
- ena%d: failed to register interrupt handler for irq %ju: %d 尝试注册管理队列中断处理程序时发生错误。
- ena%d: Cannot setup mgmnt queue intr 配置管理队列中断时发生错误。
- ena%d: Enable MSI-X failed 管理队列的 MSI-X 配置失败。br 可能是资源不足或中断无法配置。br 驱动将不会挂载。
- ena%d: VLAN is in use, detach first 尝试卸载驱动时正在使用 VLAN。br 必须先卸载 VLAN，然后再次调用卸载例程。
- ena%d: Unmapped RX DMA tag associations
- ena%d: Unmapped TX DMA tag associations 尝试销毁 RX/TX DMA 标签时发生错误。
- ena%d: Cannot init indirect table
- ena%d: Cannot fill indirect table
- ena%d: Cannot fill hash function
- ena%d: Cannot fill hash control
- ena%d: WARNING: RSS was not properly initialized, it will affect bandwidth 初始化某个 RSS 资源时发生错误。br 设备将以降低的性能工作，因为所有 RX 数据包都将传递到队列 0，且没有哈希信息。
- ena%d: LLQ is not supported. Fallback to host mode policy.
- ena%d: Failed to configure the device mode. Fallback to host mode policy.
- ena%d: unable to allocate LLQ bar resource. Fallback to host mode policy. 低延迟队列模式设置期间发生错误。br 设备将工作，但没有 LLQ 性能提升。
- ena%d: failed to enable write combining. 设置 LLQ 所需的写合并（Write Combining）模式时发生错误。
- ena%d: failed to tear down irq: %d
- ena%d: dev has no parent while releasing res for irq: %d 释放中断失败。

### 附加诊断

- ena%d: Invalid MTU setting. new_mtu: %d max_mtu: %d min mtu: %d 请求的 MTU 值不受支持，将不予设置。
- ena%d: Failed to set MTU to %d 当 MTU 更改功能不受支持或发生设备通信错误时显示此消息。
- ena%d: Keep alive watchdog timeout. Device stopped responding and will be reset.
- ena%d: Found a Tx that wasn't completed on time, qid %d, index %d. 数据包已推送到 NIC 但未在给定时间内发送。br 可能由 IO 队列挂起引起。
- ena%d: The number of lost tx completion is above the threshold (%d > %d). Reset the device 如果未按时完成的 Tx 过多，将重置设备。br 可能由队列或设备挂起引起。
- ena%d: Trigger reset is on 将重置设备。br 重置由 watchdog 触发，或因过多 TX 数据包未按时完成而触发。
- ena%d: device reset scheduled but trigger_reset is off 已触发重置任务，但驱动未请求。br 不会执行设备重置。
- ena%d: Device reset failed 尝试重置设备时发生错误。
- ena%d: Cannot initialize device
- ena%d: Error, mac address are different
- ena%d: Error, device max mtu is smaller than ifp MTU
- ena%d: Validation of device parameters failed
- ena%d: Enable MSI-X failed
- ena%d: Failed to create I/O queues
- ena%d: Reset attempt failed. Can not reset the device 尝试在重置后恢复设备时发生错误。
- ena%d: Device reset completed successfully,Driver info: %s 设备已在重置后正确恢复，可供使用。
- ena%d: Allocation for Tx Queue %u failed
- ena%d: Allocation for Rx Queue %u failed
- ena%d: Unable to create Rx DMA map for buffer %d
- ena%d: Failed to create io TX queue #%d rc: %d
- ena%d: Failed to get TX queue handlers. TX queue num %d rc: %d
- ena%d: Failed to create io RX queue[%d] rc: %d
- ena%d: Failed to get RX queue handlers. RX queue num %d rc: %d
- ena%d: could not allocate irq vector: %d
- ena%d: failed to register interrupt handler for irq %ju: %d IO 资源初始化失败。br 接口将不会启动。
- ena%d: LRO[%d] Initialization failed! RX 环的 LRO 初始化失败。
- ena%d: failed to alloc buffer for rx queue
- ena%d: failed to add buffer for rx queue %d
- ena%d: refilled rx qid %d with only %d mbufs (from %d) 分配 RX 路径使用的资源失败。br 如果在 IO 队列初始化期间发生，接口将不会启动。
- ena%d: NULL mbuf in rx_info 从描述符组装 mbuf 时发生错误。
- ena%d: tx_info doesn't have valid mbuf
- ena%d: Invalid req_id: %hu
- ena%d: failed to prepare tx bufs 准备传输数据包时发生错误。
- ena%d: ioctl promisc/allmulti 请求设备以 promisc/allmulti 模式工作的 IOCTL。br 更多详情请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 支持

如果在使用受支持的适配器时发现已发布源代码存在问题，请将与问题相关的具体信息通过电子邮件发送至 <akiyano@amazon.com>、<osamaabb@amazon.com> 和 <darinzon@amazon.com>。

## 参见

[netmap(4)](netmap.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`ena` 驱动首次出现于 FreeBSD 11.1。

## 作者

`ena` 驱动由 Amazon 开发，最初由 Semihalf 编写。
