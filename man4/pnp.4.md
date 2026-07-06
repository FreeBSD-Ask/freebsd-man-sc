# pnp.4

`pnp` — 对“即插即用”（PnP）ISA 设备的支持

## 名称

`pnp`

## 描述

`pnp` 驱动枚举系统中支持“Plug and Play ISA Specification”的 ISA 设备。它为每个设备分配 ISA 总线资源（中断线、DMA 通道、I/O 端口和内存区域）并激活它。

如果不能在不与系统中其他设备冲突的情况下为 PnP ISA 设备分配所需资源，该设备将不会被激活，并且对程序不可用。

## 参见

[pnpbios(4)](pnpbios.4.i386.md)

## 标准

> Intel, Microsoft, "Plug and Play ISA Specification, Version 1.0a", May 5, 1994.

> "Clarifications to the Plug and Play ISA Specification, Version 1.0a", December 10, 1994.

## 历史

`pnp` 驱动首次出现于 FreeBSD 2.2.5。在后续版本中进行了大幅更新。

## 作者

PnP 支持最初由 Luigi Rizzo 为 FreeBSD 2.2.5 编写，基于 Sujal Patel 的初始工作。

## 注意事项

无法禁用单个 PnP ISA 设备。`pnp` 驱动会找到所有符合 PnP ISA 规范的设备并尝试全部激活它们。

无法显式地为 PnP ISA 设备分配特定资源。资源分配是完全自动的，没有手动覆盖的规定。
