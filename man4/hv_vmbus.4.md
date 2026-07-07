# hv_vmbus(4)

`hv_vmbus` — Hyper-V 虚拟机总线（VMBus）驱动

## 名称

`hv_vmbus`

## 概要

`要将此驱动编译进内核，请在系统内核配置文件中加入以下行：`

> device hyperv
> device pci

## 描述

`hv_vmbus` 为 Hyper-V 中客户机分区和根分区之间提供高性能通信接口。Hyper-V 是 Microsoft 提供的基于 hypervisor 的虚拟化技术。Hyper-V 以分区为单位支持隔离。分区是由 hypervisor 支持的逻辑隔离单元，操作系统在其中执行。

Microsoft hypervisor 必须至少有一个父分区（即根分区），运行 Windows Server 操作系统。虚拟化栈运行在父分区中，可直接访问硬件设备。然后由根分区创建子分区，子分区中承载客户机操作系统。

子分区不能直接访问其他硬件资源，而是获得资源的虚拟视图，即虚拟设备（VDev）。对虚拟设备的请求通过 VMBus 或 hypervisor 重定向到父分区中的设备，由父分区处理这些请求。

VMBus 是一个逻辑性的分区間通信通道。父分区托管虚拟服务提供者（VSP），VSP 通过 VMBus 通信以处理来自子分区的设备访问请求。子分区托管虚拟服务消费者（VSC），VSC 通过 VMBus 将设备请求重定向到父分区中的 VSP。Hyper-V VMBus 驱动定义并实现了促进 VSC 和 VSP 之间高性能双向通信的接口。所有 VSC 都使用 VMBus 驱动。

## 参见

[hv_netvsc(4)](hv_netvsc.4.md), [hv_storvsc(4)](hv_storvsc.4.md), [hv_utils(4)](hv_utils.4.md)

## 历史

`hv_vmbus` 的支持最早出现在 FreeBSD 10.0 中。该驱动由 Citrix Incorporated、Microsoft Corporation 和 Network Appliance Incorporated 联合开发。

## 作者

`hv_vmbus` 的 FreeBSD 支持最早由 Microsoft BSD Integration Services Team <bsdic@microsoft.com> 添加。
