# simplebus(4)

`simplebus` — ePAPR simple-bus 驱动

## 名称

`simplebus`

## 概要

`options FDT`

## 描述

此总线驱动专用于符合 `ePAPR` 规范的扁平设备树（flattened device tree）的 `simple-bus` 节点。

`simplebus` 实体本身不表示任何物理元素，它更像是一个伞形节点，将片上集成的外设（如中断控制器、连接控制器、加速引擎等）归组在一起。

该驱动是通用的，适用于所有声明 `simple-bus` 兼容性的扁平设备树节点。它迭代 `simple-bus` 节点的直接子节点，实例化 newbus 子设备，并根据从 [fdt(4)](fdt.4.md) 中的节点属性检索到的配置数据为它们分配资源。

注意，`simplebus` 不管理设备资源，而是将任何请求传递给 [fdtbus(4)](fdtbus.4.md) 层。

## 参见

[fdt(4)](fdt.4.md), [fdtbus(4)](fdtbus.4.md), [openfirm(4)](openfirm.4.md)

## 标准

Power.org Standard for Embedded Power Architecture Platform Requirements (`ePAPR`)。

## 历史

`simplebus` 支持最早出现于 FreeBSD 9.0。

## 作者

`simplebus` 支持由 Semihalf 在 FreeBSD Foundation 的赞助下开发。本手册页由 Rafal Jaworowski 编写。
