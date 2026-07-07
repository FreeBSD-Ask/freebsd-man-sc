# imx6_ahci(4)

`imx6_ahci` — NXP i.MX6 片上 SATA 控制器驱动

## 名称

`imx6_ahci`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device ahci

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
imx6_ahci_load="YES"
```

## 描述

`imx6_ahci` 驱动为某些型号的 NXP i.MX6 芯片上的片上 SATA 控制器提供支持。该驱动是一个薄薄的胶水层，用于解析平台的 FDT 数据，并为标准的 [ahci(4)](ahci.4.md) 驱动整理资源。

## 参见

[ahci(4)](ahci.4.md), [fdt(4)](fdt.4.md)

## 历史

`imx6_ahci` 驱动首次出现于 FreeBSD 12.0。
