# vref.9

`vref`, `vrefl` — 增加 vnode 的使用计数

## 名称

`vref`, `vrefl`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>

void
vref(struct vnode *vp)

void
vrefl(struct vnode *vp)
```

## 描述

增加 vnode 的 `v_usecount` 字段。

**`vp`** 要增加计数的 vnode。

每个 vnode 维护一个引用计数，表示系统中有多少部分在使用该 vnode。这使系统能够检测 vnode 何时不再被使用，并可以安全地回收用于不同文件。

系统中使用 vnode 的任何代码（例如在某个算法的操作期间或存储在数据结构中）都应调用 `vref` 或 `vrefl`。

`vref` 锁定 vnode 互锁，而 `vrefl` 预期互锁已被持有。

## 参见

[vget(9)](vget.9.md), [vnode(9)](vnode.9.md), [vrefcnt(9)](vrefcnt.9.md), [vrele(9)](vrele.9.md)

## 作者

本手册页由 Doug Rabson 编写。
