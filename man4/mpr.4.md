# mpr.4

`mpr` — LSI Fusion-MPT 3/3.5 IT/IR 12Gb/s Serial Attached SCSI/SATA/PCIe 驱动

## 名称

`mpr`

## 概要

`要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device pci
> device scbus
> device mpr

`通过在 loader.conf(5) 中加入以下行，可在引导时以模块形式加载此驱动：`

```sh
mpr_load="YES"
```

## 描述

`mpr` 驱动为 Broadcom Ltd./Avago Tech（LSI）Fusion-MPT 3/3.5 IT/IR SAS/PCIe 控制器提供支持。

## 硬件

`mpr` 驱动支持以下 SATA/SAS/NVMe RAID 控制器：

- Broadcom Ltd./Avago Tech（LSI）SAS 3004（4 端口 SAS）
- Broadcom Ltd./Avago Tech（LSI）SAS 3008（8 端口 SAS）
- Broadcom Ltd./Avago Tech（LSI）SAS 3108（8 端口 SAS）
- Broadcom Ltd./Avago Tech（LSI）SAS 3216（16 端口 SAS）
- Broadcom Ltd./Avago Tech（LSI）SAS 3224（24 端口 SAS）
- Broadcom Ltd./Avago Tech（LSI）SAS 3316（16 端口 SAS）
- Broadcom Ltd./Avago Tech（LSI）SAS 3324（24 端口 SAS）
- Broadcom Ltd./Avago Tech（LSI）SAS 3408（8 端口 SAS/PCIe）
- Broadcom Ltd./Avago Tech（LSI）SAS 3416（16 端口 SAS/PCIe）
- Broadcom Ltd./Avago Tech（LSI）SAS 3508（8 端口 SAS/PCIe）
- Broadcom Ltd./Avago Tech（LSI）SAS 3516（16 端口 SAS/PCIe）
- Broadcom Ltd./Avago Tech（LSI）SAS 3616（16 端口 SAS/PCIe）
- Broadcom Ltd./Avago Tech（LSI）SAS 3708（8 端口 SAS/PCIe）
- Broadcom Ltd./Avago Tech（LSI）SAS 3716（16 端口 SAS/PCIe）
- Broadcom Ltd./Avago Tech（LSI）SAS 3808（8 端口 SAS/PCIe）
- Broadcom Ltd./Avago Tech（LSI）SAS 3816（16 端口 SAS/PCIe）
- Broadcom Ltd./Avago Tech（LSI）SAS 3916（16 端口 SAS/PCIe）

## 配置

在下文所有可调参数描述中，X 表示适配器编号。

要为所有 `mpr` 驱动实例禁用 MSI 中断，请在 loader.conf(5) 中设置此可调参数：

```sh
hw.mpr.disable_msi=1
```

要为特定的 `mpr` 驱动实例禁用 MSI 中断，请在 loader.conf(5) 中设置此可调参数：

```sh
dev.mpr.X.disable_msi=1
```

要为所有 `mpr` 驱动实例禁用 MSI-X 中断，请在 loader.conf(5) 中设置此可调参数：

```sh
hw.mpr.disable_msix=1
```

要为特定的 `mpr` 驱动实例禁用 MSI-X 中断，请在 loader.conf(5) 中设置此可调参数：

```sh
dev.mpr.X.disable_msix=1
```

要为所有适配器设置已分配的最大 DMA 链数，请在 loader.conf(5) 中设置此可调参数：

```sh
hw.mpr.max_chains=NNNN
```

要为特定适配器设置已分配的最大 DMA 链数，请在 loader.conf(5) 中设置此可调参数：

```sh
dev.mpr.X.max_chains=NNNN
```

默认的 max_chains 值为 16384。

当前空闲链帧数存储在 dev.mpr.X.chain_free [sysctl(8)](../man8/sysctl.8.md) 变量中。

自启动以来观察到的最低空闲链帧数存储在 dev.mpr.X.chain_free_lowwater [sysctl(8)](../man8/sysctl.8.md) 变量中。

自启动以来链帧分配失败的次数存储在 dev.mpr.X.chain_alloc_fail [sysctl(8)](../man8/sysctl.8.md) 变量中。这可用于确定是否应增大 max_chains 可调参数以提升性能。

当前活动的 I/O 命令数显示在 dev.mpr.X.io_cmds_active [sysctl(8)](../man8/sysctl.8.md) 变量中。

当前空闲 PRP 页数存储在 dev.mpr.X.prp_pages_free [sysctl(8)](../man8/sysctl.8.md) 变量中。PRP 页由 NVMe 设备用于 I/O 传输，作用类似于 Scatter/Gather 列表。

自启动以来观察到的最低空闲 PRP 页数存储在 dev.mpr.X.prp_pages_free_lowwater [sysctl(8)](../man8/sysctl.8.md) 变量中。

自启动以来 PRP 页分配失败的次数存储在 dev.mpr.X.prp_page_alloc_fail [sysctl(8)](../man8/sysctl.8.md) 变量中。

要为所有适配器设置每次 I/O 使用的最大页数，请在 loader.conf(5) 中设置此可调参数：

```sh
hw.mpr.max_io_pages=NNNN
```

要为特定适配器设置每次 I/O 使用的最大页数，请在 loader.conf(5) 中设置此可调参数：

```sh
dev.mpr.X.max_io_pages=NNNN
```

默认的 max_io_pages 值为 -1，表示每次 I/O 使用的最大 I/O 大小将使用控制器中存储的 IOCFacts 值进行计算。驱动为 max_io_pages 使用的最小值为 1，否则将使用 IOCFacts 计算最大 I/O 大小。从 max_io_pages 或 IOCFacts 计算得到的较小 I/O 大小即为驱动使用的最大 I/O 大小。

自启动以来观察到的最高活动 I/O 命令数存储在 dev.mpr.X.io_cmds_highwater [sysctl(8)](../man8/sysctl.8.md) 变量中。

要为所有适配器将设备排除在 `mpr` 控制之外，请在 loader.conf(5) 中设置此可调参数：

```sh
hw.mpr.exclude_ids=Y
```

Y 表示设备的目标 ID。如果要排除多个设备，目标 ID 以逗号分隔。

要为特定适配器将设备排除在 `mpr` 控制之外，请在 loader.conf(5) 中设置此可调参数：

```sh
dev.mpr.X.exclude_ids=Y
```

Y 表示设备的目标 ID。如果要排除多个设备，目标 ID 以逗号分隔。

适配器可在关机时向 SATA 直接访问设备发出 **StartStopUnit** SCSI 命令。这使设备能够平稳下电。要为所有适配器控制此功能，请在 loader.conf(5) 中将

```sh
hw.mpr.enable_ssu
```

可调参数设置为以下值之一：

**0** 不向 HDD 或 SSD 发送 SSU。

**1** 向 SSD 发送 SSU，但不向 HDD 发送。此为默认值。

**2** 向 HDD 发送 SSU，但不向 SSD 发送。

**3** 同时向 HDD 和 SSD 发送 SSU。

要为特定适配器控制此功能，请在 loader.conf(5) 中设置此可调参数：

```sh
dev.mpr.X.enable_ssu
```

可用的值集与为所有适配器设置此可调参数时相同。

启动需要数秒且 SATA Identify 命令失败的 SATA 磁盘可能无法被驱动发现。通过在 loader.conf(5) 中增大 spinup 等待时间值，有时可解决此问题，使用

```sh
hw.mpr.spinup_wait_time=NNNN
```

可调参数。NNNN 表示设备初始 SATA Identify 命令失败时，等待 SATA 设备启动的秒数。

可为特定适配器在 loader.conf(5) 中设置 spinup 等待时间，使用

```sh
dev.mpr.X.spinup_wait_time=NNNN
```

可调参数。NNNN 是设备初始 SATA Identify 命令失败时，等待 SATA 设备启动的秒数。

驱动可对适配器发现的设备进行映射，使对应于特定设备的目标 ID 在重置和重启后保持不变。在某些情况下，由于某些硬件（例如某些类型的机箱）的意外行为，设备可能丢失其映射的 ID。为克服此问题，提供了一个可调参数，强制驱动使用与设备关联的 Phy 编号映射设备。如果拓扑包含多个机箱/扩展器，则不建议使用此功能。如果拓扑中存在多个机箱/扩展器，Phy 编号会重复，导致这些 Phy 编号处除第一个设备外的所有设备枚举失败。要为所有适配器控制此功能，请在 loader.conf(5) 中将

```sh
hw.mpr.use_phy_num
```

可调参数设置为以下值之一：

**-1** 仅使用 Phy 编号映射设备，绕过驱动的映射逻辑。

**0** 永不使用 Phy 编号映射设备。

**1** 使用 Phy 编号映射设备，但仅在驱动的映射逻辑无法映射正在枚举的设备时使用。此为默认值。

要为特定适配器控制此功能，请在 loader.conf(5) 中设置此可调参数：

```sh
dev.mpr.X.use_phy_num
```

可用的值集与为所有适配器设置此可调参数时相同。

## 调试

通过在 loader.conf(5) 中使用全局 `hw.mpr.debug_level` 和按设备的 `dev.mpr.X.debug_level` 可调参数来控制驱动诊断输出。可在运行时使用 [sysctl(8)](../man8/sysctl.8.md) 变量 `dev.mpr.X.debug_level` 更改任何适配器的调试级别。

所有 `debug_level` 变量可用整数值或文本字符串命名。多个值可通过整数值进行 OR 运算或以逗号分隔的名称列表组合指定。以 "+" 为前缀的文本字符串将指定的调试级别添加到现有集合中，而前缀 "-" 则将其从现有集合中移除。为方便起见，当前 `debug_level` 状态会以两种格式报告。可用级别如下：

| 标志 | 名称 | 描述 |
| ---- | ---- | ---- |
| 0x0001 | info | 基本信息（默认启用） |
| 0x0002 | fault | 驱动故障（默认启用） |
| 0x0004 | event | 控制器事件 |
| 0x0008 | log | 来自控制器的日志数据 |
| 0x0010 | recovery | 恢复操作追踪 |
| 0x0020 | error | 参数错误和编程缺陷 |
| 0x0040 | init | 系统初始化操作 |
| 0x0080 | xinfo | 更详细的信息 |
| 0x0100 | user | 用户生成命令（IOCTL）追踪 |
| 0x0200 | mapping | 设备映射追踪 |
| 0x0400 | trace | 通过驱动函数的追踪 |

## 参见

[cam(4)](cam.4.md), [cd(4)](cd.4.md), [ch(4)](ch.4.md), [da(4)](da.4.md), [mps(4)](mps.4.md), [mpt(4)](mpt.4.md), [pci(4)](pci.4.md), [sa(4)](sa.4.md), [scsi(4)](scsi.4.md), [targ(4)](targ.4.md), [loader.conf(5)](../man5/loader.conf.5.md), [mprutil(8)](../man8/mprutil.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`mpr` 驱动首次出现于 FreeBSD 9.3。

## 作者

`mpr` 驱动最初由 Scott Long <scottl@FreeBSD.org> 编写。LSI Corporation、Avago Technologies（前身为 LSI）和 Broadcom Ltd.（前身为 Avago）对其进行了改进和测试。

本手册页由 Ken Merry <ken@FreeBSD.org> 编写，Stephen McConnell <slm@FreeBSD.org> 提供了补充意见。
