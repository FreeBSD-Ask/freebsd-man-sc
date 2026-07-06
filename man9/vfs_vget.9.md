# VFS_VGET.9

`VFS_VGET` — 将 inode 号转换为 vnode

## 名称

`VFS_VGET`

## 概要

```c
#include <sys/param.h>
#include <sys/mount.h>
#include <sys/vnode.h>

int
VFS_VGET(struct mount *mp, ino_t ino, int flags, struct vnode **vpp)
```

## 描述

`VFS_VGET` 从（挂载点，inode 号）元组查找或创建一个 vnode。

其参数为：

**`mp`** 挂载点。

**`ino`** 表示该文件的 inode。这是文件系统在首次创建 vnode 时分配的唯一编号。

**`flags`** 传递给 [vget(9)](vget.9.md) 的附加锁定标志。

**`vpp`** vnode 的返回参数。

这是一个可选的文件系统入口点，主要供 NFS 服务器使用，但许多文件系统在 [VOP_LOOKUP(9)](vop_lookup.9.md) 及类似函数中内部使用它。

如果文件系统不支持此调用，则应返回 `EOPNOTSUPP`。

关于规范示例，请参见 **sys/ufs/ffs/ffs_vfsops.c** 中的 `ffs_vget`。

## 参见

[VFS(9)](vfs.9.md), [vget(9)](vget.9.md), [vnode(9)](vnode.9.md)

## 作者

本手册页由 Doug Rabson 编写。
