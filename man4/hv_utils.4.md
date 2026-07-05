# hv_utils.4

`hv_utils` — Hyper-V 实用工具驱动

## 名称

`hv_utils`

## 概要

`要将此驱动编译进内核，请在系统内核配置文件中加入以下行：`

> device hyperv

## 描述

`hv_utils` 驱动为运行于 Hyper-V 上的 FreeBSD 客户机分区提供时间保持、关闭和心跳功能。Hyper-V 是 Microsoft 提供的基于 hypervisor 的虚拟化技术。`hv_utils` 驱动是运行于 Hyper-V 上的客户机分区中必须存在的核心驱动之一。此驱动为客户机分区提供以下功能：

(a) 时间保持：通过 Timesync 服务和可插拔时间源设备的帮助，客户机分区内的时钟与虚拟化服务器上的时钟同步，从而保持准确。

(b) 集成关闭：运行 FreeBSD 的客户机分区可通过 Hyper-V 管理器控制台使用"关闭"命令进行关机。

(c) 心跳：此功能允许虚拟化服务器检测客户机分区是否正在运行且有响应。

## 参见

hv_ata_pci_disengage(4), [hv_netvsc(4)](hv_netvsc.4.md), [hv_storvsc(4)](hv_storvsc.4.md), [hv_vmbus(4)](hv_vmbus.4.md)

## 历史

`hv_utils` 的支持最早出现在 FreeBSD 10.0 中。该驱动由 Citrix Incorporated、Microsoft Corporation 和 Network Appliance Incorporated 联合开发。

## 作者

`hv_utils` 的 FreeBSD 支持最早由 Microsoft BSD Integration Services Team <bsdic@microsoft.com> 添加。
