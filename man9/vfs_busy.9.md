# vfs_busy(9)

`vfs_busy` — 将挂载点标记为忙碌

## 名称

`vfs_busy`

## 概要

`#include <sys/param.h>`

`#include <sys/mount.h>`

`int vfs_busy(struct mount *mp, int flags)`

## 描述

`vfs_busy()` 函数通过递增挂载点的引用计数将其标记为忙碌。如果 `mp->mnt_kern_flag` 中设置了 `MNTK_UNMOUNT` 标志且未设置 `MBF_NOWAIT` 标志，它还通过在 `mp` 上睡眠来延迟卸载。

其参数如下：

**`MBF_NOWAIT`** 如果设置了 `MNTK_UNMOUNT` 则不睡眠。

**`MBF_MNTLSTLOCK`** 在关键路径中释放 mountlist_mtx。

**`mp`** 要标记为忙碌的挂载点。

**`flags`** 控制 `vfs_busy()` 行为方式的标志。

## 返回值

成功时返回 0。如果挂载点正在被卸载且指定了 MBF_NOWAIT 标志，则返回 `ENOENT`。

## 错误

**[`ENOENT`]** 挂载点正在被卸载（设置了 `MNTK_UNMOUNT`）。

## 参见

[vfs_unbusy(9)](vfs_unbusy.9.md)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
