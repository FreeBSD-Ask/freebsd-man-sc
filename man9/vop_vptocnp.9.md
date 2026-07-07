# VOP_VPTOCNP(9)

`VOP_VPTOCNP` — 将 vnode 转换为其组成部分名称

## 名称

`VOP_VPTOCNP`

## 概要

```c
#include <sys/param.h>
#include <sys/ucred.h>
#include <sys/vnode.h>
```

```c
int
VOP_VPTOCNP(struct vnode *vp, struct vnode **dvp, struct ucred *cred,
    char *buf, int *buflen)
```

## 描述

此操作将 vnode 转换为其组成部分名称，并将该名称写入由 `buf` 指定的缓冲区头部。

**`vp`** 要转换的 vnode。

**`dvp`** `vp` 的父目录的 vnode。

**`cred`** 调用者凭证。

**`buf`** 用于前缀组成部分名称的缓冲区。

**`buflen`** 缓冲区的剩余大小。

`VOP_VPTOCNP` 的默认实现会扫描 `vp` 的父目录，查找具有匹配文件号的 dirent。如果 `vp` 不是目录，则 `VOP_VPTOCNP` 返回 ENOENT。

## 锁定

vnode 应在进入时已锁定，并在退出时仍保持锁定。在成功退出时，父目录 vnode 将被解锁。但是，其使用计数会增加。

## 返回值

成功时返回零，否则返回错误代码。

## 错误

[`ENOMEM`] 缓冲区不足以容纳 vnode 的组成部分名称。

[`ENOENT`] 在文件系统上未找到该 vnode。

## 参见

[vnode(9)](vnode.9.md), [VOP_LOOKUP(9)](vop_lookup.9.md)

## 注释

此接口是正在进行的工作。

## 历史

`VOP_VPTOCNP` 函数出现在 FreeBSD 8.0 中。

## 作者

本手册页面由 Joe Marcus Clarke 编写。
