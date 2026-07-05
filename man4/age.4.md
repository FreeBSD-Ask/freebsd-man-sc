# age.4

`age` — Attansic/Atheros L1 千兆以太网驱动

## 名称

`age`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device age

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_age_load="YES"
```

## 描述

`age` 设备驱动为 Attansic/Atheros L1 PCI Express 千兆以太网控制器提供支持。

`age` 驱动支持的所有 LOM 都具有发送和接收的 TCP/UDP/IP 校验和卸载、TCP 分段卸载（TSO）、硬件 VLAN 标签剥离/插入功能、中断适度机制以及 64 位多播哈希过滤器。

L1 还支持 Jumbo Frames（最大 10240 字节），可通过接口 MTU 设置进行配置。通过 [ifconfig(8)](../man8/ifconfig.8.md) 实用程序选择大于 1500 字节的 MTU 可配置适配器收发 Jumbo Frames。

`age` 驱动支持以下介质类型：

**`autoselect`** 启用介质类型和选项的自动选择。用户可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加介质选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。

**`1000baseTX`** 设置通过双绞线的 1000baseTX 操作。

`age` 驱动支持以下介质选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`age` 驱动为基于 Attansic/Atheros L1 千兆以太网控制器芯片的 LOM 提供支持，包括：

- ASUS M2N8-VMX
- ASUS M2V
- ASUS M3A
- ASUS P2-M2A590G
- ASUS P5B-E
- ASUS P5B-MX/WIFI-AP
- ASUS P5B-VMSE
- ASUS P5K
- ASUS P5KC
- ASUS P5KPL-C
- ASUS P5KPL-VM
- ASUS P5K-SE
- ASUS P5K-V
- ASUS P5L-MX
- ASUS P5DL2-VM
- ASUS P5L-VM 1394
- ASUS G2S

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`hw.age.msi_disable`** 此可调参数禁用以太网硬件上的 MSI 支持。默认值为 0。

**`hw.age.msix_disable`** 此可调参数禁用以太网硬件上的 MSI-X 支持。默认值为 0。

## SYSCTL 变量

以下变量同时可作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数使用：

**`dev.age.%d.int_mod`** 延迟中断处理的最大时间（单位为 2 微秒）。接受范围为 0 至 65000，默认为 50（100 微秒）。值为 0 时完全禁用中断适度。

**`dev.age.%d.process_limit`** 在重新调度 taskqueue 前于事件循环中处理的最大 Rx 事件数。接受范围为 30 至 255，默认值为 128 个事件。更改生效前无需将接口关闭再重新打开。

**`dev.age.%d.stats`** 显示驱动维护的许多有用 MAC 计数器。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`age` 驱动由 Pyun YongHyeon <yongari@FreeBSD.org> 编写。最早出现在 FreeBSD 7.1 中。
