# VFS\_MOUNT.9

`VFS_MOUNT` — 挂载文件系统

## 名称

`VFS_MOUNT`

## 概要

```c
#include <sys/param.h>

#include <sys/mount.h>

#include <sys/vnode.h>

int
VFS_MOUNT(struct mount *mp)
```

## 描述

`VFS_MOUNT` 宏将文件系统挂载到系统命名空间中，或更新已挂载文件系统的属性。

其所需的参数如下：

**`mp`** 表示文件系统的结构。

`VFS_MOUNT` 宏既用于挂载新文件系统，也用于更改现有文件系统的属性。如果 `mp->mnt_flag` 中设置了 `MNT_UPDATE` 标志，则文件系统应根据 `mp->mnt_flag` 的值更新其内部状态。例如，这可用于将只读文件系统转换为读写文件系统。mountd(8) 也使用它来更新文件系统的 NFS 导出信息。

如果未指定 `MNT_UPDATE` 标志，则这是一个新挂载的文件系统。文件系统代码应分配并初始化表示该文件系统所需的任何私有数据（可使用 `mp->mnt_data` 字段存储此信息）。

## 参见

[VFS(9)](VFS.9.md), [vnode(9)](vnode.9.md)

## 作者

本手册页由 Doug Rabson 编写。
