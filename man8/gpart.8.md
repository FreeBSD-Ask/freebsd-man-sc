# gpart(8)

`gpart` — 磁盘分区 GEOM 类的控制工具

## 名称

`gpart`

## 概要

`gpart add -t type [-a alignment] [-b start] [-s size] [-i index] [-l label] [-f flags] geom`

`gpart backup geom`

`gpart bootcode [-N] [-b bootcode] [-p partcode -i index] [-f flags] geom`

`gpart commit geom`

`gpart create -s scheme [-n entries] [-f flags] provider`

`gpart delete -i index [-f flags] geom`

`gpart destroy [-F] [-f flags] geom`

`gpart modify -i index [-l label] [-t type] [-f flags] geom`

`gpart recover [-f flags] geom`

`gpart resize -i index [-a alignment] [-s size] [-f flags] geom`

`gpart restore [-lF] [-f flags] provider [...]`

`gpart set -a attrib -i index [-f flags] geom`

`gpart [--libxo] show [-l | -r] [-p] [geom ...]`

`gpart undo geom`

`gpart unset -a attrib -i index [-f flags] geom`

`gpart list`

`gpart status`

`gpart load`

`gpart unload`

## 描述

`gpart` 工具用于对 GEOM provider（通常是磁盘）进行分区。第一个参数是要执行的操作：

**`add`** 向由 `geom` 指定的分区方案中添加新分区。分区类型必须通过 `-t` `type` 指定。如果未指定相应选项，分区的位置、大小和其他属性将自动计算。`add` 命令接受以下选项：

**`-a`** `alignment` 如果指定，则 `gpart` 工具会尝试将 `start` 偏移量和分区 `size` 对齐为 `alignment` 值的倍数。

**`-b`** `start` 分区起始的逻辑块地址。允许使用单字符后缀（k、m、g 等）来指定二进制字节大小。

**`-f`** `flags` 额外的操作标志。关于其用法，参见下文“操作标志”一节的讨论。

**`-i`** `index` 新分区在分区表中放置位置的索引。该索引决定了用于表示该分区的设备特殊文件的名称。

**`-l`** `label` 附加到分区上的标签。此选项仅在使用支持分区标签的分区方案时有效。

**`-s`** `size` 创建大小为 `size` 的分区。允许使用单字符后缀（k、m、g 等）来指定二进制字节大小。

**`-t`** `type` 创建类型为 `type` 的分区。分区类型在下文“分区类型”一节中讨论。

**`backup`** 将分区表以 `restore` 操作所使用的特殊格式转储到标准输出。

**`bootcode`** 将引导代码嵌入到 `geom` 的分区方案元数据中（使用 `-b` `bootcode`），或将引导代码写入分区（使用 `-p` `partcode` 和 `-i` `index`）。`bootcode` 命令接受以下选项：

**`-N`** 不保留 MBR 的卷序列号。默认情况下 MBR 引导代码包含卷序列号，`gpart` 在安装新引导代码时会尝试保留它。此选项跳过保留，以兼容某些不支持卷序列号的 [boot0cfg(8)](boot0cfg.8.md) 版本。

**`-b`** `bootcode` 将来自文件 `bootcode` 的引导代码嵌入到 `geom` 的分区方案元数据中。并非所有分区方案都有嵌入式引导代码，因此 `-b` `bootcode` 选项本质上是特定于方案的（参见下文“引导”一节）。`bootcode` 文件必须符合分区方案对文件内容和大小方面的要求。

**`-f`** `flags` 额外的操作标志。关于其用法，参见下文“操作标志”一节的讨论。

**`-i`** `index` 为 `-p` `partcode` 指定目标分区。

**`-p`** `partcode` 将来自文件 `partcode` 的引导代码写入由 `-i` `index` 指定的 `geom` 分区。该文件的大小必须小于分区的大小。

**`commit`** 提交 geom `geom` 的所有挂起更改。默认情况下所有操作都会被提交，不会产生挂起更改。可以通过 `-f` `flags` 选项修改操作，使其不被提交而是成为挂起状态。挂起的更改会反映在 geom 和 `gpart` 工具中，但实际并未写入磁盘。`commit` 操作会将所有挂起更改写入磁盘。

**`create`** 在由 `provider` 指定的 provider 上创建新的分区方案。必须通过 `-s` `scheme` 选项指定要使用的方案。`create` 命令接受以下选项：

**`-f`** `flags` 额外的操作标志。关于其用法，参见下文“操作标志”一节的讨论。

**`-n`** `entries` 分区表中条目的数量。每个分区方案都有最小和最大条目数限制。此选项允许创建条目数在限制范围内的分区表。某些方案的最大值等于最小值，而某些方案的最大值足够大，可视为无限制。默认情况下，分区表以最小条目数创建。

**`-s`** `scheme` 指定要使用的分区方案。内核必须先支持特定方案，才能使用该方案对磁盘进行分区。

