# bce(4)

`bce` — QLogic NetXtreme II（BCM5706/5708/5709/5716）PCI/PCIe 千兆以太网适配器驱动

## 名称

`bce`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> device miibus
> device bce

或者，要在引导时以模块形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行：

```sh
if_bce_load="YES"
```

## 描述

`bce` 驱动支持 QLogic 的 NetXtreme II 产品系列，包括 BCM5706、BCM5708、BCM5709 和 BCM5716 以太网控制器。

NetXtreme II 产品系列由各种融合网卡（CNIC）以太网控制器组成，除标准 L2 以太网流量外，还支持 TCP 卸载引擎（TOE）、远程 DMA（RDMA）和 iSCSI 加速，全部在同一控制器上。

`bce` 驱动在 FreeBSD 下支持以下功能：

- IP/TCP/UDP 校验和卸载
- 巨型帧（最高 9022 字节）
- VLAN 标签剥离
- 中断合并
- 全双工模式下的 10/100/1000Mbps 操作
- 半双工模式下的 10/100Mbps 操作

`bce` 驱动支持以下媒体类型：

**`autoselect`** 启用媒体类型和选项的自动选择。用户可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加媒体选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`1000baseSX`** 设置 1000Mbps 操作。此速度下仅支持 `full-duplex` 模式。

**`1000baseT`** 设置双绞线上的 1000baseT 操作。仅支持 `full-duplex` 模式。

**`2500BaseSX`** 设置 2500Mbps 操作。仅支持 `full-duplex` 模式。

`bce` 驱动支持以下媒体选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`bce` 驱动为基于 QLogic NetXtreme II 系列千兆以太网控制器的各种 NIC 提供支持，包括：

- QLogic NetXtreme II BCM5706 1000Base-SX
- QLogic NetXtreme II BCM5706 1000Base-T
- QLogic NetXtreme II BCM5708 1000Base-SX
- QLogic NetXtreme II BCM5708 1000Base-T
- QLogic NetXtreme II BCM5709 1000Base-SX
- QLogic NetXtreme II BCM5709 1000Base-T
- QLogic NetXtreme II BCM5716 1000Base-T
- Dell PowerEdge 1950 integrated BCM5708 NIC
- Dell PowerEdge 2950 integrated BCM5708 NIC
- Dell PowerEdge R710 integrated BCM5709 NIC
- HP NC370F Multifunction Gigabit Server Adapter
- HP NC370T Multifunction Gigabit Server Adapter
- HP NC370i Multifunction Gigabit Server Adapter
- HP NC371i Multifunction Gigabit Server Adapter
- HP NC373F PCIe Multifunc Giga Server Adapter
- HP NC373T PCIe Multifunction Gig Server Adapter
- HP NC373i Multifunction Gigabit Server Adapter
- HP NC373m Multifunction Gigabit Server Adapter
- HP NC374m PCIe Multifunction Adapter
- HP NC380T PCIe DP Multifunc Gig Server Adapter
- HP NC382T PCIe DP Multifunction Gigabit Server Adapter
- HP NC382i DP Multifunction Gigabit Server Adapter
- HP NC382m DP 1GbE Multifunction BL-c Adapter

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`hw.bce.verbose`** 启用/禁用详细日志记录和控制台输出。对调试有用（默认 0）。

**`hw.bce.msi_enable`** 启用/禁用 MSI 支持（默认 1）。

**`hw.bce.tso_enable`** 启用/禁用 TSO 支持（默认 1）。

**`hw.bce.strict_rx_mtu`** 启用/禁用严格的 RX 帧大小检查（默认 0）。

**`hw.bce.hdr_split`** 启用/禁用帧头/负载分离（默认 1）。

**`hw.bce.rx_pages`** 设置驱动分配给接收数据包的内存页数。由于对齐问题，此值只能取 1、2、4 或 8（默认 2）。

**`hw.bce.tx_pages`** 设置驱动分配给发送数据包的内存页数。由于对齐问题，此值只能取 1、2、4 或 8（默认 2）。

**`hw.bce.rx_ticks`** 因 RX 处理活动而生成状态块更新前等待的微秒 tick 数。取值范围 0-100。值为 0 禁用此状态块更新。如果 hw.bce.rx_quick_cons_trip 也为 0 则不能设为 0（默认 18）。

