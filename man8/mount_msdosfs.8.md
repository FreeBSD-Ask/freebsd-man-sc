  MOUNT\_MSDOSFS(8)  

MOUNT\_MSDOSFS(8)

FreeBSD System Manager's Manual

MOUNT\_MSDOSFS(8)

[名称](#__u540D___u79F0_)
=======================

`mount_msdosfs` —

挂载 MS-DOS 文件系统

[概要](#__u6982___u8981_)
=======================

`mount_msdosfs` \[`-9ls`\] \[`-D` DOS\_codepage\] \[`-g` gid\] \[`-L` locale\] \[`-M` mask\] \[`-m` mask\] \[`-o` options\] \[`-u` uid\] \[`-W` table\] special node

[描述](#__u63CF___u8FF0_)
=======================

`mount_msdosfs` 实用程序将驻留在特殊设备上的 MS-DOS 文件系统附加到由 node 指示的位置的全局文件系统命名空间。 此命令通常由 mount(8) 在启动时执行，但任何用户都可以使用它在他们拥有的任何目录上安装 MS-DOS 文件系统（当然，前提是他们对设备具有适当的访问权限）包含文件系统）。

选项如下：

[`-o`](#o) options

使用指定的挂载 options ，如 mount(8) 中所述。 以下 MSDOS 文件系统特定选项可用：

[`longnames`](#longnames)

强制 Windows 95 长文件名可见。

[`shortnames`](#shortnames)

强制只显示旧的 MS-DOS 8.3 样式文件名。

[`nowin95`](#nowin95)

完全忽略 Windows 95 扩展文件信息。

[`-u`](#u) uid

将文件系统中文件的所有者设置为 uid 。 默认所有者是安装文件系统的目录的所有者。

[`-g`](#g) gid

将文件系统中的文件组设置为 gid 。 默认组是挂载文件系统的目录组。

[`-m`](#m) mask

指定文件系统中文件的最大文件权限。 （例如， mask `755` 指定默认情况下，所有者应具有文件的读取、写入和执行权限，但其他人应仅具有读取和执行权限。 有关八进制文件模式的更多信息，请参阅 chmod(1) 。 仅使用了 mask 的低九位。 如果提供了 \-M 的值并且省略了 \-m ，则使用它。 默认 mask 取自挂载文件系统的目录。

[`-M`](#M) mask

指定文件系统中目录的最大文件权限。 如果提供了 \-m 的值并且省略了 \-M ，则使用它。 有关详细信息，请参阅上一个选项的说明。

[`-s`](#s)

强制行为忽略并且不生成 Win'95 长文件名。

[`-l`](#l)

强制列出和生成 Win'95 长文件名和单独的创建/修改/访问日期。

如果既没有给出 `-s` 也没有给出 `-l` ，则 `-l` 是默认值。

[`-9`](#9)

即使删除或重命名文件，也忽略特殊的 Win'95 目录条目。 这迫使 `-s` 。

[`-L`](#L) locale

指定用于 DOS 和 Win'95 名称的文件名转换的语言环境名称。 默认情况下，ISO 8859-1 假定为本地字符集。

[`-D`](#D) DOS\_codepage

指定用于 DOS 名称的文件名转换的 MS-DOS 代码页（也称为 IBM/OEM 代码页）名称。

[`-W`](#W) table

此选项仅出于向后兼容的目的而保留，将来将被删除。 请避免使用此选项。

使用转换表指定文本文件名： iso22dos, iso72dos, koi2dos, koi8u2dos 。

[示例](#__u793A___u4F8B_)
=======================

要挂载位于 /dev/ada1s1 的俄语 MS-DOS 文件系统：

`mount_msdosfs -L ru_RU.KOI8-R -D CP866 /dev/ada1s1 /mnt`

挂载位于 /dev/ada1s1 的日文 MS-DOS 文件系统：

`mount_msdosfs -L ja_JP.eucJP -D CP932 /dev/ada1s1 /mnt`

[参见](#__u53C2___u89C1_)
=======================

mount(2), unmount(2), fstab(5), msdosfs(5), mount(8)

本地化 MS 操作系统列表： http://www.microsoft.com/globaldev/reference/oslocversion.mspx.

[历史](#__u5386___u53F2_)
=======================

`mount_msdos` 实用程序的前身 `mount_pcfs` 出现在 NetBSD 0.8 中。 它在 NetBSD 1.0 中被重写，并首次出现在 FreeBSD 2.0 中。 `mount_msdos` 在 FreeBSD 5.0 中更名为 `mount_msdosfs` 。 字符代码转换例程于 2003 年添加。

[作者](#__u4F5C___u8005_)
=======================

`mount_pcfs` 的初始实现由 Paul Popelka <[paulp@uts.amdahl.com](mailto:paulp@uts.amdahl.com)\> 编写。 它由 Christopher G. Demetriou <[cgd@NetBSD.org](mailto:cgd@NetBSD.org)\> 重写。 字符代码转换例程由 Ryuichiro Imura <[imura@ryu16.org](mailto:imura@ryu16.org)\> 添加。

[注意事项](#__u6CE8___u610F___u4E8B___u9879_)
=========================================

使用 `-9` 标志可能会导致文件系统损坏，尽管部分损坏由类似于 Win'95 中使用的程序处理。

May 28, 2017

FreeBSD 13.1-RELEASE