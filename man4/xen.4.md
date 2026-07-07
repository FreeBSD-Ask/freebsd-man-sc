# xen(4)

`xen` — Xen Hypervisor 支持

## 名称

`xen`

## 概要

`FreeBSD 支持在 amd64 硬件上作为 Xen 客户机和主机运行。客户机支持仅限于 HVM 和 PVH 模式，而主机支持仅限于 PVH 模式。`

`Xen 支持默认内置在 i386 和 amd64 GENERIC 内核中；但注意主机模式仅在 amd64 上可用。`

## 描述

Xen Hypervisor 允许在单台计算机系统上运行多个虚拟机。首次发布时，Xen 要求 i386 内核被编译为“半虚拟化”，因为 x86 指令集并非完全可虚拟化。主要来说，半虚拟化修改虚拟内存系统以使用 hypervisor 调用（hypercall）而非直接硬件指令来修改 TLB，尽管也需要半虚拟化设备驱动程序来访问虚拟网络接口和磁盘设备等资源。

随着 AMD 和 Intel 后来的指令集扩展支持完全可虚拟化指令，也可以支持未经修改的虚拟内存系统；这称为硬件辅助虚拟化（HVM 和 PVH）。HVM 配置可以依赖透明模拟的硬件外设，或半虚拟化驱动程序，后者感知虚拟化，因此能够优化某些行为以提高性能或语义。PVH 配置完全依赖半虚拟化驱动程序进行 IO。

FreeBSD 半虚拟化设备驱动程序是支持某些功能所必需的，例如处理管理请求、将空闲物理内存页返回给 hypervisor 等。

### Xen 设备驱动程序

支持以下半虚拟化驱动程序：

**`balloon`** 允许因手动调优或自动策略将物理内存页返回给 hypervisor。

**`blkback`** 将本地块设备或文件导出到其他 Xen 域，然后可以通过 `blkfront` 导入。

**`blkfront`** 从其他 Xen 域导入块设备作为本地块设备，用于文件系统、交换等。

**`console`** 通过 Xen 控制台服务导出低级系统控制台。

**`control`** 处理来自 Domain 0 的管理操作，包括关机、重启、挂起、崩溃和停止请求。

**`evtchn`** 通过 **`/dev/xen/evtchn`** 特殊设备公开 Xen 事件。

**`gntdev`** 允许通过 **`/dev/xen/gntdev`** 特殊设备访问授权表接口。

**`netback`** 将本地网络接口导出到其他 Xen 域，可以通过 `netfront` 导入。

**`netfront`** 从其他 Xen 域导入网络接口作为本地网络接口，可用于 IPv4、IPv6 等。

**`privcmd`** 允许通过 **`/dev/xen/privcmd`** 特殊设备发出 hypercall。

**`timer`** 使用 hypercall 接口实现每 CPU 的一次性高分辨率定时器。

**`acpi`** 作为主机运行时，将 ACPI 的电源管理相关信息转发给 hypervisor，以实现更好的性能管理。

**`xenpci`** 表示 Xen PCI 设备，这是暴露给 HVM 域的模拟 PCI 设备。此设备允许检测 Xen hypervisor，并提供与 hypervisor 交互所需的中断和共享内存服务。

**`xenstore`** 域之间共享的信息存储空间。

## 历史

`xenstore` 支持首次出现于 FreeBSD 8.1。主机模式支持在 11.0 中添加。

## 作者

FreeBSD 对 Xen 的支持最初由 Kip Macy <kmacy@FreeBSD.org> 和 Doug Rabson <dfr@FreeBSD.org> 添加。后续改进由 Justin Gibbs <gibbs@FreeBSD.org>、Adrian Chadd <adrian@FreeBSD.org>、Colin Percival <cperciva@FreeBSD.org> 和 Roger Pau Monné <royger@FreeBSD.org> 完成。本手册页由 Robert Watson <rwatson@FreeBSD.org> 和 Roger Pau Monné <royger@FreeBSD.org> 编写。