**`hw.bce.rx_ticks_int`** RX 中断处理期间生成状态块更新前等待的微秒 tick 数。取值范围 0-100。值为 0 禁用此状态块更新（默认 18）。

**`hw.bce.rx_quick_cons_trip`** 生成状态块前必须完成的 RX 快速 BD 链条目数。取值范围 0-256。值为 0 禁用此状态块更新。如果 hw.bce.rx_ticks 也为 0 则不能设为 0（默认 6）。

**`hw.bce.rx_quick_cons_trip_int`** 中断处理期间生成状态块前必须完成的 RX 快速 BD 条目数。取值范围 0-256。值为 0 禁用此状态块更新（默认 6）。

**`hw.bce.tx_ticks`** 因 TX 活动而生成状态块更新前等待的微秒 tick 数。取值范围 0-100。值为 0 禁用此状态块更新。如果 hw.bce.tx_quick_cons_trip 也为 0 则不能设为 0（默认 80）。

**`hw.bce.tx_ticks_int`** 中断处理期间因 TX 活动生成状态块更新前等待的微秒 tick 数。取值范围 0-100。值为 0 禁用此状态块更新（默认 80）。

**`hw.bce.tx_cons_trip`** 生成状态块前必须完成的 TX 快速 BD 链条目数。取值范围 0-100。值为 0 禁用此状态块更新。如果 hw.bce.tx_ticks 也为 0 则不能设为 0（默认 20）。

**`hw.bce.tx_cons_trip_int`** 中断期间生成状态块前必须完成的 TX 快速 BD 链条目数。取值范围 0-100。值为 0 禁用此状态块更新（默认 20）。

## 诊断

