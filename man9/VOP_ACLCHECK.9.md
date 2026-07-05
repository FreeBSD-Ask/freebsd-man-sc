# VOP_ACLCHECK.9

`VOP_ACLCHECK` — 检查 vnode 的访问控制列表

## 名称

`VOP_ACLCHECK`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
#include <sys/acl.h>

int
VOP_ACLCHECK(struct vnode *vp, acl_type_t type, struct acl *aclp,
    struct ucred *cred, struct thread *td)
```

## 描述

此 vnode 调用可用于确定特定访问控制列表（ACL）对特定文件或目录的有效性。

其参数为：

**`vp`** 文件或目录的 vnode。

**`type`** 要检查的 ACL 类型。

**`aclp`** 指向 ACL 结构的指针，用于从中检索 ACL 数据。

**`cred`** 用于授权请求的用户凭据。

**`td`** 检查 ACL 的线程。

`cred` 指针可以为 NULL，以指示在可能的情况下不执行访问控制检查。此 cred 设置可用于允许内核授权活动进程可能不被允许执行的 ACL 验证。

vnode ACL 接口定义了文件和目录 ACL 接口的语法，而非语义。关于内核中 ACL 管理的更多信息，请参见 [acl(9)](acl.9.md)。

## 锁定

调用此 vnode 方法不需要任何锁，入口时持有的任何锁在退出时仍将持有。

## 返回值

如果 `aclp` 指针指向对象 `vp` 的类型为 `type` 的有效 ACL，则返回零。否则，返回适当的错误代码。

## 错误

**[`EINVAL`]** 传递的 ACL 类型对此 vnode 无效，或 ACL 数据无效。

**[`EACCES`]** 文件或目录的 ACL 不允许访问。

**[`ENOMEM`]** 没有足够的内存来满足请求。

**[`EOPNOTSUPP`]** 文件系统不支持 `VOP_ACLCHECK`。

## 参见

[acl(9)](acl.9.md), [vnode(9)](vnode.9.md), [VOP_GETACL(9)](VOP_GETACL.9.md), [VOP_SETACL(9)](VOP_SETACL.9.md)

## 作者

本手册页由 Robert Watson 编写。
