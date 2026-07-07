# mvs(4)

`mvs` — Marvell 串行 ATA 主机控制器驱动

## 名称

`mvs`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device pci
> device scbus
> device mvs

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
mvs_load="YES"
```

以下可调参数可从 [loader(8)](../man8/loader.8.md) 设置：

控制指定控制器对消息信号中断（MSI）的使用。

控制指定控制器对命令完成合并（CCC）的使用。非零值启用 CCC 并定义请求等待中断的最长时间（以微秒为单位）。CCC 可减少具有许多并行请求的系统上的上下文切换次数，但由于额外的命令延迟，可能会降低某些工作负载下的磁盘性能。

定义 CCC 的已完成命令数，触发中断而无需等待指定的合并超时。

控制指定通道的 SATA 接口电源管理，允许以额外的命令延迟为代价节省一些功耗。可能值：

接口电源管理被禁用（默认）；

允许设备发起 PM 状态更改，主机是被动的；

驱动程序在端口空闲 1ms 后发起 PARTIAL PM 状态转换；

驱动程序在端口空闲 125ms 后发起 SLUMBER PM 状态转换。

**0**
**1**
**4**
**5**

注意，接口电源管理与设备存在检测不兼容。设备热插拔时需要手动总线复位。

设置为非零值会限制最大 SATA 版本（速度）。值 1、2 和 3 分别为 1.5、3 和 6Gbps。

**hint.mvs.X.msi**

**hint.mvs.X.ccc**

**hint.mvs.X.cccc**

**hint.mvsch.X.pm_level**

**hint.mvsch.X.sata_rev**

## 描述

此驱动为 CAM(4) 子系统提供对几代（Gen-I/II/IIe）Marvell SATA 控制器 SATA 端口的原生访问。找到的每个 SATA 端口都作为具有一个目标的独立总线呈现给 CAM，或者，如果 HBA 支持端口倍增器（Gen-II/IIe），则呈现为 16 个目标。大多数总线管理细节由 CAM 的 SATA 专用传输处理。连接的 ATA 磁盘由 ATA 协议磁盘外围驱动 [ada(4)](ada.4.md) 处理。ATAPI 设备由 SCSI 协议外围驱动 [cd(4)](cd.4.md)、[da(4)](da.4.md)、[sa(4)](sa.4.md) 等处理。

驱动功能包括支持串行 ATA 和 ATAPI 设备、端口倍增器（包括基于 FIS 的交换，当支持时）、硬件命令队列（每个端口最多 31 个命令）、原生命令队列、SATA 接口电源管理、设备热插拔和消息信号中断。

## 硬件

`mvs` 驱动支持以下控制器：

Gen-I（SATA 1.5Gbps）：

- 88SX5040
- 88SX5041
- 88SX5080
- 88SX5081

Gen-II（SATA 3Gbps, NCQ, PMP）：

- 88SX6040
- 88SX6041（包括 Adaptec 1420SA）
- 88SX6080
- 88SX6081

Gen-IIe（SATA 3Gbps, NCQ, 带 FBS 的 PMP）：

- 88SX6042
- 88SX7042（包括 Adaptec 1430SA）
- 88F5182 SoC
- 88F6281 SoC
- MV78100 SoC

注意，此硬件仅对 ATA DMA 命令支持命令队列和基于 FIS 的切换。ATAPI 和非 DMA ATA 命令在每个端口上逐个执行。

## 参见

[ada(4)](ada.4.md), [ata(4)](ata.4.md), cam(4), [cd(4)](cd.4.md), [da(4)](da.4.md), [sa(4)](sa.4.md)

## 历史

`mvs` 驱动首次出现于 FreeBSD 8.1。

## 作者

Alexander Motin <mav@FreeBSD.org>
