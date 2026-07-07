# lge(4)

`lge` — Level 1 LXT1001 NetCellerator PCI 千兆以太网适配器驱动

## 名称

`lge`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device lge

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_lge_load="YES"
```

## 描述

`lge` 驱动为基于 Level 1 LXT1001 NetCellerator 千兆以太网控制器芯片的各种网卡提供支持。

LXT1001 支持光纤 PHY，还支持用于 10/100/1000 铜缆 PHY 的 GMII 端口，但目前市场上没有使用此功能的网卡。

LXT1001 支持接收方向的 TCP/IP 校验和卸载和基于 VLAN 的过滤，以及 64 位多播哈希过滤器。它还支持 Jumbo 帧，可通过接口 MTU 设置进行配置。使用 [ifconfig(8)](../man8/ifconfig.8.md) 工具选择大于 1500 字节的 MTU 可将适配器配置为接收和发送 Jumbo 帧。对于某些任务（如文件传输和数据流），使用 Jumbo 帧可大幅提高性能。

`lge` 驱动支持以下介质类型：

**`autoselect`** 启用介质类型和选项的自动选择。用户可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加介质选项来手动覆盖自动选择的模式。

**`1000baseSX`** 设置通过光纤电缆进行的 1000baseSX 操作。支持 `full-duplex` 和 `half-duplex` 模式。

`lge` 驱动支持以下介质选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`lge` 驱动支持的适配器包括：

- SMC TigerCard 1000 (SMC9462SX)
- D-Link DGE-500SX

## 诊断

- lge%d: couldn't map memory 发生了致命的初始化错误。

- lge%d: couldn't map ports 发生了致命的初始化错误。

- lge%d: couldn't map interrupt 发生了致命的初始化错误。

- lge%d: no memory for softc struct! 驱动在初始化期间无法为每设备实例信息分配内存。

- lge%d: failed to enable memory mapping! 驱动无法初始化 PCI 共享内存映射。如果卡不在总线主控插槽中，可能会发生此情况。

- lge%d: no memory for jumbo buffers! 驱动在初始化期间无法为 Jumbo 帧分配内存。

- lge%d: watchdog timeout 设备已停止响应网络，或网络连接（电缆）有问题。

## 参见

arp(4), miibus(4), netintro(4), ng_ether(4), [ifconfig(8)](../man8/ifconfig.8.md)

> "Level 1 LXT1001 Programming Manual".

## 历史

`lge` 设备驱动最早出现于 FreeBSD 4.4。

## 作者

`lge` 驱动由 Bill Paul <william.paul@windriver.com> 编写。
