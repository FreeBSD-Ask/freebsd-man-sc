# mxge.4

`mxge` — Myricom Myri10GE 10 千兆以太网适配器驱动

## 名称

`mxge`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device firmware
> device mxge

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_mxge_load="YES"
mxge_ethp_z8e_load="YES"
mxge_eth_z8e_load="YES"
mxge_rss_ethp_z8e_load="YES"
mxge_rss_eth_z8e_load="YES"
```

## 描述

`mxge` 驱动提供对基于 Myricom LANai Z8E 芯片的 PCI Express 10 千兆以太网适配器的支持。该驱动支持发送/接收校验和卸载、Jumbo 帧、TCP 分段卸载（TSO）以及大接收卸载（LRO）。有关硬件的更多信息，请参见 `http://www.myri.com/`。

有关硬件要求的问题，请参阅 Myri10GE 适配器附带的文档。所有列出的硬件要求均适用于 FreeBSD。

通过接口 MTU 设置提供对 Jumbo 帧的支持。使用 [ifconfig(8)](../man8/ifconfig.8.md) 实用程序选择大于 1500 字节的 MTU 会将适配器配置为接收和传输 Jumbo 帧。Jumbo 帧的最大 MTU 大小为 9000。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`mxge` 驱动支持基于 Myricom LANai Z8E 芯片的 10 千兆以太网适配器：

- Myricom 10GBase-CX4 (10G-PCIE-8A-C, 10G-PCIE-8AL-C)
- Myricom 10GBase-R (10G-PCIE-8A-R, 10G-PCIE-8AL-R)
- Myricom 10G XAUI over ribbon fiber (10G-PCIE-8A-Q, 10G-PCIE-8AL-Q)

## 加载器可调参数

可在引导内核前在 [loader(8)](../man8/loader.8.md) 提示符下设置可调参数，或存储在 loader.conf(5) 中。

**1** 对源和目的 IPv4 地址进行哈希。

**2** 对源和目的 IPv4 地址进行哈希，如果数据包是 TCP，则还对 TCP 源和目的端口进行哈希。

**4** 对 TCP 或 UDP 源端口进行哈希。这是默认值。

**`hw.mxge.flow_control_enabled`** 适配器上是否启用硬件流控制。默认值为 1。

**`hw.mxge.intr_coal_delay`** 此值以 1 微秒为单位延迟所有中断的生成。默认值为 30。

**`hw.mxge.skip_pio_read`** 此值确定驱动程序是否可以省略在中断处理程序中执行 PIO 读取，以确保在使用 xPIC 中断时中断线已被取消置位。非零值可能会降低 CPU 开销，但也可能导致虚假中断。默认值为 0。当设备使用 MSI 或 MSI-X 中断时，此可调参数无效。

**`hw.mxge.max_slices`** 此值确定驱动程序将尝试使用的最大切片数。默认值为 1。切片由一组接收队列和关联的中断线程组成。使用多个切片时，NIC 会根据 `hw.mxge.rss_hashtype` 的值将流量哈希到不同的切片。使用多个切片需要主板和 Myri10GE NIC 都支持 MSI-X。较旧的 Myri10GE NIC 可以现场升级以添加 MSI-X，使用适用于 FreeBSD 的“10G NIC Tool Kit”，可从 `http://www.myri.com/scs/download-10g-tools.html` 获取。

**`hw.mxge.rss_hashtype`** 此值确定传入流量如何引导到不同的切片。使用单个切片时，此可调参数将被忽略。此可调参数的合法值为：

## 诊断

- mxge%d: Unable to allocate bus resource: memory 发生了致命的初始化错误。
- mxge%d: Unable to allocate bus resource: interrupt 发生了致命的初始化错误。
- mxge%d: Could not find firmware image %s 未安装适当的固件 kld 模块。这是非致命的初始化错误，但会导致以降低性能的模式运行。

## 支持

有关一般信息和支持，请访问 Myricom 支持网站：`http://www.myri.com/scs/`。

如果在受支持的内核上使用受支持的适配器发现已发布源代码的问题，请将与问题相关的具体信息通过电子邮件发送至 <help@myri.com>。

## 参见

[altq(4)](altq.4.md), arp(4), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`mxge` 设备驱动首次出现于 FreeBSD 6.3。

## 作者

`mxge` 驱动由 Andrew Gallatin <gallatin@FreeBSD.org> 编写。
