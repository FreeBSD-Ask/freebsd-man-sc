# hv_kvp(4)

`hv_kvp` — Hyper-V 键值对驱动

## 名称

`hv_kvp`

## 概要

`要将此驱动编译进内核，请在系统内核配置文件中加入以下行：`

> device hyperv

## 描述

`hv_kvp` 驱动为运行于 Hyper-V 上的 FreeBSD 客户机分区提供存储、检索、修改和删除键值对的能力。Hyper-V 允许管理员以键值对的形式在 FreeBSD 客户机分区内存储自定义元数据。管理员可以使用 Windows Powershell 脚本添加、读取、修改和删除此类键值对。

该驱动是基础框架，仅将请求转发给对应的用户态守护进程 hv_kvp_daemon(8)。守护进程维护键值对池，并执行实际的元数据管理。

相同的驱动和守护进程组合也用于从 FreeBSD 客户机设置和获取 IP 地址。

设置功能在 FreeBSD 客户机被分配静态 IP 地址并从一台 Hyper-V 主机故障转移到另一台时特别有用。故障转移后，Hyper-V 使用设置 IP 功能自动将 FreeBSD 客户机的 IP 地址更新为其原始静态值。

另一方面，获取 IP 功能用于在 Hyper-V 管理控制台窗口中更新客户机 IP 地址。

## 参见

hv_ata_pci_disengage(4), [hv_netvsc(4)](hv_netvsc.4.md), [hv_storvsc(4)](hv_storvsc.4.md), [hv_utils(4)](hv_utils.4.md), [hv_vmbus(4)](hv_vmbus.4.md), hv_kvp_daemon(8)

## 历史

`hv_kvp` 的支持最早出现在 FreeBSD 10.0 中。该驱动由 Citrix Incorporated、Microsoft Corporation 和 Network Appliance Incorporated 联合开发。

## 作者

`hv_kvp` 的 FreeBSD 支持最早由 Microsoft BSD Integration Services Team <bsdic@microsoft.com> 添加。
