# nvme(4)

`nvme` — NVM Express 核心驱动

## 名称

`nvme`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device nvme

`或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
nvme_load="YES"
```

`大多数用户还会希望启用 nvd(4) 或 nda(4) 以将 NVM Express 命名空间暴露为可分区的磁盘设备。注意，在 NVM Express 术语中，命名空间大致相当于 SCSI LUN。`

## 描述

`nvme` 驱动为 NVM Express（NVMe）控制器提供支持，例如：

- 硬件初始化
- 每 CPU I/O 队列对
- 用于注册 NVMe 命名空间消费者（如 [nvd(4)](nvd.4.md) 或 [nda(4)](nda.4.md)）的 API
- 用于向命名空间提交 NVM 命令的 API
- 用于控制器和命名空间配置及管理的 ioctl

`nvme` 驱动以 `/dev/nvmeX` 格式创建控制器设备节点，以 `/dev/nvmeXnsY` 格式创建命名空间设备节点。注意，NVM Express 规范中命名空间从 1 开始编号，而非 0，此驱动遵循该约定。

## 配置

默认情况下，`nvme` 会为每个 CPU 创建一个 I/O 队列对，前提是能分配足够的 MSI-X 向量和 NVMe 队列对。如果没有足够的向量或队列对可用，nvme(4) 将使用较少数量的队列对，并为每个队列对分配多个 CPU。

要强制所有 CPU 共享单个 I/O 队列对，请在 loader.conf(5) 中设置以下可调参数：

```sh
hw.nvme.per_cpu_io_queues=0
```

要为每个 I/O 队列对分配多个 CPU，从而减少设备消耗的 MSI-X 向量数，请在 loader.conf(5) 中设置以下可调参数：

```sh
hw.nvme.min_cpus_per_ioq=X
```

要强制所有 `nvme` 驱动实例使用传统中断，请在 loader.conf(5) 中设置以下可调参数：

```sh
hw.nvme.force_intx=1
```

注意，使用 INTx 意味着禁用每 CPU I/O 队列对。

要控制用作支持设备的宿主内存缓冲区的系统 RAM 最大字节数，请设置以下可调参数：

```sh
hw.nvme.hmb_max
```

默认值为每设备物理内存大小的 5%。

要启用自主电源状态转换（APST），请在 loader.conf(5) 中设置以下可调参数：

```sh
hw.nvme.apst_enable=1
```

将应用默认的厂商提供设置（如果有）。要覆盖此设置，请设置以下可调参数：

```sh
hw.nvme.apst_data
```

该字符串必须包含最多 32 个编码整数，例如 "0x6418 0 0 0x3e820"。每个值对应从最低开始的特定可用电源状态，并定义要转换到的目标状态（位 3..7）以及在转换之前等待的空闲时间（以毫秒为单位，位 8..31）。位 0..2 必须为零。

[nvd(4)](nvd.4.md) 驱动默认用于向系统提供磁盘驱动。也可改用 [nda(4)](nda.4.md) 驱动。[nvd(4)](nvd.4.md) 驱动在较小事务和少量 TRIM 命令下性能更好。它立即将所有命令直接发送到驱动器。[nda(4)](nda.4.md) 驱动在较大事务下性能更好，并且会合并 TRIM 命令以提供更好的性能。它可以将命令排队到驱动器；将多个 `BIO_DELETE` 命令合并为一次往返；并使用 CAM I/O 调度器将一种操作偏向于另一种。要选择 [nda(4)](nda.4.md) 驱动，请在 loader.conf(5) 中设置以下可调参数：

```sh
hw.nvme.use_nvd=0
```

此值也可在内核配置文件中设置：

```sh
`options NVME_USE_NVD=0`
```

发生错误时，`nvme` 默认仅打印关于命令的最相关信息。要启用转储有关命令的所有信息，请在 loader.conf(5) 中设置以下可调参数：

```sh
hw.nvme.verbose_cmd_dump=1
```

早期版本的驱动在引导时会重置卡两次。事实证明这不必要且低效，因此驱动现在仅重置驱动器控制器一次。可在内核配置文件中恢复旧行为：

```sh
`options NVME_2X_RESET`
```

## SYSCTL 变量

目前实现了以下控制器级 sysctl：

**`dev.nvme.0.num_cpus_per_ioq`** (R) 与每个 I/O 队列对关联的 CPU 数量。

**`dev.nvme.0.int_coal_time`** (R/W) 中断合并计时器周期，以微秒为单位。设置为 0 可禁用。

**`dev.nvme.0.int_coal_threshold`** (R/W) 中断合并阈值，以命令完成数计。设置为 0 可禁用。

目前实现了以下队列对级 sysctl。管理队列 sysctl 采用 dev.nvme.0.adminq 格式，I/O 队列 sysctl 采用 dev.nvme.0.ioq0 格式。

**`dev.nvme.0.ioq0.num_entries`** (R) 此队列对的命令队列和完成队列中的条目数。

**`dev.nvme.0.ioq0.num_tr`** 当前为此队列对分配的 nvme_tracker 结构数。

**`dev.nvme.0.ioq0.num_prp_list`** 当前为此队列对分配的 nvme_prp_list 结构数。

**`dev.nvme.0.ioq0.sq_head`** (R) 驱动观察到的提交队列头指针的当前位置。当控制器从提交队列取出命令时，头指针递增。

**`dev.nvme.0.ioq0.sq_tail`** (R) 驱动观察到的提交队列尾指针的当前位置。驱动在向提交队列写入命令后递增尾指针，表示有新命令准备好被处理。

**`dev.nvme.0.ioq0.cq_head`** (R) 驱动观察到的完成队列头指针的当前位置。驱动在处理完控制器发布的完成条目后递增头指针。

**`dev.nvme.0.ioq0.num_cmds`** (R) 已在此队列对上提交的命令数。

**`dev.nvme.0.ioq0.dump_debug`** (W) 向此 sysctl 写入 1 会将提交和完成队列的全部内容转储到控制台。

除了典型的 PCI 附接外，`nvme` 驱动还支持附接到 [ahci(4)](ahci.4.md) 设备。由于 Windows 中的限制，Intel 的 Rapid Storage Technology（RST）将 nvme 设备隐藏在 AHCI 设备之后。然而，这实际上也将其对 FreeBSD 内核隐藏。为解决此限制，FreeBSD 检测 AHCI 设备是否支持 RST 以及是否已启用。更多详情请参见 [ahci(4)](ahci.4.md)。

## 诊断

- nvme%d: System interrupt issues? 驱动发现超时事务有待处理的完成记录，表明中断未被传递。系统要么未正确配置中断，要么系统在负载下丢弃了中断。此消息每次引导每个控制器最多出现一次。

## 参见

[nda(4)](nda.4.md), [nvd(4)](nvd.4.md), [pci(4)](pci.4.md), nvmecontrol(8), [disk(9)](../man9/disk.9.md)

## 历史

`nvme` 驱动首次出现于 FreeBSD 9.2。

## 作者

`nvme` 驱动由 Intel 开发，最初由 Jim Harris <jimharris@FreeBSD.org> 编写，并得到 EMC 的 Joe Golio 的贡献。

本手册页由 Jim Harris <jimharris@FreeBSD.org> 编写。
