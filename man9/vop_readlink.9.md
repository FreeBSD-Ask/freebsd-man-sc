# VOP_READLINK.9

`VOP_READLINK` — 读取符号链接的目标

## 名称

`VOP_READLINK`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
#include <sys/uio.h>
```

```c
int
VOP_READLINK(struct vnode *vp, struct uio *uio, struct ucred *cred)
```

## 描述

读取符号链接的目标路径名。

**`vp`** 符号链接的 vnode。

**`uio`** 要读取或写入的数据位置。

**`cred`** 调用者的凭证。

## 锁定

vnode 应在进入时已锁定，并在退出时仍保持锁定。

## 返回值

成功时返回零，否则返回错误代码。

## 错误

[`EIO`] 读取符号链接内容时发生读取错误。

[`EINTEGRITY`] 读取符号链接内容时检测到损坏的数据。

## 参见

uiomove(9), [vnode(9)](vnode.9.md)

## 作者

本手册页面由 Doug Rabson 编写。
