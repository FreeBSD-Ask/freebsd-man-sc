# msk(4)

`msk` — Marvell/SysKonnect Yukon II 千兆以太网适配器驱动

## 名称

`msk`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device msk

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_msk_load="YES"
```

## 描述

`msk` 设备驱动为基于 Marvell/SysKonnect Yukon II 千兆以太网控制器芯片的各种 NIC 提供支持。

`msk` 驱动支持的所有 NIC 都具有发送和接收的 TCP/UDP/IP 校验和卸载、TCP 分段卸载（TSO）、硬件 VLAN 标签剥离/插入功能、中断适度机制以及 64 位多播哈希过滤器。Yukon II 支持 TBI（十位接口）和 GMII 收发器，这意味着它可用于铜缆或 1000baseX 光纤应用。

Yukon II 还支持 Jumbo Frames（最大 9022 字节），可通过接口 MTU 设置进行配置。通过 [ifconfig(8)](../man8/ifconfig.8.md) 实用程序选择大于 1500 字节的 MTU 可配置适配器收发 Jumbo Frames。

`msk` 驱动支持以下介质类型：

**`autoselect`** 启用介质类型和选项的自动选择。用户可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加介质选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`1000baseTX`** 设置通过双绞线的 1000baseTX 操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`1000baseSX`** 设置 1000Mbps（千兆以太网）操作。支持 `full-duplex` 和 `half-duplex` 模式。

`msk` 驱动支持以下介质选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`msk` 驱动为基于 Marvell/SysKonnect Yukon II 千兆以太网控制器芯片的各种 NIC 提供支持，包括：

- D-Link 550SX Gigabit Ethernet
- D-Link 560SX Gigabit Ethernet
- D-Link 560T Gigabit Ethernet
- Marvell Yukon 88E8021CU Gigabit Ethernet
- Marvell Yukon 88E8021 SX/LX Gigabit Ethernet
- Marvell Yukon 88E8022CU Gigabit Ethernet
- Marvell Yukon 88E8022 SX/LX Gigabit Ethernet
- Marvell Yukon 88E8061CU Gigabit Ethernet
- Marvell Yukon 88E8061 SX/LX Gigabit Ethernet
- Marvell Yukon 88E8062CU Gigabit Ethernet
- Marvell Yukon 88E8062 SX/LX Gigabit Ethernet
- Marvell Yukon 88E8035 Fast Ethernet
- Marvell Yukon 88E8036 Fast Ethernet
- Marvell Yukon 88E8038 Fast Ethernet
- Marvell Yukon 88E8039 Fast Ethernet
- Marvell Yukon 88E8040 Fast Ethernet
- Marvell Yukon 88E8040T Fast Ethernet
- Marvell Yukon 88E8042 Fast Ethernet
- Marvell Yukon 88E8048 Fast Ethernet
- Marvell Yukon 88E8050 Gigabit Ethernet
- Marvell Yukon 88E8052 Gigabit Ethernet
- Marvell Yukon 88E8053 Gigabit Ethernet
- Marvell Yukon 88E8055 Gigabit Ethernet
- Marvell Yukon 88E8056 Gigabit Ethernet
- Marvell Yukon 88E8057 Gigabit Ethernet
- Marvell Yukon 88E8058 Gigabit Ethernet
- Marvell Yukon 88E8059 Gigabit Ethernet
- Marvell Yukon 88E8070 Gigabit Ethernet
- Marvell Yukon 88E8071 Gigabit Ethernet
- Marvell Yukon 88E8072 Gigabit Ethernet
- Marvell Yukon 88E8075 Gigabit Ethernet
- SysKonnect SK-9Sxx Gigabit Ethernet
- SysKonnect SK-9Exx Gigabit Ethernet

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`hw.msk.msi_disable`** 此可调参数禁用以太网硬件上的 MSI 支持。默认值为 0。

## SYSCTL 变量

以下变量同时可作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数使用：

**`dev.mskc.%d.int_holdoff`** 延迟中断处理的最大时间。对于 125MHz 时钟，有效范围为 0 至 34359738，单位为 1 微秒，默认为 100（100 微秒）。更改生效前需要将接口关闭再重新打开。

**`dev.mskc.%d.process_limit`** 在重新调度 taskqueue 前于事件循环中处理的最大 Rx 事件数。接受范围为 30 至 256，默认值为 128 个事件。更改生效前无需将接口关闭再重新打开。

## 参见

[altq(4)](altq.4.md), [arp(4)](arp.4.md), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`msk` 驱动由 Pyun YongHyeon <yongari@FreeBSD.org> 编写，基于 [sk(4)](sk.4.md) 和 Marvell 的 FreeBSD 驱动。最早出现在 FreeBSD 7.0 和 FreeBSD 6.3 中。
