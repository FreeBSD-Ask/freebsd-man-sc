# xnb(4)

`xnb` — Xen 半虚拟化后端以太网驱动

## 名称

`xnb`

## 概要

`要将此驱动编译进内核，请将以下行放入你的内核配置文件：`

> options XENHVM
> device xenpci

## 描述

`xnb` 驱动提供半虚拟化 [xen(4)](xen.4.md) 网络连接的后端部分。netback 和 netfront 驱动在各自的操作系统中表现为通过交叉电缆连接的以太网设备。通常，`xnb` 运行在 Domain 0 上，而 netfront 驱动运行在客户机域上。但也可以在客户机域上运行 `xnb`。可以对其进行桥接或路由，以使 netfront 域能够访问其他客户机域或物理网络。

在大多数方面，`xnb` 设备与任何其他以太网设备一样向操作系统呈现。可以在运行时完全使用 [ifconfig(8)](../man8/ifconfig.8.md) 进行配置。特别是，它支持 MAC 更改、任意 MTU 大小、IP、UDP 和 TCP 的接收和发送校验和卸载，以及 TSO。但在启用 txcsum、rxcsum 或 tso 之前，请参见注意事项。

## SYSCTL 变量

以下只读变量可通过 [sysctl(8)](../man8/sysctl.8.md) 使用：

**`dev.xnb.%d.dump_rings`** 显示有关用于在 netfront 和 netback 之间传递请求的环形缓冲区的信息。主要用于调试，但也可用于获取流量统计。

**`dev.xnb.%d.unit_test_results`** 运行内置的单元测试套件并显示结果。不会以任何方式影响驱动的操作。注意，测试套件会模拟错误条件；这将导致错误消息被打印到系统日志。

## 参见

arp(4), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [xen(4)](xen.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`xnb` 设备驱动首次出现于 FreeBSD 10.0。

## 作者

`xnb` 驱动由 Alan Somers <asomers@FreeBSD.org> 和 John Suykerbuyk 编写。

## 注意事项

通过 Xennet 发送的数据包经过共享内存，因此协议不包含任何形式的链路层校验和或 CRC。此外，Xennet 驱动总是向其主机报告它们支持接收和发送校验和卸载。它们通过简单地跳过校验和计算来“卸载”校验和计算。对于在同一机器上的两个域之间交换的数据包，这工作得很好。但是，当 Xennet 接口桥接到物理接口时，必须将正确的校验和附加到发往该物理接口的任何数据包。目前，FreeBSD 缺少任何机制让以太网设备通知操作系统新接收的数据包即使校验和不正确也是有效的。因此，如果 netfront 驱动配置为卸载校验和计算，它将把未校验的数据包传递给 `xnb`，后者必须在将数据包传递给操作系统之前用软件计算校验和。

由于此原因，建议如果 `xnb` 桥接到物理接口，则在 netfront 上禁用发送校验和卸载。Xennet 协议没有任何机制让 netback 请求 netfront 执行此操作；操作员必须手动完成。

## 缺陷

`xnb` 驱动不能正确校验跨越多个以太网帧的 UDP 数据报。也不能正确校验 IPv6 数据包。要解决此缺陷，请在 netfront 驱动上禁用发送校验和卸载。
