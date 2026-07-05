# VOP_SETACL.9

`VOP_SETACL` — 设置 vnode 的访问控制列表

## 名称

`VOP_SETACL`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
#include <sys/acl.h>
```

```c
int
VOP_SETACL(struct vnode *vp, acl_type_t type, struct acl *aclp,
    struct ucred *cred, struct thread *td)
```

## 描述

此 vnode 调用可用于设置文件或目录的访问控制列表（ACL）。

参数如下：

**`vp`** 文件或目录的 vnode。

**`type`** 要设置的 ACL 类型。

**`aclp`** 指向 ACL 结构的指针，用于从中检索 ACL 数据。

**`cred`** 用于授权请求的用户凭证。

**`td`** 设置 ACL 的线程。

`aclp` 指针可以为 `NULL`，表示应删除指定的 ACL。

`cred` 指针可以为 `NULL`，表示如果可能的话不执行访问控制检查。此 cred 设置可用于允许内核授权当前进程可能无权执行的 ACL 更改。

vnode ACL 接口定义了文件和目录 ACL 接口的语法而非语义。有关内核中 ACL 管理的更多信息，请参见 [acl(9)](acl.9.md)。

## 锁定

vnode 在进入时将被锁定，并在返回时应保持锁定状态。

## 返回值

如果 ACL 成功设置，则返回零。否则，返回适当的错误代码。

## 错误

[`EINVAL`] 传递的 ACL 类型对此 vnode 无效，或 ACL 数据无效。

[`EACCES`] 调用者没有适当的权限。

[`ENOMEM`] 没有足够的内存来满足请求。

[`EOPNOTSUPP`] 文件系统不支持 `VOP_SETACL`。

[`ENOSPC`] 文件系统空间不足。

[`EROFS`] 文件系统是只读的。

## 参见

[acl(9)](acl.9.md), [vnode(9)](vnode.9.md), [VOP_ACLCHECK(9)](VOP_ACLCHECK.9.md), [VOP_GETACL(9)](VOP_GETACL.9.md)

## 作者

本手册页面由 Robert Watson 编写。