**`delete`** 从 geom `geom` 中删除分区，并通过 `-i` `index` 选项进一步标识。该分区不能正被内核活跃使用。`delete` 命令接受以下选项：

**`-f`** `flags` 额外的操作标志。关于其用法，参见下文“操作标志”一节的讨论。

**`-i`** `index` 指定要删除的分区的索引。

**`destroy`** 销毁由 geom `geom` 实现的分区方案。`destroy` 命令接受以下选项：

**`-F`** 即使分区表非空也强制销毁。

**`-f`** `flags` 额外的操作标志。关于其用法，参见下文“操作标志”一节的讨论。

**`modify`** 修改 geom `geom` 中的分区，并通过 `-i` `index` 选项进一步标识。只能修改分区的类型和/或标签。并非所有分区方案都支持标签，在这种情况下尝试更改分区标签是无效的。`modify` 命令接受以下选项：

**`-f`** `flags` 额外的操作标志。关于其用法，参见下文“操作标志”一节的讨论。

**`-i`** `index` 指定要修改的分区的索引。

**`-l`** `label` 将分区标签更改为 `label`。

**`-t`** `type` 将分区类型更改为 `type`。

**`recover`** 恢复 geom `geom` 上损坏分区的方案元数据。更多信息参见下文“恢复”一节。`recover` 命令接受以下选项：

**`-f`** `flags` 额外的操作标志。关于其用法，参见下文“操作标志”一节的讨论。

**`resize`** 调整 geom `geom` 中分区的大小，并通过 `-i` `index` 选项进一步标识。如果未指定新大小，则自动计算为 `geom` 上可用的最大值。`resize` 命令接受以下选项：

**`-a`** `alignment` 如果指定，则 `gpart` 工具会尝试将分区 `size` 对齐为 `alignment` 值的倍数。

**`-f`** `flags` 额外的操作标志。关于其用法，参见下文“操作标志”一节的讨论。

**`-i`** `index` 指定要调整大小的分区的索引。

**`-s`** `size` 指定分区的新大小，以逻辑块为单位；如果提供单字符后缀（k、m、g 等），则以二进制字节大小为单位。

**`restore`** 从先前由 `backup` 操作创建并从标准输入读取的备份中恢复分区表。仅恢复分区表。此操作不影响分区内容。恢复分区表并在需要时写入引导代码后，必须从备份恢复用户数据。`restore` 命令接受以下选项：

**`-F`** 在执行恢复之前销毁给定 `provider` 上的分区表。

**`-f`** `flags` 额外的操作标志。关于其用法，参见下文“操作标志”一节的讨论。

**`-l`** 为支持分区标签的分区方案恢复分区标签。

**`set`** 在分区条目上设置指定属性。可用属性列表参见下文“属性”一节。`set` 命令接受以下选项：

**`-a`** `attrib` 指定要设置的属性。

**`-f`** `flags` 额外的操作标志。关于其用法，参见下文“操作标志”一节的讨论。

**`-i`** `index` 指定要设置属性的分区的索引。

**`show`** 显示指定 geom 的当前分区信息，如果未指定则显示所有 geom 的信息。默认输出包括每个分区的逻辑起始块、以块为单位的分区大小、分区索引号、分区类型以及人类可读的分区大小。块大小和位置基于设备的 Sectorsize，如 `gpart list` 所示。`show` 命令接受以下选项：

**`-l`** 对于支持分区标签的分区方案，打印标签而非分区类型。

**`-p`** 显示 provider 名称而非分区索引。

**`-r`** 显示原始分区类型而非符号名称。

**`undo`** 还原 geom `geom` 的所有挂起更改。此操作与 `commit` 操作相反，可用于撤销尚未提交的所有更改。

**`unset`** 清除分区条目上的指定属性。可用属性列表参见下文“属性”一节。`unset` 命令接受以下选项：

**`-a`** `attrib` 指定要清除的属性。

**`-f`** `flags` 额外的操作标志。关于其用法，参见下文“操作标志”一节的讨论。

**`-i`** `index` 指定要清除属性的分区的索引。

**`list`** 参见 geom(8)。

**`status`** 参见 geom(8)。

**`load`** 参见 geom(8)。

**`unload`** 参见 geom(8)。

**`--libxo`** 通过 libxo(3) 以多种人类和机器可读格式生成输出。有关命令行参数的详细信息，参见 xo_options(7)。

## 分区方案

`gpart` 工具支持多种分区方案：

**`APM`** Apple Partition Map，用于 PowerPC(R) Macintosh(R) 计算机。需要 `GEOM_PART_APM` 内核选项。

**`BSD`** 传统 BSD disklabel(8)，通常用于细分 MBR 分区。（此方案也可作为唯一的分区方法使用，无需 MBR。其他操作系统的分区编辑工具通常无法理解裸 disklabel 分区布局，因此有时被称为“dangerously dedicated”。）需要 `GEOM_PART_BSD` 内核选项。

