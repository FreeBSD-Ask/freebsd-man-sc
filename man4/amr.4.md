# amr.4

`amr` — MegaRAID SCSI/ATA/SATA RAID 驱动

## 名称

`amr`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> device pci
> device scbus
> device amr

或者，要在引导时以模块形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行：

```sh
amr_load="YES"
```

## 弃用通知

`amr` 驱动在 FreeBSD 14.0 中已不存在。

## 描述

`amr` 驱动为 LSI Logic MegaRAID SCSI、ATA 和 SATA RAID 控制器以及传统 American Megatrends MegaRAID SCSI RAID 控制器提供支持，包括由 Dell 和 Hewlett-Packard 重新贴牌并销售的型号。

LSI MegaRAID SAS 控制器由 [mfi(4)](mfi.4.md) 支持，无法与此驱动配合使用。

## 硬件

`amr` 驱动支持的控制器包括：

- MegaRAID SATA 150-4
- MegaRAID SATA 150-6
- MegaRAID SATA 300-4X
- MegaRAID SATA 300-8X
- MegaRAID SCSI 320-1E
- MegaRAID SCSI 320-2E
- MegaRAID SCSI 320-4E
- MegaRAID SCSI 320-0X
- MegaRAID SCSI 320-2X
- MegaRAID SCSI 320-4X
- MegaRAID SCSI 320-0
- MegaRAID SCSI 320-1
- MegaRAID SCSI 320-2
- MegaRAID SCSI 320-4
- MegaRAID Series 418
- MegaRAID i4 133 RAID
- MegaRAID Elite 1500（Series 467）
- MegaRAID Elite 1600（Series 493）
- MegaRAID Elite 1650（Series 4xx）
- MegaRAID Enterprise 1200（Series 428）
- MegaRAID Enterprise 1300（Series 434）
- MegaRAID Enterprise 1400（Series 438）
- MegaRAID Enterprise 1500（Series 467）
- MegaRAID Enterprise 1600（Series 471）
- MegaRAID Express 100（Series 466WS）
- MegaRAID Express 200（Series 466）
- MegaRAID Express 300（Series 490）
- MegaRAID Express 500（Series 475）
- Dell PERC
- Dell PERC 2/SC
- Dell PERC 2/DC
- Dell PERC 3/DCL
- Dell PERC 3/QC
- Dell PERC 4/DC
- Dell PERC 4/IM
- Dell PERC 4/SC
- Dell PERC 4/Di
- Dell PERC 4e/DC
- Dell PERC 4e/Di
- Dell PERC 4e/Si
- Dell PERC 4ei
- HP NetRAID-1/Si
- HP NetRAID-3/Si（D4943A）
- HP Embedded NetRAID
- Intel RAID Controller SRCS16
- Intel RAID Controller SRCU42X

## 诊断

### 驱动初始化/关闭阶段

```text
amr%d: memory window not available
amr%d: I/O window not available
```

PCI BIOS 未分配控制器正常运行所需的资源。驱动无法附加到此控制器。

```text
amr%d: busmaster bit not set, enabling
```

PCI BIOS 未启用总线主控 DMA，而这是控制器正常运行所必需的。驱动已启用此位，初始化将继续。

```text
amr%d: can't allocate register window
amr%d: can't allocate interrupt
amr%d: can't set up interrupt
amr%d: can't allocate parent DMA tag
amr%d: can't allocate buffer DMA tag
amr%d: can't allocate scatter/gather DMA tag
amr%d: can't allocate s/g table
amr%d: can't allocate mailbox tag
amr%d: can't allocate mailbox memory
```

初始化驱动时发生资源分配错误；初始化失败，驱动将不会附加到此控制器。

```text
amr%d: can't obtain configuration data from controller
amr%d: can't obtain product data from controller
```

驱动无法从控制器获取关键配置数据。初始化失败，驱动将不会附加到此控制器。

```text
amr%d: can't establish configuration hook
amr%d: can't scan controller for drives
```

扫描控制器管理的逻辑驱动器失败。不会附加任何驱动器。

```text
amr%d: device_add_child failed
amr%d: bus_generic_attach returned %d
```

创建逻辑驱动器实例失败；一个或多个逻辑驱动器可能未能附加。

```text
amr%d: flushing cache...
```

控制器缓存在关闭或分离前正在刷新。

### 运行时诊断

```text
amr%d: I/O beyond end of unit (%u,%d > %u)
```

分区错误或磁盘损坏导致 I/O 请求超出逻辑驱动器末尾。如果启用了 FlexRAID Virtual Sizing 并对虚拟驱动器中超出实际可用容量的部分尝试 I/O 操作，也可能发生此情况。

```text
amr%d: polled command timeout
```

初始化命令超时。初始化过程可能因此失败。

```text
amr%d: bad slot %d completed
```

控制器报告完成了驱动未发出的命令。可能导致数据损坏，表明系统或控制器存在硬件或固件问题。

```text
amr%d: I/O error - %x
```

发生了 I/O 错误。

## 参见

[cd(4)](cd.4.md), [da(4)](da.4.md), [mfi(4)](mfi.4.md), [sa(4)](sa.4.md), [scsi(4)](scsi.4.md)

## 作者

`amr` 驱动由 Mike Smith <msmith@FreeBSD.org> 编写。

本手册页由 Mike Smith <msmith@FreeBSD.org> 和 Jeroen Ruigrok van der Werven <asmodai@FreeBSD.org> 编写。
