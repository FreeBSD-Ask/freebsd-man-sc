# VOP_PATHCONF(9)

`VOP_PATHCONF` — 返回 POSIX pathconf 信息

## 名称

`VOP_PATHCONF`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
#include <sys/unistd.h>
```

```c
int
VOP_PATHCONF(struct vnode *vp, int name, long *retval)
```

## 描述

参数如下：

**`vp`** 要获取相关信息的 vnode。

**`name`** 要返回的信息类型。

**`retval`** 返回信息的位置。

`name` 的值指定了应返回的内容：

**`_PC_LINK_MAX`** 文件的最大链接数。

**`_PC_NAME_MAX`** 文件名的最大字节数。

**`_PC_PATH_MAX`** 路径名的最大字节数。

**`_PC_PIPE_BUF`** 原子写入管道的最大字节数。

**`_PC_CHOWN_RESTRICTED`** 如果 chown(2) 系统调用需要适当的特权则返回 1，否则返回 0。

**`_PC_NO_TRUNC`** 如果文件名长度超过 `KERN_NAME_MAX` 时会被截断则返回 1。

## 锁定

vnode 在进入时将被锁定，并在返回时应保持锁定状态。

## 返回值

如果 `name` 被识别，则将 `*retval` 设置为指定值并返回零，否则返回 `EINVAL`。

## 参见

[pathconf(2)](../man2/pathconf.2.md), [vnode(9)](vnode.9.md)

## 作者

本手册页面由 Doug Rabson 编写。