**`BSD64`** 用于 Dx 的 64 位 BSD disklabel 实现，用于细分 MBR 或 GPT 分区。需要 `GEOM_PART_BSD64` 内核选项。

**`LDM`** Logical Disk Manager 是 Microsoft Windows NT 的卷管理器实现。需要 `GEOM_PART_LDM` 内核选项。

**`GPT`** GUID Partition Table，用于基于 Intel 的 Macintosh 计算机，并正逐步在大多数 PC 和其他系统上取代 MBR。需要 `GEOM_PART_GPT` 内核选项。

**`MBR`** Master Boot Record，用于 PC 和可移动介质。需要 `GEOM_PART_MBR` 内核选项。`GEOM_PART_EBR` 选项添加对 Extended Boot Record（EBR）的支持，用于定义逻辑分区。`GEOM_PART_EBR_COMPAT` 选项为 EBR 方案中的分区名称启用向后兼容性，同时阻止对此类分区执行任何操作。

有关设备和分区标签化的更多信息，参见 glabel(8)。

## 分区类型

分区在磁盘上由特定的字符串或魔术值标识。`gpart` 工具为常见分区类型使用符号名称，因此用户无需知道这些值或相关分区方案的其他细节。`gpart` 工具还允许用户为没有符号名称的分区类型指定特定于方案的分区类型。FreeBSD 当前理解并使用的符号名称如下：

**`apple-boot`** 在某些 Apple 系统上专用于存储引导加载程序的系统分区。特定于方案的类型为：MBR 使用 `!171`，APM 使用 `!Apple_Bootstrap`，GPT 使用 `!426f6f74-0000-11aa-aa11-00306543ecac`。

**`bios-boot`** 专用于引导加载程序第二阶段的系统分区。通常由 GRUB 2 加载器用于 GPT 分区方案。特定于方案的类型为 `!21686148-6449-6e6f-744e-656564454649`。

**`efi`** 用于使用可扩展固件接口（EFI）的计算机的系统分区。特定于方案的类型为：MBR 使用 `!239`，GPT 使用 `!c12a7328-f81f-11d2-ba4b-00a0c93ec93b`。

**`freebsd`** 用 BSD disklabel 细分为多个文件系统的 FreeBSD 分区。这是一种传统的分区类型，不应用于 APM 或 GPT 方案。特定于方案的类型为：MBR 使用 `!165`，APM 使用 `!FreeBSD`，GPT 使用 `!516e7cb4-6ecf-11d6-8ff8-00022d09712b`。

**`freebsd-boot`** 专用于引导代码的 FreeBSD 分区。特定于方案的类型为 GPT 使用 `!83bd6b9d-7f41-11dc-be0b-001560b84f0f`。

**`freebsd-swap`** 专用于交换空间的 FreeBSD 分区。特定于方案的类型为：APM 使用 `!FreeBSD-swap`，GPT 使用 `!516e7cb5-6ecf-11d6-8ff8-00022d09712b`。

**`freebsd-ufs`** 包含 UFS 或 UFS2 文件系统的 FreeBSD 分区。特定于方案的类型为：APM 使用 `!FreeBSD-UFS`，GPT 使用 `!516e7cb6-6ecf-11d6-8ff8-00022d09712b`。

**`freebsd-zfs`** 包含 ZFS 卷的 FreeBSD 分区。特定于方案的类型为：APM 使用 `!FreeBSD-ZFS`，GPT 使用 `!516e7cba-6ecf-11d6-8ff8-00022d09712b`。

其他可用于 `gpart` 工具的符号名称：

**`apple-apfs`** 用于 Apple 文件系统 APFS 的 Apple macOS 分区。

**`apple-core-storage`** 由称为 Core Storage 的逻辑卷管理器使用的 Apple Mac OS X 分区。特定于方案的类型为 GPT 使用 `!53746f72-6167-11aa-aa11-00306543ecac`。

**`apple-hfs`** 包含 HFS 或 HFS+ 文件系统的 Apple Mac OS X 分区。特定于方案的类型为：MBR 使用 `!175`，APM 使用 `!Apple_HFS`，GPT 使用 `!48465300-0000-11aa-aa11-00306543ecac`。

**`apple-label`** 专用于描述磁盘设备的分区元数据的 Apple Mac OS X 分区。特定于方案的类型为 GPT 使用 `!4c616265-6c00-11aa-aa11-00306543ecac`。

**`apple-raid`** 用于软件 RAID 配置的 Apple Mac OS X 分区。特定于方案的类型为 GPT 使用 `!52414944-0000-11aa-aa11-00306543ecac`。

**`apple-raid-offline`** 用于软件 RAID 配置的 Apple Mac OS X 分区。特定于方案的类型为 GPT 使用 `!52414944-5f4f-11aa-aa11-00306543ecac`。

