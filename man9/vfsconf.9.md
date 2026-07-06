# vfsconf.9

`vfsconf` — vfs 配置信息

## 名称

`vfsconf`

## 概要

`#include <sys/param.h>`

`#include <sys/mount.h>`

`int vfs_register(struct vfsconf *vfc)`

`int vfs_unregister(struct vfsconf *vfc)`

`int vfs_modevent(module_t mod, int type, void *data)`

## 描述

内核已知的每种文件系统类型都有一个 `vfsconf` 结构，其中包含创建该文件系统类型新挂载所需的信息。

```c
struct vfsconf {
	struct	vfsops *vfc_vfsops;	/* 文件系统操作向量 */
	char	vfc_name[MFSNAMELEN];	/* 文件系统类型名称 */
	int	vfc_typenum;		/* 历史文件系统类型编号 */
	int	vfc_refcount;		/* 该类型的挂载数量 */
	int	vfc_flags;		/* 永久标志 */
	struct	vfsconf *vfc_next;	/* 列表中的下一个 */
};
```

挂载新文件系统时，mount(2) 按名称查找 `vfsconf` 结构，如果尚未注册，则尝试为其加载内核模块。新挂载点的文件系统操作取自 `vfc_vfsops`，`mount` 结构中的 `mnt_vfc` 直接指向该文件系统类型的 `vfsconf` 结构。文件系统类型编号取自在 `vfs_register()` 中分配的 `vfc_typenum`，挂载标志取自 `vfc_flags` 的掩码。每次挂载给定类型的文件系统时，`vfc_refcount` 都会递增。

`vfs_register()` 接受一个新的 `vfsconf` 结构并将其添加到现有文件系统列表中。如果该类型尚未注册，则通过调用文件系统操作向量中的 `vfs_init()` 函数进行初始化。`vfs_register()` 还将此文件系统类型的任何 sysctl 节点的 oid 更新为与新分配的类型编号相同。

如果当前没有已挂载的实例，`vfs_unregister()` 将 `vfc` 从已注册文件系统类型列表中取消链接。如果文件系统初始化向量中定义了 `vfs_uninit()` 函数，则调用它。

`vfs_modevent()` 由 `VFS_SET` 注册，用于处理文件系统内核模块的加载和卸载。在 `MOD_LOAD` 的情况下，调用 `vfs_register()`。在 `MOD_UNLOAD` 的情况下，调用 `vfs_unregister()`。

## 返回值

`vfs_register()` 成功时返回 0；否则返回 `EEXIST`，表示该文件系统类型已注册。

`vfs_unregister()` 成功时返回 0。如果找不到与 `vfc` 中名称匹配的 `vfsconf` 条目，则返回 `EINVAL`。如果该文件系统类型的已挂载实例引用计数不为零，则返回 `EBUSY`。如果调用了 `vfs_uninit()`，其返回的任何错误都将由 `vfs_unregister()` 返回。

`vfs_modevent()` 返回调用 `vfs_register()` 或 `vfs_unregister()` 的结果（视情况而定）。

## 参见

mount(2), [vfs_rootmountalloc(9)](vfs_rootmountalloc.9.md), [VFS_SET(9)](VFS_SET.9.md)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
