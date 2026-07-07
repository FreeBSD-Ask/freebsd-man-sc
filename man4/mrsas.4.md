# mrsas(4)

`mrsas` — Broadcom/LSI MegaRAID 6/12Gb/s SAS+SATA RAID 控制器驱动

## 名称

`mrsas`

## 概要

`device pci device mrsas`

`在 loader.conf(5) 中：mrsas_load="YES"`

`在 sysctl.conf(5) 中：dev.mrsas.X.disable_ocr dev.mrsas.X.fw_outstanding dev.mrsas.X.mrsas_fw_fault_check_delay dev.mrsas.X.mrsas_io_timeout hw.mrsas.X.debug_level`

## 描述

`mrsas` 驱动将检测 Broadcom/LSI 的 6Gb/s 和 12Gb/s PCI Express SAS/SATA/NVMe RAID 控制器。附加到 `mrsas` 驱动的磁盘（虚拟磁盘/物理磁盘）将通过 [camcontrol(8)](../man8/camcontrol.8.md) 以 `/dev/da?` 设备节点的形式对用户可见。每个控制器还通过 `/dev/mrsas?` 设备节点提供简单的管理接口。

`mrsas` 这个名称源自短语 "MegaRAID SAS HBA"，它与旧的 "MegaRAID" 驱动 [mfi(4)](mfi.4.md) 有本质区别，后者不将目标连接到 cam(4) 层，因此需要一个将目标附加到 cam(4) 层的新驱动。较旧的 MegaRAID 控制器由 [mfi(4)](mfi.4.md) 支持，无法与 `mrsas` 一起工作，但 [mfi(4)](mfi.4.md) 和 `mrsas` 驱动都能检测并管理 Broadcom/LSI MegaRAID SAS 2208/2308/3008/3108 系列控制器。

提供了 [device.hints(5)](../man5/device.hints.5.md) 选项用于调整 `mrsas` 驱动对 LSI MegaRAID SAS 2208/2308/3008/3108 控制器的行为。默认情况下，[mfi(4)](mfi.4.md) 驱动将检测这些控制器。有关 MR-Fusion 设备的驱动优先级，参见下文的优先级章节。

`mrsas` 在设备 ID 为 0x005B、0x005D 和 0x005F 的探测调用中提供 -30 的优先级（介于 `BUS_PROBE_DEFAULT` 和 `BUS_PROBE_LOW_PRIORITY` 之间），因此 `mrsas` 不会在无用户干预的情况下控制这些设备。

如果底层适配器允许，固态硬盘（SSD）在使用 `mrsas` 时可获得 ATA TRIM 支持。这可能需要将 SSD 配置为 Non-RAID 驱动器而非 JBOD 虚拟模式。

## 硬件

`mrsas` 驱动支持以下 Broadcom/LSI SATA/SAS RAID 控制器：

| 控制器 | 芯片 | 速率 |
| ------ | ---- | ---- |
| Broadcom SAS3916 | Aero | 12Gb/s |
| Broadcom SAS3908 | Aero | 12Gb/s |
| LSI MegaRAID SAS 9380 | Invader/Fury | 12Gb/s |
| LSI MegaRAID SAS 9361 | Invader/Fury | 12Gb/s |
| LSI MegaRAID SAS 9341 | Invader/Fury | 12Gb/s |
| LSI MegaRAID SAS 9286 | Thunderbolt | 6Gb/s |
| LSI MegaRAID SAS 9285 | Thunderbolt | 6Gb/s |
| LSI MegaRAID SAS 9272 | Thunderbolt | 6Gb/s |
| LSI MegaRAID SAS 9271 | Thunderbolt | 6Gb/s |
| LSI MegaRAID SAS 9270 | Thunderbolt | 6Gb/s |
| LSI MegaRAID SAS 9267 | Thunderbolt | 6Gb/s |
| LSI MegaRAID SAS 9266 | Thunderbolt | 6Gb/s |
| LSI MegaRAID SAS 9265 | Thunderbolt | 6Gb/s |
| LSI SAS 3108 | | 12Gb/s |
| LSI SAS 3008 | | 12Gb/s |
| LSI SAS 2308 | | 6Gb/s |
| LSI SAS 2208 | | 6Gb/s |
| DELL PERC H830 | Invader/Fury | 12Gb/s |
| DELL PERC H810 | Thunderbolt | 6Gb/s |
| DELL PERC H730/P | Invader/Fury | 12Gb/s |
| DELL PERC H710/P | Thunderbolt | 6Gb/s |
| DELL PERC H330 | Invader/Fury | 12Gb/s |
| Fujitsu D3116 | Thunderbolt | 6Gb/s |

## 配置

要为特定的 `mrsas` 驱动实例禁用 Online Controller Reset（OCR），请在 loader.conf(5) 中设置以下可调参数：

```sh
`dev.mrsas.X.disable_ocr=1`
```

其中 X 是适配器编号。

要为特定的 `mrsas` 驱动实例更改 I/O 超时值，请在 loader.conf(5) 中设置以下可调参数：

```sh
`dev.mrsas.X.mrsas_io_timeout=NNNNNN`
```

其中 NNNNNN 是以毫秒为单位的超时值。

要为特定的 `mrsas` 驱动实例更改固件故障检查计时器值，请在 loader.conf(5) 中设置以下可调参数：

```sh
`dev.mrsas.X.mrsas_fw_fault_check_delay=NN`
```

其中 NN 是以秒为单位的故障检查延迟值。

当前活动的 I/O 命令数显示在 `dev.mrsas.X.fw_outstanding` [sysctl(8)](../man8/sysctl.8.md) 变量中。

