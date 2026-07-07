# VOP_REMOVE(9)

`VOP_REMOVE` — 删除文件或目录

## 名称

`VOP_REMOVE`, `VOP_RMDIR`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
```

```c
int
VOP_REMOVE(struct vnode *dvp, struct vnode *vp,
    struct componentname *cnp)

int
VOP_RMDIR(struct vnode *dvp, struct vnode *vp,
    struct componentname *cnp)
```

## 描述

这些入口点分别用于删除文件和目录。

参数如下：

**`dvp`** 目录的 vnode。

**`vp`** 要删除的文件的 vnode。

**`cnp`** 文件的路径名信息。

## 锁定

`dvp` 和 `vp` 都应在进入时已锁定，并在返回时保持锁定。

## 返回值

成功时返回零，否则返回错误代码。

## 错误

[`EPERM`] 文件是不可变的。

[`ENOTEMPTY`] 试图删除一个非空目录。

## 参见

[vnode(9)](vnode.9.md), [VOP_LOOKUP(9)](vop_lookup.9.md)

## 作者

本手册页面由 Doug Rabson 编写。
