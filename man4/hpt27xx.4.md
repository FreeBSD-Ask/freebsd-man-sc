# hpt27xx.4

`hpt27xx` — HighPoint RocketRAID 27xx SAS 6Gb/s HBA 卡驱动

## 名称

`hpt27xx`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device hpt27xx

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
hpt27xx_load="YES"
```

## 描述

`hpt27xx` 驱动为基于 HighPoint RocketRAID 27xx 的 RAID 控制器提供支持。

这些设备支持 SAS 磁盘驱动器，并提供 RAID0（条带化）、RAID1（镜像）和 RAID5 功能。

## 硬件

`hpt27xx` 驱动支持以下 SAS 控制器：

- HighPoint RocketRAID 271x 系列
- HighPoint RocketRAID 272x 系列
- HighPoint RocketRAID 274x 系列
- HighPoint RocketRAID 276x 系列
- HighPoint RocketRAID 278x 系列

## 注释

`hpt27xx` 驱动仅能在 i386 和 amd64 平台上工作，因为它需要厂商提供的二进制 blob 对象，而厂商仅为这些平台提供。在启用了 [pae(4)](pae.4.i386.md) 的 i386 上，`hpt27xx` 驱动*无法*工作。

## 参见

[kld(4)](kld.4.md), [kldload(8)](../man8/kldload.8.md), [loader(8)](../man8/loader.8.md)

## 历史

`hpt27xx` 设备驱动最早出现在 FreeBSD 10.0 中。

## 作者

`hpt27xx` 设备驱动由 HighPoint Technologies, Inc. 编写。本手册页由 Xin LI <delphij@FreeBSD.org> 为 iXsystems, Inc. 编写。
