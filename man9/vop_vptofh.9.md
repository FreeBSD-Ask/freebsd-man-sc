# VOP_VPTOFH(9)

`VOP_VPTOFH` — 将 vnode 转换为 NFS 文件句柄

## 名称

`VOP_VPTOFH`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
```

```c
int
VOP_VPTOFH(struct vnode *vp, struct fid *fhp)
```

## 描述

此操作由 NFS 服务器使用，用于创建一个不透明的文件句柄，该句柄唯一标识文件，并可供 NFS 客户端将来访问该文件时使用。

参数如下：

**`vp`** 要为其创建文件句柄的 vnode。

**`fhp`** 文件句柄的返回参数。

## 参见

[VFS(9)](vfs.9.md), [VFS_FHTOVP(9)](vfs_fhtovp.9.md), [vnode(9)](vnode.9.md)

## 作者

本手册页面由 Doug Rabson 编写。
