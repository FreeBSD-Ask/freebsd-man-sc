# ataraid.4

`ataraid` — ATA 软件 RAID 支持

## 名称

`ataraid`

## 概要

```ini
device ata
device ataraid
```

## 描述

`ataraid` 驱动为所谓的软件 RAID（有时被称为 fake RAID 或伪 RAID）提供支持。

当支持软件 RAID 的控制器被指示创建 RAID 阵列时，其 BIOS 会以特定元数据格式将数据结构写入磁盘。这些数据结构会被 `ataraid` 驱动读取，以便 FreeBSD 能够使用该阵列。`ataraid` 驱动必须理解控制器 BIOS 的特定元数据格式，才能支持其 RAID 功能。

对元数据格式的只读支持意味着 FreeBSD 可将给定的 RAID 阵列用于正常的读/写操作。此类阵列的创建和重建必须在控制器 BIOS 中完成。

对元数据格式的读写支持意味着 FreeBSD 可将给定的 RAID 阵列用于正常的读/写操作。此外，可使用 atacontrol(8) 实用程序创建、重建、更新和使此类 RAID 阵列失败。

`ataraid` 驱动可读取以下元数据格式：

- Adaptec HostRAID
- Highpoint V2 RocketRAID
- Highpoint V3 RocketRAID
- Intel MatrixRAID
- Integrated Technology Express（ITE）
- JMicron
- LSI Logic V2 MegaRAID
- LSI Logic V3 MegaRAID
- NVIDIA MediaShield
- Promise FastTrak
- Silicon Image Medley
- Silicon Integrated Systems（SiS）
- VIA Tech V-RAID
- FreeBSD PseudoRAID

`ataraid` 驱动可写入以下元数据格式：

- Highpoint V2 RocketRAID
- Intel MatrixRAID
- JMicron
- Promise FastTrak
- Silicon Integrated Systems（SiS）
- VIA Tech V-RAID
- FreeBSD PseudoRAID

也可在没有特殊软件 RAID 功能的控制器上使用软件 RAID。详情参见 atacontrol(8)。

## 文件

**/dev/ar\***：ATA RAID 设备节点

## 参见

[ata(4)](ata.4.md), atacontrol(8)

## 作者

`ataraid` 驱动由 Soren Schmidt <sos@FreeBSD.org> 编写。本手册页由 Christian Brueffer <brueffer@FreeBSD.org> 编写。

## 注意事项

目前不支持 RAID5。相关代码存在，但既不使用也不维护奇偶校验信息。
