# stge.4

`stge` — Sundance/Tamarack TC9021 千兆以太网适配器驱动

## 名称

`stge`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device stge

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_stge_load="YES"
```

## 描述

`stge` 设备驱动为基于 Sundance/Tamarack TC9021 千兆以太网控制器芯片的各种 NIC 提供支持。

Sundance/Tamarack TC9021 见于 D-Link DGE-550T 和 Antares Microsystems 千兆以太网板卡。它使用外部 PHY 或外部 10 位接口。

`stge` 驱动支持的所有 NIC 都具有收发的 TCP/UDP/IP 校验和卸载、硬件 VLAN 标签剥离/插入功能、接收中断适度机制以及 64 位多播哈希过滤器。Sundance/Tamarack TC9021 支持 TBI（十位接口）和 GMII 收发器，这意味着它可用于铜缆或 1000baseX 光纤应用。

Sundance/Tamarack TC9021 还支持 jumbo frames，可通过接口 MTU 设置进行配置。通过 [ifconfig(8)](../man8/ifconfig.8.md) 实用程序选择大于 1500 字节的 MTU 可配置适配器收发 jumbo frames。

`stge` 驱动支持以下介质类型：

**`autoselect`** 启用介质类型和选项的自动选择。用户可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加介质选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。还可使用 [ifconfig(8)](../man8/ifconfig.8.md) `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。还可使用 [ifconfig(8)](../man8/ifconfig.8.md) `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`1000baseTX`** 设置通过双绞线的 1000baseTX 操作。Sundance/Tamarack 仅在 `autoselect` 模式下支持 1000Mbps。

`stge` 驱动支持以下介质选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`stge` 驱动为基于 Sundance/Tamarack TC9021 的千兆以太网控制器芯片的各种 NIC 提供支持，包括：

- Antares Microsystems Gigabit Ethernet
- ASUS NX1101 Gigabit Ethernet
- D-Link DL-4000 Gigabit Ethernet
- IC Plus IP1000A Gigabit Ethernet
- Sundance ST-2021 Gigabit Ethernet
- Sundance ST-2023 Gigabit Ethernet
- Sundance TC9021 Gigabit Ethernet
- Tamarack TC9021 Gigabit Ethernet

## SYSCTL 变量

以下变量同时可作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数使用：

**`dev.stge.%d.rxint_nframe`** 两次 RxDMAComplete 中断之间的帧数。接受范围为 1 至 255，默认值为 8 帧。更改生效前需将接口关闭再重新打开。

**`dev.stge.%d.rxint_dmawait`** 在接收帧数少于 `rxint_nframe` 时，发出 Rx 中断前等待的最大时间（以 1us 为增量）。接受范围为 0 至 4194，默认值为 30 微秒。更改生效前需将接口关闭再重新打开。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [polling(4)](polling.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`stge` 驱动从 NetBSD 移植，最早出现于 FreeBSD 6.2。NetBSD 版本由 Jason R. Thorpe <thorpej@NetBSD.org> 编写。

## 作者

`stge` 驱动由 Pyun YongHyeon <yongari@FreeBSD.org> 移植。
