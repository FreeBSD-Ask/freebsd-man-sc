# bhndb_pci.4

`bhndb_pci` — Broadcom 家庭网络部门 PCI 主桥驱动

## 名称

`bhndb_pci`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device bhnd
> device bhndb
> device bhndb_pci
> device pci

要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
bhndb_pci_load="YES"
```

## 描述

`bhndb_pci` 驱动为 Broadcom 家庭网络部门的无线芯片组和网络适配器中使用的 PCI 和 PCIe 主桥核心提供 [bhndb(4)](bhndb.4.md) 支持。

## 参见

[bhnd(4)](bhnd.4.md), [bhndb(4)](bhndb.4.md), [bwn(4)](bwn.4.md), [intro(4)](intro.4.md), [pci(4)](pci.4.md)

## 历史

`bhndb_pci` 设备驱动首次出现于 FreeBSD 11.0。

## 作者

`bhndb_pci` 驱动由 Landon Fuller <landonf@FreeBSD.org> 编写。
