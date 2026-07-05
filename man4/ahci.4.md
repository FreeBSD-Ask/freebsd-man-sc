# ahci.4

`ahci` — 串行 ATA 高级主机控制器接口驱动

## 名称

`ahci`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device pci
> device scbus
> device ahci

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
ahci_load="YES"
```

`以下可调参数可从 loader(8) 设置：`

`控制指定控制器对消息信号中断（MSI）的使用。`

`MSI 禁用；`

`若支持，使用单个 MSI 向量；`

`若支持，使用多个 MSI 向量（默认）。`

**0**
**1**
**2**

`控制指定控制器对命令完成合并（CCC）的使用。非零值启用 CCC 并定义请求在中断前可等待的最大时间（毫秒），前提是控制器队列上还有更多请求。CCC 减少了具有大量并行请求的系统上的上下文切换次数，但由于额外的命令延迟，可能降低某些工作负载下的磁盘性能。`

`控制驱动是应从中断线程直接完成命令，还是将其排队到 CAM 完成线程。默认值取决于支持的 MSI 中断数和已实现的 SATA 端口数。`

`控制驱动是否应在 SGPIO 或其他接口之上实现虚拟机箱管理设备。默认值取决于控制器能力。`

`控制指定通道的 SATA 接口电源管理，允许以额外命令延迟为代价节省部分功耗。可能值：`

`接口电源管理禁用（默认）；`

`允许设备发起 PM 状态更改，主机被动；`

`每次端口空闲时主机发起 PARTIAL PM 状态转换；`

`每次端口空闲时主机发起 SLUMBER PM 状态转换。`

`端口空闲 1 毫秒后驱动发起 PARTIAL PM 状态转换；`

`端口空闲 125 毫秒后驱动发起 SLUMBER PM 状态转换。`

**0**
**1**
**2**
**3**
**4**
**5**

`一些控制器（如 ICH8）在使用 NCQ 时不实现模式 2 和 3。由于人为的进入延迟，模式 4 和 5 中的性能下降远小于模式 2 和 3。`

`注意，接口电源管理会使设备存在检测复杂化。除非硬件实现冷存在检测，否则设备热插拔后可能需要手动总线重置/重新扫描。`

`设为非零值可限制最大 SATA 版本（速度）。值 1、2 和 3 分别对应 1.5、3 和 6 Gbps。`

`设为非零值可强制驱动附加到某些已知的支持 AHCI 的芯片，即使它们配置为传统 IDE 仿真模式。默认为 1。`

**hint.ahci.X.msi**

**hint.ahci.X.ccc**

**hint.ahci.X.direct**

**hint.ahci.X.em**

**hint.ahcich.X.pm_level**

**hint.ahcich.X.sata_rev**

**hw.ahci.force**

## 描述

此驱动为 CAM(4) 子系统提供对 AHCI 兼容控制器的 SATA 端口的本地访问。找到的每个 SATA 端口都作为一个具有一个目标的总线呈现给 CAM，或者，如果 HBA 支持 Port Multipliers，则为 16 个目标。大多数总线管理细节由 CAM 的 SATA 专用传输层处理。连接的 ATA 磁盘由 ATA 协议磁盘外设驱动 [ada(4)](ada.4.md) 处理。ATAPI 设备由 SCSI 协议外设驱动 [cd(4)](cd.4.md)、[da(4)](da.4.md)、[sa(4)](sa.4.md) 等处理。

驱动特性包括支持串行 ATA 和 ATAPI 设备、Port Multipliers（支持时包括基于 FIS 的切换）、硬件命令队列（每端口最多 32 个命令）、原生命令队列、SATA 接口电源管理、设备热插拔和消息信号中断。

驱动支持 AHCI 定义的 "LED" 机箱管理消息。当硬件支持时，它允许通过 [led(4)](led.4.md) API 或模拟的 [ses(4)](ses.4.md) 设备控制每端口活动、定位和故障 LED，以用于定位和状态报告。支持 AHCI 的控制器可通过 SGPIO 接口将这些信息传输到背板控制器。背板控制器以某种方式（IBPI 标准）解释接收到的状态，以使用现有指示器进行报告。

## 硬件

`ahci` 驱动支持 PCI 类为 1（海量存储）、子类为 6（SATA）、编程接口为 1（AHCI）的 AHCI 兼容控制器。

此外，配合 ata(4) 的 atamarvell 和 atajmicron 驱动，它支持传统 PATA + AHCI-SATA 组合控制器的 AHCI 部分，如 JMicron JMB36x 和 Marvell 88SE61xx。

`ahci` 驱动还支持使用 Intel Rapid Storage Technology (RST) 作为 [nvme(4)](nvme.4.md) 的 PCI 桥接的 AHCI 设备。要使用 [nvme(4)](nvme.4.md) 设备，必须在 BIOS 中将 SATA 模式从 RST 设置为 AHCI，或者必须接受由于中断共享而使用 RST 启用时的性能。FreeBSD 会自动检测处于 RST 模式的具有此扩展的 AHCI 设备。发生这种情况时，`ahci` 会将 [nvme(4)](nvme.4.md) 子设备附加到 `ahci` 设备。

## 文件

**`/dev/led/ahci*.*.act`** 活动 LED 设备节点

**`/dev/led/ahci*.*.fault`** 故障 LED 设备节点

**`/dev/led/ahci*.*.locate`** 定位 LED 设备节点

## SYSCTL

**`dev.ahcich.X.disable_phy`** 设为 1 可禁用通道 X 上驱动器的 phy。设为 0 可启用 phy。用于关闭制造麻烦的设备。也可用于需要 ada 驱动器时有时无的调试。

## 参见

[ada(4)](ada.4.md), [ata(4)](ata.4.md), cam(4), [cd(4)](cd.4.md), [da(4)](da.4.md), [sa(4)](sa.4.md), [ses(4)](ses.4.md)

## 历史

`ahci` 驱动最早出现在 FreeBSD 8.0 中。

## 作者

Alexander Motin <mav@FreeBSD.org>
