# smartpqi(4)

`smartpqi` — Microchip Smart Storage SCSI 驱动

## 名称

`smartpqi`

## 概要

`要将此驱动编译进内核，请将以下行添加到内核配置文件中：`

> device pci
> device scbus
> device smartpqi

`可在引导时以模块形式加载此驱动，方法是将以下行添加到 loader.conf(5) 中：`

```sh
smartpqi_load="YES"
```

## 描述

`smartpqi` 驱动为 Microchip Technology Inc. / Adaptec SmartRaid 和 SmartHBA SATA/SAS/NVMe PCIe 控制器提供支持。

## 硬件

`smartpqi` 驱动支持的控制器包括但不限于：

- HPE Gen10 Smart Array Controller Family
- Adaptec SmartRaid 和 SmartHBA 控制器
- 基于 Microchip Technology Inc. SmartROC 和 SmartIOC 芯片组的 OEM 控制器

## 调试

驱动诊断打印可在引导时通过 loader.conf(5) 中的全局 `hw.smartpqi.debug_level` 可调参数控制，或在运行时通过每控制器的 `dev.smartpqi.<unit>.debug_level` sysctl 控制。

`debug_level` 变量以整数值设置。默认值为 0x0060（warn && error）。

以下级别可用：

| *Flag* | *Name* | *Description* |
| ------ | ------ | ------------- |
| 0x0001 | init | 系统初始化操作 |
| 0x0002 | info | 基本信息 |
| 0x0004 | function | 用于显示函数进入和退出 |
| 0x0008 | io | 来自控制器的日志数据 |
| 0x0010 | discovery | 设备发现状态转换 |
| 0x0020 | warning | 操作警告 |
| 0x0040 | error | 参数错误和编程缺陷 |
| 0x0080 | note | 更详细的信息 |

除了基于级别的调试输出外，驱动还始终通过 [device_printf(9)](../man9/device_printf.9.md) 记录设备添加、设备移除和控制器事件（热插拔、硬件、物理/逻辑设备更改、AIO 状态和配置更改），这些信息会出现在 [dmesg(8)](../man8/dmesg.8.md) 中，无论 `debug_level` 设置如何。

例如，要在运行时对第一个控制器启用发现日志记录：

```sh
sysctl dev.smartpqi.0.debug_level=0x0070
```

## 设备提示

以下可调值可在 **`/boot/device.hints`** 中设置，以控制 `smartpqi` 驱动的行为。这些提示的指定格式为：

```sh
hint.smartpqi.<unit>.<variable>=<value>
```

支持的变量有：

**`stream_disable`** 设为 0 时禁用流检测。默认为（启用）。

**`sata_unique_wwn_disable`** 设为 0 时禁用 SATA 唯一全球编号。默认为（启用）。

**`aio_raid1_write_disable`** 设为 0 时禁用 RAID1 写入加速。默认为（启用）。

**`aio_raid5_write_disable`** 设为 0 时禁用 RAID5 写入加速。默认为（启用）。

**`aio_raid6_write_disable`** 设为 0 时禁用 RAID6 写入加速。默认为（启用）。

**`queue_depth`** 设置控制器的队列深度。如果队列深度值大于驱动或控制器支持的最大队列大小，将设为最低大小。如果队列深度值低于最小队列深度，则设为最小队列深度。默认由驱动决定。

**`sg_count`** 设置分散聚集（sg）计数。如果此 sg 计数大于最大 sg 计数，将设为最大 sg 计数。如果此 sg 计数小于最小 sg 计数，将设为最小 sg 计数。默认由驱动决定。

例如，要在第一个控制器上禁用流检测，请将以下行添加到 **`/boot/device.hints`**：

```sh
hint.smartpqi.0.stream_disable="0"
```

## 文件

**`/dev/smartpqi?`** smartpqi 管理接口

## 注释

### 配置

要配置 Microchip Smart Storage 控制器，请参阅控制器的用户指南，可在 <https://www.microchip.com/design-centers/storage> 搜索特定控制器找到。

## 参见

[kld(4)](kld.4.md), [linux(4)](linux.4.md), [pass(4)](pass.4.md), [scsi(4)](scsi.4.md), [xpt(4)](xpt.4.md), loader.conf(5), [camcontrol(8)](../man8/camcontrol.8.md), [dmesg(8)](../man8/dmesg.8.md), [kldload(8)](../man8/kldload.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`smartpqi` 驱动最早出现于 FreeBSD 11.1。

## 作者

John Hall <john.hall@microchip.com>

## 缺陷

挂起/恢复时控制器实际上并未暂停。
