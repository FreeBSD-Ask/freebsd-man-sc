# VFS_STATFS(9)

`VFS_STATFS` — 返回文件系统状态

## 名称

`VFS_STATFS`

## 概要

```c
#include <sys/param.h>
#include <sys/mount.h>
#include <sys/vnode.h>

int
VFS_STATFS(struct mount *mp, struct statfs *sbp)
```

## 描述

`VFS_STATFS` 宏返回关于文件系统的各种信息，包括推荐的 I/O 大小、空闲空间、空闲 inode 等。

它期望的参数为：

```c
#include <sys/mount.h>
```

**`mp`** 文件系统。

**`sbp`** 一个 `statfs` 结构，关于文件系统的信息将被放入其中。

与文件系统相关的 `struct statfs` 字段如下：

**`f_type`** 文件系统类型。

**`f_flags`** 挂载导出标志的副本。

**`f_bsize`** 片段大小。

**`f_iosize`** 最佳传输块大小。

**`f_blocks`** 文件系统中数据块的总数。

**`f_bfree`** 文件系统中空闲块的数量。

**`f_bavail`** 非超级用户进程可用的空闲块数量。

**`f_files`** 文件系统中文件节点的总数。

**`f_ffree`** 非超级用户进程可用的空闲节点数量。

**`f_syncwrites`** 自文件系统挂载以来的同步写入次数。

**`f_asyncwrites`** 自文件系统挂载以来的异步写入次数。

**`f_syncreads`** 自文件系统挂载以来的同步读取次数。

**`f_asyncreads`** 自文件系统挂载以来的异步读取次数。

**`f_namemax`** 此文件系统的最大文件名长度。

**`f_owner`** 挂载文件系统的用户的用户 ID。

**`f_fsid`** 唯一的文件系统 ID。

**`f_fstypename`** 文件系统类型名；最多 `MFSNAMELEN` 字节的字符串。

**`f_mntfromname`** 文件系统的挂载源设备名；最多 `MNAMELEN` 字节的字符串。

**`f_mntonname`** 文件系统挂载到的目录名；最多 `MNAMELEN` 字节的字符串。

## 参见

[VFS(9)](vfs.9.md), [vnode(9)](vnode.9.md)

## 作者

本手册页由 Doug Rabson 编写。
