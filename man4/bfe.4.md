# bfe(4)

`bfe` — Broadcom BCM4401 以太网设备驱动

## 名称

`bfe`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> device miibus
> device bfe

或者，要在引导时以模块形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行：

```sh
if_bfe_load="YES"
```

## 弃用通知

`bfe` 驱动已不再维护，可能在未来的 FreeBSD 版本中被移除。

## 描述

`bfe` 驱动为基于 Broadcom BCM4401 的快速以太网适配器提供支持。

`bfe` 驱动支持以下媒体类型：

**`autoselect`** 启用媒体类型和选项的自动选择。

**`10baseT/UTP`** 设置 10Mbps 操作。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。

`bfe` 驱动支持以下媒体选项：

**`full-duplex`** 设置全双工操作。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 诊断

- bfe%d: couldn't map memory：发生致命初始化错误。
- bfe%d: couldn't map interrupt：发生致命初始化错误。
- bfe%d: failed to allocate DMA resources：没有足够的 mbuf 可供分配。
- bfe%d: watchdog timeout -- resetting：设备已停止响应网络，或网络连接（电缆）存在问题。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`bfe` 设备驱动首次出现于 FreeBSD 5.1。

## 作者

`bfe` 设备驱动由 Stuart Walsh 和 Duncan Barclay 编写。本手册页由 Stuart Walsh 编写。
