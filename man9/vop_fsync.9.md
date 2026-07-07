# VOP_FSYNC(9)

`VOP_FDATASYNC` — 刷新文件的文件系统缓冲区

## 名称

`VOP_FDATASYNC`, `VOP_FSYNC`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>

int
VOP_FDATASYNC(struct vnode *vp, struct thread *td)

int
VOP_FSYNC(struct vnode *vp, int waitfor, struct thread *td)
```

## 描述

`VOP_FSYNC` 确保文件在崩溃后可以恢复到其当前状态。这通常需要将文件的脏缓冲区、其 inode 以及可能的其他文件系统元数据刷新到持久介质。`VOP_FSYNC` 用于实现 [sync(2)](../sys/sync.2.md) 和 [fsync(2)](../sys/fsync.2.md) 系统调用。

其参数为：

**`MNT_WAIT`** 同步等待 I/O 完成。

**`MNT_NOWAIT`** 启动所有 I/O，但不等待其完成。

**`MNT_LAZY`** 推送并非由文件系统同步器写入的数据。

**`vp`** 文件的 vnode。

**`waitfor`** 函数是否应等待 I/O 完成。可能取值为：

**`td`** 调用线程。

`VOP_FDATASYNC` 类似，但不要求刷新文件的所有元数据。它只要求文件的数据在崩溃后可恢复。这意味着数据本身必须刷新到磁盘，以及一些元数据（如文件大小），但不一定包括其属性。`VOP_FDATASYNC` 应始终等待 I/O 完成，就像以 `MNT_WAIT` 调用一样。`VOP_FDATASYNC` 用于实现 [fdatasync(2)](../sys/fsync.2.md)。

## 锁定

vnode 在入口时应被独占锁定，并在返回时保持锁定状态。

## 返回值

如果调用成功则返回零，否则返回适当的错误代码。

## 错误

**[`ENOSPC`]** 文件系统已满。

**[`EDQUOT`]** 超出配额。

## 参见

[vnode(9)](vnode.9.md)

## 作者

本手册页由 Doug Rabson 编写。
