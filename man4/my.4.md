# my.4

`my` — Myson Technology 以太网 PCI 驱动

## 名称

`my`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device my

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
if_my_load="YES"
```

## 描述

`my` 驱动提供对基于 Myson 芯片组的各种 NIC 的支持。Myson 芯片组是 DEC Tulip NIC 芯片组的变体。

该驱动程序可与几乎任何 MII 兼容的 PHY 一起工作，因此无法准确识别芯片不是致命错误。

## 硬件

`my` 驱动提供对基于 Myson 芯片组的各种 NIC 的支持。支持的型号包括：

- Myson MTD800 PCI 快速以太网芯片
- Myson MTD803 PCI 快速以太网芯片
- Myson MTD89X PCI 千兆以太网芯片

## 参见

[altq(4)](altq.4.md), [netintro(4)](netintro.4.md), [pci(4)](pci.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`my` 驱动首次出现于 FreeBSD 4.6。

## 作者

`my` 驱动由 Myson Technology Inc. 编写。

本手册页由 Hiten M. Pandya <hmp@FreeBSD.org> 编写。

## 缺陷

`my` 驱动不支持电源管理事件（PME）。
