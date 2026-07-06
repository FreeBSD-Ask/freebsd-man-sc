# VFS\_QUOTACTL.9

`VFS_QUOTACTL` — 操作文件系统配额

## 名称

`VFS_QUOTACTL`

## 概要

```c
#include <sys/param.h>

#include <sys/mount.h>

#include <sys/vnode.h>

int
VFS_QUOTACTL(struct mount *mp, int cmds, uid_t uid, void *arg,
    bool *mp_busy)
```

## 描述

实现文件系统配额。

`mp_busy` 参数是一个输入/输出参数。调用 `VFS_QUOTACTL` 时必须通过 [vfs_busy(9)](vfs_busy.9.md) 将 `mp` 标记为忙，并将 `*mp_busy` 设置为 true。文件系统的 `VFS_QUOTACTL` 实现随后可在执行配额文件 I/O 之前使用 [vfs_unbusy(9)](vfs_unbusy.9.md) 解忙 `mp`。在这种情况下，实现必须将 `*mp_busy` 设置为 false，以指示调用者在 `VFS_QUOTACTL` 完成时不得解忙 `mp`。

其余参数的描述参见 quotactl(2)。

## 参见

quotactl(2), [vnode(9)](vnode.9.md)

## 作者

本手册页由 Doug Rabson 编写。