## 调试

要启用 `mrsas` 驱动的调试输出，请在 loader.conf(5) 中或通过 [sysctl(8)](../man8/sysctl.8.md) 设置 `hw.mrsas.X.debug_level` 变量，其中 X 是适配器编号。以下位具有所述效果：

**0x01** 启用信息性输出。

**0x02** 启用追踪输出。

**0x04** 启用驱动故障输出。

**0x08** 启用 OCR 和 I/O 超时输出。

**0x10** 启用 AEN 事件输出。

## 优先级

`mrsas` 驱动在 PCI 子系统中始终为 MR-Fusion 卡的选择设置默认的 -30 优先级。（介于 `BUS_PROBE_DEFAULT` 和 `BUS_PROBE_LOW_PRIORITY` 之间）。MR-Fusion 控制器包括所有设备 ID 为 0x005B、0x005D、0x005F 的卡。

[mfi(4)](mfi.4.md) 驱动在 PCI 子系统中为 MR-Fusion 卡的选择设置 `BUS_PROBE_DEFAULT` 或 `BUS_PROBE_LOW_PRIORITY` 优先级（取决于 device.hints 设置）。在上述设计下，[mfi(4)](mfi.4.md) 驱动将附加到 MR-Fusion 卡，因为它的优先级高于 `mrsas`。

使用 `/boot/device.hints`（如下所述），用户可指定由 `mrsas` 驱动检测 MR-Fusion 卡，而非 [mfi(4)](mfi.4.md) 驱动。

> `hw.mfi.mrsas_enable="1"`

在引导时，[mfi(4)](mfi.4.md) 驱动默认获得检测 MR-Fusion 控制器的优先级。在更改此默认驱动选择策略之前，LSI 建议用户了解驱动选择策略的工作方式。LSI 的策略是优先由 [mfi(4)](mfi.4.md) 驱动检测 MR-Fusion 卡，但允许选择 `mrsas` 驱动来检测 MR-Fusion 卡。

LSI 建议使用旧 [mfi(4)](mfi.4.md) 驱动且不希望切换到 `mrsas` 的客户设置 `hw.mfi.mrsas_enable="0"`。对于首次使用 MR-Fusion 控制器的用户，LSI 建议使用 `mrsas` 驱动并设置 `hw.mfi.mrsas_enable="1"`。

在大多数情况下，更改默认行为都经过了充分测试，但如果在 [mfi(4)](mfi.4.md) 和 `mrsas` 驱动之间切换以对 MR-Fusion 执行更复杂且不切实际的操作，可能会出现意外行为。切换驱动设计为仅发生一次。虽然多次切换是可能的，但不建议这样做。用户应从**引导**时决定要为 MR-Fusion 卡使用哪个驱动。

用户在从 [mfi(4)](mfi.4.md) 切换到 `mrsas` 时可能会看到不同的设备名。此行为**按预期工作**，如果用户在 [mfi(4)](mfi.4.md) 和 `mrsas` 互操作性方面进行任何实验，则需要手动更改 [fstab(5)](../man5/fstab.5.md) 条目。

## 文件

**`/dev/da?`** 阵列/逻辑磁盘接口
**`/dev/mrsas?`** 管理接口

## 参见

[cam(4)](scsi.4.md), [mfi(4)](mfi.4.md), [pci(4)](pci.4.md), [device.hints(5)](../man5/device.hints.5.md), [camcontrol(8)](../man8/camcontrol.8.md)

## 历史

`mrsas` 驱动首次出现于 FreeBSD 10.1。

> `mfi 驱动：`
> [mfi(4)](mfi.4.md)
> 是旧的
> FreeBSD
> 驱动，最初支持 Gen-1 控制器，
> 后扩展以支持至 MR-Fusion
> （设备 ID = 0x005B、0x005D、0x005F）。

> `mrsas 驱动：`
> `mrsas`
> 是由 LSI 重新设计的新驱动，支持 Thunderbolt 及以后
> 产品。
> 设备 ID 为 0x005B 的 SAS+SATA RAID 控制器在本手册页中
> 称为 Thunderbolt 控制器。

> **cam 感知 HBA 驱动：**
> FreeBSD
> 有一个
> cam(4)
> 层，用于附加存储设备，并为存储控制器和附加设备
> 提供公共访问机制。
> `mrsas`
> 驱动是
> cam(4)
> 感知的，与
> `mrsas`
> 关联的设备可使用
> [camcontrol(8)](../man8/camcontrol.8.md)
> 查看。
> [mfi(4)](mfi.4.md)
> 驱动不理解
> cam(4)
> 层，它直接将存储磁盘关联到块层。
> **Thunderbolt 控制器：**
> 这是设备 ID 为 0x005B 的 6Gb/s MegaRAID HBA 卡。
> **Invader 控制器：**
> 这是设备 ID 为 0x005D 的 12Gb/s MegaRAID HBA 卡。
> **Fury 控制器：**
> 这是设备 ID 为 0x005F 的 12Gb/s MegaRAID HBA 卡。

## 作者

`mrsas` 驱动和本手册页由 Kashyap Desai <Kashyap.Desai@lsi.com> 编写。

## 注意事项

`mrsas` 驱动将设备公开为 `/dev/da?`，而 [mfi(4)](mfi.4.md) 将设备公开为 `/dev/mfid?`。

`mrsas` 不支持 Linux 模拟器接口、mfiutil(8)，也不支持在不编辑 [fstab(5)](../man5/fstab.5.md) 的情况下切换驱动的设备名别名。
