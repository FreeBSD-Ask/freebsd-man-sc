# hptmv(4)

`hptmv` — HighPoint RocketRAID 182x 设备驱动

## 名称

`hptmv`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device hptmv

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
hptmv_load="YES"
```

## 描述

`hptmv` 驱动为基于 HighPoint RocketRAID 182x 的 RAID 控制器提供支持。

这些设备支持 ATA 磁盘驱动器，并提供 RAID0（条带化）、RAID1（镜像）和 RAID5 功能。

## 硬件

`hptmv` 驱动支持以下 ATA RAID 控制器：

- HighPoint RocketRAID 182x 系列

## 注释

`hptmv` 驱动仅能在 i386 和 amd64 平台上工作，因为它需要厂商提供的二进制 blob 对象，而厂商仅为这些平台提供。在启用了 [pae(4)](pae.4.i386.md) 的 i386 上，`hptmv` 驱动*无法*工作。

## 参见

[kld(4)](kld.4.md), [kldload(8)](../man8/kldload.8.md), [loader(8)](../man8/loader.8.md)

## 历史

`hptmv` 设备驱动最早出现在 FreeBSD 5.3 中。

## 作者

`hptmv` 设备驱动由 HighPoint Technologies, Inc. 编写，并由 Scott Long 移植到 FreeBSD。本手册页由 David E. O'Brien 编写。

## 缺陷

`hptmv` 驱动不支持从操作系统端管理 RAID，RAID 需要从板载 BIOS 中设置。
