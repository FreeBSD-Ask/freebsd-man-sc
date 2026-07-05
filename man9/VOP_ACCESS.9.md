# VOP_ACCESS.9

`VOP_ACCESS` — 检查文件或 Unix 域套接字的访问权限

## 名称

`VOP_ACCESS`, `VOP_ACCESSX`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>

int
VOP_ACCESS(struct vnode *vp, accmode_t accmode, struct ucred *cred,
    struct thread *td)

int
VOP_ACCESSX(struct vnode *vp, accmode_t accmode, struct ucred *cred,
    struct thread *td)
```

## 描述

此入口点根据给定凭据检查文件的访问权限。

其参数为：

**`vp`** 要检查的文件的 vnode。

**`accmode`** 所需的访问类型。

**`cred`** 要检查的用户凭据。

**`td`** 正在检查的线程。

`accmode` 是一个掩码，可以包含 <sys/vnode.h> 中描述的标志，例如 `VREAD`、`VWRITE` 或 `VEXEC`。对于 `VOP_ACCESS`，`accmode` 中可以设置的标志只有 `VEXEC`、`VWRITE`、`VREAD`、`VADMIN` 和 `VAPPEND`。要检查其他标志，必须改用 `VOP_ACCESSX`。

## 锁定

vnode 在入口时将被锁定，并在返回时应保持锁定状态。

## 返回值

如果文件可以以指定方式访问，则返回零，否则返回适当的错误代码。

## 错误

**[`EPERM`]** 试图更改不可变文件。

**[`EACCES`]** 文件模式的权限位或 ACL 不允许请求的访问。

## 参见

[vaccess(9)](vaccess.9.md), [vaccess_acl_nfs4(9)](vaccess_acl_nfs4.9.md), [vaccess_acl_posix1e(9)](vaccess_acl_posix1e.9.md), [vnode(9)](vnode.9.md)

## 作者

本手册页由 Doug Rabson 编写。