**`apple-tv-recovery`** Apple TV 使用的 Apple Mac OS X 分区。特定于方案的类型为 GPT 使用 `!5265636f-7665-11aa-aa11-00306543ecac`。

**`apple-ufs`** 包含 UFS 文件系统的 Apple Mac OS X 分区。特定于方案的类型为：MBR 使用 `!168`，APM 使用 `!Apple_UNIX_SVR2`，GPT 使用 `!55465300-0000-11aa-aa11-00306543ecac`。

**`apple-zfs`** 包含 ZFS 卷的 Apple Mac OS X 分区。特定于方案的类型为 GPT 使用 `!6a898cc3-1dd2-11b2-99a6-080020736631`。相同的 GUID 也用于 **illumos/Solaris /usr 分区。** 参见下文“注意事项”一节。

**`dragonfly-label32`** 用 BSD disklabel 细分为多个文件系统的 Dx 分区。特定于方案的类型为 GPT 使用 `!9d087404-1ca5-11dc-8817-01301bb8a9f5`。

**`dragonfly-label64`** 用 disklabel64 细分为多个文件系统的 Dx 分区。特定于方案的类型为 GPT 使用 `!3d48ce54-1d16-11dc-8696-01301bb8a9f5`。

**`dragonfly-legacy`** Dx 中使用的传统分区类型。特定于方案的类型为 GPT 使用 `!bd215ab2-1d16-11dc-8696-01301bb8a9f5`。

**`dragonfly-ccd`** 用于 Concatenated Disk 驱动程序的 Dx 分区。特定于方案的类型为 GPT 使用 `!dbd5211b-1ca5-11dc-8817-01301bb8a9f5`。

**`dragonfly-hammer`** 包含 Hammer 文件系统的 Dx 分区。特定于方案的类型为 GPT 使用 `!61dc63ac-6e38-11dc-8513-01301bb8a9f5`。

**`dragonfly-hammer2`** 包含 Hammer2 文件系统的 Dx 分区。特定于方案的类型为 GPT 使用 `!5cbb9ad1-862d-11dc-a94d-01301bb8a9f5`。

**`dragonfly-swap`** 专用于交换空间的 Dx 分区。特定于方案的类型为 GPT 使用 `!9d58fdbd-1ca5-11dc-8817-01301bb8a9f5`。

**`dragonfly-ufs`** 包含 UFS1 文件系统的 Dx 分区。特定于方案的类型为 GPT 使用 `!9d94ce7c-1ca5-11dc-8817-01301bb8a9f5`。

**`dragonfly-vinum`** 用于逻辑卷管理器的 Dx 分区。特定于方案的类型为 GPT 使用 `!9dd4478f-1ca5-11dc-8817-01301bb8a9f5`。

**`ebr`** 用 EBR 细分为多个文件系统的分区。特定于方案的类型为 MBR 使用 `!5`。

**`fat16`** 包含 FAT16 文件系统的分区。特定于方案的类型为 MBR 使用 `!6`。

**`fat32`** 包含 FAT32 文件系统的分区。特定于方案的类型为 MBR 使用 `!11`。

**`fat32lba`** 包含 FAT32 (LBA) 文件系统的分区。特定于方案的类型为 MBR 使用 `!12`。

**`hifive-fsbl`** 包含 HiFive 第一阶段引导加载程序的原始分区。特定于方案的类型为 GPT 使用 `!5b193300-fc78-40cd-8002-e86c45580b47`。

**`hifive-bbl`** 包含 HiFive 第二阶段引导加载程序的原始分区。特定于方案的类型为 GPT 使用 `!2e54b353-1271-4842-806f-e436d6af6985`。

**`linux-data`** 包含某种带数据文件系统的 Linux 分区。特定于方案的类型为：MBR 使用 `!131`，GPT 使用 `!0fc63daf-8483-4772-8e79-3d69d8477de4`。

**`linux-lvm`** 专用于逻辑卷管理器的 Linux 分区。特定于方案的类型为：MBR 使用 `!142`，GPT 使用 `!e6d6d379-f507-44c2-a23c-238f2a3df928`。

**`linux-raid`** 用于软件 RAID 配置的 Linux 分区。特定于方案的类型为：MBR 使用 `!253`，GPT 使用 `!a19d880f-05fc-4d3b-a006-743f0f84911e`。

**`linux-swap`** 专用于交换空间的 Linux 分区。特定于方案的类型为：MBR 使用 `!130`，GPT 使用 `!0657fd6d-a4ab-43c4-84e5-0933c84b4f4f`。

**`mbr`** 由 Master Boot Record（MBR）进行再分区的分区。此类型在 GPT 中称为 `!024dee41-33e7-11d3-9d69-0008c781f39f`。

