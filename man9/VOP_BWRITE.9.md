# VOP_BWRITE.9

`VOP_BWRITE` — 写入文件系统缓冲区

## 名称

`VOP_BWRITE`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>

int
VOP_BWRITE(struct vnode *vp, struct buf *bp)
```

## 描述

参数为：

**`vp`** 正在被写入的文件的 vnode。

**`bp`** 要写入的缓冲区。

## 返回值

成功时返回零，否则返回错误。

## 参见

[vnode(9)](vnode.9.md)

## 作者

本手册页由 Doug Rabson 编写。
