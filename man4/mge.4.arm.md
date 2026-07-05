# `mge(4)`

`mge` — Marvell 千兆以太网设备驱动

## 名称

`mge`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device mge
> device miibus

## 描述

`mge` 驱动提供对集成于 Marvell 系统级芯片设备中的千兆以太网控制器的支持。

`mge` 驱动支持以下媒体类型：

**autoselect** 启用媒体类型和选项的自动选择

**10baseT/UTP** 设置 10Mbps 操作

**100baseTX** 设置 100Mbps 操作

**1000baseT** 设置 1000baseT 操作

`mge` 驱动支持以下媒体选项：

**full-duplex** 设置全双工操作

当系统配置了 DEVICE_POLLING 内核选项时，`mge` 驱动支持轮询操作，更多详情请参见 [polling(4)](polling.4.md)。

`mge` 驱动支持 [vlan(4)](vlan.4.md) 的扩展帧接收和传输。`mge` 的此功能可通过 [ifconfig(8)](../man8/ifconfig.8.md) 的 `vlanmtu` 参数控制。

`mge` 驱动支持中断合并（IC），以便在可能的情况下延迟引发发送/接收帧中断，直到超过阈值定义的时间段。以下 sysctl 调节此行为（每个路径单独设置）：

**`dev.mge.X.int_coal.rx_time`**

**`dev.mge.X.int_coal.tx_time`** 值为 0 时禁用给定路径上的 IC，大于零的值对应于实际时间段，以 MGE 时钟的 64 个滴答为单位表示。允许的最大值取决于 MGE 硬件版本。用户提供的值如果大于支持的值，将被修剪为支持的最大值。更多详情可参见设备的参考手册。

## 硬件

已知以下 Marvell 系统级芯片中内置的千兆以太网控制器可与 `mge` 驱动一起工作：

- Orion 88F5182
- Orion 88F5281
- Kirkwood 88F6281 (MGE V2)
- Discovery MV78100 (MGE V2)

还有一些用于 PowerPC 处理器的 Marvell 系统控制器，其中包括片上集成的此千兆以太网模块的变体，它们也应能与 `mge` 驱动一起工作，但未经测试：

- MV64430
- MV64460, MV64461, MV64462

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [polling(4)](polling.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`mge` 设备驱动首次出现于 FreeBSD 8.0。

## 作者

`mge` 设备驱动的基础版本由 Grzegorz Bernacki 编写。Piotr Ziecik 为其扩展了高级功能（轮询、中断合并、多播、硬件校验和计算等）。本手册页由 Rafal Jaworowski 编写。
