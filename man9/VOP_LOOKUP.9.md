# VOP_LOOKUP.9

`VOP_LOOKUP` — 查找路径名的组成部分

## 名称

`VOP_LOOKUP`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
#include <sys/namei.h>
```

```c
int
VOP_LOOKUP(struct vnode *dvp, struct vnode **vpp,
    struct componentname *cnp)
```

## 描述

此入口点在给定目录中查找单个路径名组成部分。

参数如下：

**`dvp`** 要搜索的目录的已锁定 vnode。

**`vpp`** 用于存储结果的已锁定 vnode 的变量地址。

**`cnp`** 要搜索的路径名组成部分。它是指向 componentname 结构的指针，该结构定义如下：

```c
struct componentname {
	/*
	 * lookup 的参数。
	 */
	u_long	cn_nameiop;	/* namei 操作 */
	u_long	cn_flags;	/* namei 标志 */
	struct	thread *cn_thread;	/* 请求 lookup 的线程 */
	struct	ucred *cn_cred;	/* 凭证 */
	int     cn_lkflags;     /* 锁标志 LK_EXCLUSIVE 或 LK_SHARED */
	/*
	 * lookup 和 commit 例程之间共享。
	 */
	char	*cn_pnbuf;	/* 路径名缓冲区 */
	char	*cn_nameptr;	/* 指向所查找名称的指针 */
	long	cn_namelen;	/* 所查找组成部分的长度 */
};
```

将路径名的一个组成部分转换为指向已锁定 vnode 的指针。这是一个非常核心且相当复杂的例程。如果文件系统不是以严格的树形层次结构维护的，这可能导致死锁。

`cnp->cn_nameiop` 参数为 `LOOKUP`、`CREATE`、`RENAME` 或 `DELETE`，具体取决于对象的预期用途。当指定 `CREATE`、`RENAME` 或 `DELETE` 时，可以计算用于创建、重命名或删除目录条目的可用信息。

VOP_LOOKUP 的总体大纲：

> 检查目录的可访问性。
> 在缓存中查找名称，如果找到则返回名称。
> 在目录中搜索名称，根据情况跳转到 found 或 notfound。

notfound：

> 如果正在创建或重命名且处于路径名末尾，
> 返回
> `EJUSTRETURN`，
> 保留关于可用插槽的信息，否则返回
> `ENOENT`。

found：

> 如果处于路径末尾且正在删除，返回允许删除的信息。
> 如果处于路径末尾且正在重命名，锁定目标
> inode 并返回允许重命名的信息。
> 如果不在末尾，将名称添加到缓存；如果在末尾且既不创建
> 也不删除，将名称添加到缓存。

## 锁定

目录 `dvp` 应在进入和退出时保持锁定，无论错误条件如何。如果在目录中找到条目，它将以锁定状态返回。

## 返回值

如果找到组成部分，则返回零并将 `*vpp` 设置为该文件的已锁定 vnode。如果正在搜索的组成部分是“.”，则只是为该 vnode 增加一个额外的引用，通过 [vref(9)](vref.9.md)。在这种情况下，调用者必须注意适当地释放锁。

如果未找到组成部分且操作为 `CREATE` 或 `RENAME`，且指定了 `ISLASTCN` 标志且操作会成功，则返回特殊返回值 `EJUSTRETURN`。否则，返回适当的错误代码。

## 错误

[`ENOTDIR`] vnode `dvp` 不代表一个目录。

[`ENOENT`] 在此目录中未找到组成部分 `dvp`。

[`EACCES`] 拒绝指定操作的访问权限。

[`EJUSTRETURN`] `CREATE` 或 `RENAME` 操作将会成功。

## 参见

[vnode(9)](vnode.9.md), [VOP_ACCESS(9)](VOP_ACCESS.9.md), [VOP_CREATE(9)](VOP_CREATE.9.md), VOP_MKDIR(9), VOP_MKNOD(9), [VOP_RENAME(9)](VOP_RENAME.9.md), VOP_SYMLINK(9)

## 历史

`VOP_LOOKUP` 函数出现在 4.3BSD 中。

## 作者

本手册页面由 Doug Rabson 编写，其中部分文字来自 `ufs_lookup.c` 中的注释。
