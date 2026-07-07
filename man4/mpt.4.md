# mpt(4)

`mpt` — LSI Fusion-MPT SCSI/光纤通道驱动

## 名称

`mpt`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device scbus
> device mpt

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
mpt_load="YES"
```

## 描述

`mpt` 驱动为 LSI Logic Fusion-MPT 系列 SCSI、光纤通道和 SAS 控制器提供支持。

## 硬件

`mpt` 驱动支持以下控制器：

- LSI Logic 53c1030、LSI Logic LSI2x320-X（单/双 Ultra320 SCSI）
- LSI Logic AS1064、LSI Logic AS1068（SAS/SATA）
- LSI Logic FC909（1Gb/s 光纤通道）
- LSI Logic FC909A（双 1Gb/s 光纤通道）
- LSI Logic FC919、LSI Logic 7102XP-LC（单 2Gb/s 光纤通道）
- LSI Logic FC929、LSI Logic FC929X、LSI Logic 7202XP-LC（双 2Gb/s 光纤通道）
- LSI Logic FC949X（双 4Gb/s 光纤通道）
- LSI Logic FC949E、LSI Logic FC949ES（双 4Gb/s 光纤通道 PCI-Express）

`mpt` 驱动支持的 Ultra 320 SCSI 控制器芯片可在许多系统主板上找到，包括：

- Dell PowerEdge 1750 至 2850
- IBM eServer xSeries 335

这些系统还包含 Integrated RAID Mirroring 和 Integrated RAID Mirroring Enhanced，本驱动也予以支持。

SAS 控制器芯片也出现在许多基于 AMD/Opteron 的新系统上，例如 Sun 4100。注意，此控制器可同时驱动 SAS 和 SATA 驱动器或两者的混合。这些控制器可用的 Integrated RAID Mirroring 最多只能算是支持不佳。

光纤通道控制器芯片组支持多种速率和系统。Apple 光纤通道 HBA 实际上就是 FC949ES 卡。

此驱动还支持光纤通道卡的目标模式。可通过 LSI Logic 固件实用程序设置核心的预期角色来启用此支持，该实用程序用于确定卡可承担的角色——无需单独编译。

## 警告

`mpt` 驱动支持的大多数控制器对支持的磁盘大小有限制（通常 <2TB）。虽然大多数控制器会截断可用的磁盘大小，但其他控制器可能出现意外行为，并可能导致严重的数据丢失。有关支持的磁盘大小和限制，请参阅芯片组和固件版本的数据手册。

## 参见

[cd(4)](cd.4.md), [ch(4)](ch.4.md), [da(4)](da.4.md), [mps(4)](mps.4.md), [pci(4)](pci.4.md), [sa(4)](sa.4.md), [scsi(4)](scsi.4.md), [targ(4)](targ.4.md), [gmultipath(8)](../man8/gmultipath.8.md), [mptutil(8)](../man8/mptutil.8.md)

> "LSI Logic Website"。

## 历史

`mpt` 驱动首次出现于 FreeBSD 4.6。

## 作者

`mpt` 驱动最初由 Greg Ansley 为 FreeBSD 编写，Matt Jacob <mjacob@FreeBSD.org> 进行了少量改进。

Justin Gibbs <gibbs@FreeBSD.org> 和 Scott Long <scottl@FreeBSD.org> 进行了更实质性的改进。
