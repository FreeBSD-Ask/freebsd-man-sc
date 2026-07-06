# vrele.9

`vput`, `vrele`, `vunref` — 减少 vnode 的使用计数

## 名称

`vput`, `vrele`, `vunref`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>

void
vput(struct vnode *vp)

void
vrele(struct vnode *vp)

void
vunref(struct vnode *vp)
```

## 描述

减少 vnode 的 `v_usecount` 字段。

**`vp`** 要减少计数的 vnode。

`vrele` 函数接受未锁定的 vnode，返回时 vnode 未锁定。

`vput` 函数应接受锁定的 vnode 作为参数，函数返回后 vnode 被解锁。`vput` 在操作上等同于先调用 [VOP_UNLOCK(9)](vop_lock.9.md) 再调用 `vrele`，但开销更小。

`vunref` 函数接受锁定的 vnode 作为参数，返回时 vnode 保持锁定。

系统中通过使用计数表示使用 vnode 的任何代码都应调用列出的函数之一来减少使用计数。如果非 doomed vnode 的 `v_usecount` 字段达到零，则它将被停用并放入空闲列表。

`vrele` 函数可能会锁定 vnode。所有三个函数都可能睡眠。

vnode 的保持计数始终大于或等于使用计数。非强制卸载在挂载点拥有使用计数非零的 vnode 时失败，参见 [vflush(9)](vflush.9.md)。

## 参见

[vget(9)](vget.9.md), [vnode(9)](vnode.9.md), [vref(9)](vref.9.md), [vrefcnt(9)](vrefcnt.9.md)

## 作者

本手册页由 Doug Rabson 和 Konstantin Belousov 编写。