**`ms-basic-data`** Microsoft 操作系统的基本数据分区（BDP）。在 GPT 中，此类型等同于 MBR 中的 `fat16`、`fat32` 和 `ntfs` 分区类型。此类型用于 GPT exFAT 分区。特定于方案的类型为 GPT 使用 `!ebd0a0a2-b9e5-4433-87c0-68b6b72699c7`。

**`ms-ldm-data`** 包含 Logical Disk Manager（LDM）卷的分区。特定于方案的类型为：MBR 使用 `!66`，GPT 使用 `!af9b60a0-1431-4f62-bc68-3311714a69ad`。

**`ms-ldm-metadata`** 包含 Logical Disk Manager（LDM）数据库的分区。特定于方案的类型为 GPT 使用 `!5808c8aa-7e8f-42e0-85d2-e1e90434cfb3`。

**`netbsd-ccd`** 用于 Concatenated Disk 驱动程序的 NetBSD 分区。特定于方案的类型为 GPT 使用 `!2db519c4-b10f-11dc-b99b-0019d1879648`。

**`netbsd-cgd`** 加密的 NetBSD 分区。特定于方案的类型为 GPT 使用 `!2db519ec-b10f-11dc-b99b-0019d1879648`。

**`netbsd-ffs`** 包含 UFS 文件系统的 NetBSD 分区。特定于方案的类型为 GPT 使用 `!49f48d5a-b10e-11dc-b99b-0019d1879648`。

**`netbsd-lfs`** 包含 LFS 文件系统的 NetBSD 分区。特定于方案的类型为 GPT 使用 `!49f48d82-b10e-11dc-b99b-0019d1879648`。

**`netbsd-raid`** 用于软件 RAID 配置的 NetBSD 分区。特定于方案的类型为 GPT 使用 `!49f48daa-b10e-11dc-b99b-0019d1879648`。

**`netbsd-swap`** 专用于交换空间的 NetBSD 分区。特定于方案的类型为 GPT 使用 `!49f48d32-b10e-11dc-b99b-0019d1879648`。

**`ntfs`** 包含 NTFS 或 exFAT 文件系统的分区。特定于方案的类型为 MBR 使用 `!7`。

**`prep-boot`** 在某些 PowerPC 系统（尤其是 IBM 制造的系统）上专用于存储引导加载程序的系统分区。特定于方案的类型为：MBR 使用 `!65`，GPT 使用 `!9e1a2d38-c612-4316-aa26-8b49521e5a8b`。

**`solaris-boot`** 专用于引导加载程序的 illumos/Solaris 分区。特定于方案的类型为 GPT 使用 `!6a82cb45-1dd2-11b2-99a6-080020736631`。

**`solaris-root`** 专用于根文件系统的 illumos/Solaris 分区。特定于方案的类型为 GPT 使用 `!6a85cf4d-1dd2-11b2-99a6-080020736631`。

**`solaris-swap`** 专用于交换空间的 illumos/Solaris 分区。特定于方案的类型为 GPT 使用 `!6a87c46f-1dd2-11b2-99a6-080020736631`。

**`solaris-backup`** 专用于备份的 illumos/Solaris 分区。特定于方案的类型为 GPT 使用 `!6a8b642b-1dd2-11b2-99a6-080020736631`。

**`solaris-var`** 专用于 /var 文件系统的 illumos/Solaris 分区。特定于方案的类型为 GPT 使用 `!6a8ef2e9-1dd2-11b2-99a6-080020736631`。

**`solaris-home`** 专用于 /home 文件系统的 illumos/Solaris 分区。特定于方案的类型为 GPT 使用 `!6a90ba39-1dd2-11b2-99a6-080020736631`。

**`solaris-altsec`** 专用于备用扇区的 illumos/Solaris 分区。特定于方案的类型为 GPT 使用 `!6a9283a5-1dd2-11b2-99a6-080020736631`。

**`solaris-reserved`** 专用于保留空间的 illumos/Solaris 分区。特定于方案的类型为 GPT 使用 `!6a945a3b-1dd2-11b2-99a6-080020736631`。

**`u-boot-env`** 专用于 U-Boot 存储其环境的原始分区。特定于方案的类型为 GPT 使用 `!3de21764-95bd-54bd-a5c3-4abe786f38a8`。

**`vmware-vmfs`** 包含 VMware File System（VMFS）的分区。特定于方案的类型为：MBR 使用 `!251`，GPT 使用 `!aa31e02a-400f-11db-9590-000c2911d1b8`。

**`vmware-vmkdiag`** 包含 VMware 诊断文件系统的分区。特定于方案的类型为：MBR 使用 `!252`，GPT 使用 `!9d275380-40ad-11db-bf97-000c2911d1b8`。

**`vmware-reserved`** VMware 保留分区。特定于方案的类型为 GPT 使用 `!9198effc-31c0-11db-8f-78-000c2911d1b8`。

**`vmware-vsanhdr`** 由 VMware VSAN 占用的分区。特定于方案的类型为 GPT 使用 `!381cfccc-7288-11e0-92ee-000c2911d0b2`。

