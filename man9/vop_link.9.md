# VOP_LINK(9)

`VOP_LINK` — 为文件创建新名称

## 名称

`VOP_LINK`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
```

```c
int
VOP_LINK(struct vnode *dvp, struct vnode *vp, struct componentname *cnp)
```

## 描述

此操作在指定目录中为一个已存在的文件链接一个新名称。

参数如下：

**`dvp`** 目录的 vnode。

**`vp`** 要被链接的文件的 vnode。

**`cnp`** 文件的路径名信息。

退出时*不应*释放路径名信息，因为这是由调用者完成的。退出时也*不应*释放目录和文件的 vnode。

## 锁定

`VOP_LINK` 要求目录和文件的 vnode 在进入时已锁定，并在返回时保持锁定状态。

## 返回值

如果文件成功链接则返回零，否则返回错误。

## 错误

[`EMLINK`] 文件的链接数过多。

[`EPERM`] 文件是不可变的。

[`EXDEV`] 不能在不同文件系统之间创建硬链接。

## 参见

vn_lock(9), [vnode(9)](vnode.9.md)

## 作者

本手册页面最初由 Doug Rabson 编写。
