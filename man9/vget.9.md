# vget.9

`vget` — 从空闲列表获取 vnode

## 名称

`vget`

## 概要

`#include <sys/param.h>`

`#include <sys/vnode.h>`

`int vget(struct vnode *vp, int lockflag, struct thread *td)`

## 描述

从空闲列表获取 vnode 并递增其引用计数。

**`vp`** 要从空闲列表中移除的 vnode。

**`lockflag`** 如果非零，还将锁定该 vnode。

不使用时，vnode 保存在空闲列表上。这些 vnode 仍然引用有效文件，但可能随时被重用以引用新文件。通常，这些 vnode 也保存在系统的缓存中，如名称缓存。

当空闲列表上的 vnode 再次被使用时（例如，由于调用 [VOP_LOOKUP(9)](vop_lookup.9.md) 而在名称缓存中找到该 vnode），新使用者必须调用 `vget()` 以递增引用计数并将其从空闲列表中移除。

## 参见

[vnode(9)](vnode.9.md), vput(9), [vref(9)](vref.9.md), [vrele(9)](vrele.9.md)

## 作者

本手册页由 Doug Rabson 编写。
