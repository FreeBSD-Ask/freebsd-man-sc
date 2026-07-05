# aac.4

`aac` — Adaptec AdvancedRAID 控制器驱动

## 名称

`aac`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device pci
> device aac
> device aacp
> 要编译调试代码：
> options AAC_DEBUG=N

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
aac_load="YES"
```

## 描述

`aac` 驱动提供对 Adaptec AAC 系列 SCSI Ultra2、Ultra160 和 Ultra320、SATA 及 SAS RAID 控制器的支持。

可通过 **`/dev/aacd?`** 设备节点访问 RAID 容器。`aacp` 设备启用 SCSI 直通接口，允许通过 CAM [scsi(4)](scsi.4.md) 子系统使用连接到卡上的设备（如 CD-ROM）。请注意，并非所有卡都允许启用此接口。

**`/dev/aac?`** 设备节点提供对控制器管理接口的访问。每块已安装的卡对应一个节点。别名 **`/dev/afa?`** 和 **`/dev/hpn?`** 分别用于兼容 Dell 和 HP 版本的管理工具。如果加载了 `aac_linux.ko` 和 `linux.ko` 模块，将启用管理设备的 Linux 兼容 ioctl(2) 接口，并允许基于 Linux 的管理应用程序控制该卡。

## 硬件

`aacp` 驱动支持以下 Adaptec AAC 系列并行 SCSI、SATA 和 3G SAS RAID 控制器：

- Adaptec AAC-364
- Adaptec RAID 2045
- Adaptec RAID 2405
- Adaptec RAID 2445
- Adaptec RAID 2805
- Adaptec RAID 3085
- Adaptec RAID 31205
- Adaptec RAID 31605
- Adaptec RAID 5085
- Adaptec RAID 51205
- Adaptec RAID 51245
- Adaptec RAID 51605
- Adaptec RAID 51645
- Adaptec RAID 52445
- Adaptec RAID 5405
- Adaptec RAID 5445
- Adaptec RAID 5805
- Adaptec SAS RAID 3405
- Adaptec SAS RAID 3805
- Adaptec SAS RAID 4000SAS
- Adaptec SAS RAID 4005SAS
- Adaptec SAS RAID 4800SAS
- Adaptec SAS RAID 4805SAS
- Adaptec SATA RAID 2020SA ZCR
- Adaptec SATA RAID 2025SA ZCR
- Adaptec SATA RAID 2026ZCR
- Adaptec SATA RAID 2410SA
- Adaptec SATA RAID 2420SA
- Adaptec SATA RAID 2610SA
- Adaptec SATA RAID 2620SA
- Adaptec SATA RAID 2810SA
- Adaptec SATA RAID 2820SA
- Adaptec SATA RAID 21610SA
- Adaptec SCSI RAID 2020ZCR
- Adaptec SCSI RAID 2025ZCR
- Adaptec SCSI RAID 2120S
- Adaptec SCSI RAID 2130S
- Adaptec SCSI RAID 2130SLP
- Adaptec SCSI RAID 2230SLP
- Adaptec SCSI RAID 2200S
- Adaptec SCSI RAID 2240S
- Adaptec SCSI RAID 3230S
- Adaptec SCSI RAID 3240S
- Adaptec SCSI RAID 5400S
- Dell CERC SATA RAID 2
- Dell PERC 2/Si
- Dell PERC 2/QC
- Dell PERC 3/Si
- Dell PERC 3/Di
- Dell PERC 320/DC
- HP ML110 G2 (Adaptec SATA RAID 2610SA)
- HP NetRAID 4M
- IBM ServeRAID 8i
- IBM ServeRAID 8k
- IBM ServeRAID 8s
- ICP RAID ICP5045BL
- ICP RAID ICP5085BL
- ICP RAID ICP5085SL
- ICP RAID ICP5125BR
- ICP RAID ICP5125SL
- ICP RAID ICP5165BR
- ICP RAID ICP5165SL
- ICP RAID ICP5445SL
- ICP RAID ICP5805BL
- ICP RAID ICP5805SL
- ICP ICP5085BR SAS RAID
- ICP ICP9085LI SAS RAID
- ICP ICP9047MA SATA RAID
- ICP ICP9067MA SATA RAID
- ICP ICP9087MA SATA RAID
- ICP ICP9014RO SCSI RAID
- ICP ICP9024RO SCSI RAID
- Legend S220
- Legend S230
- Sun STK RAID REM
- Sun STK RAID EM
- SG-XPCIESAS-R-IN
- SG-XPCIESAS-R-EX
- AOC-USAS-S4i
- AOC-USAS-S8i
- AOC-USAS-S4iR
- AOC-USAS-S8iR
- AOC-USAS-S8i-LP
- AOC-USAS-S8iR-LP

## 文件

**`/dev/aac?`** aac 管理接口

**`/dev/aacd?`** 磁盘/容器接口

## 诊断

在编译时将 `AAC_DEBUG` 设置为 0 到 3 之间的数字将启用逐步详细的调试消息。

适配器可异步向驱动发送状态和告警消息。这些消息会打印在系统控制台上，并排队等待管理应用程序检索。

## 参见

[kld(4)](kld.4.md), [linux(4)](linux.4.md), [scsi(4)](scsi.4.md), [kldload(8)](../man8/kldload.8.md)

## 历史

`aacp` 驱动首次出现于 FreeBSD 4.3。

## 作者

Mike Smith <msmith@FreeBSD.org> Scott Long <scottl@FreeBSD.org>

## 缺陷

此驱动不兼容固件版本为 1.x 的 Dell 控制器。固件版本与 BIOS POST 和驱动附加消息中打印的内核版本相同。

在挂起/恢复时，控制器实际上并未暂停。
