# VFS.9

`VFS` — 文件系统的内核接口

## 名称

`VFS`

## 描述

用于设置或查询文件系统设置或信息的调用。

未实现 VFS 操作的文件系统应使用 **`src/sys/kern/vfs_default.c`** 中适当的 `vfs_std` 函数，而不是实现空函数或转换为 `eopnotsupp`。

## 参见

[dtrace_vfs(4)](../man4/dtrace_vfs.4.md), [VFS_CHECKEXP(9)](VFS_CHECKEXP.9.md), [VFS_FHTOVP(9)](VFS_FHTOVP.9.md), [VFS_MOUNT(9)](VFS_MOUNT.9.md), [VFS_QUOTACTL(9)](VFS_QUOTACTL.9.md), [VFS_SET(9)](VFS_SET.9.md), [VFS_STATFS(9)](VFS_STATFS.9.md), [VFS_SYNC(9)](VFS_SYNC.9.md), [VFS_UNMOUNT(9)](VFS_UNMOUNT.9.md), [VFS_VGET(9)](VFS_VGET.9.md), [vnode(9)](vnode.9.md), [VOP_VPTOFH(9)](VOP_VPTOFH.9.md)

## 作者

本手册页由 Doug Rabson 编写。
