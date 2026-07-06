# vfs\_getvfs.9

`vfs_getvfs` — 根据文件系统标识符返回挂载点

## 名称

`vfs_getvfs`

## 概要

`#include <sys/param.h>`

`#include <sys/mount.h>`

`struct mount * vfs_getvfs(fsid_t *fsid)`

## 描述

`vfs_getvfs()` 函数根据文件系统标识符返回该文件系统的挂载点结构。该文件系统 ID 应通过调用 [vfs_getnewfsid(9)](vfs_getnewfsid.9.md) 分配；否则将无法找到。

`vfs_getvfs()` 的主要使用者是 NFS，它使用 `fsid` 作为文件句柄的一部分，以确定给定 RPC 所属的文件系统。如果 `vfs_getvfs()` 未能找到与 `fsid` 相关的挂载点，则认为该文件系统已过期。

## 返回值

如果找到 `fsid`，则返回该 ID 对应的挂载点；否则返回 `NULL`。

## 伪代码

```c
if ((mp = vfs_getvfs(&fhp->fh_fsid)) == NULL) {
	error = ESTALE;
	goto out;
}
```

## 参见

[vfs_getnewfsid(9)](vfs_getnewfsid.9.md)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
