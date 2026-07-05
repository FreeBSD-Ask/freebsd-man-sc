# VOP_BMAP.9

`VOP_BMAP` — 逻辑块号到物理块号的转换

## 名称

`VOP_BMAP`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>

int
VOP_BMAP(struct vnode *vp, daddr_t bn, struct bufobj **bop,
    daddr_t *bnp, int *runp, int *runb)
```

## 描述

此 vnode 调用用于查找文件系统底层设备上存储文件的给定逻辑块的物理块号。其参数为：

**`vp`** 文件的 vnode。

**`bn`** 由 `vp` 标识的文件内的逻辑块号。

**`bop`** 与文件系统底层设备关联的缓冲区对象的返回存储位置。

**`bnp`** 物理块号的返回存储位置。

**`runp`** 可以与请求块同时高效读取的后续逻辑块数量的返回存储位置。这通常是物理块连续分配的逻辑块数量。但是文件系统可以自由地按自己认为合适的方式定义"高效"。

**`runb`** 类似于 `runp`，但针对的是前导块而非后续块。

任何返回参数都可以为 `NULL`，以指示调用者不关心该信息。

## 锁定

vnode 在入口时将被锁定，并在返回时应保持锁定状态。

## 返回值

成功时返回零，否则返回错误代码。

## 参见

[vnode(9)](vnode.9.md)

## 历史

`bmap` 函数首次出现于 4.2BSD。

## 作者

本手册页由 Alan Somers 编写。
