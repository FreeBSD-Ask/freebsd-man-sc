# VOP_CREATE.9

`VOP_CREATE` — 创建文件、套接字、fifo、设备、目录或符号链接

## 名称

`VOP_CREATE`, `VOP_MKNOD`, `VOP_MKDIR`, `VOP_SYMLINK`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
#include <sys/namei.h>

int
VOP_CREATE(struct vnode *dvp, struct vnode **vpp,
    struct componentname *cnp, struct vattr *vap)

int
VOP_MKNOD(struct vnode *dvp, struct vnode **vpp,
    struct componentname *cnp, struct vattr *vap)

int
VOP_MKDIR(struct vnode *dvp, struct vnode **vpp,
    struct componentname *cnp, struct vattr *vap)

int
VOP_SYMLINK(struct vnode *dvp, struct vnode **vpp,
    struct componentname *cnp, struct vattr *vap, const char *target)
```

## 描述

这些入口点在给定目录中创建新的文件、套接字、fifo、设备、目录或符号链接。

参数为：

**`dvp`** 目录的已锁定 vnode。

**`vpp`** 用于存储生成的已锁定 vnode 的变量地址。

**`cnp`** 创建的路径名组件。

**`vap`** 新对象应具有的创建属性。

**`target`** 符号链接目标的路径名。

当创建对象时，这些入口点在 [VOP_LOOKUP(9)](VOP_LOOKUP.9.md) 之后被调用。

## 锁定

目录 `dvp` 在入口时将被锁定，并且在返回时必须保持锁定。如果调用成功，新对象将以锁定状态返回。

## 返回值

如果成功，新对象的 vnode 将被放入 `*vpp` 并返回零。否则，返回适当的错误。

## 错误

**[`ENOSPC`]** 文件系统已满。

**[`EDQUOT`]** 将超过用户的文件系统空间或 inode 配额。

## 参见

[vnode(9)](vnode.9.md), [VOP_LOOKUP(9)](VOP_LOOKUP.9.md)

## 历史

`VOP_SYMLINK` 函数出现于 4.3BSD。

## 作者

本手册页由 Doug Rabson 编写。
