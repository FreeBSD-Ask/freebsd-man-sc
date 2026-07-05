# ale.4

`ale` — Atheros AR8121/AR8113/AR8114 千兆/快速以太网驱动

## 名称

`ale`

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device miibus
> device ale

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_ale_load="YES"
```

## 描述

`ale` 设备驱动为 Atheros AR8121 PCI Express 千兆以太网控制器以及 Atheros AR8113/AR8114 PCI Express 快速以太网控制器提供支持。

`ale` 驱动支持的所有 LOM 在接收和发送两方面均具有 TCP/UDP/IP 校验和卸载、TCP 分段卸载（TSO）、硬件 VLAN 标签剥离/插入功能、局域网唤醒（WOL）以及中断合并/调节机制，此外还有 64 位多播哈希过滤器。

AR8121 还支持 Jumbo 帧（最大 8132 字节），可通过接口 MTU 设置进行配置。使用 [ifconfig(8)](../man8/ifconfig.8.md) 工具选择大于 1500 字节的 MTU 可将适配器配置为收发 Jumbo 帧。

`ale` 驱动支持以下媒体类型：

**`autoselect`** 启用媒体类型和选项的自动选择。用户可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中加入媒体选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。

**`1000baseTX`** 设置通过双绞线进行的 1000baseTX 操作。

`ale` 驱动支持以下媒体选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`ale` 设备驱动为以下以太网控制器提供支持：

- Atheros AR8113 PCI Express 快速以太网控制器
- Atheros AR8114 PCI Express 快速以太网控制器
- Atheros AR8121 PCI Express 千兆以太网控制器

## 加载器可调参数

可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符处设置可调参数，或将其存放在 loader.conf(5) 中。

**`hw.ale.msi_disable`** 此可调参数禁用以太网硬件上的 MSI 支持。默认值为 0。

**`hw.ale.msix_disable`** 此可调参数禁用以太网硬件上的 MSI-X 支持。默认值为 0。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数提供：

**`dev.ale.%d.int_rx_mod`** 延迟接收中断处理的最大时间量，单位为 1 微秒。可接受范围为 0 到 130000，默认值为 30（30 微秒）。值为 0 时完全禁用中断调节。

**`dev.ale.%d.int_tx_mod`** 延迟发送中断处理的最大时间量，单位为 1 微秒。可接受范围为 0 到 130000，默认值为 1000（1 毫秒）。值为 0 时完全禁用中断调节。

**`dev.ale.%d.process_limit`** 在重新调度 taskqueue 之前，事件循环中处理的最大接收帧数。可接受范围为 32 到 255，默认值为 128 个事件。修改此参数后无需将接口先停用再启用即可生效。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`ale` 驱动由 Pyun YongHyeon <yongari@FreeBSD.org> 编写。它首次出现于 FreeBSD 7.1。
