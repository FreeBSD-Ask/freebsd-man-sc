# VFS_SYNC(9)

`VFS_SYNC` — 刷新未写入的数据

## 名称

`VFS_SYNC`

## 概要

```c
#include <sys/param.h>
#include <sys/mount.h>
#include <sys/vnode.h>

int
VFS_SYNC(struct mount *mp, int waitfor)
```

## 描述

`VFS_SYNC` 宏写出挂载为 `mp` 的文件系统中所有未写入的数据。

它期望的参数为：

**`MNT_WAIT`** 同步等待 I/O 完成

**`MNT_NOWAIT`** 启动所有 I/O，但不等待其完成

**`MNT_LAZY`** 推送并非由文件系统同步器写入的数据

**`mp`** 文件系统。

**`waitfor`** 函数是否应等待 I/O 完成。可能取值为：

`VFS_SYNC` 宏调用文件系统的 `vfs_sync` 方法，该方法通常会为文件系统中的所有 vnode 调用 [VOP_FSYNC(9)](vop_fsync.9.md)。

## 参见

[fsync(2)](../man2/fsync.2.md), [sync(2)](../man2/sync.2.md), [VFS(9)](vfs.9.md), [vnode(9)](vnode.9.md), [VOP_FSYNC(9)](vop_fsync.9.md)

## 作者

本手册页由 Doug Rabson 编写。
