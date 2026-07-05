# vte.4

`vte` — Vortex86 RDC R6040 快速以太网驱动

## 名称

`vte`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device vte

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_vte_load="YES"
```

## 描述

`vte` 设备驱动为常见于 Vortex86 片上系统（SoC）的 RDC R6040 快速以太网控制器提供支持。

RDC R6040 集成了 10/100 PHY，支持全双工或半双工的 10/100Mbps 操作。该控制器支持中断适度机制、64 位多播哈希过滤器、VLAN 超大帧以及四个站点地址。`vte` 设备驱动使用四个站点地址中的三个作为完美多播过滤器。

`vte` 驱动支持以下介质类型：

**`autoselect`** 启用介质类型和选项的自动选择。用户可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加介质选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。

`vte` 驱动支持以下介质选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`vte` 设备驱动为以下以太网控制器提供支持：

- DM&P Vortex86 RDC R6040 快速以太网控制器

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`hw.vte.tx_deep_copy`** RDC R6040 控制器对短帧没有自动填充支持，且控制器的 DMA 引擎无法为 TX 帧处理多个缓冲区，因此驱动必须创建单个连续的 TX 缓冲区。此硬件限制导致 TX 性能较差，因为大多数 CPU 周期都浪费在 mbuf 链的去碎片化和填充上。此可调参数为 TX 帧启用深度复制操作，使驱动在去碎片化上花费更少的 CPU 周期，代价是额外的 TX 缓冲区内存。默认值为 1，使用深度复制。

## SYSCTL 变量

以下变量同时可作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数使用：

**`dev.vte.%d.rx_mod`** 触发 RX 完成中断的最大数据包数。接受范围为 0 至 15，默认为 15。

**`dev.vte.%d.tx_mod`** 触发 TX 完成中断的最大数据包数。接受范围为 0 至 15，默认为 15。

**`dev.vte.%d.stats`** 显示驱动中维护的硬件 MAC 统计信息。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

> "DM&P Electronics Inc. Vortex86".

## 历史

`vte` 驱动由 Pyun YongHyeon <yongari@FreeBSD.org> 编写。最早出现在 FreeBSD 8.3 中。
