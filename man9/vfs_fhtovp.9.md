# VFS_FHTOVP(9)

`VFS_FHTOVP` — 将 NFS 文件句柄转换为 vnode

## 名称

`VFS_FHTOVP`

## 概要

```c
#include <sys/param.h>
#include <sys/mount.h>
#include <sys/vnode.h>

int
VFS_FHTOVP(struct mount *mp, struct fid *fhp, int flags, struct vnode **vpp)
```

## 描述

`VFS_FHTOVP` 宏由 NFS 服务器用来将 NFS 文件句柄转换为 vnode。

它所需的参数为：

**`mp`** 文件系统。

**`fhp`** 要转换的文件句柄。

**`flags`** 传递给 [vget(9)](vget.9.md) 的附加锁定标志。文件系统可以忽略 `flags` 并改用 `LK_EXCLUSIVE`。

**`vpp`** 返回新的已锁定 vnode 的返回参数。

文件句柄的内容由文件系统定义，不被系统的任何其他部分检查。它应包含足够的信息以唯一标识文件系统内的文件，并能注意到文件何时已被删除以及文件系统资源何时已被重用于新文件。例如，UFS 文件系统在其文件句柄中存储 inode 号和 inode 生成计数器。

调用 `VFS_FHTOVP` 之前通常应先调用 [VFS_CHECKEXP(9)](vfs_checkexp.9.md) 来检查客户端是否可访问该文件。

## 返回值

该文件的已锁定 vnode 将通过 `*vpp` 返回。

## 参见

[VFS(9)](vfs.9.md), [VFS_CHECKEXP(9)](vfs_checkexp.9.md), [vnode(9)](vnode.9.md), [VOP_VPTOFH(9)](vop_vptofh.9.md)

## 作者

本手册页由 Doug Rabson 编写。
