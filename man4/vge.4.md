# vge(4)

`vge` — VIA Networking Technologies Velocity 千兆以太网适配器驱动

## 名称

`vge`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device vge

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_vge_load="YES"
```

## 描述

`vge` 驱动为基于 VIA Technologies VT6120、VT6122、VT6130 和 VT6132 Velocity 系列 千兆以太网控制器芯片的各种网卡和嵌入式以太网接口提供支持。

VT6120/VT6122 是一款 33/66MHz 64 位 PCI 设备，将三速 MAC 与集成的 10/100/1000 铜质 PHY 结合在一起。（部分旧卡使用外部 PHY。）VT6130/VT6132 是 Velocity 系列的 PCI express 版本。MAC 支持 TCP/IP 硬件校验和（仅 IPv4）、TCP 大发送、VLAN 标签插入与剥离，以及 VLAN 过滤、64 项 CAM 过滤器和 64 项 VLAN 过滤器、64 位多播哈希过滤器、4 个独立发送 DMA 队列、流控和最大 16K 的巨型帧（VT6130/VT6132 不支持）。Velocity 系列控制器具有 16K 接收 FIFO 和 48K 发送 FIFO。

`vge` 驱动利用控制器的校验和卸载与 VLAN 打标签功能，以及巨型帧（VT6130/VT6132 除外）和 CAM 过滤器支持。CAM 过滤器用于多播地址过滤，提供 64 项完美多播地址过滤支持。如果接口需要加入超过 64 个多播组，驱动将切换到使用哈希过滤器。

通过将接口 MTU 设置为大于默认值 1500 字节的任意值（最大为 9000 字节），可启用巨型帧支持。VT6130/VT6132 控制器上禁用巨型帧，因为当尝试发送大于 4K 的帧时 TX MAC 会挂起。可使用 [ifconfig(8)](../man8/ifconfig.8.md) 工具开启或关闭接收和发送校验和卸载支持。

`vge` 驱动支持以下介质类型：

**`autoselect`** 启用介质类型和选项的自动选择。用户可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加介质选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`1000baseTX`** 设置通过双绞线进行的 1000baseTX 操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

`vge` 驱动支持以下介质选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`vge` 驱动支持基于 VIA Networking VT6120、VT6122、VT6130 和 VT6132 的千兆以太网适配器，包括：

- VIA Networking 板载千兆以太网
- ZyXEL GN650-T 64 位 PCI 千兆以太网网卡（ZX1701）
- ZyXEL GN670-T 32 位 PCI 千兆以太网网卡（ZX1702）

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`hw.vge.msi_disable`** 此可调参数禁用以太网硬件上的 MSI 支持。默认值为 0。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`dev.vge.%d.int_holdoff`** 延迟中断的最大时间。有效范围为 0 到 5100，单位为 1us，默认值为 150（150us）。定时器的分辨率约为 20us，因此无法进行比 20us 更精细的调节。在变更生效前，应将接口先关闭再重新启用。

**`dev.vge.%d.rx_coal_pkt`** 触发接收完成中断的最大数据包数。有效范围为 1 到 255，默认值为 64。

**`dev.vge.%d.tx_coal_pkt`** 触发发送完成中断的最大数据包数。有效范围为 1 到 255，默认值为 128。

## 诊断

- vge%d: couldn't map memory。发生了致命的初始化错误。
- vge%d: couldn't map ports。发生了致命的初始化错误。
- vge%d: couldn't map interrupt。发生了致命的初始化错误。
- vge%d: failed to enable memory mapping!。驱动初始化 PCI 共享内存映射失败。如果卡未插在总线主控插槽中，可能发生此情况。
- vge%d: watchdog timeout。设备已停止响应网络，或网络连接（电缆）存在问题。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [polling(4)](polling.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`vge` 设备驱动最早出现于 FreeBSD 5.3。

## 作者

`vge` 驱动由 Bill Paul <wpaul@windriver.com> 编写。
