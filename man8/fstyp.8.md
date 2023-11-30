  FSTYP(8)  

FSTYP(8)

FreeBSD System Manager's Manual

FSTYP(8)

[名称](#__u540D___u79F0_)
=======================

`fstyp` —

确定文件系统类型

[概要](#__u6982___u8981_)
=======================

`fstyp` \[`-l`\] \[`-s`\] \[`-u`\] special

[描述](#__u63CF___u8FF0_)
=======================

`fstyp` 实用程序用于确定给定设备上的文件系统类型。 它可以识别 ISO-9660、exFAT、Ext2、FAT、NTFS 和 UFS 文件系统。 当指定 `-u` 标志时， `fstyp` 还可以识别某些无法使用 mount(8) 处理的附加元数据格式，例如 geli(8)-
提供程序和 ZFS 池。

文件系统名称分别打印到标准输出：

*   cd9660
*   exfat
*   ext2fs
*   geli
*   hammer
*   hammer2
*   msdosfs
*   ntfs
*   ufs
*   zfs

因为 `fstyp` 是专门为检测文件系统类型而构建的，所以它在几个方面与 file(1) 不同。 输出是机器可解析的，支持文件系统标签，该实用程序使用 capsicum(4) 以沙盒方式运行，并且不尝试识别文件系统以外的任何文件格式。

这些选项可用：

[`-l`](#l)

除了文件系统类型，如果可用，打印文件系统标签。

[`-s`](#s)

忽略文件类型。 默认情况下， `fstyp` 仅适用于常规文件和类似磁盘的设备节点。 尝试读取其他文件类型可能会产生意想不到的后果或无限期挂起。

[`-u`](#u)

包括无法通过 mount(8) 直接挂载的文件系统和设备。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

`fstyp` 实用程序在成功时退出 0，如果发生错误或文件系统类型无法识别，则 >0。

[参见](#__u53C2___u89C1_)
=======================

file(1), capsicum(4), autofs(5), geli(8), glabel(8), mount(8), zpool(8)

[历史](#__u5386___u53F2_)
=======================

`fstyp` 命令出现在 FreeBSD 10.2 中。

[作者](#__u4F5C___u8005_)
=======================

`fstyp` 实用程序由 Edward Tomasz Napierala <[trasz@FreeBSD.org](mailto:trasz@FreeBSD.org)\> 在 FreeBSD 基金会的赞助下开发。 ZFS 和 GELI 支持由 Allan Jude <[allanjude@FreeBSD.org](mailto:allanjude@FreeBSD.org)\> 添加。

December 24, 2019

FreeBSD 13.1-RELEASE