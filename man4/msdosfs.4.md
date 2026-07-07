# msdosfs(4)

`msdosfs` — MS-DOS（FAT）文件系统

## 名称

`msdosfs`

## 概要

`options MSDOSFS`

## 描述

`msdosfs` 驱动使 FreeBSD 内核能够读写基于 MS-DOS 的文件系统。

最常见的用法如下：

```sh
mount -t msdosfs /dev/ada0sN /mnt
```

其中 `N` 是分区号，`/mnt` 是挂载点。一些用户倾向于为 `msdosfs` 挂载点创建一个 `/dos` 目录。这有助于更好地跟踪文件系统，并使其更易于访问。

可以在 `/etc/fstab` 中定义一个条目，类似于：

```sh
/dev/ada0sN		/dos	msdosfs		rw	0	0
```

这将在系统引导时将基于 MS-DOS 的分区挂载到 `/dos` 挂载点。不建议使用 `/mnt` 作为永久挂载点，因为它的初衷始终是作为软盘和 ZIP 磁盘的临时挂载点。有关 FreeBSD 目录布局的更多信息，参见 [hier(7)](../man7/hier.7.md)。

## 实例

确定某个分区格式化为哪种 FAT 文件系统版本（例如 FAT16、FAT32）：

```sh
file -s /dev/da0s1
```

也可使用 [gpart(8)](../man8/gpart.8.md) 提取此信息。

## 参见

[mount(2)](../sys/mount.2.md), [unmount(2)](../sys/mount.2.md), [fsck_msdosfs(8)](../man8/fsck_msdosfs.8.md), [mount(8)](../man8/mount.8.md), [mount_msdosfs(8)](../man8/mount_msdosfs.8.md), [newfs_msdos(8)](../man8/newfs_msdos.8.md), [umount(8)](../man8/umount.8.md)

## 作者

本手册页由 Tom Rhodes <trhodes@FreeBSD.org> 编写。
