# vfs_getnewfsid(9)

`vfs_getnewfsid` — 分配新的文件系统标识符

## 名称

`vfs_getnewfsid`

## 概要

`#include <sys/param.h>`

`#include <sys/mount.h>`

`void vfs_getnewfsid(struct mount *mp)`

## 描述

`vfs_getnewfsid()` 函数为给定的挂载点分配新的文件系统标识符。文件系统通常在其挂载例程中调用 `vfs_getnewfsid()` 以获取系统内的唯一 ID，稍后可通过诸如 [vfs_getvfs(9)](vfs_getvfs.9.md) 之类的调用唯一标识该文件系统。

实际的 `fsid` 由两个 32 位整数组成，存储在 `mp` 的 `statfs` 结构中。第一个整数在已挂载文件系统集合中唯一，而第二个整数保存文件系统类型。

```c
typedef	struct fsid {
	int32_t val[2];
} fsid_t;
```

## 伪代码

```c
xxx_mount(struct mount *mp, char *path, caddr_t data,
	struct nameidata *ndp, struct thread *td)
{
	...
	vfs_getnewfsid(mp);
	...
}
```

## 参见

[vfs_getvfs(9)](vfs_getvfs.9.md)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
