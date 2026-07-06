# scsi.4

`CAM` — 通用访问方法存储子系统

## 名称

`CAM`

## 概要

`device scbus device ada device cd device ch device da device pass device pt device sa options CAMDEBUG options CAM_DEBUG_BUS=-1 options CAM_DEBUG_TARGET=-1 options CAM_DEBUG_LUN=-1 options CAM_DEBUG_COMPILE=CAM_DEBUG_INFO|CAM_DEBUG_CDB|CAM_DEBUG_PROBE options CAM_DEBUG_FLAGS=CAM_DEBUG_INFO|CAM_DEBUG_CDB options CAM_MAX_HIGHPOWER=4 options SCSI_NO_SENSE_STRINGS options SCSI_NO_OP_STRINGS options SCSI_DELAY=8000`

## 描述

`CAM` 子系统提供了一个统一且模块化的系统，用于实现驱动程序以控制各种 SCSI、ATA、NVMe 和 MMC / SD 设备，并通过主机适配器驱动程序利用不同的 SCSI、ATA、NVMe 和 MMC / SD 主机适配器。当系统探测总线时，它会将找到的所有设备附加到相应的驱动程序。如果 [pass(4)](pass.4.md) 驱动配置在内核中，它将附加到所有设备。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`kern.cam.cam_srch_hi`** 对 SCSI3 及以上设备在 LUN 7 以上搜索。

**`kern.cam.tur_timeout`** 初始探测期间向设备发送初始 TEST UNIT READY 命令的超时时间（毫秒）。默认为 1s。FreeBSD 15 及更早版本设置为 60s。

**`kern.cam.inquiry_timeout`** 初始探测期间向设备发送初始 INQUIRY 命令的超时时间（毫秒）。默认为 1s。FreeBSD 15 及更早版本设置为 60s。

**`kern.cam.reportluns_timeout`** 初始探测期间向设备发送初始 REPORT LUNS 命令的超时时间（毫秒）。默认为 50s。

**`kern.cam.max_high_power`** 可同时发出的高功率命令（如 START UNIT）的最大数量。默认为 4。

**`kern.cam.modesense_timeout`** 初始探测期间向设备发送初始 MODE SENSE 命令的超时时间（毫秒）。默认为 1s。FreeBSD 15 及更早版本设置为 60s。

## 内核配置

`CAM` 子系统有若干通用内核配置选项：

**`CAM_BOOT_DELAY`** 在内核静态部分运行之后等待的额外时间，用于发现可能需要时间连接的额外设备，如 USB 连接的存储设备。

**`CAM_IOSCHED_DYNAMIC`** 在 I/O 调度器中基于提示和存储设备的当前性能启用动态决策。

**`CAM_IO_STATS`** 启用外设的统计信息收集。

**`CAM_TEST_FAILURE`** 启用模拟 I/O 失败的能力。

**`CAMDEBUG`** 此选项编译所有 `CAM` 调试 printf 代码。单独包含时不会实际打印任何调试信息。详见下文。

**`CAM_MAX_HIGHPOWER=4`** 设置允许的并发“高功率”命令的最大数量。“高功率”命令是完成时所需电功率比大多数命令更高的命令。SCSI START UNIT 命令就是一个例子。启动磁盘通常比正常操作需要多得多的电功率。此选项允许用户指定在不使计算机电源过载的情况下可以同时有多少个高功率命令未完成。

**`SCSI_NO_SENSE_STRINGS`** 消除每个 SCSI 附加检测码和附加检测码限定符对的文本描述。由于这是一个相当大的文本数据库，消除它可以稍微减小内核大小。这主要用于启动软盘和其他低磁盘空间或低内存空间环境。但在大多数情况下应启用它，因为它能加快 SCSI 错误信息的解释速度。不要被“内核膨胀”狂热者影响——在你的内核中保留检测描述！

