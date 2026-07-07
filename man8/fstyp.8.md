# fstyp(8)

`fstyp` — 确定文件系统类型

## 名称

`fstyp`

## 概要

`fstyp [-l] [-s] [-u] special`

## 描述

`fstyp` 工具用于确定给定设备上的文件系统类型。它能识别 BeFS（BeOS）、ISO-9660、exFAT、Ext2、FAT、NTFS 和 UFS 文件系统。指定 `-u` 标志时，`fstyp` 还能识别某些无法使用 [mount(8)](mount.8.md) 处理的额外元数据格式，例如 geli(8) 提供者和 ZFS 存储池。

文件系统名称将分别按以下形式打印到标准输出：

- befs
- cd9660
- exfat
- ext2fs
- geli
- hammer
- hammer2
- msdosfs
- ntfs
- ufs
- zfs

由于 `fstyp` 专门为检测文件系统类型而构建，它与 file(1) 有以下几点不同。其输出可被机器解析，支持文件系统标签，该工具使用 [capsicum(4)](../man4/capsicum.4.md) 在沙箱中运行，并且不会尝试识别除文件系统以外的任何文件格式。

可用选项如下：

**`-l`** 除文件系统类型外，如果可用，还打印文件系统标签。

**`-s`** 忽略文件类型。默认情况下，`fstyp` 仅对常规文件和类磁盘设备节点有效。尝试读取其他文件类型可能会产生意外后果或无限挂起。

**`-u`** 包含无法直接由 [mount(8)](mount.8.md) 挂载的文件系统和设备。

## 退出状态

`fstyp` 工具成功时退出码为 0，发生错误或无法识别文件系统类型时退出码大于 0。

## 参见

file(1), [autofs(4)](../man4/autofs.4.md), [capsicum(4)](../man4/capsicum.4.md), geli(8), glabel(8), [mount(8)](mount.8.md), zpool(8)

## 历史

`fstyp` 命令出现于 FreeBSD 10.2。

## 作者

`fstyp` 工具由 Edward Tomasz Napierala <trasz@FreeBSD.org> 在 FreeBSD 基金会赞助下开发。ZFS 和 GELI 支持由 Allan Jude <allanjude@FreeBSD.org> 添加。
