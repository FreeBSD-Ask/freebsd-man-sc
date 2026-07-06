# VOP_OPENCLOSE.9

`VOP_OPEN` — 打开或关闭文件

## 名称

`VOP_OPEN`, `VOP_CLOSE`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
```

```c
int
VOP_OPEN(struct vnode *vp, int mode, struct ucred *cred,
    struct thread *td, struct file *fp)

int
VOP_CLOSE(struct vnode *vp, int mode, struct ucred *cred,
    struct thread *td)
```

## 描述

`VOP_OPEN` 入口点在进程访问文件之前调用，`VOP_CLOSE` 入口点在进程完成文件使用后调用。

参数如下：

**`vp`** 文件的 vnode。

**`mode`** 调用进程所需的访问模式。

**`cred`** 调用者的凭证。

**`td`** 正在访问文件的线程。

**`fp`** 正在打开的文件。

指向文件 `fp` 的指针对于需要此类信息的文件系统非常有用，例如 fdescfs(5)。对于内核内部打开操作，使用 `NULL` 作为 `VOP_OPEN` 的 `fp` 参数。

访问模式是一组标志，包括 `FREAD`、`FWRITE`、`O_NONBLOCK`、`O_APPEND`。

传递给 `VOP_CLOSE` 的线程 `td` 可以为 `NULL`，如果对打开文件的最后一个引用是从内核上下文中释放的，例如在 `SCM_RIGHTS` 消息中包含文件引用的套接字缓冲区被销毁时。

## 锁定

`VOP_OPEN` 要求 `vp` 在进入时已锁定，并在返回时保持锁定状态。

`VOP_CLOSE` 要求至少有一个引用与 vnode 关联，且不关心 vnode 是否已锁定。锁和引用状态在返回时保持不变。注意，`vn_close` 需要一个未锁定但已引用的 vnode，并在返回前减少 vnode 的引用。

## 返回值

成功时返回零，否则返回错误代码。

## 参见

[vnode(9)](vnode.9.md), [VOP_LOOKUP(9)](vop_lookup.9.md)

## 作者

本手册页面由 Doug Rabson 编写。
