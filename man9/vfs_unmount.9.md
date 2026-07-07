# VFS_UNMOUNT(9)

`VFS_UNMOUNT` — 卸载文件系统

## 名称

`VFS_UNMOUNT`

## 概要

```c
#include <sys/param.h>
#include <sys/mount.h>
#include <sys/vnode.h>

int
VFS_UNMOUNT(struct mount *mp, int mntflags)
```

## 描述

`VFS_UNMOUNT` 宏卸载文件系统。

它期望的参数为：

**`MNT_FORCE`** 在卸载文件系统之前强制关闭已打开的文件。

**`mp`** 文件系统。

**`mntflags`** 卸载操作的标志位掩码。`VFS_UNMOUNT` 当前支持的标志为：

## 参见

[vflush(9)](vflush.9.md), [VFS(9)](vfs.9.md), [vnode(9)](vnode.9.md)

## 作者

本手册页由 Doug Rabson 编写。
