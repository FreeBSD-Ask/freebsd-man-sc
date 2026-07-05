# an.4

`an` — Aironet Communications 4500/4800 无线网络适配器驱动

## 名称

`an`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> device an
> device wlan

或者，要在引导时以模块形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行：

```sh
if_an_load="YES"
```

## 描述

`an` 驱动为 Aironet Communications 4500 和 4800 无线网络适配器及其变体提供支持，包括：

- Aironet Communications 4500 和 4800 系列
- Cisco Aironet 340 和 350 系列

对这些设备的支持包括 ISA 和 PCI 类型。Aironet 4500 系列适配器以 1 和 2Mbps 速率运行，而 Aironet 4800 系列和 Cisco 适配器可以 1、2、5.5 和 11Mbps 速率运行。ISA 和 PCI 设备都基于相同的 PCMCIA 核心硬件，并具有相同的编程接口。ISA 和 PCI 卡对主机表现为正常的 ISA 和 PCI 设备。

ISA 卡可通过正确设置板上的 DIP 开关配置为使用 ISA 即插即用，或使用特定的 I/O 地址和 IRQ。（默认开关设置为即插即用。）`an` 驱动具有即插即用支持，可在任一配置下工作，但使用硬连线的 I/O 地址和 IRQ 时，驱动配置与 NIC 的开关设置必须一致。PCI 卡无需任何开关设置，将被自动探测和附加。

主机与 Aironet 卡的所有交互通过编程 I/O 进行。Aironet 设备支持 802.11 和 802.3 帧、电源管理、BSS（基础设施）和 IBSS（自组网）工作模式。`an` 驱动将所有 IP 和 ARP 流量封装为 802.11 帧，但可接收 802.11 或 802.3 帧。发送速率可在 1Mbps、2Mbps、5.5Mbps、11Mbps 或“auto”（NIC 自动选择最佳速率）之间选择。

默认情况下，`an` 驱动将 Aironet 卡配置为基础设施操作。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 诊断

- an%d: init failed：发出初始化命令后，Aironet 卡未能就绪。
- an%d: failed to allocate %d bytes on NIC：驱动无法在 NIC 的板载 RAM 中为发送帧分配内存。
- an%d: device timeout：Aironet 卡未能生成中断以确认发送命令。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [wlan(4)](wlan.4.md), ancontrol(8), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`an` 设备驱动首次出现于 FreeBSD 4.0。

`an` 设备驱动在 FreeBSD 14.0 中已被移除。

## 作者

`an` 驱动由 Bill Paul <wpaul@ee.columbia.edu> 编写。
