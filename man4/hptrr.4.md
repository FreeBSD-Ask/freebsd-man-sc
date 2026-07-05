# hptrr.4

`hptrr` — HighPoint RocketRAID 设备驱动

## 名称

`hptrr`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device hptrr
> device scbus
> device da

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
hptrr_load="YES"
```

`以下可调参数可从 loader(8) 设置：`

`设为 1 可允许驱动附加到使用通用 Marvell（非 HighPoint）PCI 标识的芯片。这些芯片也由 ata(4) 和 mvs(4) 支持。一些厂商使用相同的芯片，但不提供 RAID BIOS。`

**hw.hptrr.attach_generic**

## 描述

`hptrr` 驱动为基于 HighPoint RocketRAID 的 RAID 控制器提供支持。

这些设备支持 SATA/ATA 磁盘驱动器，并提供 RAID0（条带化）、RAID1（镜像）和 RAID5 功能。

## 硬件

`hptrr` 驱动支持以下 RAID 控制器：

- RocketRAID 172x 系列
- RocketRAID 174x 系列
- RocketRAID 2210
- RocketRAID 222x 系列
- RocketRAID 2240
- RocketRAID 230x 系列
- RocketRAID 231x 系列
- RocketRAID 232x 系列
- RocketRAID 2340
- RocketRAID 2522

## 注释

`hptrr` 驱动仅能在 i386 和 amd64 平台上工作，因为它需要厂商提供的二进制 blob 对象，而厂商仅为这些平台提供。在启用了 [pae(4)](pae.4.i386.md) 的 i386 上，`hptrr` 驱动*无法*工作。

此驱动不支持 RR182x 系列控制器。有关支持的详细信息，请参见 [hptmv(4)](hptmv.4.md) 手册页。

此驱动取代了旧的 rr232x 驱动。

## 参见

[ata(4)](ata.4.md), cam(4), [hptmv(4)](hptmv.4.md), [mvs(4)](mvs.4.md), [loader(8)](../man8/loader.8.md)

## 历史

`hptrr` 设备驱动最早出现在 FreeBSD 6.3 中。

## 作者

`hptrr` 设备驱动由 HighPoint Technologies, Inc. 编写，并由 Scott Long 移植到 FreeBSD。本手册页由 David E. O'Brien 编写。

## 缺陷

`hptrr` 驱动不支持从操作系统端管理 RAID，RAID 需要从板载 BIOS 中设置。