- bce%d: PCI memory allocation failed!：驱动遇到致命初始化错误。
- bce%d: PCI map interrupt failed!：驱动遇到致命初始化错误。
- bce%d: Unsupported controller revision (%c%d)：驱动不支持当前使用的控制器修订版。
- bce%d: Controller initialization failed!：驱动遇到致命初始化错误。
- bce%d: NVRAM test failed!：驱动无法正确访问控制器 NVRAM。
- bce%d: DMA resource allocation failed!：驱动无法分配 DMA 内存以设置控制器主机内存数据结构。
- bce%d: Interface allocation failed!：驱动无法为控制器创建网络接口。
- bce%d: PHY probe failed!：驱动无法访问控制器使用的 PHY。
- bce%d: Failed to setup IRQ!：驱动无法初始化 IRQ 处理程序。
- bce%d: Error: PHY read timeout!：驱动在超时前无法读取 PHY 寄存器。
- bce%d: PHY write timeout!：驱动因超时无法写入 PHY 寄存器。
- bce%d: Timeout error reading NVRAM at offset 0x%08X!：驱动因超时无法写入 NVRAM。
- bce%d: Unknown Flash NVRAM found!：驱动不识别当前使用的 NVRAM 设备，因此无法正确访问。
- bce%d: Invalid NVRAM magic value!：驱动无法读取 NVRAM 或 NVRAM 已损坏。
- bce%d: Invalid Manufacturing Information NVRAM CRC!：驱动无法读取 NVRAM 或 NVRAM 已损坏。
- bce%d: Invalid Feature Configuration Information NVRAM CRC!：驱动无法读取 NVRAM 或 NVRAM 已损坏。
- bce%d: DMA mapping error!：驱动无法将内存映射到控制器所需的 DMA 可寻址空间。
- bce%d: Could not allocate parent DMA tag!：驱动无法分配 PCI 兼容的 DMA 标签。
- bce%d: Could not allocate status block DMA tag!：驱动无法为控制器状态块分配 DMA 标签。
- bce%d: Could not allocate status block DMA memory!：驱动无法为控制器状态块分配 DMA 可寻址内存。
- bce%d: Could not map status block DMA memory!：驱动无法将状态块内存映射到控制器的 DMA 地址空间。
- bce%d: Could not allocate statistics block DMA tag!：驱动无法为控制器统计块分配 DMA 标签。
- bce%d: Could not allocate statistics block DMA memory!：驱动无法为控制器统计块分配 DMA 可寻址内存。
- bce%d: Could not map statistics block DMA memory!：驱动无法将统计块内存映射到控制器的 DMA 地址空间。
- bce%d: Could not allocate TX descriptor chain DMA tag!：驱动无法为控制器 TX 链分配 DMA 标签。
- bce%d: Could not allocate TX descriptor chain DMA memory!：驱动无法为控制器 TX 链分配 DMA 可寻址内存。
- bce%d: Could not map TX descriptor chain DMA memory!：驱动无法将 TX 描述符链内存映射到控制器的 DMA 地址空间。
- bce%d: Could not allocate TX mbuf DMA tag!：驱动无法为控制器 TX mbuf 内存分配 DMA 标签。
- bce%d: Unable to create TX mbuf DMA map!：驱动无法将 TX mbuf 内存映射到控制器的 DMA 地址空间。
- bce%d: Could not allocate RX descriptor chain DMA tag!：驱动无法为控制器 RX 链分配 DMA 标签。
- bce%d: Could not allocate RX descriptor chain：驱动无法为控制器 RX 链分配 DMA 可寻址内存。
- bce%d: Could not map RX descriptor chain DMA memory!：驱动无法将 RX 描述符链内存映射到控制器的 DMA 地址空间。
- bce%d: Could not allocate RX mbuf DMA tag!：驱动无法为控制器 RX mbuf 内存分配 DMA 标签。
- bce%d: Unable to create RX mbuf DMA map!：驱动无法将 RX mbuf 内存映射到控制器的 DMA 地址空间。
- bce%d: Firmware synchronization timeout!：驱动无法与控制器上运行的固件同步。固件可能已停止或挂起。
- bce%d: Invalid Ethernet address!：驱动无法从 NVRAM 读取有效的以太网 MAC 地址。
- bce%d: Reset failed!：驱动遇到致命初始化错误。
- bce%d: Byte swap is incorrect!：驱动遇到致命初始化错误。请联系作者并提供所使用的 CPU 架构和系统芯片组的详细信息。
- bce%d: Firmware did not complete initialization!：驱动遇到致命初始化错误。
- bce%d: Bootcode not running!：驱动遇到致命初始化错误。
- bce%d: Error mapping mbuf into RX chain!：驱动无法将 RX mbuf 映射到 DMA 可寻址内存。
- bce%d: Error filling RX chain: rx_bd[0x%04X]!：驱动在初始化期间无法分配足够的 mbuf 填充 RX 链。尝试增加系统中可用的 mbuf 数量、增加系统内存，或如果使用巨型帧，确保有足够的 9KB mbuf 可用。
- bce%d: Failed to allocate new mbuf, incoming frame dropped!：驱动无法为 RX 链分配新 mbuf，并复用所接收帧的 mbuf，过程中丢弃传入帧。尝试增加系统中可用的 mbuf 数量或增加系统内存。
- bce%d: Controller reset failed!：发生致命初始化错误。
- bce%d: Controller initialization failed!：发生致命初始化错误。
- bce%d: Block initialization failed!：发生致命初始化错误。
- bce%d: Error mapping mbuf into TX chain!：驱动无法将 TX mbuf 映射到 DMA 可寻址内存。
- bce%d: Error registering poll function!：驱动在尝试注册轮询函数时收到错误。
- bce%d: Changing VLAN_MTU not supported.：驱动当前不支持更改 VLAN MTU。
- bce%d: Cannot change VLAN_HWTAGGING while management firmware (ASF/IPMI/UMP) is running!：支持 ASF/IPMI/UMP 的管理固件要求在控制器中启用 VLAN 标签剥离。
- bce%d: Changing VLAN_HWTAGGING not supported!：驱动当前不支持禁用 VLAN 标签剥离。
- bce%d: Watchdog timeout occurred, resetting!：设备已停止响应网络，电缆连接存在问题，或发生了驱动逻辑问题。
- bce%d: Fatal attention detected: 0x%08X!：发生控制器硬件故障。如果问题持续，请更换控制器。

## 支持

如需支持，请联系你的 QLogic 授权经销商或 QLogic 技术支持，网址 `http://support.qlogic.com`，或发送电子邮件至 <support@qlogic.com>。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`bce` 设备驱动首次出现于 FreeBSD 6.1。

## 作者

`bce` 驱动由 David Christensen <davidch@broadcom.com> 编写。
