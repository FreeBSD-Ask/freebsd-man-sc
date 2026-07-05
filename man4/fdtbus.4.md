# fdtbus.4

`fdtbus` — Flattened Device Tree 总线驱动程序

## 名称

`fdtbus`

## 概要

`options FDT`

## 描述

`fdtbus` 抽象总线驱动程序是 [fdt(4)](fdt.4.md) 硬件资源描述与 FreeBSD 原生 newbus 设备驱动程序框架之间的主要连接和转换层。对于嵌入式系统，`fdtbus` 代表通常在高度集成芯片（system-on-chip）上发现的外设。

`fdtbus` 驱动程序为所有面向 [fdt(4)](fdt.4.md) 的设备驱动程序提供通用的公共基础设施，其主要职责如下：

- 创建反映 flattened device tree 中 [fdt(4)](fdt.4.md) 节点的 newbus 子设备。
- 管理 SYS_RES_IRQ 资源。
- 管理 SYS_RES_MEMORY、SYS_RES_IOPORT 资源。

## 参见

[fdt(4)](fdt.4.md), [openfirm(4)](openfirm.4.md), [simplebus(4)](simplebus.4.md)

## 标准

IEEE Std 1275：IEEE Boot（初始化配置）固件标准：核心要求与实践（`Open Firmware`）。

Power.org 嵌入式 Power 架构平台要求标准（`ePAPR`）。

## 历史

`fdtbus` 支持首次出现于 FreeBSD 9.0。

## 作者

`fdtbus` 支持由 Semihalf 在 FreeBSD Foundation 赞助下开发。本手册页由 Rafal Jaworowski 编写。