**`xbootldr`** 扩展引导加载程序分区（XBOOTLDR），是 EFI 系统分区的辅助分区，用于存储额外的固件或引导加载程序菜单项。特定于方案的类型为 GPT 使用 `!bc13c2ff-59e6-4262-a352-b275fd6f7172`。

## 属性

EBR 的特定于方案的属性：

**`active`**

GPT 的特定于方案的属性：

**`bootme`** 设置后，`gptboot` 第一阶段引导加载程序会尝试从该分区引导系统。多个分区可以标记 `bootme` 属性。详见 [gptboot(8)](gptboot.8.md)。

**`bootonce`** 设置此属性会自动设置 `bootme` 属性。设置后，`gptboot` 第一阶段引导加载程序会尝试仅从该分区引导一次。多个分区可以标记 `bootonce` 和 `bootme` 属性对。详见 [gptboot(8)](gptboot.8.md)。

**`bootfailed`** 此属性不应由手动管理。它由 `gptboot` 第一阶段引导加载程序和 `/etc/rc.d/gptboot` 启动脚本管理。详见 [gptboot(8)](gptboot.8.md)。

**`lenovofix`** 设置此属性会用一个新的保护性 MBR 覆盖原有的保护性 MBR，其中 0xee 分区是第二条记录而非第一条记录。这解决了某些 Lenovo 型号（包括 X220、T420 和 T520）的 BIOS 兼容性问题，使其能够在不使用 EFI 的情况下从 GPT 分区的磁盘引导。

MBR 的特定于方案的属性：

**`active`**

## 引导

FreeBSD 支持多种分区方案，每种方案使用不同的引导代码。引导代码位于每种分区方案的特定磁盘区域，并且不同方案的大小可能不同。

引导代码可分为两种类型。第一种类型嵌入在分区方案的元数据中，第二种类型位于特定分区上。嵌入引导代码只能通过 `gpart bootcode` 命令配合 `-b` `bootcode` 选项来完成。GEOM PART 类知道如何安全地将引导代码嵌入到特定分区方案的元数据中而不会造成任何损坏。

Master Boot Record（MBR）使用 512 字节的引导代码映像，嵌入到分区表的元数据区域。此引导代码有两种变体：`/boot/mbr` 和 `/boot/boot0`。`/boot/mbr` 在分区表中查找具有 `active` 属性（参见“属性”一节）的分区，然后运行下一引导阶段。`/boot/boot0` 映像包含一个引导管理器，具有一些额外的交互功能，用于从用户选择的分区进行多重引导。

BSD disklabel 通常创建在类型为 `freebsd`（参见“分区类型”一节）的 MBR 分区（slice）内。它使用 8 KiB 大小的引导代码映像 `/boot/boot`，嵌入到分区表的元数据区域。

两种类型的引导代码都用于从 GUID Partition Table 引导。首先，从 `/boot/pmbr` 映像将保护性 MBR 嵌入到第一个磁盘扇区。它会在 GPT 中查找 `freebsd-boot` 分区（参见“分区类型”一节）并从中运行下一引导阶段。`freebsd-boot` 分区应小于 545 KiB。它可以位于磁盘上其他 FreeBSD 分区之前或之后。写入此分区的引导代码有两种变体：`/boot/gptboot` 和 `/boot/gptzfsboot`。

`/boot/gptboot` 用于从 UFS 分区引导。`gptboot` 在 GPT 中的 `freebsd-ufs` 分区中搜索，并根据 `bootonce` 和 `bootme` 属性选择一个进行引导。如果未找到任何属性，`/boot/gptboot` 会从第一个 `freebsd-ufs` 分区引导。`/boot/loader`（第三引导阶段）从第一个符合这些条件的分区加载。详见 [gptboot(8)](gptboot.8.md)。

`/boot/gptzfsboot` 用于从 ZFS 引导。它在 GPT 中查找 `freebsd-zfs` 分区，尝试检测 ZFS 存储池。检测到所有存储池后，从第一个被发现设置为可引导的存储池启动 `/boot/loader`。

APM 方案也不支持嵌入引导代码。相反，应使用 `gpart bootcode` 命令将 800 KiB 的引导代码映像 `/boot/boot1.hfs` 写入到 `apple-boot` 类型的分区中，该分区大小也应为 800 KiB。

## 操作标志

除 `commit` 和 `undo` 操作外，其他操作都接受可选的 `-f` `flags` 选项。此选项用于指定特定于操作的标志。默认情况下，`gpart` 工具定义了 `C` 标志，使操作立即提交。用户可以指定“`-f` `x`”使操作结果成为挂起更改，之后可与其他挂起更改一起，通过 `commit` 操作作为单个复合更改提交，或通过 `undo` 操作还原。

## 恢复

