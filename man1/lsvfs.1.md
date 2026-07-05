# lsvfs.1

`lsvfs` — 列出已安装的虚拟文件系统

## 名称

`lsvfs`

## 概要

`lsvfs [vfsname ...]`

## 描述

`lsvfs` 命令列出当前已加载的虚拟文件系统模块的信息。当给定 `vfsname` 参数时，`lsvfs` 列出指定 VFS 模块的信息；否则，`lsvfs` 列出所有当前已加载的模块。所列信息如下：

**Filesystem** 文件系统名称，与 mount(2) 的 `type` 参数和 [mount(8)](../man8/mount.8.md) 的 `-t` 选项所使用的名称相同
**Num** 文件系统类型编号。
**Refs** 此 VFS 的引用数，即当前已挂载的此类型文件系统数量
**Flags** 标志位。

## 实例

显示 `ufs` 和 [devfs(4)](../man4/devfs.4.md) 文件系统的信息，并检查前者的挂载数量：

```sh
$ lsvfs ufs devfs
Filesystem                              Num  Refs  Flags
-------------------------------- ---------- -----  ---------------
ufs                              0x00000035     2
devfs                            0x00000071     1  synthetic, jail
$ mount -t ufs | wc -l
       2
```

## 参见

mount(2), getvfsbyname(3), [mount(8)](../man8/mount.8.md)

## 历史

`lsvfs` 命令出现于 FreeBSD 2.0。
