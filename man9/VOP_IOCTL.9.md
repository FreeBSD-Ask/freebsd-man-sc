# VOP_IOCTL.9

`VOP_IOCTL` — 设备特定控制

## 名称

`VOP_IOCTL`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
```

```c
int
VOP_IOCTL(struct vnode *vp, u_long command, caddr_t data, int fflag,
    struct ucred *cred, struct thread *td)
```

## 描述

以设备相关的方式操作文件。

参数如下：

**`vp`** 文件的 vnode（通常代表一个设备）。

**`command`** 要执行的设备特定操作。

**`data`** 用于指定操作的额外数据。

**`fflag`** 一些标志（???）。

**`cred`** 调用者的凭证。

**`td`** 调用线程。

大多数文件系统不实现此入口点。

## 锁定

文件在进入时不应被锁定。

## 返回值

成功时返回零，否则返回适当的错误代码。

如果 ioctl 未被识别或未处理，应返回 `ENOTTY`。

## 参见

[vnode(9)](vnode.9.md)

## 作者

本手册页面由 Doug Rabson 编写。