**`SCSI_NO_OP_STRINGS`** 禁用每个 SCSI 操作码的文本描述。与上面的检测字符串选项一样，此选项主要适用于启动软盘等内核大小至关重要的环境。不建议在正常使用中启用此选项，因为它会减慢 SCSI 问题的调试。

**`SCSI_DELAY=8000`** 这是 SCSI“总线稳定延迟”。在 `CAM` 中，它以*毫秒*为单位指定，而不是旧 SCSI 层使用的秒。内核启动时，会向每条 SCSI 总线发送总线复位，告诉每个设备将自身复位为默认的传输协商和其他设置。大多数 SCSI 设备需要一些时间从总线复位中恢复。较新的磁盘可能只需 100ms，而旧的速度慢的设备可能需要更长时间。如果未指定 `SCSI_DELAY`，默认为 2 秒。`SCSI_DELAY` 的最小允许值为“100”，即 100ms。一个特殊情况是，如果 `SCSI_DELAY` 设置为 0，将被视为“最低可能值”。在这种情况下，`SCSI_DELAY` 将被重置为 100ms。

所有设备和总线都支持动态分配，因此无需配置设备和控制器的上限；`device da` 即可满足任意数量的磁盘驱动器。

设备要么被*固定*（wired）以显示为特定设备单元，要么被*计数*（counted）以显示为下一个可用未使用单元。

通过设置内核环境提示来固定单元。这通常通过 [loader(8)](../man8/loader.8.md) 交互完成，或通过 **`/boot/device.hints`** 文件自动完成。基本语法为：

```sh
hint.device.unit.property="value"
```

可以将单独的 `CAM` 总线号固定到特定控制器，配置行类似于：

```sh
hint.scbus.0.at="mpr1"
```

这会将 `CAM` 总线号 0 分配给 *mpr1* 驱动程序实例。对于支持多条总线的控制器，可以按如下方式分配特定总线：

```sh
hint.scbus.0.at="ahci1"
hint.scbus.0.bus="1"
```

这会将 `CAM` 总线 0 分配给 *ahci1* 上的总线 1 实例。外设驱动程序可以固定到特定的总线、目标和 LUN：

```sh
hint.da.0.at="scbus0"
hint.da.0.target="0"
hint.da.0.lun="0"
```

这会将 *da0* 分配给 scbus 0 的目标 0、单元（lun）0。省略目标或单元提示将指示 `CAM` 将它们视为通配符，并使用第一个相应的计数实例。这些示例可以组合在一起，允许将外设固定到任何特定的控制器、总线、目标和/或单元实例。

这也适用于 [nvme(4)](nvme.4.md) 驱动器。

```sh
hint.nvme.4.at="pci7:0:0"
hint.scbus.10.at="nvme4"
hint.nda.10.at="scbus10"
hint.nda.10.target="1"
hint.nda.10.lun="12"
hint.nda.11.at="scbus10"
hint.nda.11.target="1"
hint.nda.11.lun="2"
```

这会将 PCI 总线 7 插槽 0 功能 1 处的 NVMe 卡分配给 scbus 10。[nda(4)](nda.4.md) 设备的目标始终为 1。单元是来自驱动器的命名空间标识符。命名空间 ID 1 导出为 *nda10*，命名空间 ID 2 导出为 *nda11*。

对于提供序列号的设备，可以将单元固定到该序列号，而不考虑驱动器连接的位置：

```sh
hint.nda.3.sn="CY0AN07101120B12P"
hint.da.44.sn="143282400011"
hint.ada.2.sn="A065D591"
```

将 *nda3*、*da44* 和 *ada2* 固定到具有指定序列号的驱动器。使用序列号时无需指定 *at* 行。

## 适配器

系统允许通用设备驱动程序通过许多不同类型的适配器工作。适配器从上层获取请求，并在 SCSI、ATA、NVMe 或 MMC / SD 总线与系统之间完成所有 IO。传输的最大大小由适配器决定。大多数适配器可以在单次操作中传输 1MB，但许多适配器可以传输更大量数据。

