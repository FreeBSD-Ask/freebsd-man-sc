# rge(4)

`rge` — RealTek RTL8125/RTL8126/RTL8127/Killer E3000 PCIe 以太网适配器驱动

## 名称

`rge`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device rge

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_rge_load="YES"
```

## 描述

`rge` 驱动为基于 RealTek RTL8125、RTL8126 和 RTL8127 PCIe 以太网控制器的各种 NIC 提供支持。

此驱动支持的所有 NIC 都可在 CAT5 电缆上以 10、100 和 1000Mbit 速率运行。基于 RTL8125 的 NIC 还支持通过 CAT6 电缆的 2.5Gbit 速率。基于 RTL8126 的 NIC 还支持通过 CAT6 电缆的 2.5Gbit 和 5Gbit 速率。基于 RTL8127 的 NIC 还支持通过 CAT6 电缆的 2.5Gbit、5Gbit 和 10Gbit 速率。

`rge` 驱动支持的所有 NIC 都具有 TCP/IP 校验和卸载、硬件 VLAN 标签/插入功能、局域网唤醒（WOL），并使用基于描述符的 DMA 机制。它们还支持 TCP 大发送（TCP 分段卸载）。

RTL8125、RTL8126 和 RTL8127 器件是单芯片方案，集成了 MAC 和 PHY。`rge` 驱动直接管理 PHY，而不使用 [miibus(4)](miibus.4.md) 接口。独立卡有 1x PCIe 型号。

RTL8125、RTL8126 和 RTL8127 还支持 jumbo frames，可通过接口 MTU 设置进行配置。MTU 上限为 9126。通过 [ifconfig(8)](../man8/ifconfig.8.md) 实用程序选择大于 1500 字节的 MTU 可配置适配器收发 jumbo frames。

`rge` 驱动支持以下介质类型：

**`autoselect`** 启用介质类型和选项的自动选择。用户可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加介质选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`1000baseT`** 设置通过双绞线的 1000baseT 操作。RealTek 千兆芯片仅在 `full-duplex` 模式下支持 1000Mbps。

**`2500Base-T`** 设置通过双绞线的 2500Base-T 操作。RealTek 器件仅在 `full-duplex` 模式下支持 2.5Gbit。

**`5000Base-T`** 设置通过双绞线的 5000Base-T 操作。RealTek 器件仅在 `full-duplex` 模式下支持 5Gbit。

**`10Gbase-T`** 设置通过双绞线的 10Gbase-T 操作。RealTek 器件仅在 `full-duplex` 模式下支持 10Gbit。

`rge` 驱动支持以下介质选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`rge` 驱动支持以下 PCIe 以太网适配器：

- RealTek RTL8125（最高 2.5 Gbps）
- RealTek RTL8126（最高 5 Gbps）
- RealTek RTL8127（最高 10 Gbps）
- Killer E3000（最高 2.5 Gbps）
- Killer E5000（最高 5 Gbps）

## SYSCTL 变量

以下变量同时可作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数使用：

**`dev.rge.%d.debug`** 配置运行时调试输出。这是一个 32 位位掩码。

**`dev.rge.%d.rx_process_limit`** 每次中断处理的最大 RX 数据包数。默认值为 16。增大此值可提高高速链路上的吞吐量，但会增加中断延迟。

**`dev.rge.%d.disable_aspm`** 禁用 PCIe 活动状态电源管理（ASPM）和扩展配置电源管理（ECPM）。默认值为 0（保持 ASPM 启用）。设置为 1 可降低延迟，但会增加功耗。此可调参数只能在 loader.conf(5) 中设置，需要重启才能生效。

## 诊断

- rge%d: watchdog timeout 设备已停止响应网络，或网络连接（电缆）存在问题。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [polling(4)](polling.4.md), [re(4)](re.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`rge` 设备驱动最早出现在 FreeBSD 16.0 中。

## 作者

`rge` 驱动由 Kevin Lo <kevlo@openbsd.org> 编写，并由 Adrian Chadd <adrian@freebsd.org> 移植至 FreeBSD。
