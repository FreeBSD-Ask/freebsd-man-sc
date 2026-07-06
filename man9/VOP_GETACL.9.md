# VOP_GETACL.9

`VOP_GETACL` — 检索 vnode 的访问控制列表

## 名称

`VOP_GETACL`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
#include <sys/acl.h>

int
VOP_GETACL(struct vnode *vp, acl_type_t type, struct acl *aclp,
    struct ucred *cred, struct thread *td)
```

## 描述

此 vnode 调用可用于从文件或目录检索访问控制列表（ACL）。

其参数为：

**`vp`** 文件或目录的 vnode。

**`type`** 要检索的 ACL 类型。

**`aclp`** 指向用于接收 ACL 数据的 ACL 结构的指针。

**`cred`** 用于授权请求的用户凭据。

**`td`** 请求 ACL 的线程。

`cred` 指针可以为 `NULL`，以指示在可能的情况下不执行访问控制检查。此 cred 设置可用于允许内核授权活动进程可能不被允许执行的 ACL 检索。

vnode ACL 接口定义了文件和目录 ACL 接口的语法，而非语义。关于内核中 ACL 管理的更多信息，请参见 [acl(9)](acl.9.md)。

## 锁定

vnode 在入口时将被锁定，并在返回时应保持锁定状态。

## 返回值

如果 `aclp` 指针将指向有效的 ACL，则返回零。否则，返回适当的错误代码。

## 错误

**[`EINVAL`]** 传递的 ACL 类型对此 vnode 无效。

**[`EACCES`]** 调用者没有适当的权限。

**[`ENOMEM`]** 没有足够的内存来满足请求。

**[`EOPNOTSUPP`]** 文件系统不支持 `VOP_GETACL`。

## 参见

[acl(9)](acl.9.md), [vnode(9)](vnode.9.md), [VOP_ACLCHECK(9)](vop_aclcheck.9.md), [VOP_SETACL(9)](vop_setacl.9.md)

## 作者

本手册页由 Robert Watson 编写。
