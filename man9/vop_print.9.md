# VOP_PRINT(9)

`VOP_PRINT` — 打印调试信息

## 名称

`VOP_PRINT`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
```

```c
int
VOP_PRINT(struct vnode *vp)
```

## 描述

参数如下：

**`vp`** 要打印的 vnode。

## 返回值

成功时返回零，否则返回错误。

## 参见

[vnode(9)](vnode.9.md)

## 作者

本手册页面由 Doug Rabson 编写。