## 目标模式

某些适配器支持*目标模式*，即系统能够作为设备运行，响应由另一个系统发起的操作。某些适配器支持目标模式，但在 `CAM` SCSI 子系统的此版本中尚未完善。

## 架构

`CAM` 子系统将系统上层与存储设备粘合在一起。PERIPH（外设）设备接受来自 GEOM 和系统其他上层的存储请求，并将其转换为协议请求。XPT（传输层）将这些协议请求分发给 SIM 驱动程序。SIM 驱动程序接收协议请求并将其转换为主机适配器能理解的硬件命令，以传输协议请求和数据（如果有）到存储设备。CCB 作为消息在这些请求之间传输。

### CAM

通用访问方法是 20 世纪 90 年代定义的用于与磁盘驱动器通信的标准。FreeBSD 是少数完全实现此模型的操作系统之一。CAM 不同部分之间的接口是 CCB（或 CAM 控制块）。每个 CCB 都有一个标准头，包含请求类型和分派信息，以及一个命令特定部分。CAM Periph 生成请求。XPT 层将这些请求分发给相应的 SIM。一些 CCB 直接发送到 SIM 进行立即处理，而其他的则排队并在 I/O 完成时完成。SIM 接收 CCB 并将其转换为硬件特定命令，将 SCSI CDB 或其他协议控制块推送到外设，并为相关数据设置 DMA。

### 外设设备

外设驱动程序知道如何将标准请求转换为 SIM 可以传递给硬件的协议消息。这些请求可以来自任何上层源，但主要通过 GEOM 作为 bio 请求传入。它们也可以直接来自磁带和 pass through 命令的字符设备请求。

磁盘设备，或 CAM 中的直接访问（da），是外设的一种类型。这些设备向内核呈现以“da”结尾的设备。每个协议都有唯一的设备名：

**[da(4)](da.4.md)** SCSI 或 SAS 设备，或接受 SCSI CDB 进行 I/O 的设备。

**[ada(4)](ada.4.md)** ATA 或 SATA 设备

**[nda(4)](nda.4.md)** NVME 设备

**sdda(4)** SD 或 MMC 块存储设备。

磁带设备在 CAM 中称为顺序访问（[sa(4)](sa.4.md)）。它们通过字符设备与系统接口，并为磁带机提供 ioctl(2) 控制。

[pass(4)](pass.4.md) 设备将来自用户空间的 CCB 请求直接传递给 SIM。此设备用于向设备发送读取、写入、修剪或刷新以外的命令。[camcontrol(8)](../man8/camcontrol.8.md) 命令使用此设备。

### XPT 驱动程序

传输驱动程序将外设连接到 SIM。它不单独配置。它还负责为那些不自我枚举的 SIM 驱动程序进行设备发现。

### SIM 驱动程序

SIM 过去代表 SCSI 接口模块（SCSI Interface Module）。现在它只是 SIM，因为它理解 SCSI 以外的协议。SIM 驱动程序有两种类型：虚拟和物理。物理 SIM 通常称为主机总线适配器（HBA），但并非全部如此。虚拟 SIM 驱动程序用于与网络或虚拟机主机通信。

## 文件

参见其他 `CAM` 设备条目。

## 诊断

可以使用 XPT_DEBUG CCB 从编译进内核的选项列表中，对任何特定总线/设备启用各种数量的跟踪信息。目前有七个调试标志可以编译进内核并使用：

**`CAM_DEBUG_INFO`** 此标志为相关设备启用一般信息 printf。

**`CAM_DEBUG_TRACE`** 此标志启用函数级命令流跟踪，即内核 printf 将在各种函数的入口和出口发生。

**`CAM_DEBUG_SUBTRACE`** 此标志启用各种函数内部的调试输出。

**`CAM_DEBUG_CDB`** 此标志将导致内核打印发送到特定设备的所有 ATA 和 SCSI 命令。

