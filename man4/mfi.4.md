# mfi.4

`mfi` — LSI MegaRAID SAS 驱动

## 名称

`mfi`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device pci
> device mfi

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
mfi_load="YES"
```

## 描述

此驱动用于 LSI 的下一代 PCI Express SAS RAID 控制器。通过 **`/dev/mfid?`** 设备节点可访问此驱动的 RAID 阵列（逻辑磁盘）。每个控制器还通过 **`/dev/mfi?`** 设备节点提供简单的管理接口。

`mfi` 名称来源于短语“MegaRAID Firmware Interface”，它与旧的 “MegaRAID” 接口有本质不同，因此需要新的驱动。旧的 SCSI 和 SATA MegaRAID 卡由 amr(4) 支持，不适用于此驱动。

提供了两个 sysctl 用于调整 `mfi` 驱动在请求删除已挂载卷时的行为。默认情况下，驱动会拒绝任何删除已挂载卷的请求。如果将 sysctl `dev.mfi.%d.delete_busy_volumes` 设置为 1，则驱动允许删除已挂载的卷。

提供了一个可调参数用于调整 `mfi` 驱动在附加到卡时的行为。默认情况下，驱动会以高探测优先级附加到所有已知卡。如果将可调参数 `hw.mfi.mrsas_enable` 设置为 1，则驱动会降低其探测优先级，以允许 [mrsas(4)](mrsas.4.md) 代替 `mfi` 附加到卡。

`mfi` 不支持 ATA TRIM。如需 TRIM 支持，请参见 [mrsas(4)](mrsas.4.md)。

## 硬件

`mfi` 驱动支持以下硬件：

- LSI MegaRAID SAS 1078
- LSI MegaRAID SAS 8408E
- LSI MegaRAID SAS 8480E
- LSI MegaRAID SAS 9240
- LSI MegaRAID SAS 9260
- Dell PERC5
- Dell PERC6
- Fujitsu RAID Controller SAS 6Gbit/s 1GB (D3116)
- IBM ServeRAID M1015 SAS/SATA
- IBM ServeRAID M1115 SAS/SATA
- IBM ServeRAID M5015 SAS/SATA
- IBM ServeRAID M5110 SAS/SATA
- IBM ServeRAID-MR10i
- Intel RAID Controller SRCSAS18E
- Intel RAID Controller SROMBSAS18E

## 文件

**`/dev/mfid?`** 阵列/逻辑磁盘接口

**`/dev/mfi?`** 管理接口

## 诊断

- mfid%d: Unable to delete busy device 试图删除已挂载的卷。

## 参见

amr(4), [pci(4)](pci.4.md), mfiutil(8)

## 历史

`mfi` 驱动首次出现于 FreeBSD 6.1。

## 作者

`mfi` 驱动和本手册页由 Scott Long <scottl@FreeBSD.org> 编写。

## 缺陷

此驱动目前不支持大端架构。
