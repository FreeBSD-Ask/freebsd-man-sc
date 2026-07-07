# siis(4)

`siis` — SiliconImage 串行 ATA 主机控制器驱动

## 名称

`siis`

## 概要

`要将此驱动编译进内核，请将以下行添加到你的内核配置文件中：`

> device pci
> device scbus
> device siis

`或者，要在引导时以模块形式加载此驱动，请将以下行添加到 loader.conf(5) 中：`

```sh
siis_load="YES"
```

`以下可调参数可从 loader(8) 设置：`

`控制指定控制器对消息信号中断（MSI）的使用。`

`控制指定通道的 SATA 接口电源管理，允许以额外命令延迟为代价节省部分功耗。可能值：`

`接口电源管理禁用（默认）；`

`允许设备发起 PM 状态更改，主机被动。`

**0**

**1**

`注意，接口电源管理与设备存在检测不兼容。设备热插拔时需要手动总线重置。`

`设为非零值可限制最大 SATA 版本（速度）。值 1、2 和 3 分别对应 1.5、3 和 6 Gbps。`

**hint.siis.X.msi**

**hint.siisch.X.pm_level**

**hint.siisch.X.sata_rev**

## 描述

此驱动为 CAM(4) 子系统提供对控制器 SATA 端口的本地访问。每个 SATA 端口都作为一个具有 16 个目标的独立总线呈现给 CAM。大多数总线管理细节由 CAM 的 SATA 专用传输层处理。连接的 ATA 磁盘由 ATA 协议磁盘外设驱动 [ada(4)](ada.4.md) 处理。ATAPI 设备由 SCSI 协议外设驱动 [cd(4)](cd.4.md)、[da(4)](da.4.md)、[sa(4)](sa.4.md) 等处理。

驱动特性包括支持串行 ATA 和 ATAPI 设备、Port Multipliers（包括基于 FIS 的切换）、硬件命令队列（每端口 31 个命令）、原生命令队列、SATA 接口电源管理、设备热插拔和消息信号中断。

`siis` 驱动支持的适配器活动 LED 可通过 [led(4)](led.4.md) API 控制，用于定位或状态报告。

## 硬件

`siis` 驱动支持以下控制器芯片：

- SiI3124（PCI-X 133MHz/64bit，4 端口）
- SiI3131（PCIe 1.0 x1，1 端口）
- SiI3132（PCIe 1.0 x1，2 端口）
- SiI3531（PCIe 1.0 x1，1 端口）

## 文件

**`/dev/led/siisch*`** 标识 LED 设备节点

## 参见

[ada(4)](ada.4.md), [ata(4)](ata.4.md), cam(4), [cd(4)](cd.4.md), [da(4)](da.4.md), [led(4)](led.4.md), [sa(4)](sa.4.md)

## 历史

`siis` 驱动最早出现于 FreeBSD 8.0。

## 作者

Alexander Motin <mav@FreeBSD.org>
