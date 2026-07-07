# alc(4)

`alc` — Atheros AR813x/AR815x/AR816x/AR817x 千兆/快速以太网驱动

## 名称

`alc`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device alc

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_alc_load="YES"
```

## 描述

`alc` 设备驱动为 Atheros AR813x、AR815x、AR816x 和 AR817x PCI Express 千兆/快速以太网控制器提供支持。

`alc` 驱动支持的所有 LOM 都具有发送的 TCP/UDP/IP 校验和卸载、TCP 分段卸载（TSO）、硬件 VLAN 标签剥离/插入功能、网络唤醒（WOL）和中断适度机制，以及 64 位多播哈希过滤器。

AR813x、AR815x、AR816x 和 AR817x 支持 Jumbo Frames（分别为最大 9216、6144、9216 和 9216 字节），可通过接口 MTU 设置进行配置。通过 [ifconfig(8)](../man8/ifconfig.8.md) 实用程序选择大于 1500 字节的 MTU 可配置适配器收发 Jumbo Frames。

`alc` 驱动支持以下介质类型：

**`autoselect`** 启用介质类型和选项的自动选择。用户可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加介质选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。

**`1000baseTX`** 设置通过双绞线的 1000baseTX 操作。

`alc` 驱动支持以下介质选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`alc` 设备驱动支持以下以太网控制器：

- Atheros AR8131 PCI Express 千兆以太网控制器
- Atheros AR8132 PCI Express 快速以太网控制器
- Atheros AR8151 v1.0 PCI Express 千兆以太网控制器
- Atheros AR8151 v2.0 PCI Express 千兆以太网控制器
- Atheros AR8152 v1.1 PCI Express 快速以太网控制器
- Atheros AR8152 v2.0 PCI Express 快速以太网控制器
- Atheros AR8161 PCI Express 千兆以太网控制器
- Atheros AR8162 PCI Express 快速以太网控制器
- Atheros AR8171 PCI Express 千兆以太网控制器
- Atheros AR8172 PCI Express 快速以太网控制器
- Killer E2200 千兆以太网控制器
- Killer E2400 千兆以太网控制器
- Killer E2500 千兆以太网控制器

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`hw.alc.msi_disable`** 此可调参数禁用以太网硬件上的 MSI 支持。默认值为 0。

**`hw.alc.msix_disable`** 此可调参数禁用以太网硬件上的 MSI-X 支持。默认值为 2，表示根据卡类型启用或禁用 MSI-X；对于“Killer”卡（E2x00）将禁用 MSI-X，而对于其他卡将启用。将其设为 0 可强制启用 MSI-X，设为 1 可强制禁用 MSI-X（不论卡类型）。

## SYSCTL 变量

以下变量同时可作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数使用：

**`dev.alc.%d.int_rx_mod`** 延迟接收中断处理的最大时间（单位为 1 微秒）。接受范围为 0 至 130000，默认为 100（100 微秒）。值为 0 时完全禁用中断适度。

**`dev.alc.%d.int_tx_mod`** 延迟发送中断处理的最大时间（单位为 1 微秒）。接受范围为 0 至 130000，默认为 1000（1 毫秒）。值为 0 时完全禁用中断适度。

**`dev.alc.%d.process_limit`** 在重新调度 taskqueue 前于事件循环中处理的最大 Rx 帧数。接受范围为 32 至 255，默认值为 64 个事件。更改生效前无需将接口关闭再重新打开。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`alc` 驱动由 Pyun YongHyeon <yongari@FreeBSD.org> 编写。最早出现在 FreeBSD 8.0 中。
