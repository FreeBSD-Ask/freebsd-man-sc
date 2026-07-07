# dtsec(4)

`dtsec` — 基于 Freescale Datapath Acceleration Architecture 的三速以太网控制器设备驱动

## 名称

`dtsec`

## 概要

`要将此驱动编译进内核，请将以下行放入你的内核配置文件：`

> include dpaa/config.dpaa
> device dpaa
> device miibus

## 描述

`dtsec` 驱动为集成在某些 Freescale 片上系统设备中的基于 DPAA 的千兆以太网控制器提供支持。

`dtsec` 驱动支持以下媒体类型：

**autoselect** 启用媒体类型和选项的自动选择

**10baseT/UTP** 设置 10Mbps 操作

**100baseTX** 设置 100Mbps 操作

**1000baseT** 设置 1000baseT 操作

`dtsec` 驱动支持以下媒体选项：

**full-duplex** 设置全双工操作

`dtsec` 驱动支持两种操作模式：

**Regular** 正常模式，利用完整的数据路径加速、缓冲区管理器和队列管理器。

**Independent** 与缓冲区管理器和队列管理器断开运行。

## 硬件

已知以下 Freescale 片上系统设备中内置的千兆以太网控制器可与 `dtsec` 驱动配合工作：

- P2041、P3041
- P5010、P5020

此外，以下设备预期可工作，但未经测试：

- P4080、P4040
- P5040

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`dtsec` 设备驱动首次出现于 FreeBSD 11.0。

## 作者

`dtsec` 设备驱动的基础版本由 Semihalf 编写。本手册页由 Justin Hibbits 编写。
