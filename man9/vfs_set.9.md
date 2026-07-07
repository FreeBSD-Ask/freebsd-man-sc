# VFS_SET(9)

`VFS_SET` — 设置可加载文件系统

## 名称

`VFS_SET`, `vfsconf`

## 概要

```c
#include <sys/param.h>
#include <sys/kernel.h>
#include <sys/module.h>
#include <sys/mount.h>

void
VFS_SET(struct vfsops *vfsops, fsname, int flags)
```

## 描述

`VFS_SET` 为具有给定 `vfsops`、`fsname` 和 `flags` 的可加载模块创建一个 `vfsconf` 结构，并通过使用 `vfs_modevent` 作为事件处理程序调用 [DECLARE_MODULE(9)](declare_module.9.md) 来声明它。

`flags` 参数的可能取值为：

**`VFCF_STATIC`** 文件系统应在内核中静态可用。

**`VFCF_NETWORK`** 可通过网络导出的文件系统。

**`VFCF_READONLY`** 不支持写操作。

**`VFCF_SYNTHETIC`** 伪文件系统，数据不代表磁盘上的文件。

**`VFCF_LOOPBACK`** 回环文件系统层。

**`VFCF_UNICODE`** 文件名以 Unicode 存储。

**`VFCF_JAIL`** 如果设置了 `allow.mount` 和 `allow.mount.<fsname>` jail 参数，则可以从 jail 内部挂载。

**`VFCF_DELEGADMIN`** 如果 `vfs.usermount` sysctl 设置为 `1`，则支持委托管理。

**`VFCF_SBDRY`** 在 VFS 方法中时，线程挂起在到达停止操作时推迟到用户边界。

## 伪代码

```c
/*
 * 填入我们有特殊方法的字段。
 * 其余字段初始为 null。这告诉 vfs 在文件系统注册期间
 * 将它们更改为指向 vfs_std* 函数的指针。
 */
static struct vfsops myfs_vfsops = {
        .vfs_mount =    myfs_mount,
        .vfs_root =     myfs_root,
        .vfs_statfs =   myfs_statfs,
        .vfs_unmount =  myfs_unmount,
};
VFS_SET(myfs_vfsops, myfs, 0);
```

## 参见

[jail(2)](../sys/jail.2.md), [jail(8)](../man8/jail.8.md), [DECLARE_MODULE(9)](declare_module.9.md), vfs_modevent(9), [vfsconf(9)](vfsconf.9.md)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
