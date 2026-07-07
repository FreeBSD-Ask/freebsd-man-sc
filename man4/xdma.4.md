# xdma(4)

`xdma` — DMA 抽象层

## 名称

`xdma`

## 概要

`要将 xDMA 设备支持编译进内核，请将以下行放入你的内核配置文件：`

> device xdma

`要编译基于 xDMA FDT 的测试驱动，还要加入以下行：`

```sh
device xdma_test
```

## 描述

xDMA 是一个 DMA 框架，旨在抽象设备驱动程序与 DMA 引擎之间的交互。

xDMA 定义了设备驱动程序与 DMA 控制器之间高效交互的接口。`xdma` 设备提供虚拟 DMA 控制器和称为 xchan 的虚拟通道。控制器提供虚拟通道管理（分配、释放、配置）和中断通知建立，以接收来自硬件 DMA 控制器的事件。`xdma` 支持以下传输类型：

**`Cyclic`** 不停的周期性传输，专为音频等应用设计。

**`Memcpy`** 内存到内存的传输。

## 参见

[bus_dma(9)](../man9/bus_dma.9.md)

## 历史

xDMA 支持首次出现于 FreeBSD 12.0。

## 作者

FreeBSD xDMA 框架最初由 Ruslan Bukin <br@FreeBSD.org> 添加。
