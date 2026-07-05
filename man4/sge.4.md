# sge.4

`sge` — Silicon Integrated Systems SiS190/191 快速/千兆以太网驱动

## 名称

`sge`

## 概要

`要将此驱动编译进内核，请将以下行添加到你的内核配置文件中：`

> device miibus
> device sge

`或者，要在引导时以模块形式加载此驱动，请将以下行添加到 loader.conf(5) 中：`

```sh
if_sge_load="YES"
```

## 描述

`sge` 设备驱动为 SiS190 快速以太网控制器和 SiS191 快速/千兆以太网控制器提供支持。

`sge` 驱动支持的所有 LOM 都具有发送和接收的 TCP/UDP/IP 校验和卸载、TCP 分段卸载（TSO）、硬件 VLAN 标签剥离/插入功能。由于缺乏文档，网络唤醒（WOL）、jumbo 帧和中断节流机制暂不支持。

`sge` 驱动支持以下媒体类型：

**`autoselect`** 启用媒体类型和选项的自动选择。用户可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加媒体选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。

**`1000baseTX`** 设置通过双绞线的 1000baseTX 操作。

`sge` 驱动支持以下媒体选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`sge` 设备驱动支持以下以太网控制器：

- SiS190 快速以太网控制器
- SiS191 快速/千兆以太网控制器

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [rgephy(4)](rgephy.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`sge` 驱动由 Alexander Pohoyda <alexander.pohoyda@gmx.net> 编写，并由 Nikolay Denev <ndenev@gmail.com> 增强。最早出现于 FreeBSD 8.1。