GEOM PART 类仅支持 GPT 分区表的恢复。GPT 的主元数据存储在设备的开头。为冗余起见，元数据的辅助（备份）副本存储在设备的末尾。由于有两份副本，某些元数据损坏对 GPT 的工作并不致命。当内核检测到损坏的元数据时，会将该表标记为损坏并报告问题。`destroy` 和 `recover` 是允许在损坏表上执行仅有的操作。

如果一个 GPT 头看起来已损坏，但另一份副本仍然完好，内核将记录以下信息：

```sh
GEOM: provider: the primary GPT table is corrupt or invalid.
GEOM: provider: using the secondary instead -- recovery strongly advised.
```

或

```sh
GEOM: provider: the secondary GPT table is corrupt or invalid.
GEOM: provider: using the primary only -- recovery suggested.
```

此外，`gpart` 的 `show`、`status` 和 `list` 等命令也会报告损坏的表。

如果设备大小已更改（例如卷扩展），辅助 GPT 头将不再位于最后一个扇区。这不是元数据损坏，但很危险，因为主 GPT 的任何损坏都会导致分区表丢失。内核会通过以下消息报告此问题：

```sh
GEOM: provider: the secondary GPT header is not in the last LBA.
```

这种情况可以通过 `recover` 命令恢复。此命令使用已知的有效元数据重建损坏的元数据，并将辅助 GPT 重新定位到设备末尾。

*注意：* GEOM PART 类可以检测到通过不同 GEOM provider 可见的同一分区表，其中一些会被标记为损坏。在选择用于恢复的 provider 时要小心。如果选择错误，可能会破坏其他 GEOM 类（例如 GEOM MIRROR 或 GEOM LABEL）的元数据。

## SYSCTL 变量

以下 [sysctl(8)](sysctl.8.md) 变量可用于控制 `PART` GEOM 类的行为。每个变量的默认值显示在其旁边。

**`kern.geom.part.allow_nesting`** : 0 默认情况下，某些方案（目前是 BSD 和 BSD64）不允许进一步的嵌套分区。此变量覆盖此限制并允许任意嵌套（在偏移量 0 处创建的分区除外）。某些方案有自己独立的检查，详见下文。

**`kern.geom.part.auto_resize`** : 1 此变量控制 `PART` GEOM 类的自动调整大小行为。当此变量启用并检测到 provider 的新大小时，会调整方案元数据的大小，但所有更改不会保存到磁盘，直到运行 `gpart commit` 确认更改。此行为也会通过诊断消息报告：**GEOM_PART: (provider) was automatically resized.** **Use `gpart commit (provider)` to save changes or `gpart undo (provider)`** **to revert them.**

**`kern.geom.part.check_integrity`** : 1 此变量控制元数据完整性检查的行为。启用完整性检查时，`PART` GEOM 类会验证从磁盘元数据获取的所有通用分区参数。如果检测到某些不一致，分区表将被拒绝并附带诊断消息：**GEOM_PART: Integrity check failed (provider, scheme).**

**`kern.geom.part.gpt.allow_nesting`** : 0 默认情况下，GPT 方案仅允许在最外层嵌套级别。此变量允许移除此限制。

**`kern.geom.part.ldm.debug`** : 0 Logical Disk Manager（LDM）模块的调试级别。可设置为 0 到 2（含）之间的数字。设置为 0 时打印最少的调试信息，设置为 2 时打印最多的调试信息。

**`kern.geom.part.ldm.show_mirrors`** : 0 此变量控制 Logical Disk Manager（LDM）模块如何处理镜像卷。默认情况下，镜像卷显示为类型为 `ms-ldm-data` 的分区（参见“分区类型”一节）。如果此变量设置为 1，镜像卷的每个组件将作为独立分区呈现。*注意：* 这可能破坏镜像卷并导致数据损坏。

**`kern.geom.part.mbr.enforce_chs`** : 0 指定 Master Boot Record（MBR）模块如何进行对齐。如果此变量设置为非零值，模块将自动重新计算用户指定的偏移量和大小以与 CHS 几何对齐。否则，这些值将保持不变。

**`kern.geom.part.separator`** : 指定一个可选的分隔符，该分隔符将插入到 GEOM 名称和分区名称之间。此变量是 [loader(8)](loader.8.md) 可调参数。请注意，设置此变量可能会破坏假定特定命名方案的软件。

## 退出状态

成功时退出状态为 0，命令失败时为 1。

## 实例

以下示例假设磁盘的逻辑块大小为 512 字节，无论其物理块大小如何。

### GPT

在此示例中，我们将使用 GPT 方案对 `ada0` 进行格式化，并创建引导、交换和根分区。首先，我们需要创建分区表：

```sh
/sbin/gpart create -s GPT ada0
```

接下来，我们安装带有第一阶段引导代码的保护性 MBR。保护性 MBR 列出一个跨整个磁盘的、可引导的单个分区，从而允许不支持 GPT 的 BIOS 从该磁盘引导，并防止不理解 GPT 方案的工具认为该磁盘未格式化。

