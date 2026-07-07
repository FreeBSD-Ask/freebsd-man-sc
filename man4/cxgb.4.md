# cxgb(4)

`cxgb` — Chelsio T3 10 千兆以太网适配器驱动

## 名称

`cxgb`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device firmware
> device cxgb

`若要在引导时以模块方式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_cxgb_load="YES"
```

## 描述

`cxgb` 驱动支持发送/接收校验和卸载、Jumbo 帧、TCP 分段卸载（TSO）、大接收卸载（LRO）、VLAN 硬件插入/提取以及 VLAN 校验和卸载。有关进一步的硬件信息，请参见 `http://www.chelsio.com/`。

有关硬件要求的问题，请参阅 Chelsio T3 适配器附带的文档。所有列出的硬件要求均适用于 FreeBSD。

通过接口 MTU 设置提供对 Jumbo 帧的支持。使用 [ifconfig(8)](../man8/ifconfig.8.md) 工具选择大于 1500 字节的 MTU 可将适配器配置为接收和发送 Jumbo 帧。Jumbo 帧的最大 MTU 为 9000。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`cxgb` 驱动支持基于 T3 和 T3B 芯片组的 10 千兆和 1 千兆以太网适配器：

- Chelsio 10GBase-CX4
- Chelsio 10GBase-LR
- Chelsio 10GBase-SR

## LOADER 可调参数

可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符处设置可调参数，或将其存储在 loader.conf(5) 中。

## 诊断

- cxgb%d: Unable to allocate bus resource: memory 发生了致命的初始化错误。
- cxgb%d: Unable to allocate bus resource: interrupt 发生了致命的初始化错误。
- cxgb%d: Could not find firmware image %s 未安装相应的固件 kld 模块。这是致命的初始化错误。

## 支持

有关一般信息和支持，请访问 Chelsio 支持网站：`http://www.chelsio.com/`。

如果在使用受支持内核和受支持适配器时发现已发布源代码的问题，请将与该问题相关的具体信息通过电子邮件发送至 <support@chelsio.com>。

## 参见

[altq(4)](altq.4.md), arp(4), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`cxgb` 设备驱动首次出现于 FreeBSD 6.3 和 FreeBSD 7.0。

## 作者

`cxgb` 驱动由 Kip Macy <kmacy@FreeBSD.org> 编写，Scott Long <scottl@FreeBSD.org> 提供了大量支持。
