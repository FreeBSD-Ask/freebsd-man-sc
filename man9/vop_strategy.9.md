# VOP_STRATEGY(9)

`VOP_STRATEGY` — 读取或写入文件系统缓冲区

## 名称

`VOP_STRATEGY`

## 概要

```c
#include <sys/param.h>
#include <sys/buf.h>
#include <sys/vnode.h>
```

```c
int
VOP_STRATEGY(struct vnode *vp, struct buf *bp)
```

## 描述

参数如下：

**`vp`** 缓冲区对应的 vnode。

**`bp`** 要读取或写入的缓冲区。

此调用根据 `bp->b_iocmd` 的值从文件中读取或写入数据。

此调用可能会阻塞。

## 返回值

始终返回零。错误应通过在 `bp->b_ioflags` 中设置 `BIO_ERROR` 位并将 `bp->b_error` 设置为适当的 `errno` 值来表示。

## 参见

[errno(2)](../sys/intro.2.md), [buf(9)](buf.9.md), [vnode(9)](vnode.9.md)

## 作者

本手册页面由 Doug Rabson 编写。
