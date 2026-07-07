# VOP_INACTIVE(9)

`VOP_INACTIVE`, `VOP_RECLAIM` — 为 vnode 回收文件系统资源

## 名称

`VOP_INACTIVE`, `VOP_RECLAIM`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>

int
VOP_INACTIVE(struct vnode *vp, struct thread *td)

int
VOP_RECLAIM(struct vnode *vp, struct thread *td)
```

## 描述

参数如下：

**`vp`** 被回收的 vnode。

`VOP_INACTIVE` 通常在内核不再使用 vnode 时调用。但无法保证它一定会被调用，例如如果在无法在不睡眠的情况下将 vnode 锁升级为独占时最后一个引用被丢弃。这可能是因为引用计数达到零，也可能是因为文件系统在有打开文件时被强制卸载。它可用于在"打开但已删除"文件的最后一次关闭时回收空间。

`VOP_RECLAIM` 在 vnode 被重新用于不同文件系统时调用。应释放与 vnode 关联的任何文件系统特定资源。

## 锁

对于 `VOP_INACTIVE` 和 `VOP_RECLAIM`，`vp` 在入口处以独占方式锁定，在返回时必须保持独占锁定。

## 参见

[vnode(9)](vnode.9.md)

## 作者

本手册页由 Doug Rabson 编写。
