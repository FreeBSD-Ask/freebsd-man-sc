# sume(4)

`sume` — NetFPGA SUME 4x10Gb 以太网驱动

## 名称

`sume`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device sume

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_sume_load="YES"
```

## 描述

`sume` 驱动为加载了参考 NIC 比特流的 NetFPGA SUME Virtex-7 FPGA 开发板提供支持。参考 NIC 项目的 HDL 设计使用基于 RIFFA 的 DMA 引擎通过 PCIe 与主机通信。每个数据包通过单次 DMA 事务向/从板卡传输，每次事务占用两到三次中断，导致性能较低。

不支持 jumbo frames，因为硬件只能处理最大 1514 字节的帧。硬件不支持多播过滤，不提供校验和，也不提供其他卸载功能。

## 参见

arp(4), [netgraph(4)](netgraph.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 作者

Linux `sume` 驱动最初由 Bjoern A. Zeeb 编写。FreeBSD 版本由 Denis Salopek 作为 GSoC 项目编写。有关该项目的更多信息可在此处找到：`https://wiki.freebsd.org/SummerOfCode2020Projects/NetFPGA_SUME_Driver`

## 缺陷

参考 NIC 硬件设计未提供机制来静止来自配置为 DOWN 的接口的入站流量。所有来自被管理性禁用接口的数据包都会被传输到主内存，驱动不得不丢弃这些数据包，从而徒劳地消耗 PCI 带宽、中断和 CPU 周期。

来自 NetFPGA 项目的预构建 FPGA 比特流可能无法正常工作。在较高的 RX 数据包速率下，新到达的数据包会覆盖内部 FIFO 中的已有数据包，导致数据包到达主内存时已损坏，直到对板卡进行物理重置。

偶尔，由于遗漏中断，驱动可能卡在非 IDLE TX 状态。驱动包含一个看门狗功能，可监视此类情况并自动重置板卡。更多细节请访问 NetFPGA SUME 项目站点。
