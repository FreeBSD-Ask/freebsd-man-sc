# vrefcnt(9)

`vrefcnt` — 返回 vnode 的使用计数

## 名称

`vrefcnt`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>

int
vrefcnt(struct vnode *vp)
```

## 描述

返回 vnode 的使用计数。

有关 vnode 引用计数的详细描述，请参见 [vnode(9)](vnode.9.md)。

## 参见

[vget(9)](vget.9.md), [vnode(9)](vnode.9.md), [vrele(9)](vrele.9.md)

## 作者

本手册页由 Chad David 编写。
