# nda(4)

`nda` — NVMe 直接访问设备驱动

## 名称

`nda`

## 概要

`device nvme device scbus`

## 描述

`nda` 驱动提供对实现 NVMe 命令协议并通过 CAM 子系统支持的主机适配器连接到系统的直接访问设备的支持。

## 硬件

`nda` 驱动支持通过 CAM 子系统经 PCIe 或经 NVMF（NVMe over Fabric）连接的 NVMe（Non-Volatile Memory Express）存储设备。

## SYSCTL 变量

以下变量既可作为 [sysctl(8)](../man8/sysctl.8.md) 变量，也可作为 [loader(8)](../man8/loader.8.md) 可调参数使用：

**`hw.nvme.use_nvd`** 设置为 0 时，[nvme(4)](nvme.4.md) 驱动会为块存储创建 `nda` 设备节点。设置为 1 时创建 [nvd(4)](nvd.4.md) 块存储设备节点。设置为 1 时请参见 [nvd(4)](nvd.4.md)。

**`kern.cam.nda.nvd_compat`** 设置为 1 时，会为所有 `nda` 设备（包括分区和其他从磁盘名称派生名称的 [geom(4)](geom.4.md) 提供者）创建 [nvd(4)](nvd.4.md) 别名。然而，[nvd(4)](nvd.4.md) 设备不会在 `kern.disks` [sysctl(8)](../man8/sysctl.8.md) 中报告。

**`kern.cam.nda.sort_io_queue`** 此变量确定软件排队条目是否按 LBA 顺序排序。排序几乎总是浪费时间。默认不排序。

**`kern.cam.nda.enable_biospeedup`** 此变量确定 `nda` 设备是否参与加速协议。当设备参与加速时，上层发送 `BIO_SPEEDUP` 时，所有尚未发送到硬件的当前 `BIO_DELETE` 请求都会立即成功完成，而不会发送到硬件。在文件系统遇到严重短缺并立即需要块的低磁盘空间场景中使用。由于在 LBA 长时间未使用时 trim 收益最大，因此在需要立即写入空间时跳过 trim 几乎不会导致额外的磨损。禁用参与时，`BIO_SPEEDUP` 请求将被忽略。

**`kern.cam.nda.max_trim`** 每次发送到硬件的 DSM trim 一起收集的最大 LBA 范围数。默认为 256，这是协议支持的最大范围数。有时可以通过限制发送到设备的范围数来缓解 trim 性能差的问题。此值必须在 1 到 256 之间（含）。

以下报告按设备的设置，除另有说明外均为只读。将 `N` 替换为设备单元号。

**`OPEN`** 设备已打开。

**`DIRTY`** 在调度对驱动器的写入时设置。在刷新命令后清除。

**`SCtx_INIT`** 创建 [sysctl(8)](../man8/sysctl.8.md) 节点后设置的内部标志。

**`kern.cam.nda.N.rotating`** 此变量报告存储卷是旋转的还是闪存。其值硬编码为 0，表示闪存。

**`kern.cam.nda.N.unmapped_io`** 此变量报告 `nda` 驱动是否接受此单元的未映射 I/O。

**`kern.cam.nda.N.flags`** 此变量报告当前标志。

**`kern.cam.nda.N.sort_io_queue`** 与 `kern.cam.nda.sort_io_queue` 可调参数相同。

**`kern.cam.nda.N.trim_ticks`** 可写。大于零时，在发送到驱动器之前保留 trim 最多此数量的滴答。有时等待一会儿以收集更多 trim 一起发送可以提高 trim 性能。为 0 时不延迟 trim。

**`kern.cam.nda.N.trim_goal`** 可写。延迟收集多个 trim 时，将累积的 DSM TRIM 发送到驱动器。

**`kern.cam.nda.N.trim_lbas`** 已 trim 的 LBA 总数。

**`kern.cam.nda.N.trim_ranges`** 已 trim 的 LBA 范围总数。

**`kern.cam.nda.N.trim_count`** 发送到硬件的 trim 总数。

**`kern.cam.nda.N.deletes`** 排队到设备的 `BIO_DELETE` 请求总数。

## 命名空间映射

每个 [nvme(4)](nvme.4.md) 驱动器都有一个或多个与之关联的命名空间。驱动器上的每个命名空间都会创建一个 `nda` 驱动程序实例。[nvme(4)](nvme.4.md) 设备的所有 `nda` 节点都在目标 0 处。然而，命名空间 ID 映射到 CAM lun，如内核消息和 [camcontrol(8)](../man8/camcontrol.8.md) 的 `devlist` 子命令中所报告。

命名空间通过 nvmecontrol(8) 的 `ns` 子命令管理。并非所有驱动器都支持命名空间管理，但所有驱动器都至少支持一个命名空间。`nda` 的设备节点会在命名空间激活或分离时动态创建和销毁。

## 文件

**`/dev/nda*`** NVMe 存储设备节点

## 参见

cam(4), [geom(4)](geom.4.md), [nvd(4)](nvd.4.md), [nvme(4)](nvme.4.md), [gpart(8)](../man8/gpart.8.md)

## 历史

`nda` 驱动首次出现于 FreeBSD 12.0。

## 作者

Warner Losh <imp@FreeBSD.org>
