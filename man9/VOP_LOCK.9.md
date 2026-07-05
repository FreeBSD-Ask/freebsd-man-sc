# VOP_LOCK.9

`VOP_LOCK` — 序列化对 vnode 的访问

## 名称

`VOP_LOCK`, `VOP_UNLOCK`, `VOP_ISLOCKED`, `vn_lock`

## 概要

```c
#include <sys/param.h>
#include <sys/lock.h>
#include <sys/vnode.h>
```

```c
int
VOP_LOCK(struct vnode *vp, int flags)

int
VOP_UNLOCK(struct vnode *vp)

int
VOP_ISLOCKED(struct vnode *vp)

int
vn_lock(struct vnode *vp, int flags)
```

## 描述

这些调用用于序列化对文件系统的访问，例如防止两个写操作同时写入同一个文件。

参数如下：

**`LK_SHARED`** 共享锁。
**`LK_EXCLUSIVE`** 独占锁。
**`LK_UPGRADE`** 共享锁升级为独占锁。
**`LK_DOWNGRADE`** 独占锁降级为共享锁。
**`LK_RELEASE`** 释放任何类型的锁。
**`LK_DRAIN`** 等待所有锁活动结束。

**`LK_NOWAIT`** 不休眠等待锁。
**`LK_SLEEPFAIL`** 休眠后返回失败。
**`LK_CANRECURSE`** 允许递归独占锁。
**`LK_NOWITNESS`** 指示 [witness(4)](../man4/witness.4.md) 忽略此实例。

**`LK_INTERLOCK`** 当调用者已持有简单锁时指定（`VOP_LOCK` 在获取锁后会释放该简单锁）。
**`LK_RETRY`** 重试直到锁定。

**`vp`** 要锁定或解锁的 vnode。

**`flags`** 锁请求类型之一：锁类型可以与这些锁标志进行*或*运算：锁类型可以与这些控制标志进行*或*运算：内核代码应使用 `vn_lock` 来锁定 vnode，而不是直接调用 `VOP_LOCK`。`vn_lock` 也不接受线程作为参数，而是假定使用 curthread。

## 返回值

成功时返回零，否则返回错误。

## 参见

[vnode(9)](vnode.9.md)

## 作者

本手册页面由 Doug Rabson 编写。
