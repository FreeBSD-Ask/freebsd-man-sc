# vgone.9

`vgone` — 准备 vnode 以便重用

## 名称

`vgone`

## 概要

`#include <sys/param.h>`

`#include <sys/vnode.h>`

`void vgone(struct vnode *vp)`

## 描述

`vgone()` 函数准备销毁 vnode。准备工作包括清理所有文件系统特定数据以及从其挂载点 vnode 列表中移除。

如果 vnode 的 `v_usecount` 为零，且未设置其 `VIRF_DOOMED` 标志，则将其移至空闲列表头部，因为在大多数情况下该 vnode 即将被重用，或其文件系统正在被卸载。

`vgone()` 函数接受一个独占锁定的 vnode，并返回时保持该 vnode 独占锁定。

## 参见

[vnode(9)](vnode.9.md)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
