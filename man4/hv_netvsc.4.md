# hv_netvsc.4

`hv_netvsc` — Hyper-V 网络虚拟服务消费者

## 名称

`hv_netvsc`

## 概要

`要将此驱动编译进内核，请在系统内核配置文件中加入以下行：`

> device hyperv

## 描述

`hv_netvsc` 驱动为运行于 Hyper-V 上的 FreeBSD 客户机分区实现虚拟网络设备。运行于 Hyper-V 上的 FreeBSD 客户机分区无法直接访问连接到 Hyper-V 服务器的网络设备。虽然 FreeBSD 客户机可以使用 Hyper-V 的完全仿真模式访问网络设备，但此模式下的性能往往不能令人满意。

为解决上述问题，`hv_netvsc` 驱动实现了网络虚拟服务消费者（VSC），使用 [hv_vmbus(4)](hv_vmbus.4.md) 驱动提供的高性能数据交换基础设施，将来自客户机分区的网络请求中继到根分区中托管的网络虚拟服务提供者（VSP）。根分区中的 VSP 随后将网络相关请求转发到物理网卡。

## 参见

hv_ata_pci_disengage(4), [hv_storvsc(4)](hv_storvsc.4.md), [hv_utils(4)](hv_utils.4.md), [hv_vmbus(4)](hv_vmbus.4.md)

## 历史

`hv_netvsc` 的支持最早出现在 FreeBSD 10.0 中。该驱动由 Citrix Incorporated、Microsoft Corporation 和 Network Appliance Incorporated 联合开发。

## 作者

`hv_netvsc` 的 FreeBSD 支持最早由 Microsoft BSD Integration Services Team <bsdic@microsoft.com> 添加。
