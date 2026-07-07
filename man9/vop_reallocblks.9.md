# VOP_REALLOCBLKS(9)

`VOP_REALLOCBLKS` — 重新排列文件中的块使其连续

## 名称

`VOP_REALLOCBLKS`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
```

```c
int
VOP_REALLOCBLKS(struct vnode *vp, struct cluster_save *buflist)
```

## 描述

参数如下：

**`vp`** 要操作的文件。

**`buflist`** 要重新排列的缓冲区列表。

这似乎是正在进行的工作的一部分。

## 返回值

成功时返回零，否则返回错误。

## 参见

[buf(9)](buf.9.md), [vnode(9)](vnode.9.md)

## 作者

本手册页面由 Doug Rabson 编写。
