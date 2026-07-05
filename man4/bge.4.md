# bge.4

`bge` — Broadcom BCM57xx/BCM590x 千兆/快速以太网驱动

## 名称

`bge`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> device miibus
> device bge

或者，要在引导时以模块形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行：

```sh
if_bge_load="YES"
```

## 描述

`bge` 驱动为基于 Broadcom BCM570x、571x、572x、575x、576x、578x、5776x 和 5778x 千兆以太网控制器芯片以及 590x 和 5779x 快速以太网控制器芯片的各种 NIC 提供支持。

除 SysKonnect SK-9D41 仅支持多模光纤上的 1000Mbps 外，所有这些 NIC 都能通过 CAT5 铜缆以 10、100 和 1000Mbps 速率工作。BCM570x 建立在 Alteon Tigon II 技术之上。它具有两个 R4000 CPU 核心，兼容 PCI v2.2 和 PCI-X v1.0。它支持接收和发送的 IP、TCP 和 UDP 校验和卸载、用于 QoS 应用的多个 RX 和 TX DMA 环、基于规则的接收过滤，以及 VLAN 标签剥离/插入和 256 位多播哈希过滤器。可通过增值固件更新提供额外功能。BCM570x 支持 TBI（十位接口）和 GMII 收发器，意味着可用于铜缆或 1000baseX 光纤应用。但注意该设备在 TBI 模式下仅支持单一速率。

大多数基于 BCM5700 的卡还使用 Broadcom BCM5401 或 BCM5411 10/100/1000 铜缆千兆收发器，支持全双工或半双工下 10、100 和 1000Mbps 模式的自动协商。

BCM5700、BCM5701、BCM5702、BCM5703、BCM5704、BCM5714、BCM5717、BCM5719、BCM5720、BCM5780 和 BCM57765 还支持巨型帧，可通过接口 MTU 设置进行配置。使用 [ifconfig(8)](../man8/ifconfig.8.md) 选择大于 1500 字节的 MTU 会将适配器配置为接收和发送巨型帧。使用巨型帧可大幅提升某些任务的性能，如文件传输和数据流。

`bge` 驱动支持以下媒体类型：

**`autoselect`** 启用媒体类型和选项的自动选择。用户可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加媒体选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`1000baseTX`** 设置双绞线上的 1000baseTX 操作。仅支持 `full-duplex` 模式。

**`1000baseSX`** 设置 1000Mbps（千兆以太网）操作。支持 `full-duplex` 和 `half-duplex` 模式。

`bge` 驱动支持以下媒体选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`bge` 驱动为基于 Broadcom BCM570x 系列千兆以太网控制器芯片的各种 NIC 提供支持，包括：

- 3Com 3c996-SX（1000baseSX）
- 3Com 3c996-T（10/100/1000baseTX）
- Apple Thunderbolt Display（10/100/1000baseTX）
- Apple Thunderbolt to Gigabit Ethernet Adapter（10/100/1000baseTX）
- Dell PowerEdge 1750 integrated BCM5704C NIC（10/100/1000baseTX）
- Dell PowerEdge 2550 integrated BCM5700 NIC（10/100/1000baseTX）
- Dell PowerEdge 2650 integrated BCM5703 NIC（10/100/1000baseTX）
- Dell PowerEdge R200 integrated BCM5750 NIC（10/100/1000baseTX）
- Dell PowerEdge R300 integrated BCM5722 NIC（10/100/1000baseTX）
- IBM x235 server integrated BCM5703x NIC（10/100/1000baseTX）
- HP Compaq dc7600 integrated BCM5752 NIC（10/100/1000baseTX）
- HP ProLiant NC7760 embedded Gigabit NIC（10/100/1000baseTX）
- HP ProLiant NC7770 PCI-X Gigabit NIC（10/100/1000baseTX）
- HP ProLiant NC7771 PCI-X Gigabit NIC（10/100/1000baseTX）
- HP ProLiant NC7781 embedded PCI-X Gigabit NIC（10/100/1000baseTX）
- Netgear GA302T（10/100/1000baseTX）
- SysKonnect SK-9D21（10/100/1000baseTX）
- SysKonnect SK-9D41（1000baseSX）

## 加载器可调参数

以下可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`hw.bge.allow_asf`** 允许 ASF 功能与 IPMI 协同工作。在少数系统上可能导致系统锁定问题。默认启用。

**`dev.bge.%d.msi`** 非零值在以太网硬件上启用 MSI 支持。默认值为 1。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`dev.bge.%d.forced_collapse`** 允许将多个发送缓冲区合并为单个缓冲区，以增加发送性能，但代价是消耗 CPU 周期。默认值为 0，即禁用发送缓冲区合并。

**`dev.bge.%d.forced_udpcsum`** 即使控制器可能生成校验和值为 0 的 UDP 数据报，也启用 UDP 发送校验和卸载。校验和值为 0 的 UDP 数据报可能使接收方主机困惑，因为这表示发送方未计算 UDP 校验和。默认值为 0，即禁用 UDP 发送校验和卸载。更改生效前需将接口先关闭再重新启用。

## 诊断

- bge%d: couldn't map memory：发生致命初始化错误。
- bge%d: couldn't map ports：发生致命初始化错误。
- bge%d: couldn't map interrupt：发生致命初始化错误。
- bge%d: no memory for softc struct!：驱动在初始化期间无法为每设备实例信息分配内存。
- bge%d: failed to enable memory mapping!：驱动无法初始化 PCI 共享内存映射。这可能发生在卡不在总线主控插槽中的情况。
- bge%d: firmware handshake timed out, found 0xffffffff：设备已从系统物理断开，或设备存在问题导致其停止响应所连接的主机。
- bge%d: no memory for jumbo buffers!：驱动在初始化期间无法为巨型帧分配内存。
- bge%d: watchdog timeout：设备已停止响应网络，或网络连接（电缆）存在问题。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [polling(4)](polling.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`bge` 设备驱动首次出现于 FreeBSD 4.5。

## 作者

`bge` 驱动由 Bill Paul <wpaul@windriver.com> 编写。

## 缺陷

FreeBSD 当前不支持热插拔，因此在 Apple 系统上，Thunderbolt 接口必须在系统开机前连接，接口才能被检测到。同时，由于缺乏热插拔支持，系统运行期间不得移除基于 Thunderbolt 的接口，因为内核当前无法处理 `bge` 接口消失的情况。

UDP 发送校验和卸载默认禁用，参见 `dev.bge.%d.forced_udpcsum`。为避免接口作为 [bridge(4)](bridge.4.md) 接口成员时出现问题，这种情况下所有发送校验和卸载初始均为禁用。可使用 [ifconfig(8)](../man8/ifconfig.8.md) 启用发送校验和卸载。
