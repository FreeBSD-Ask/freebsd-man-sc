# virtio.4

`virtio` — VirtIO 设备支持

## 名称

`virtio`

## 概要

`要将 VirtIO 设备支持编译进内核，请在你的内核配置文件中加入以下行：`

> device virtio
> device virtio_pci

`或者，要在引导时以模块形式加载 VirtIO 支持，请在 loader.conf(5) 中加入以下行：`

```sh
virtio_load="YES"
virtio_pci_load="YES"
```

## 描述

VirtIO 是用于虚拟机（VM）中半虚拟化 I/O 的规范。传统上，hypervisor 模拟真实设备（如以太网接口或磁盘控制器）来为 VM 提供 I/O。这种模拟通常效率低下。

VirtIO 定义了 hypervisor 与 VM 之间的高效 I/O 接口。`virtio` 模块提供了一种称为 virtqueue 的共享内存传输机制。**virtio_pci** 设备驱动代表 hypervisor 向 VM 提供的一个模拟 PCI 设备。此设备提供了与 hypervisor 交互所需的探测、配置和中断通知。FreeBSD 支持以下 VirtIO 设备：

**Ethernet** 模拟的以太网设备由 [vtnet(4)](vtnet.4.md) 设备驱动提供。

**Block** 模拟的磁盘控制器由 [virtio_blk(4)](virtio_blk.4.md) 设备驱动提供。

**Console** 由 [virtio_console(4)](virtio_console.4.md) 驱动提供。

**Entropy** 由 [virtio_random(4)](virtio_random.4.md) 驱动提供。

**Balloon** 允许 VM 将内存释放回 hypervisor 的伪设备由 [virtio_balloon(4)](virtio_balloon.4.md) 设备驱动提供。

**GPU** 图形支持由 [virtio_gpu(4)](virtio_gpu.4.md) 设备驱动提供。

**SCSI** 模拟的 SCSI HBA 由 [virtio_scsi(4)](virtio_scsi.4.md) 设备驱动提供。

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`hw.virtio.pci.disable_msix`** 设置为 1 时禁用 MSI-X。默认值为 0。

**`hw.virtio.pci.transitional`** 对于过渡型 `virtio` 设备，此可调参数指定是协商现代模式并使用现代 `virtio` 驱动（1），还是协商传统模式并使用传统 `virtio` 驱动（0）。默认值为 1。

## 参见

[virtio_balloon(4)](virtio_balloon.4.md), [virtio_blk(4)](virtio_blk.4.md), [virtio_console(4)](virtio_console.4.md), [virtio_gpu(4)](virtio_gpu.4.md), [virtio_random(4)](virtio_random.4.md), [virtio_scsi(4)](virtio_scsi.4.md), [vtnet(4)](vtnet.4.md)

## 历史

VirtIO 支持最早出现于 FreeBSD 9.0。

## 作者

FreeBSD 的 VirtIO 支持最早由 Bryan Venteicher <bryanv@FreeBSD.org> 添加。
