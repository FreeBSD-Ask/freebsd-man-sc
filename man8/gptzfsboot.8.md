  GPTZFSBOOT(8)  

GPTZFSBOOT(8)

FreeBSD System Manager's Manual

GPTZFSBOOT(8)

[名称](#__u540D___u79F0_)
=======================

`gptzfsboot` —

基于 BIOS 的计算机上 ZFS 的 GPT 引导代码

[描述](#__u63CF___u8FF0_)
=======================

`gptzfsboot` 在基于 BIOS 的计算机上用于从 ZFS 池中的文件系统引导。 `gptzfsboot` 使用 gpart(8) 安装在 GPT 分区磁盘的 `freebsd-boot` 分区中。

[实施说明](#__u5B9E___u65BD___u8BF4___u660E_)
=========================================

GPT 标准允许可变数量的分区，但 `gptzfsboot` 仅从具有 128 个或更少分区的表引导。

[开机](#__u5F00___u673A_)
=======================

`gptzfsboot` 尝试查找由 BIOS 可见的硬盘或分区组成的所有 ZFS 池。 `gptzfsboot` 在所有可见磁盘和发现的所有支持分区方案类型的支持分区中查找 ZFS 设备标签。 搜索从加载 `gptzfsboot` 本身的磁盘开始。 其他磁盘按 BIOS 定义的顺序进行探测。 在探测磁盘并且 `gptzfsboot` 确定整个磁盘不是 ZFS 池成员后，将按其分区表顺序探测各个分区。 目前支持 GPT 和 MBR 分区方案。 使用 GPT 方案，只探测类型为 `freebsd-zfs` 的分区。 探测期间看到的第一个池用作默认引导池。

池的 `bootfs` 属性指定的文件系统用作默认引导文件系统。 如果未设置 `bootfs` 属性，则默认使用池的根文件系统。 loader(8) 从引导文件系统加载。 如果 /boot.config 或 /boot/config 存在于引导文件系统中，则以与 boot(8) 相同的方式从中读取引导选项。

第一个成功探测的设备和第一个检测到的池的 ZFS GUID 在 `vfs.zfs.boot.primary_vdev` 和 `vfs.zfs.boot.primary_pool` 变量中可供 loader(8) 使用。

[用法](#__u7528___u6CD5_)
=======================

通常 `gptzfsboot` 将以全自动模式启动。但是，与 boot(8) 一样，可以中断自动引导过程并通过提示符与 `gptzfsboot` 交互。 `gptzfsboot` 接受 boot(8) 支持的所有选项。

文件系统规范和 loader(8) 的路径与 boot(8) 不同。 格式是

\[zfs:pool/filesystem:\]\[/path/to/loader\]

文件系统和路径都可以指定。 如果仅指定路径，则使用默认文件系统。 如果仅指定了池和文件系统，则 /boot/loader 用作路径。

此外， `status` 命令可用于查询有关已发现池的信息。 输出格式类似于 `zpool status` 的输出格式 (请参阅 zpool(8)) 。

配置的或自动确定的 ZFS 引导文件系统存储在 loader(8) 的 `loaddev` 变量中，并设置为 `currdev` 变量的初始值。

[文件](#__u6587___u4EF6_)
=======================

/boot/gptzfsboot

启动代码二进制

/boot.config

引导块的参数 (可选)

/boot/config

引导块的替代参数 (可选)

[实例](#__u5B9E___u4F8B_)
=======================

`gptzfsboot` 通常与 “protective MBR” 一起安装 (参见 gpart(8)) 。 在 ada0 驱动器上安装 `gptzfsboot` :

gpart bootcode -b /boot/pmbr -p /boot/gptzfsboot -i 1 ada0 

`gptzfsboot` 也可以在没有 PMBR 的情况下安装：

gpart bootcode -p /boot/gptzfsboot -i 1 ada0 

[参见](#__u53C2___u89C1_)
=======================

boot.config(5), boot(8), gpart(8), loader(8), zpool(8)

[历史](#__u5386___u53F2_)
=======================

`gptzfsboot` 出现在 FreeBSD 7.3 中。

[作者](#__u4F5C___u8005_)
=======================

本手册由 Andriy Gapon ⟨avg@FreeBSD.org⟩ 编写。

[缺陷](#__u7F3A___u9677_)
=======================

`gptzfsboot` 仅在 MBR 分区 (在 FreeBSD 上称为切片) 中查找 ZFS 元数据。 它不查看传统上称为分区的 BSD disklabel(8) 分区。 如果恰好放置了一个磁盘标签分区，以便可以在相对于切片的固定偏移量处找到 ZFS 元数据，则 `gptzfsboot` 会将分区识别为 ZFS 池的一部分，但这并不保证会发生。

September 15, 2014

FreeBSD 13.1-RELEASE