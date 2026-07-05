# pnpbios.4.i386

`pnpbios` — 对主板上嵌入式设备的支持

## 名称

`pnpbios`

## 描述

`pnpbios` 驱动枚举主板上其 BIOS 支持“Plug and Play BIOS Specification”的嵌入式 ISA 设备。它为每个设备分配 ISA 总线资源（中断线、DMA 通道、I/O 端口和内存区域）并激活它。

如果不能在不与系统中其他设备冲突的情况下为设备分配所需资源，该设备将不会被激活，并且对程序不可用。

## 参见

[pnp(4)](pnp.4.i386.md)

## 标准

> Compaq, Phenix, Intel, "Plug and Play BIOS Specification Version 1.0A", May 5, 1994.

> Compaq, Phenix, Intel, "Plug and Play BIOS CLARIFICATION Paper for Plug and Play BIOS Specification Version 1.0A", October 6, 1994.

## 历史

`pnpbios` 驱动首次出现于 FreeBSD 4.0。

## 作者

`pnpbios` 驱动由 Mike Smith 编写。

## 注意事项

没有显式的方法来禁用单个嵌入式设备。`pnpbios` 驱动会找到“即插即用（PnP）”BIOS 报告的所有设备并尝试全部激活它们。

无法显式地为设备分配特定资源。资源分配是完全自动的，没有手动覆盖的规定。
