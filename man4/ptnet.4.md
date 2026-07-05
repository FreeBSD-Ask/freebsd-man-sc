# ptnet.4

`ptnet` — 直通 netmap 端口的以太网驱动程序

## 名称

`ptnet`

## 概要

此网络驱动程序包含在 netmap(4) 中，可在你的内核配置文件中加入以下行将其编译进内核：

> device netmap

## 描述

`ptnet` 设备驱动程序提供从虚拟机（VM）内直接访问主机 netmap 端口的能力。运行于 VM 内的应用程序可以访问 hypervisor 直通给 VM 的 netmap 端口的 TX/RX 环和缓冲区。目前 QEMU/KVM 提供对 `ptnet` 的 hypervisor 支持。任何 [netmap(4)](netmap.4.md) 端口都可以被直通，包括物理网卡、[vale(4)](vale.4.md) 端口、netmap 管道等。

netmap 直通的主要用例是网络功能虚拟化（NFV），其中运行于 VM 内的中盒应用程序可能需要处理非常高的数据包速率（例如每秒 1 至 1000 万个数据包或更多）。但请注意，这些应用程序必须以 netmap 模式使用设备才能达到这样的速率。除了 netmap 的通用优势外，与 hypervisor 设备模拟或半虚拟化（例如 [vtnet(4)](vtnet.4.md)、[vmx(4)](vmx.4.md)）相比，`ptnet` 性能提升的关键在于数据路径上完全绕过 hypervisor。例如，使用 [vtnet(4)](vtnet.4.md) 时，VM 必须将每个 [mbuf(9)](../man9/mbuf.9.md) 转换为 VirtIO 特定的数据包表示并发布到 VirtIO 队列；在 hypervisor 端，从 VirtIO 队列提取数据包并转换为 hypervisor 特定的数据包表示。在 netmap 模式下，`ptnet` 不会产生格式转换（以及某些情况下的数据包复制）的开销，因为完全不使用 mbuf，并且整个数据路径上的数据包格式由 netmap 定义（例如 `struct netmap_slot`）。不会发生格式转换或复制。

也可以像常规网络接口那样使用 `ptnet` 设备，与 FreeBSD 网络协议栈交互（即不处于 netmap 模式）。但在这种情况下，必须付出 mbuf 与 netmap 缓冲区之间数据复制的代价，通常会导致 TCP/UDP 性能低于 [vtnet(4)](vtnet.4.md) 或其他半虚拟化网络设备。如果被直通的 netmap 端口支持 VirtIO 网络头，`ptnet` 能够使用它，并支持 TCP/UDP 校验和卸载（发送和接收）、TCP 分段卸载（TSO）和 TCP 大接收卸载（LRO）。目前 [vale(4)](vale.4.md) 端口支持此头部。注意，VirtIO 网络头通常不用于 NFV 用例，因为中盒不是 TCP/UDP 连接的端点。

## 加载器可调参数

可调参数可在引导内核前在 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`dev.netmap.ptnet_vnet_hdr`** 此可调参数启用（1）或禁用（0）VirtIO 网络头。启用时，`ptnet` 使用与 [vtnet(4)](vtnet.4.md) 相同的头部与 hypervisor 交换卸载元数据。禁用时，不会在发送和接收的数据包前添加头部。该元数据是支持 TCP/UDP 校验和卸载、TSO 和 LRO 所必需的。默认值为 1。

## 参见

[netintro(4)](netintro.4.md), [netmap(4)](netmap.4.md), [vale(4)](vale.4.md), [virtio(4)](virtio.4.md), [vmx(4)](vmx.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`ptnet` 驱动程序由 Vincenzo Maffione <vmaffione@FreeBSD.org> 编写。首次出现于 FreeBSD 12.0。
