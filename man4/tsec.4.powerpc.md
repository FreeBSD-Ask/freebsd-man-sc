# `tsec(4)`

`tsec` — Freescale 三速以太网控制器设备驱动程序

## 名称

`tsec`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device tsec
> device miibus

## 描述

`tsec` 驱动为某些 Freescale 片上系统设备中集成的千兆以太网控制器提供支持。

`tsec` 驱动支持以下媒体类型：

**autoselect** 启用媒体类型和选项的自动选择

**10baseT/UTP** 设置 10Mbps 操作

**100baseTX** 设置 100Mbps 操作

**1000baseT** 设置 1000baseT 操作

`tsec` 驱动支持以下媒体选项：

**full-duplex** 设置全双工操作

当系统配置了 DEVICE_POLLING 内核选项时，`tsec` 驱动支持轮询操作，详见 [polling(4)](polling.4.md)。

`tsec` 驱动支持 [vlan(4)](vlan.4.md) 的扩展帧接收和传输。`tsec` 的此能力可通过 [ifconfig(8)](../man8/ifconfig.8.md) 的 `vlanmtu` 参数控制。

`tsec` 驱动支持中断合并（IC），以便在可能的情况下延迟发送接收/发送帧中断，直到阈值定义的时间段过去或达到阈值定义的帧计数（以先到者为准）。以下 sysctl 调节此行为：

**`dev.tsec.X.int_coal.rx_time`**

**`dev.tsec.X.int_coal.rx_count`**

**`dev.tsec.X.int_coal.tx_time`**

**`dev.tsec.X.int_coal.tx_count`** 时间或计数的值为 0 时禁用给定路径上的 IC。时间值 1-65535 对应于实际时间段，以等同于 TSEC 时钟 64 个滴答的单位表示。计数 1-255 表示帧数（注意值为 1 等同于禁用 IC）。用户提供的值如果大于支持的值，将被修剪到最大支持值。更多详情可参阅设备参考手册。

## 硬件

已知以下 Freescale 片上系统设备中内置的千兆以太网控制器可与 `tsec` 驱动一起工作：

- MPC8349
- MPC8533, MPC8541, MPC8555

以下设备中集成的控制器增强版本（eTSEC）也受此驱动支持：

- MPC8548, MPC8572

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [polling(4)](polling.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`tsec` 设备驱动首次出现于 FreeBSD 8.0。

## 作者

`tsec` 设备驱动的基础版本由 Piotr Kruszynski 编写。Rafal Jaworowski 扩展了轮询和中断合并支持。Piotr Ziecik 进一步增强了多播、硬件校验和计算和 VLAN 支持。本手册页由 Rafal Jaworowski 编写。
