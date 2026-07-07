# mpi3mr(4)

`mpi3mr` — Broadcom MPIMR 3.0 IT/IR 24Gb/s SAS Tri-Mode RAID PCIe 4.0 驱动

## 名称

`mpi3mr`

## 概要

`通过在 loader.conf(5) 中加入以下行，可在引导时以模块形式加载此驱动：`

```sh
mpi3mr_load="YES"
```

## 描述

`mpi3mr` 驱动为 Broadcom Ltd. MPIMR 3.0 IT/IR PCIe 4 控制器提供支持。

## 硬件

`mpi3mr` 驱动支持以下控制器：

- Broadcom Ltd. SAS 4116 Tri-Mode RAID 适配器
- Broadcom Ltd. 9670W-16i 24G PCIe 4.0 Tri-Mode RAID 适配器
- Broadcom Ltd. 9670-24i 24G PCIe 4.0 Tri-Mode RAID 适配器
- Broadcom Ltd. 9660-16i 24G PCIe 4.0 Tri-Mode RAID 适配器
- Broadcom Ltd. 9620-16i 24G PCIe 4.0 Tri-Mode RAID 适配器
- Broadcom Ltd. 9600-24i 24G PCIe 4.0 Tri-Mode RAID 适配器
- Broadcom Ltd. 9600-16i 24G PCIe 4.0 Tri-Mode RAID 适配器
- Broadcom Ltd. 9600W-16e 24G PCIe 4.0 Tri-Mode RAID 适配器
- Broadcom Ltd. 9600-16e 24G PCIe 4.0 Tri-Mode RAID 适配器
- Broadcom Ltd. 9600-8i8e 24G PCIe 4.0 Tri-Mode RAID 适配器

## 参见

[cam(4)](cam.4.md), [cd(4)](cd.4.md), [ch(4)](ch.4.md), [da(4)](da.4.md), [mpr(4)](mpr.4.md), [pci(4)](pci.4.md), [sa(4)](sa.4.md), [scsi(4)](scsi.4.md)

## 历史

`mpi3mr` 驱动首次出现于 FreeBSD 14.0。

## 作者

`mpi3mr` 驱动由 Sumit Saxena <sumit.saxena@broadcom.com> 和 Chandrakanth Patil <chandrakanth.patil@broadcom.com> 编写。本手册页由 Warner Losh <imp@FreeBSD.org> 编写。
