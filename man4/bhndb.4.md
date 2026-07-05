# bhndb.4

`bhndb` — Broadcom 家庭网络部门互连桥驱动

## 名称

`bhndb`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device bhnd
> device bhndb

要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
bhndb_load="YES"
```

## 描述

`bhndb` 驱动为 Broadcom 家庭网络部门的无线芯片组和网络适配器提供 [bhnd(4)](bhnd.4.md) 主桥支持。

要启用对 PCI/PCIe 系统的使用，请参见 [bhndb_pci(4)](bhndb_pci.4.md) 驱动。

## 参见

[bhnd(4)](bhnd.4.md), [bhndb_pci(4)](bhndb_pci.4.md), [bwn(4)](bwn.4.md), [intro(4)](intro.4.md)

## 历史

`bhndb` 设备驱动首次出现于 FreeBSD 11.0。

## 作者

`bhndb` 驱动由 Landon Fuller <landonf@FreeBSD.org> 编写。

## 注意事项

`bhndb` 驱动目前不支持 PCMCIA 或 SDIO 设备。