```sh
/sbin/gpart bootcode -b /boot/pmbr ada0
```

然后，我们创建一个专用的 `freebsd-boot` 分区来存放第二阶段引导加载程序，它将从 UFS 或 ZFS 文件系统加载 FreeBSD 内核和模块。此分区必须大于引导代码（UFS 使用 `/boot/gptboot`，ZFS 使用 `/boot/gptzfsboot`），但要小于 545 KiB，因为第一阶段加载程序在引导时会将整个分区加载到内存中，无论它实际包含多少数据。我们在偏移量 40 处创建一个 472 块（236 KiB）的引导分区，这是分区表大小（34 块或 17 KiB）向上取整到最近的 4 KiB 边界。

```sh
/sbin/gpart add -b 40 -s 472 -t freebsd-boot ada0
/sbin/gpart bootcode -p /boot/gptboot -i 1 ada0
```

现在，我们在第一个可用偏移量（即 40 + 472 = 512 块，即 256 KiB）处创建一个 4 GiB 的交换分区。

```sh
/sbin/gpart add -s 4G -t freebsd-swap ada0
```

将交换分区及所有后续分区对齐到 256 KiB 边界，可确保在从具有 512 字节块的普通旧磁盘、具有 4096 字节物理块的现代“高级格式”磁盘，到条带大小高达 256 KiB 的 RAID 卷等广泛介质上获得最佳性能。

最后，我们为根文件系统创建并格式化一个 8 GiB 的 `freebsd-ufs` 分区，将设备的其余部分留给额外的文件系统：

```sh
/sbin/gpart add -s 8G -t freebsd-ufs ada0
/sbin/newfs -Uj /dev/ada0p3
```

### MBR

在此示例中，我们将使用 MBR 方案对 `ada0` 进行格式化，并创建一个使用传统 BSD disklabel 细分的单个分区。

首先，我们创建分区表以及一个大小为 64 GiB、对齐为 4 KiB 的单个分区，然后我们将该分区标记为活动（可引导）并安装第一阶段引导加载程序：

```sh
/sbin/gpart create -s MBR ada0
/sbin/gpart add -t freebsd -s 64G -a 4k ada0
/sbin/gpart set -a active -i 1 ada0
/sbin/gpart bootcode -b /boot/boot0 ada0
```

接下来，我们在该分区（disklabel 术语中的“slice”）中创建一个 disklabel，最多可容纳 20 个分区：

```sh
/sbin/gpart create -s BSD -n 20 ada0s1
```

然后，我们创建一个 8 GiB 的根分区和一个 4 GiB 的交换分区：

```sh
/sbin/gpart add -t freebsd-ufs -s 8G ada0s1
/sbin/gpart add -t freebsd-swap -s 4G ada0s1
```

最后，我们为 BSD label 安装相应的引导加载程序：

```sh
/sbin/gpart bootcode -b /boot/boot ada0s1
```

### 删除分区和销毁分区方案

如果尝试销毁分区表时显示 *Device busy* 错误，请记住必须先用 `delete` 操作删除所有分区。在此示例中，`da0` 有三个分区：

```sh
/sbin/gpart delete -i 3 da0
/sbin/gpart delete -i 2 da0
/sbin/gpart delete -i 1 da0
/sbin/gpart destroy da0
```

除了删除每个分区然后销毁分区方案外，还可以在 `destroy` 时使用 `-F` 选项在销毁分区方案之前删除所有分区。这等同于上一个示例：

```sh
/sbin/gpart destroy -F da0
```

### 备份和恢复

从 `da0` 创建分区表的备份：

```sh
/sbin/gpart backup da0 > da0.backup
```

从备份恢复分区表到 `da0`：

```sh
/sbin/gpart restore -l da0 < /mnt/da0.backup
```

将分区表从 `ada0` 克隆到 `ada1` 和 `ada2`：

```sh
/sbin/gpart backup ada0 | /sbin/gpart restore -F ada1 ada2
```

## 诊断

- gpart: arg0 '%s': Invalid argument 提供的 `geom` 参数不是 GEOM provider。并非 [devfs(4)](../man4/devfs.4.md) 中的每个设备都是 GEOM provider。例如，zfs(4) zvol 只有在其 **volmode** 设置正确时才会显示为 GEOM provider（详情参见 zfsprops(7)）。

## 参见

[geom(4)](../man4/geom.4.md), xo_options(7), [boot0cfg(8)](boot0cfg.8.md), geom(8), glabel(8), [gptboot(8)](gptboot.8.md)

## 历史

`PART` 工具出现于 FreeBSD 7.0。

## 作者

Marcel Moolenaar <marcel@FreeBSD.org>

## 注意事项

分区类型 *apple-zfs*（6a898cc3-1dd2-11b2-99a6-080020736631）也用于 illumos/Solaris 平台上的 ZFS 卷。
