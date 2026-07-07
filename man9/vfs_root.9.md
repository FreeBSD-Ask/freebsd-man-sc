# VFS_ROOT(9)

`VFS_ROOT` — 返回文件系统的根 vnode

## 名称

`VFS_ROOT`

## 概要

```c
#include <sys/param.h>
#include <sys/mount.h>
#include <sys/vnode.h>

int
VFS_ROOT(struct mount *mp, int flags, struct vnode **vpp)
```

## 描述

返回文件系统根目录的已锁定 vnode。

其参数为：

**`mp`** 文件系统。

**`flags`** 锁类型。可以是 `LK_EXCLUSIVE` 或 `LK_SHARED`。文件系统可以自由忽略 `flags` 参数，转而获取独占锁。

**`vpp`** 根 vnode 的返回参数。

## 参见

[VFS(9)](vfs.9.md), [vnode(9)](vnode.9.md)

## 作者

本手册页由 Doug Rabson 编写。
