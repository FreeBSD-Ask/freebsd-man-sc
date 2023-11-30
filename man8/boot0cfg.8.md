  BOOT0CFG(8)  

BOOT0CFG(8)

FreeBSD System Manager's Manual

BOOT0CFG(8)

[名称](#__u540D___u79F0_)
=======================

`boot0cfg` —

引导管理器安装/配置实用程序

[概要](#__u6982___u8981_)
=======================

`boot0cfg` \[`-Bv`\] \[`-b` boot0\] \[`-d` drive\] \[`-e` bell character\] \[`-f` file\] \[`-i` volume-id\] \[`-m` mask\] \[`-o` options\] \[`-s` slice\] \[`-t` ticks\] disk

[描述](#__u63CF___u8FF0_)
=======================

FreeBSD ‘boot0’ 引导管理器允许操作员选择从哪个磁盘和切片中引导 i386 机器 (PC)。

请注意，这里所说的 “slices” 在与 PC 相关的非 BSD 文档中通常称为 “partitions” 。 通常，仅对不可移动磁盘进行切片。

`boot0cfg` 实用程序可选择在指定 disk 上安装 ‘boot0’ 引导管理器；并允许配置各种操作参数。

在 PC 上，引导管理器通常占用磁盘的第 0 扇区，这称为主引导记录 (MBR)。 MBR 包含代码（PC BIOS 将控制传递给它）和数据（定义切片的嵌入式表）。

选项包括：

[`-B`](#B)

安装 ‘boot0’ 引导管理器。 此选项会导致 MBR 代码被替换，而不影响嵌入的切片表。

[`-b`](#b) boot0

指定要使用的 ‘boot0’ 映像。 默认是 /boot/boot0 ，它将使用显卡作为输出，或者 /boot/boot0sio 可以用于输出到COM1 端口。 （请注意，除非调制解调器信号 DSR 和 CTS 处于活动状态，否则不会向 COM1 端口输出任何内容。）

[`-d`](#d) drive

指定 PC BIOS 在引用包含指定 disk 的驱动器时使用的驱动器号。 通常，第一个硬盘驱动器为 0x80，第二个硬盘驱动器为 0x81，依此类推；但是，这里可以接受 0 到 0xff 之间的任何整数。

[`-e`](#e) bell character

设置输入错误时要打印的字符。

[`-f`](#f) file

指定应将预先存在的 MBR 的备份副本写入 file 。 如果该文件不存在，则创建该文件，如果存在则替换该文件。

[`-i`](#i) volume-id

指定要保存在 MBR 中位置 0x1b8 的卷 ID（格式为 XXXX-XXXX）。 NT、XP 和 Vista 有时使用此信息来识别磁盘驱动器。 该选项仅与 512 字节引导块的 2.00 版兼容。

[`-m`](#m) mask

指定要启用/禁用的切片，其中 mask 是介于 0（未启用切片）和 0xf（所有四个切片都已启用）之间的整数。 如果设置为 1，则每个掩码位启用相应的切片。 掩码的最低有效位对应于切片 1，掩码的最高有效位对应于切片 4。

[`-o`](#o) options

可以指定以下任何选项的逗号分隔字符串（必要时在前面加上 “no” ）：

packet

在执行磁盘 I/O 时，使用磁盘数据包（BIOS INT 0x13 扩展）接口，而不是传统 (CHS) 接口。 这允许在柱面 1023 以上引导，但需要特定的 BIOS 支持。 默认值为 ‘packet’ 。

setdrv

强制使用可通过 -d 选项定义的驱动器号来引用包含磁盘的驱动器。 默认值为 ‘nosetdrv’ 。

update

允许引导管理器更新 MBR。 （可以更新 MBR 以将切片标记为 ‘active’, 并保存切片选择信息。） 这是默认设置； ‘noupdate’ 选项导致 MBR 被视为只读。

[`-s`](#s) slice

将默认引导选择设置为 slice 。 1 到 4 之间的值表示切片；值 5 表示从第二个磁盘引导的选项。 特殊字符串 “PXE” 或值 6 可用于通过 PXE 引导。

[`-t`](#t) ticks

将超时值设置为 ticks 。 （每秒大约有 18.2 个滴答声。）

[`-v`](#v)

详细：显示有关定义的切片等的信息。

[文件](#__u6587___u4EF6_)
=======================

/boot/boot0

默认的 ‘boot0’ 映像

/boot/boot0sio

串行控制台图像 (COM1,9600,8,N,1,MODEM)

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `boot0cfg` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

在下次启动时启动分片 2：

`boot0cfg -s 2 ada0`

要在菜单中仅启用切片 1 和 3：

`boot0cfg -m 0x5 ada0`

要返回非交互式引导，请使用 gpart(8) 安装默认 MBR：

`gpart bootcode -b /boot/mbr ada0`

[参见](#__u53C2___u89C1_)
=======================

geom(4), boot(8), gpart(8)

[作者](#__u4F5C___u8005_)
=======================

Robert Nordier <[rnordier@FreeBSD.org](mailto:rnordier@FreeBSD.org)\>

[缺陷](#__u7F3A___u9677_)
=======================

使用 ‘packet’ 选项可能会导致 ‘boot0’ 失败，这取决于 BIOS 支持的性质。

使用带有错误 -d 操作数的 ‘setdrv’ 选项可能会导致 boot0 代码将 MBR 写入错误的磁盘，从而破坏其先前的内容。 当心。

October 1, 2013

FreeBSD 13.1-RELEASE