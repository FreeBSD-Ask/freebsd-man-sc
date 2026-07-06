# VOP_ADVLOCK.9

`VOP_ADVLOCK` — 建议性记录锁定

## 名称

`VOP_ADVLOCK`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
#include <sys/fcntl.h>
#include <sys/lockf.h>

int
VOP_ADVLOCK(struct vnode *vp, caddr_t id, int op, struct flock *fl,
    int flags)
```

## 描述

参数为：

**`F_WAIT`** 等待直到获得锁。

**`F_FLOCK`** 对锁使用 [flock(2)](../man2/flock.2.md) 语义。

**`F_POSIX`** 对锁使用 POSIX 语义。

**`F_REMOTE`** 锁所有者是远程 NFS 客户端。

**`F_NOINTR`** 等待锁时屏蔽信号。

**`vp`** 正在被操作的 vnode。

**`id`** 正在更改锁的 id 令牌。

**`op`** 要执行的操作（参见 [fcntl(2)](../man2/fcntl.2.md)）。

**`fl`** 锁的描述。

**`flags`** 以下一个或多个：

此入口点操作文件上的建议性记录锁。大多数文件系统将此调用的工作委托给 `lf_advlock`。

## 返回值

成功时返回零，否则返回错误。

## 参见

[fcntl(2)](../man2/fcntl.2.md), [flock(2)](../man2/flock.2.md), [vnode(9)](vnode.9.md)

## 作者

本手册页由 Doug Rabson 编写。
