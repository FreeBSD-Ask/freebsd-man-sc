# vhold(9)

`vhold` — 获取/释放对 vnode 的持有

## 名称

`vhold`

## 概要

`#include <sys/param.h>`

`#include <sys/vnode.h>`

`void vhold(struct vnode *vp)`

`void vholdl(struct vnode *vp)`

`void vdrop(struct vnode *vp)`

`void vdropl(struct vnode *vp)`

## 描述

`vhold()` 和 `vholdl()` 函数递增给定 vnode 的 `v_holdcnt`。如果 vnode 已添加到空闲列表且仍被引用，则将其移除。

`vdrop()` 和 `vdropl()` 函数递减 vnode 的 `v_holdcnt`。如果在调用 `vdrop()` 或 `vdropl()` 之前持有计数小于或等于零，系统将 panic。如果 vnode 不再被引用，则将其释放。

`vhold()` 和 `vdrop()` 锁定 vnode 互斥锁，而 `vholdl()` 和 `vdropl()` 期望互斥锁已被持有。

## 参见

[vnode(9)](vnode.9.md)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
