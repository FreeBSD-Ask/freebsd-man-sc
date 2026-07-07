# VOP_ATTRIB(9)

`VOP_GETATTR` — 获取和设置文件或目录的属性

## 名称

`VOP_GETATTR`, `VOP_SETATTR`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>

int
VOP_GETATTR(struct vnode *vp, flags, struct vattr *vap, struct ucred *cred)

int
VOP_SETATTR(struct vnode *vp, struct vattr *vap, struct ucred *cred)

int
VOP_STAT(struct vnode *vp, struct stat *sb, flags, struct ucred *active_cred,
    struct ucred *file_cred)
```

## 描述

这些入口点操作文件或目录的各种属性，包括文件权限、所有者、组、大小、访问时间和修改时间。

`VOP_STAT` 返回适合 [stat(2)](../man2/stat.2.md) 系统调用的格式的数据，默认实现为 `VOP_GETATTR` 的包装器。文件系统可能出于性能原因想要实现自己的变体。

对于 `VOP_GETATTR` 和 `VOP_SETATTR`，参数为：

**`vp`** 文件的 vnode。

**`vap`** 文件的属性。

**`cred`** 调用线程的用户凭据。

对于 `VOP_STAT`，参数为：

**`vp`** 文件的 vnode。

**`sb`** 文件的属性。

**`active_cred`** 调用线程的用户凭据。

**`file_cred`** 安装在指向 vnode 的文件描述上的凭据，或 NOCRED。

不被 `VOP_SETATTR` 修改的属性应设置为值 `VNOVAL`；可以使用 `VATTR_NULL` 清除所有值，并且通常应在设置特定值之前用于重置 `*vap` 的内容。

## 锁定

`VOP_GETATTR` 和 `VOP_STAT` 都期望 vnode 在入口时被锁定，并在返回时保持 vnode 锁定。锁类型可以是共享或独占的。

`VOP_SETATTR` 期望 vnode 在入口时被锁定，并在返回时保持 vnode 锁定。锁类型必须是独占的。

## 返回值

如果 `VOP_GETATTR` 能够通过 `*vap` 检索属性数据，则返回 0，否则返回适当的错误。如果属性成功更改，`VOP_SETATTR` 返回零，否则返回适当的错误。如果 `VOP_STAT` 能够检索属性数据 `*sb`，则返回 0，否则返回适当的错误。

## 错误

**[`EPERM`]** 文件是不可变的。

**[`EACCES`]** 调用者没有权限修改文件或目录属性。

**[`EROFS`]** 文件系统是只读的。

## 参见

[VFS(9)](vfs.9.md), [vnode(9)](vnode.9.md), [VOP_ACCESS(9)](vop_access.9.md)

## 作者

本手册页由 Doug Rabson 编写。