**`CAM_DEBUG_XPT`** 此标志将启用命令调度器跟踪。

**`CAM_DEBUG_PERIPH`** 此标志将启用外设驱动程序消息。

**`CAM_DEBUG_PROBE`** 此标志将启用设备探测过程跟踪。

其中一些标志，特别是 `CAM_DEBUG_TRACE` 和 `CAM_DEBUG_SUBTRACE`，会产生极大量的内核 printf。

用户可以通过以下内核配置选项从内核配置文件中启用调试：

**`CAMDEBUG`** 将所有可能的 `CAM` 调试构建到内核中。

**`CAM_DEBUG_COMPILE`** 指定应构建到内核中的上述调试标志的支持。如果用户希望看到多个调试级别的 printf，可以将标志进行 OR 运算组合。

**`CAM_DEBUG_FLAGS`** 从内核配置文件设置各种调试标志。

**`CAM_DEBUG_BUS`** 指定要调试的总线。要调试所有总线，设置为 -1。

**`CAM_DEBUG_TARGET`** 指定要调试的目标。要调试所有目标，设置为 -1。

**`CAM_DEBUG_LUN`** 指定要调试的 LUN。要调试所有 LUN，设置为 -1。

如果内核中构建了所需选项，用户还可以使用 [camcontrol(8)](../man8/camcontrol.8.md) 工具即时启用调试。详见 [camcontrol(8)](../man8/camcontrol.8.md)。

## 参见

**命令：** [camcontrol(8)](../man8/camcontrol.8.md), camdd(8)

**库：** cam(3)

**外设驱动：** [ada(4)](ada.4.md), [da(4)](da.4.md), [nda(4)](nda.4.md), [pass(4)](pass.4.md), [sa(4)](sa.4.md)

**SIM 设备：** [aac(4)](aac.4.md), [aacraid(4)](aacraid.4.md), [ahc(4)](ahc.4.md), [ahci(4)](ahci.4.md), [ata(4)](ata.4.md), [aw_mmc(4)](aw_mmc.4.md), [ciss(4)](ciss.4.md), [hv_storvsc(4)](hv_storvsc.4.md), [isci(4)](isci.4.md), [iscsi(4)](iscsi.4.md), [isp(4)](isp.4.md), [mpr(4)](mpr.4.md), [mps(4)](mps.4.md), [mpt(4)](mpt.4.md), [mrsas(4)](mrsas.4.md), [mvs(4)](mvs.4.md), [nvme(4)](nvme.4.md), [pms(4)](pms.4.md), [pvscsi(4)](pvscsi.4.md), [sdhci(4)](sdhci.4.md), [smartpqi(4)](smartpqi.4.md), [sym(4)](sym.4.md), [tws(4)](tws.4.md), [umass(4)](umass.4.md), [virtio_scsi(4)](virtio_scsi.4.md)

**已弃用或支持不佳的 SIM 设备：** [ahd(4)](ahd.4.md), amr(4), [arcmsr(4)](arcmsr.4.md), esp(4), [hpt27xx(4)](hpt27xx.4.md), [hptiop(4)](hptiop.4.md), [hptmv(4)](hptmv.4.md), [hptnr(4)](hptnr.4.md), iir(4) [mfi(4)](mfi.4.md), [sbp(4)](sbp.4.md), twa(4)

**DTrace 提供者：** [dtrace_cam(4)](dtrace_cam.4.md)

## 历史

`CAM` SCSI 子系统首次出现于 FreeBSD 3.0。`CAM` ATA 支持在 FreeBSD 8.0 中添加。

## 作者

`CAM` SCSI 子系统由 Justin Gibbs 和 Kenneth Merry 编写。`CAM` ATA 支持由 Alexander Motin <mav@FreeBSD.org> 添加。`CAM` NVMe 支持由 Warner Losh <imp@FreeBSD.org> 添加。
