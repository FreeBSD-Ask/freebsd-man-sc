  GPART(8)  

GPART(8)

FreeBSD System Manager's Manual

GPART(8)

[名称](#__u540D___u79F0_)
=======================

`gpart` —

磁盘分区 GEOM 类的控制实用程序

[概要](#__u6982___u8981_)
=======================

`gpart` `add` `-t` type \[`-a` alignment\] \[`-b` start\] \[`-s` size\] \[`-i` index\] \[`-l` label\] \[`-f` flags\] geom `gpart` `backup` geom `gpart` `bootcode` \[`-N`\] \[`-b` bootcode\] \[`-p` partcode `-i` index\] \[`-f` flags\] geom `gpart` `commit` geom `gpart` `create` `-s` scheme \[`-n` entries\] \[`-f` flags\] provider `gpart` `delete` `-i` index \[`-f` flags\] geom `gpart` `destroy` \[`-F`\] \[`-f` flags\] geom `gpart` `modify` `-i` index \[`-l` label\] \[`-t` type\] \[`-f` flags\] geom `gpart` `recover` \[`-f` flags\] geom `gpart` `resize` `-i` index \[`-a` alignment\] \[`-s` size\] \[`-f` flags\] geom `gpart` `restore` \[`-lF`\] \[`-f` flags\] provider \[...\] `gpart` `set` `-a` attrib `-i` index \[`-f` flags\] geom `gpart` `show` \[`-l` | `-r`\] \[`-p`\] \[geom ...\] `gpart` `undo` geom `gpart` `unset` `-a` attrib `-i` index \[`-f` flags\] geom `gpart` `list` `gpart` `status` `gpart` `load` `gpart` `unload`

[描述](#__u63CF___u8FF0_)
=======================

`gpart` 实用程序用于对 GEOM 提供程序进行分区，通常是磁盘。 第一个参数是要采取的行动：

[`add`](#add)

在 geom 给出的分区方案中添加一个新分区。 必须使用 `-t` type 指定分区类型。 如果未指定相应选项，将自动计算分区的位置、大小和其他属性。

`add` 命令接受以下选项：

[`-a`](#a) alignment

如果指定，则 `gpart` 实用程序会尝试将 start 偏移量和分区 size 对齐为 alignment 值的倍数。

[`-b`](#b) start

分区开始的逻辑块地址。 允许使用 SI 单位后缀。

[`-f`](#f) flags

额外的操作标志。 有关其使用的讨论，请参见下面标题为 [操作标志](#__u64CD___u4F5C___u6807___u5FD7_) 的部分。

[`-i`](#i) index

分区表中要放置新分区的索引。 索引确定用于表示分区的设备专用文件的名称。

[`-l`](#l) label

贴在分区上的标签。 此选项仅在用于支持分区标签的分区方案时有效。

[`-s`](#s) size

创建一个大小为 size 的分区。 允许使用 SI 单位后缀。

[`-t`](#t) type

创建类型 type 的分区。 分区类型将在下面标题为 [分区类型](#__u5206___u533A___u7C7B___u578B_) 的部分中讨论。

[`backup`](#backup)

以 `restore` 操作使用的特殊格式将分区表转储到标准输出。

[`bootcode`](#bootcode)

将引导代码嵌入到 geom 上的分区方案的元数据中（使用 `-b` bootcode) 或将引导代码写入分区（使用 `-p` partcode 和 `-i` index )。

`bootcode` 命令接受以下选项：

[`-N`](#N)

不要为 MBR 保留卷序列号。 MBR 引导代码默认包含卷序列号， `gpart` 会在安装新的引导代码时尝试保留它。 此选项允许跳过保存以帮助某些不支持卷序列号的 boot0(8)-
版本。

[`-b`](#b_2) bootcode

将文件 bootcode 中的引导代码嵌入到 geom 的分区方案的元数据中。 并非所有分区方案都嵌入了引导代码，因此 `-b` bootcode 选项本质上是特定于方案的（请参阅下面标题为 [BOOTSTRAPPING](#BOOTSTRAPPING) 的部分）。 bootcode 文件必须符合分区方案对文件内容和大小的要求。

[`-f`](#f_2) flags

额外的操作标志。 有关其使用的讨论，请参见下面标题为 [操作标志](#__u64CD___u4F5C___u6807___u5FD7_) 的部分。

[`-i`](#i_2) index

为 `-p` partcode 指定目标分区。

[`-p`](#p) partcode

将文件 partcode 中的引导代码写入 `-i` index 指定的 geom 分区。 文件的大小必须小于分区的大小。

[`commit`](#commit)

提交 geom geom 的任何未决更改。 默认情况下，所有操作都已提交，不会导致挂起的更改。 可以使用 `-f` flags 选项修改操作，以便它们不会被提交，而是处于挂起状态。 挂起的更改由 geom 和 `gpart` 实用程序反映，但它们实际上并未写入磁盘。 `commit` 操作会将所有挂起的更改写入磁盘。

[`create`](#create)

在 provider 给定的提供者上创建一个新的分区方案。 必须使用 `-s` scheme 选项指定要使用的方案。

`create` 命令接受以下选项：

[`-f`](#f_3) flags

额外的操作标志。 有关其使用的讨论，请参见下面标题为 [操作标志](#__u64CD___u4F5C___u6807___u5FD7_) 的部分。

[`-n`](#n) entries

分区表中的条目数。 每个分区方案都有最小和最大条目数。 此选项允许使用限制内的条目数创建表。 一些方案的最大值等于最小值，而一些方案的最大值大到可以认为是无限的。 默认情况下，分区表是使用最少条目数创建的。

[`-s`](#s_2) scheme

指定要使用的分区方案。 内核必须支持特定的方案，然后才能使用该方案对磁盘进行分区。

[`delete`](#delete)

从 geom geom 中删除一个分区，并通过 `-i` index 选项进一步标识。 该分区不能被内核主动使用。

`delete` 命令接受以下选项：

[`-f`](#f_4) flags

额外的操作标志。 有关其使用的讨论，请参见下面标题为 [操作标志](#__u64CD___u4F5C___u6807___u5FD7_) 的部分。

[`-i`](#i_3) index

指定要删除的分区的索引。

[`destroy`](#destroy)

销毁由 geom geom 实现的分区方案。

`destroy` 命令接受以下选项：

[`-F`](#F)

强制销毁分区表，即使它不为空。

[`-f`](#f_5) flags

额外的操作标志。 有关其使用的讨论，请参见下面标题为 [操作标志](#__u64CD___u4F5C___u6807___u5FD7_) 的部分。

[`modify`](#modify)

从 geom geom 修改一个分区，并通过 `-i` index 选项进一步标识。 只能修改分区的类型和/或标签。 并非所有分区方案都支持标签，在这种情况下尝试更改分区标签是无效的。

`modify` 命令接受以下选项：

[`-f`](#f_6) flags

额外的操作标志。 有关其使用的讨论，请参见下面标题为 [操作标志](#__u64CD___u4F5C___u6807___u5FD7_) 的部分。

[`-i`](#i_4) index

指定要修改的分区的索引。

[`-l`](#l_2) label

将分区标签更改为 label 。

[`-t`](#t_2) type

将分区类型更改为 type 。

[`recover`](#recover)

在 geom geom 上恢复损坏的分区方案元数据。 有关其他信息，请参阅下面标题为 [恢复](#__u6062___u590D_) 的部分。

`recover` 命令接受以下选项：

[`-f`](#f_7) flags

额外的操作标志。 有关其使用的讨论，请参见下面标题为 [操作标志](#__u64CD___u4F5C___u6807___u5FD7_) 的部分。

[`resize`](#resize)

从 geom geom 调整分区大小，并通过 `-i` index 选项进一步标识。 如果未指定新大小，则会自动计算为 geom 可用的最大值。

`resize` 命令接受以下选项：

[`-a`](#a_2) alignment

如果指定，则 `gpart` 实用程序尝试将分区 size 对齐为 alignment 值的倍数。

[`-f`](#f_8) flags

额外的操作标志。 有关其使用的讨论，请参见下面标题为 [操作标志](#__u64CD___u4F5C___u6807___u5FD7_) 的部分。

[`-i`](#i_5) index

指定要调整大小的分区的索引。

[`-s`](#s_3) size

指定分区的新大小，以逻辑块为单位。 允许使用 SI 单位后缀。

[`restore`](#restore)

从先前由 `backup` 操作创建的备份恢复分区表并从标准输入读取。 仅恢复分区表。 此操作不会影响分区的内容。 恢复分区表并根据需要编写引导代码后，必须从备份中恢复用户数据。

`restore` 命令接受以下选项：

[`-F`](#F_2)

在进行还原之前销毁给定 provider 程序上的分区表。

[`-f`](#f_9) flags

额外的操作标志。 有关其使用的讨论，请参见下面标题为 [操作标志](#__u64CD___u4F5C___u6807___u5FD7_) 的部分。

[`-l`](#l_3)

为支持它们的分区方案恢复分区标签。

[`set`](#set)

在分区条目上设置命名属性。 有关可用属性的列表，请参阅下面标题为 [ATTRIBUTES](#ATTRIBUTES) 的部分。

`set` 命令接受以下选项：

[`-a`](#a_3) attrib

指定要设置的属性。

[`-f`](#f_10) flags

额外的操作标志。 有关其使用的讨论，请参见下面标题为 [操作标志](#__u64CD___u4F5C___u6807___u5FD7_) 的部分。

[`-i`](#i_6) index

指定将在其上设置属性的分区的索引。

[`show`](#show)

显示指定几何图形的当前分区信息，如果没有指定几何图形，则显示所有几何图形。 默认输出包括每个分区的逻辑起始块、分区大小（以块为单位）、分区索引号、分区类型和人类可读的分区大小。 块大小和位置基于设备的扇区大小，如 `gpart list` 所示。

`show` 命令接受以下选项：

[`-l`](#l_4)

对于支持分区标签的分区方案，打印它们而不是分区类型。

[`-p`](#p_2)

显示提供程序名称而不是分区索引。

[`-r`](#r)

显示原始分区类型而不是符号名称。

[`undo`](#undo)

恢复 geom geom 的任何未决更改。 此操作与 `commit` 操作相反，可用于撤消任何尚未提交的更改。

[`unset`](#unset)

清除分区条目上的命名属性。 有关可用属性的列表，请参阅下面标题为 [ATTRIBUTES](#ATTRIBUTES) 的部分。

`unset` 命令接受以下选项：

[`-a`](#a_4) attrib

指定要清除的属性。

[`-f`](#f_11) flags

额外的操作标志。 有关其使用的讨论，请参见下面标题为 [操作标志](#__u64CD___u4F5C___u6807___u5FD7_) 的部分。

[`-i`](#i_7) index

指定要清除其属性的分区的索引。

[`list`](#list)

参见 geom(8) 。

[`status`](#status)

参见 geom(8) 。

[`load`](#load)

参见 geom(8) 。

[`unload`](#unload)

参见 geom(8) 。

[分区方案](#__u5206___u533A___u65B9___u6848_)
=========================================

`gpart` 实用程序支持几种分区方案：

[`APM`](#APM)

分区图，供 PowerPC(R) Macintosh(R) 计算机使用。 需要 `GEOM_PART_APM` 内核选项。

[`BSD`](#BSD)

传统的 BSD 磁盘标签，通常用于细分 MBR 分区。 (（此方案也可以用作唯一的分区方法，无需 MBR。 来自其他操作系统的分区编辑工具通常不了解裸磁盘标签分区布局，因此有时称为 “dangerously dedicated” 。）) 需要 `GEOM_PART_BSD` 内核选项。

[`BSD64`](#BSD64)

在 DragonFlyBSD 中用于细分 MBR 或 GPT 分区的 BSD 磁盘标签的 64 位实现。 需要 `GEOM_PART_BSD64` 内核选项。

[`LDM`](#LDM)

逻辑磁盘管理器是 Microsoft Windows NT 卷管理器的实现。 需要 `GEOM_PART_LDM` 内核选项。

[`GPT`](#GPT)

GUID 分区表用于基于 Intel 的 Macintosh 计算机，并逐渐取代大多数 PC 和其他系统上的 MBR。 需要 `GEOM_PART_GPT` 内核选项。

[`MBR`](#MBR)

主引导记录用于 PC 和可移动媒体。 需要 `GEOM_PART_MBR` 内核选项。 `GEOM_PART_EBR` 选项增加了对用于定义逻辑分区的扩展引导记录 (EBR) 的支持。 `GEOM_PART_EBR_COMPAT` 选项启用 EBR 方案中分区名称的向后兼容性。 它还可以防止对此类分区执行任何类型的操作。

[`VTOC8`](#VTOC8)

Sun 的 SMI 卷目录，供 SPARC64 和 UltraSPARC 计算机使用。 需要 `GEOM_PART_VTOC8` 内核选项。

[分区类型](#__u5206___u533A___u7C7B___u578B_)
=========================================

分区类型在磁盘上由特定的字符串或魔术值标识。 `gpart` 实用程序对常见的分区类型使用符号名称，因此用户不需要知道这些值或相关分区方案的其他详细信息。 `gpart` 实用程序还允许用户为没有符号名称的分区类型指定特定于方案的分区类型。 FreeBSD 目前理解和使用的符号名称是：

[`apple-boot`](#apple-boot)

在某些 Apple 系统上专门用于存储引导加载程序的系统分区。 特定于方案的类型是 MBR 的 “`!171`” ，APM 的 “`!Apple_Bootstrap`” 和 GPT 的 “`!426f6f74-0000-11aa-aa11-00306543ecac`” 。

[`bios-boot`](#bios-boot)

专用于引导加载程序第二阶段的系统分区。 通常它被 GRUB 2 加载器用于 GPT 分区方案。 特定于方案的类型是 “`!21686148-6449-6E6F-744E-656564454649`”.

[`efi`](#efi)

使用可扩展固件接口 (EFI) 的计算机的系统分区。 特定于方案的类型是 MBR 的 “`!239`” 和 GPT 的 “`!c12a7328-f81f-11d2-ba4b-00a0c93ec93b`” 。

[`freebsd`](#freebsd)

FreeBSD 分区细分为带有 BSD 磁盘标签的文件系统。 这是传统分区类型，不应用于 APM 或 GPT 方案。 特定于方案的类型是 MBR 的 “`!165`” ，APM 的 “`!FreeBSD`” 和 GPT 的 “`!516e7cb4-6ecf-11d6-8ff8-00022d09712b`” 。

[`freebsd-boot`](#freebsd-boot)

专用于引导代码的 FreeBSD 分区。 对于 GPT，特定于方案的类型是 “`!83bd6b9d-7f41-11dc-be0b-001560b84f0f`” 。

[`freebsd-swap`](#freebsd-swap)

专用于交换空间的 FreeBSD 分区。 特定于方案的类型是 APM 的 “`!FreeBSD-swap`” 、GPT 的 “`!516e7cb5-6ecf-11d6-8ff8-00022d09712b`” 和 VTOC8 的标记 0x0901。

[`freebsd-ufs`](#freebsd-ufs)

包含 UFS 或 UFS2 文件系统的 FreeBSD 分区。 特定于方案的类型是 APM 的 “`!FreeBSD-UFS`” 、GPT 的 “`!516e7cb6-6ecf-11d6-8ff8-00022d09712b`” 和 VTOC8 的标记 0x0902。

[`freebsd-vinum`](#freebsd-vinum)

一个包含 Vinum 卷的 FreeBSD 分区。 特定于方案的类型是 APM 的 “`!FreeBSD-Vinum`” 、GPT 的 “`!516e7cb8-6ecf-11d6-8ff8-00022d09712b`” 和 VTOC8 的标记 0x0903。

[`freebsd-zfs`](#freebsd-zfs)

一个包含 ZFS 卷的 FreeBSD 分区。 特定于方案的类型是 APM 的 “`!FreeBSD-ZFS`” 、GPT 的 “`!516e7cba-6ecf-11d6-8ff8-00022d09712b`” 和 VTOC8 的 0x0904。

可以与 `gpart` 实用程序一起使用的其他符号名称是：

[`apple-apfs`](#apple-apfs)

用于 Apple 文件系统 APFS 的 Apple macOS 分区。

[`apple-core-storage`](#apple-core-storage)

逻辑卷管理器（称为核心存储）使用的 Apple Mac OS X 分区。 对于 GPT，特定于方案的类型是 “`!53746f72-6167-11aa-aa11-00306543ecac`” 。

[`apple-hfs`](#apple-hfs)

包含 HFS 或 HFS+ 文件系统的 Apple Mac OS X 分区。 特定于方案的类型是 MBR 的 “`!175`” ，APM 的 “`!Apple_HFS`” 和 GPT 的 “`!48465300-0000-11aa-aa11-00306543ecac`” 。

[`apple-label`](#apple-label)

用于软件 RAID 配置的 Apple Mac OS X 分区。 对于 GPT，特定于方案的类型是 “`!4c616265-6c00-11aa-aa11-00306543ecac`” 。

[`apple-raid`](#apple-raid)

用于软件 RAID 配置的 Apple Mac OS X 分区。 对于 GPT，特定于方案的类型是 “`!52414944-0000-11aa-aa11-00306543ecac`” 。

[`apple-raid-offline`](#apple-raid-offline)

Apple TV 使用的 Apple Mac OS X 分区。 对于 GPT，特定于方案的类型是 “`!52414944-5f4f-11aa-aa11-00306543ecac`” 。

[`apple-tv-recovery`](#apple-tv-recovery)

包含 UFS 文件系统的 Apple Mac OS X 分区。 特定于方案的类型是 MBR 的 “`!5265636f-7665-11aa-aa11-00306543ecac`” 。

[`apple-ufs`](#apple-ufs)

包含 UFS 文件系统的 Apple Mac OS X 分区。 特定于方案的类型是 MBR 的 “`!168`” 、APM 的 “`!Apple_UNIX_SVR2`” 和 GPT 的 “`!55465300-0000-11aa-aa11-00306543ecac`” 。

[`apple-zfs`](#apple-zfs)

包含 ZFS 卷的 Apple Mac OS X 分区。 对于 GPT，特定于方案的类型是 “`!6a898cc3-1dd2-11b2-99a6-080020736631`” 。 **illumos/Solaris /usr partition** 分区也使用相同的 GUID。 请参阅下面的 [CAVEATS](#CAVEATS) 部分。

[`dragonfly-label32`](#dragonfly-label32)

DragonFlyBSD 分区被细分为带有 BSD 磁盘标签的文件系统。 对于 GPT，特定于方案的类型是 “`!9d087404-1ca5-11dc-8817-01301bb8a9f5`” 。

[`dragonfly-label64`](#dragonfly-label64)

一个 DragonFlyBSD 分区细分为具有 disklabel64 的文件系统。 对于 GPT，特定于方案的类型是 “`!3d48ce54-1d16-11dc-8696-01301bb8a9f5`” 。

[`dragonfly-legacy`](#dragonfly-legacy)

DragonFlyBSD 中使用的传统分区类型。 对于 GPT，特定于方案的类型是 “`!bd215ab2-1d16-11dc-8696-01301bb8a9f5`” 。

[`dragonfly-ccd`](#dragonfly-ccd)

与 Concatenated Disk 驱动程序一起使用的 DragonFlyBSD 分区。 对于 GPT，特定于方案的类型是 “`!dbd5211b-1ca5-11dc-8817-01301bb8a9f5`” 。

[`dragonfly-hammer`](#dragonfly-hammer)

一个包含 Hammer 文件系统的 DragonFlyBSD 分区。 对于 GPT，特定于方案的类型是 “`!61dc63ac-6e38-11dc-8513-01301bb8a9f5`” 。

[`dragonfly-hammer2`](#dragonfly-hammer2)

一个包含 Hammer2 文件系统的 DragonFlyBSD 分区。 对于 GPT，特定于方案的类型是 “`!5cbb9ad1-862d-11dc-a94d-01301bb8a9f5`” 。

[`dragonfly-swap`](#dragonfly-swap)

专用于交换空间的 DragonFlyBSD 分区。 对于 GPT，特定于方案的类型是 “`!9d58fdbd-1ca5-11dc-8817-01301bb8a9f5`” 。

[`dragonfly-ufs`](#dragonfly-ufs)

一个包含 UFS1 文件系统的 DragonFlyBSD 分区。 对于 GPT，特定于方案的类型是 “`!9d94ce7c-1ca5-11dc-8817-01301bb8a9f5`” 。

[`dragonfly-vinum`](#dragonfly-vinum)

与逻辑卷管理器一起使用的 DragonFlyBSD 分区。 对于 GPT，特定于方案的类型是 “`!9dd4478f-1ca5-11dc-8817-01301bb8a9f5`” 。

[`ebr`](#ebr)

使用 EBR 细分为文件系统的分区。 对于 MBR，特定于方案的类型是 “`!5`” 。

[`fat16`](#fat16)

包含 FAT16 文件系统的分区。 对于 MBR，特定于方案的类型是 “`!6`” 。

[`fat32`](#fat32)

包含 FAT32 文件系统的分区。 对于 MBR，特定于方案的类型是 “`!11`” 。

[`fat32lba`](#fat32lba)

包含 FAT32 (LBA) 文件系统的分区。 对于 MBR，特定于方案的类型是 “`!12`” 。

[`linux-data`](#linux-data)

一个 Linux 分区，其中包含一些带有数据的文件系统。 特定于方案的类型是 MBR 的 “`!131`” 和 GPT 的 “`!0fc63daf-8483-4772-8e79-3d69d8477de4`” 。

[`linux-lvm`](#linux-lvm)

专用于逻辑卷管理器的 Linux 分区。 特定于方案的类型是 MBR 的 “`!142`” 和 GPT 的 “`!e6d6d379-f507-44c2-a23c-238f2a3df928`” 。

[`linux-raid`](#linux-raid)

用于软件 RAID 配置的 Linux 分区。 特定于方案的类型是 MBR 的 “`!253`” 和 GPT 的 “`!a19d880f-05fc-4d3b-a006-743f0f84911e`” 。

[`linux-swap`](#linux-swap)

专用于交换空间的 Linux 分区。 特定于方案的类型是 MBR 的 “`!130`” 和 GPT 的 “`!0657fd6d-a4ab-43c4-84e5-0933c84b4f4f`” 。

[`mbr`](#mbr)

由主引导记录 (MBR) 进行子分区的分区。 这种类型被 GPT 称为 “`!024dee41-33e7-11d3-9d69-0008c781f39f`” 。

[`ms-basic-data`](#ms-basic-data)

Microsoft 操作系统的基本数据分区 (BDP)。 在 GPT 中，此类型相当于 MBR 中的分区类型 `fat16`, `fat32` 和 `ntfs` 。 此类型用于 GPT exFAT 分区。 对于 GPT，特定于方案的类型是 “`!ebd0a0a2-b9e5-4433-87c0-68b6b72699c7`” 。

[`ms-ldm-data`](#ms-ldm-data)

包含逻辑磁盘管理器 (LDM) 卷的分区。 特定于方案的类型对于 MBR 是 “`!66`” ，对于 GPT 是 “`!af9b60a0-1431-4f62-bc68-3311714a69ad`” 。

[`ms-ldm-metadata`](#ms-ldm-metadata)

包含逻辑磁盘管理器 (LDM) 数据库的分区。 对于 GPT，特定于方案的类型是 “`!5808c8aa-7e8f-42e0-85d2-e1e90434cfb3`” 。

[`netbsd-ccd`](#netbsd-ccd)

与 Concatenated Disk 驱动程序一起使用的 NetBSD 分区。 对于 GPT，特定于方案的类型是 “`!2db519c4-b10f-11dc-b99b-0019d1879648`” 。

[`netbsd-cgd`](#netbsd-cgd)

一个加密的 NetBSD 分区。 对于 GPT，特定于方案的类型是 “`!2db519ec-b10f-11dc-b99b-0019d1879648`” 。

[`netbsd-ffs`](#netbsd-ffs)

包含 UFS 文件系统的 NetBSD 分区。 对于 GPT，特定于方案的类型是 “`!49f48d5a-b10e-11dc-b99b-0019d1879648`” 。

[`netbsd-lfs`](#netbsd-lfs)

包含 LFS 文件系统的 NetBSD 分区。 对于 GPT，特定于方案的类型是 “`!49f48d82-b10e-11dc-b99b-0019d1879648`” 。

[`netbsd-raid`](#netbsd-raid)

用于软件 RAID 配置的 NetBSD 分区。 对于 GPT，特定于方案的类型是 “`!49f48daa-b10e-11dc-b99b-0019d1879648`” 。

[`netbsd-swap`](#netbsd-swap)

专用于交换空间的 NetBSD 分区。 对于 GPT，特定于方案的类型是 “`!49f48d32-b10e-11dc-b99b-0019d1879648`” 。

[`ntfs`](#ntfs)

包含 NTFS 或 exFAT 文件系统的分区。 对于 MBR，特定于方案的类型是 “`!7`” 。

[`prep-boot`](#prep-boot)

专用于在某些 PowerPC 系统上存储引导加载程序的系统分区，特别是那些由 IBM 制造的系统。 特定于方案的类型是 MBR 的 “`!65`” 和 GPT 的 “`!9e1a2d38-c612-4316-aa26-8b49521e5a8b`” 。

[`solaris-boot`](#solaris-boot)

专用于引导加载程序的 illumos/Solaris 分区。 对于 GPT，特定于方案的类型是 “`!6a82cb45-1dd2-11b2-99a6-080020736631`” 。

[`solaris-root`](#solaris-root)

专用于根文件系统的 illumos/Solaris 分区。 对于 GPT，特定于方案的类型是 “`!6a85cf4d-1dd2-11b2-99a6-080020736631`” 。

[`solaris-swap`](#solaris-swap)

专用于交换的 illumos/Solaris 分区。 对于 GPT，特定于方案的类型是 “`!6a87c46f-1dd2-11b2-99a6-080020736631`” 。

[`solaris-backup`](#solaris-backup)

专门用于备份的 illumos/Solaris 分区。 对于 GPT，特定于方案的类型是 “`!6a8b642b-1dd2-11b2-99a6-080020736631`” 。

[`solaris-var`](#solaris-var)

专用于 /var 文件系统的 illumos/Solaris 分区。 对于 GPT，特定于方案的类型是 “`!6a8ef2e9-1dd2-11b2-99a6-080020736631`” 。

[`solaris-home`](#solaris-home)

专用于 /home 文件系统的 illumos/Solaris 分区。 对于 GPT，特定于方案的类型是 “`!6a90ba39-1dd2-11b2-99a6-080020736631`” 。

[`solaris-altsec`](#solaris-altsec)

专用于备用扇区的 illumos/Solaris 分区。 对于 GPT，特定于方案的类型是 “`!6a9283a5-1dd2-11b2-99a6-080020736631`” 。

[`solaris-reserved`](#solaris-reserved)

专用于保留空间的 illumos/Solaris 分区。 对于 GPT，特定于方案的类型是 “`!6a945a3b-1dd2-11b2-99a6-080020736631`” 。

[`vmware-vmfs`](#vmware-vmfs)

包含 VMware 文件系统 (VMFS) 的分区。 特定于方案的类型是 MBR 的 “`!251`” 和 GPT 的 “`!aa31e02a-400f-11db-9590-000c2911d1b8`” 。

[`vmware-vmkdiag`](#vmware-vmkdiag)

包含 VMware 诊断文件系统的分区。 特定于方案的类型是 MBR 的 “`!252`” 和 GPT 的 “`!9d275380-40ad-11db-bf97-000c2911d1b8`” 。

[`vmware-reserved`](#vmware-reserved)

VMware 保留分区。 对于 GPT，特定于方案的类型是 “`!9198effc-31c0-11db-8f-78-000c2911d1b8`” 。

[`vmware-vsanhdr`](#vmware-vsanhdr)

VMware VSAN 声明的分区。 对于 GPT，特定于方案的类型是 “`!381cfccc-7288-11e0-92ee-000c2911d0b2`” 。

[属性](#__u5C5E___u6027_)
=======================

EBR 的特定于方案的属性：

[`active`](#active)

GPT 的特定于方案的属性：

[`bootme`](#bootme)

设置后， `gptboot` 阶段 1 引导加载程序将尝试从该分区引导系统。 可以使用 `bootme` 属性标记多个分区。 有关详细信息，请参阅 gptboot(8) 。

[`bootonce`](#bootonce)

设置此属性会自动设置 `bootme` 属性。 设置后， `gptboot` 阶段 1 引导加载程序将仅尝试从该分区引导系统一次。 可以使用 `bootonce` 和 `bootme` 属性对标记多个分区。 有关详细信息，请参阅 gptboot(8) 。

[`bootfailed`](#bootfailed)

不应手动管理此属性。 它由 `gptboot` 阶段 1 引导加载程序和 /etc/rc.d/gptboot 启动脚本管理。 有关详细信息，请参阅 gptboot(8) 。

[`lenovofix`](#lenovofix)

设置此属性会用一个新的 MBR 覆盖 Protective MBR，其中 0xee 分区是第二个，而不是第一个记录。 这解决了包括 X220、T420 和 T520 在内的一些 Lenovo 型号的 BIOS 兼容性问题，允许它们从 GPT 分区磁盘引导而无需使用 EFI。

MBR 的特定于方案的属性：

[`active`](#active_2)

[自举](#__u81EA___u4E3E_)
=======================

FreeBSD FreeBSD 支持多种分区方案，每个方案使用不同的引导代码。 引导代码位于每个分区方案的特定磁盘区域中，并且对于不同的方案其大小可能不同。

引导代码可以分为两种类型。 第一种类型嵌入在分区方案的元数据中，而第二种类型位于特定分区上。 嵌入引导代码只能使用带有 `-b` bootcode 选项的 `gpart bootcode` 命令来完成。 GEOM PART 类知道如何安全地将引导代码嵌入到特定的分区方案元数据中而不会造成任何损坏。

主引导记录 (MBR) 使用 512 字节的引导代码映像，嵌入到分区表的元数据区域中。 此引导代码有两种变体： /boot/mbr 和 /boot/boot0 。 /boot/mbr-
在分区表中搜索具有 `active` 属性（请参阅 [属性](#__u5C5E___u6027_) 部分）的分区。 /boot/boot0 映像包含一个引导管理器，该管理器具有一些额外的交互功能，用于从用户选择的分区进行多重引导。

BSD 磁盘标签通常在类型为 `freebsd` 的 MBR 分区（片）内创建（请参阅 [分区类型](#__u5206___u533A___u7C7B___u578B_) 部分）。 它使用 8 KB 大小的引导代码映像 /boot/boot, 嵌入到分区表的元数据区域。

两种类型的引导代码都用于从 GUID 分区表引导。 首先，保护性 MBR 嵌入到 /boot/pmbr 映像的第一个磁盘扇区中。 它在 GPT 中搜索一个 `freebsd-boot` 分区（参见 [分区类型](#__u5206___u533A___u7C7B___u578B_) 部分）并从中运行下一个引导阶段。 `freebsd-boot` 分区应该小于 545 KB。 它可以位于磁盘上其他 FreeBSD 分区之前或之后。 有两种引导代码变体可写入此分区： /boot/gptboot 和 /boot/gptzfsboot 。

/boot/gptboot 用于从 UFS 分区引导。 `gptboot` 搜索 GPT 中的 `freebsd-ufs` 分区，并根据 `bootonce` 和 `bootme` 属性选择一个进行引导。 如果两个属性都没有找到， /boot/gptboot 从第一个 `freebsd-ufs` 分区引导。 /boot/loader (第三个引导阶段) 从符合这些条件的第一个分区加载。 有关详细信息，请参阅 gptboot(8) 。

/boot/gptzfsboot 用于从 ZFS 引导。 它在 GPT 中搜索 `freebsd-zfs` 分区，尝试检测 ZFS 池。 检测到所有池后， /boot/loader 将从找到的第一个设置为可引导的池启动。

VTOC8 方案不支持嵌入引导代码。 相反，应该使用带有 `-p` bootcode 选项的 `gpart bootcode` 命令将 8 KB 引导代码映像 /boot/boot1 写入所有足够大的 VTOC8 分区。 为此，可以省略 `-i` index 选项。

APM 方案也不支持嵌入引导代码。 相反，应该使用 `gpart bootcode` 命令将 800 KB 引导代码映像 /boot/boot1.hfs 写入 `apple-boot` 类型的分区，该分区的大小也应为 800 KB。

[操作标志](#__u64CD___u4F5C___u6807___u5FD7_)
=========================================

`commit` 和 `undo` 操作以外的操作采用可选的 `-f` flags 选项。 此选项用于指定特定于操作的操作标志。 默认情况下， `gpart` 实用程序定义了 ‘`C`’ 标志，以便立即提交操作。 用户可以指定 “`-f` `x`” 以使操作导致挂起的更改，稍后可以与其他挂起的更改一起作为单个复合更改与提交操作一起 `commit` 或通过 `undo` 操作恢复。

[正在恢复](#__u6B63___u5728___u6062___u590D_)
=========================================

GEOM PART 类仅支持恢复 GPT 的分区表。 GPT 主要元数据存储在设备的开头。 为了冗余，元数据的辅助 (backup) 副本存储在设备的末端。 由于有两个副本，元数据的某些损坏对 GPT 的工作来说并不是致命的。 当内核检测到损坏的元数据时，它会将这个表标记为损坏并报告问题。 `destroy` 和 `recover` 是对损坏表唯一允许的操作。

如果一个 GPT 标头似乎已损坏，但另一个副本保持不变，内核将记录以下内容：

GEOM：提供者：主 GPT 表已损坏或无效。 GEOM：提供者：使用辅助节点——强烈建议恢复。 

或

GEOM：提供者：辅助 GPT 表已损坏或无效。 GEOM：提供者：仅使用主节点——建议恢复。 

`gpart` 命令（如 `show`, `status` 和 `list` ）也会报告损坏的表。

如果设备的大小发生了变化（例如，卷扩展），则辅助 GPT 标头将不再位于最后一个扇区中。 这不是元数据损坏，但它很危险，因为主 GPT 的任何损坏都会导致分区表丢失。 内核通过以下消息报告此问题：

GEOM：提供者：辅助 GPT 标头不在最后一个 LBA 中。 

这种情况可以使用 `recover` 命令恢复。 此命令使用已知的有效元数据重建损坏的元数据，并将辅助 GPT 重新定位到设备的末尾。

_NOTE_: GEOM PART 类可以检测到通过不同 GEOM 提供程序可见的相同分区表，其中一些将被标记为损坏。 选择恢复提供商时要小心。 如果选择不正确，您可能会破坏另一个 GEOM 类的元数据，例如 GEOM MIRROR 或 GEOM LABEL。

[SYSCTL 变量](#SYSCTL___u53D8___u91CF_)
=====================================

以下 sysctl(8) 变量可用于控制 `PART` GEOM 类的行为。 默认值显示在每个变量旁边。

kern.geom.part.allow\_nesting: 0

默认情况下，一些方案（目前是 BSD、BSD64 和 VTOC8）不允许进一步的嵌套分区。 此变量会覆盖此限制并允许任意嵌套（在偏移量 0 创建的分区内除外）。 有些方案有自己的单独检查，见下文。

kern.geom.part.auto\_resize: 1

此变量控制 `PART` GEOM 类的自动调整大小行为。 当启用此变量并检测到提供程序的新大小时，架构元数据会调整大小，但所有更改都不会保存到磁盘，直到运行 `gpart commit` 以确认更改。 诊断消息也会报告此行为： **GEOM\_PART: (provider) was automatically resized.** **Use \`gpart commit (provider)\` to save changes or \`gpart undo (provider)\`** **to revert them.**

kern.geom.part.check\_integrity: 1

此变量控制元数据完整性检查的行为。 启用完整性检查后， `PART` GEOM 类会验证从磁盘元数据获取的所有通用分区参数。 如果检测到一些不一致，分区表将被拒绝并显示诊断消息： **GEOM\_PART: Integrity check failed (provider, scheme)**.

kern.geom.part.gpt.allow\_nesting: 0

默认情况下，仅允许在最外层嵌套级别使用 GPT 方案。 此变量允许删除此限制。

kern.geom.part.ldm.debug: 0

逻辑磁盘管理器 (LDM) 模块的调试级别。 这可以设置为介于 0 和 2 之间的数字。 如果设置为 0，则打印最小调试信息，如果设置为 2，则打印最大调试信息量。

kern.geom.part.ldm.show\_mirrors: 0

此变量控制逻辑磁盘管理器 (LDM) 模块如何处理镜像卷。 默认情况下，镜像卷显示为类型为 `ms-ldm-data` 的分区（请参阅 [分区类型](#__u5206___u533A___u7C7B___u578B_) 部分）。 如果将此变量设置为 1，则镜像卷的每个组件都将作为独立分区存在。 _NOTE_: 这可能会破坏镜像卷并导致数据损坏。

kern.geom.part.mbr.enforce\_chs: 0

指定主引导记录 (MBR) 模块如何进行对齐。 如果此变量设置为非零值，模块将自动重新计算用户指定的偏移量和大小，以与 CHS 几何对齐。 否则这些值将保持不变。

kern.geom.part.separator:

指定将在 GEOM 名称和分区名称之间插入的可选分隔符。 这个变量是一个 loader(8) 可调参数。 请注意，设置此变量可能会破坏采用特定命名方案的软件。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

成功时退出状态为 0，如果命令失败则为 1。

[实例](#__u5B9E___u4F8B_)
=======================

下面的示例假定磁盘的逻辑块大小为 512 字节，而不管其物理块大小。

[GPT](#GPT_2)
-------------

在本例中，我们将使用 GPT 方案格式化 ada0 并创建引导、交换和根分区。首先，我们需要创建分区表：

/sbin/gpart create -s GPT ada0 

接下来，我们使用第一阶段引导代码安装保护 MBR。 保护性 MBR 列出了跨越整个磁盘的单个可引导分区，从而允许不支持 GPT 的 BIOS 从磁盘引导，并防止不了解 GPT 方案的工具认为磁盘未格式化。

/sbin/gpart bootcode -b /boot/pmbr ada0 

然后，我们创建一个专用的 `freebsd-boot` 分区来保存第二阶段引导加载程序，它将从 UFS 或 ZFS 文件系统加载 FreeBSD 内核和模块。 该分区必须大于引导代码 (UFS 的 /boot/gptboot 或 ZFS 的 /boot/gptzfsboot), 但小于 545 kB，因为第一阶段加载程序将在引导期间将整个分区加载到内存中，无论如何它实际包含的大量数据。 我们在偏移量 40 处创建一个 472 块 (236 kB) 的引导分区，这是分区表的大小（34 块或 17 kB）四舍五入到最近的 4 kB 边界。

/sbin/gpart add -b 40 -s 472 -t freebsd-boot ada0 /sbin/gpart bootcode -p /boot/gptboot -i 1 ada0 

我们现在在第一个可用偏移处创建一个 4 GB 的交换分区，即 40 + 472 = 512 个块 (256 kB)。

/sbin/gpart add -s 4G -t freebsd-swap ada0 

在 256 kB 边界上对齐交换分区和所有后续分区可确保在各种介质上实现最佳性能，从具有 512 字节块的普通旧磁盘到具有 4096 字节物理块的现代 “advanced format” 磁盘，再到 RAID 卷条带大小高达 256 kB。

最后，我们为根文件系统创建并格式化了一个 8 GB 的 `freebsd-ufs` 分区，将剩余部分留作其他文件系统：

/sbin/gpart add -s 8G -t freebsd-ufs ada0 /sbin/newfs -Uj /dev/ada0p3 

[MBR](#MBR_2)
-------------

在本例中，我们将使用 MBR 方案格式化 ada0 并创建一个单独的分区，我们使用传统的 BSD 磁盘标签对其进行细分。

首先，我们创建分区表和单个 64 GB 分区，然后将该分区标记为活动（可引导）并安装第一阶段引导加载程序：

/sbin/gpart create -s MBR ada0 /sbin/gpart add -t freebsd -s 64G ada0 /sbin/gpart set -a active -i 1 ada0 /sbin/gpart bootcode -b /boot/boot0 ada0 

接下来，我们在该分区中创建一个磁盘标签 (磁盘标签术语中的 “slice”) ，最多可容纳 20 个分区：

/sbin/gpart create -s BSD -n 20 ada0s1 

然后我们创建一个 8 GB 的根分区和一个 4 GB 的交换分区：

/sbin/gpart add -t freebsd-ufs -s 8G ada0s1 /sbin/gpart add -t freebsd-swap -s 4G ada0s1 

最后，我们为 BSD 标签安装适当的引导加载程序：

/sbin/gpart bootcode -b /boot/boot ada0s1 

[VTOC8](#VTOC8_2)
-----------------

在 da0 上创建一个 VTOC8 方案：

/sbin/gpart create -s VTOC8 da0 

创建一个 512MB 大小的 `freebsd-ufs` 分区以包含一个 UFS 文件系统，系统可以从该文件系统引导。

/sbin/gpart add -s 512M -t freebsd-ufs da0 

创建一个 15GB 大小的 `freebsd-ufs` 分区以包含 UFS 文件系统并在 4KB 边界上对齐：

/sbin/gpart add -s 15G -t freebsd-ufs -a 4k da0 

创建所有必需的分区后，将引导代码嵌入其中：

/sbin/gpart bootcode -p /boot/boot1 da0 

[删除分区和销毁分区方案](#__u5220___u9664___u5206___u533A___u548C___u9500___u6BC1___u5206___u533A___u65B9___u6848_)
--------------------------------------------------------------------------------------------------------

如果在尝试销毁分区表时显示 _Device busy_ 错误，请记住必须先使用 `delete` 操作删除所有分区。 在此示例中， da0 具有三个分区：

/sbin/gpart delete -i 3 da0 /sbin/gpart delete -i 2 da0 /sbin/gpart delete -i 1 da0 /sbin/gpart destroy da0 

不是删除每个分区然后销毁分区方案，而是可以使用 `-F` 选项与 `destroy` 一起删除所有分区，然后再销毁分区方案。这等效于前面的示例：

/sbin/gpart destroy -F da0 

[备份还原](#__u5907___u4EFD___u8FD8___u539F_)
-----------------------------------------

从 da0 创建分区表的备份：

/sbin/gpart backup da0 > da0.backup 

将分区表从备份恢复到 da0:

/sbin/gpart restore -l da0 < /mnt/da0.backup 

将分区表从 ada0 克隆到 ada1 和 ada2:

/sbin/gpart backup ada0 | /sbin/gpart restore -F ada1 ada2 

[参见](#__u53C2___u89C1_)
=======================

geom(4), boot0cfg(8), geom(8), gptboot(8)

[历史](#__u5386___u53F2_)
=======================

`gpart` 实用程序出现在 FreeBSD 7.0 中。

[作者](#__u4F5C___u8005_)
=======================

Marcel Moolenaar <[marcel@FreeBSD.org](mailto:marcel@FreeBSD.org)\>

[注意事项](#__u6CE8___u610F___u4E8B___u9879_)
=========================================

分区类型 _apple-zfs_ (6a898cc3-1dd2-11b2-99a6-080020736631) 也用于 ZFS 卷的 illumos/Solaris 平台。

August 17, 2020

FreeBSD 13.1-RELEASE