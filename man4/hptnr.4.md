# hptnr.4

`hptnr` — HighPoint DC 系列数据中心 HBA 卡驱动

## 名称

`hptnr`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device hptnr

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
hptnr_load="YES"
```

## 描述

`hptnr` 驱动为 HighPoint DC 系列数据中心 HBA 卡提供支持。

## 硬件

`hptnr` 驱动支持以下 SATA 控制器：

- HighPoint DC7280 系列
- HighPoint Rocket R750 系列

## 注释

`hptnr` 驱动仅能在 i386 和 amd64 平台上工作，因为它需要厂商提供的二进制 blob 对象，而厂商仅为这些平台提供。在启用了 [pae(4)](pae.4.i386.md) 的 i386 上，`hptnr` 驱动*无法*工作。

## 参见

[kld(4)](kld.4.md), [kldload(8)](../man8/kldload.8.md), [loader(8)](../man8/loader.8.md)

## 历史

`hptnr` 设备驱动最早出现在 FreeBSD 9.2 中。

## 作者

`hptnr` 设备驱动由 HighPoint Technologies, Inc. 编写。本手册页由 Xin LI <delphij@FreeBSD.org> 为 iXsystems, Inc. 编写。
