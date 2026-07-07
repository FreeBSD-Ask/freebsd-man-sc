# ext2fs(4)

`ext2fs` — ext2/ext3/ext4 文件系统

## 名称

`ext2fs`

## 概要

`链接进内核：`

> options EXT2FS

`作为可加载内核模块加载：`

```sh
kldload ext2fs
```

## 描述

`ext2fs` 驱动程序允许 FreeBSD 内核访问 ext2 文件系统及其衍生文件系统。目前实现了 *ext3* 和 *ext4* 文件系统所需的大部分功能。*ext4* 中的扩展属性支持为实验性质。当前不支持日志和加密。

## 实例

挂载位于 **/dev/ada1s1** 的 `ext2fs` 卷：

```sh
mount -t ext2fs /dev/ada1s1 /mnt
```

## 参见

nmount(2), unmount(2), [fstab(5)](../man5/fstab.5.md), [mount(8)](../man8/mount.8.md)

## 历史

`ext2fs` 驱动程序首次出现于 FreeBSD 2.2。

## 作者

`ext2fs` 内核实现派生自 Godmar Back 编写或修改的代码，这些代码基于 CMU Mach 的 UFS CSRG 源码。

John Dyson 完成了到 FreeBSD 的初始移植。Aditya Sarawgi 从 NetBSD 的纯净实现中合并了分配代码的重要部分。Zheng Liu 和 Fedor Uporov 分别实现了 *ext4* 文件系统的读写支持。FreeBSD 社区贡献了大量修改。

本手册页的初始版本由 Craig Rodrigues <rodrigc@FreeBSD.org> 编写。
