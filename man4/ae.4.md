# ae.4

`ae` — Attansic/Atheros L2 快速以太网控制器驱动

## 名称

`ae`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device ae

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_ae_load="YES"
```

## 描述

`ae` 设备驱动为 Attansic/Atheros L2 PCIe 快速以太网控制器提供支持。

该控制器支持硬件以太网校验和处理、硬件 VLAN 标签剥离/插入以及中断适度机制。Attansic L2 还具有 64 位多播哈希过滤器。

`ae` 驱动支持以下介质类型：

**`autoselect`** 启用介质类型和选项的自动选择。用户可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加介质选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 选择 10Mbps 操作。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。

`ae` 驱动支持以下介质选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`ae` 驱动支持 Attansic/Atheros L2 PCIe 快速以太网控制器，已知支持以下硬件：

- ASUS EeePC 701
- ASUS EeePC 900

其他硬件可能可以也可能不与此驱动一起工作。

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`hw.ae.msi_disable`** 此可调参数禁用以太网硬件上的 MSI 支持。默认值为 0。

## SYSCTL 变量

`ae` 驱动在工作期间收集若干有用的 MAC 计数器。统计信息可通过 `dev.ae.%d.stats` [sysctl(8)](../man8/sysctl.8.md) 树访问，其中 %d 对应控制器编号。

## 诊断

- ae%d: watchdog timeout。设备已停止响应网络，或网络连接（电缆）存在问题。
- ae%d: reset timeout。卡重置操作已超时。
- ae%d: Generating random ethernet address。在控制器 NVRAM 和寄存器中未找到有效的以太网地址。将改用带有 ASUS OUI 标识符的随机本地管理地址。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`ae` 驱动及本手册页由 Stanislav Sedov <stas@FreeBSD.org> 编写。最早出现在 FreeBSD 7.1 中。

## 缺陷

Attansic L2 快速以太网控制器支持 DMA，但不使用通过分散-聚集 DMA 的基于描述符的传输机制。因此每次发送/接收时都需要将数据复制到/从控制器内存。此外，还存在许多数据对齐限制。这可能在网络活动密集的系统上引入高 CPU 负载。幸运的是，由于 L2 不支持高于 100Mbps 的速度，这在现代硬件上不应成为问题。
