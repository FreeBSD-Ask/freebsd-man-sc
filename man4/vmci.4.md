# vmci(4)

`vmci` — VMware 虚拟机通信接口

## 名称

`vmci`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device vmci

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_vmci_load="YES"
```

## 描述

`vmci` 驱动为 VMware 虚拟机中的 VMware 虚拟机通信接口（VMCI）提供支持。

VMCI 允许虚拟机与主机内核模块及 VMware hypervisor 通信。虚拟机中的用户级应用程序可通过 vSockets（也称为 VMCI Sockets，未包含在此内核模块中）使用 VMCI，这是一种在接口级别设计为与 UDP 和 TCP 兼容的 socket 地址族。如今，VMCI 和 vSockets 被客户机内的各种 VMware Tools 组件用于零配置、无网络访问 VMware 主机服务。此外，VMware 用户还将 vSockets 用于各种应用程序，特别是在虚拟机的网络访问受限或不存在的情况下。例如，虚拟机与作为主机应用程序运行的专有硬件的设备代理通信，以及对虚拟机中运行的应用程序进行自动化测试。

在虚拟机中，VMCI 作为常规 PCI 设备暴露。支持的主要通信机制是基于一对内存映射队列的点对点双向传输，以及数据报和 doorbell 形式的异步通知。这些功能通过 VMCI 内核 API 提供给 vSockets 等内核级组件。此外，VMCI 内核 API 还支持接收与 VMCI 通信通道及虚拟机本身状态相关的事件。

## 参见

socket(2), [pci(9)](../man9/pci.9.md)

> "VMware vSockets Documentation".

## 历史

`vmci` 驱动最早出现于 FreeBSD 12.0。

## 作者

`vmci` 驱动及手册页由 Vishnu Dasa <vdasahar@gmail.com> 编写。
