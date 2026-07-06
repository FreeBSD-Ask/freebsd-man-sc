# VOP_SETEXTATTR.9

`VOP_SETEXTATTR` — 为 vnode 设置命名扩展属性

## 名称

`VOP_SETEXTATTR`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
#include <sys/extattr.h>
```

```c
int
VOP_SETEXTATTR(struct vnode *vp, int attrnamespace, const char *name,
    struct uio *uio, struct ucred *cred, struct thread *td)
```

## 描述

此 vnode 调用可用于为文件或目录设置特定的命名扩展属性。

参数如下：

**`vp`** 文件或目录的 vnode。

**`attrnamespace`** 整数常量，指示属性名所在的扩展属性命名空间。

**`name`** 指向以 null 结尾的字符串的指针，包含属性名。

**`uio`** 要读取或写入的数据位置。

**`cred`** 用于授权请求的用户凭证。

**`td`** 设置扩展属性的线程。

uio 结构的使用方式与 VOP_WRITE(9) 中同名参数类似。但是，由于扩展属性提供严格的“name=value”语义，非零偏移将被拒绝。

`uio` 指针可以为 `NULL`，表示应删除指定的扩展属性。

`cred` 指针可以为 `NULL`，表示如果可能的话不执行访问控制检查。此 `cred` 设置可用于允许内核授权当前进程可能无权执行的扩展属性更改。

扩展属性语义可能因实现该调用的文件系统而异。有关扩展属性的更多信息，请参见 [extattr(9)](extattr.9.md)。

## 锁定

vnode 在进入时将被锁定，并在返回时应保持锁定状态。

## 返回值

如果扩展属性成功设置，则返回零。否则，返回适当的错误代码。

## 错误

[`EACCES`] 调用者没有适当的权限。

[`ENXIO`] 对于指定的 vnode 和属性名，此请求在该文件系统中无效。

[`ENOMEM`] 没有足够的内存来满足请求。

[`EFAULT`] uio 结构引用了无效的用户空间地址。

[`EINVAL`] name、namespace 或 uio 参数无效。

[`EOPNOTSUPP`] 文件系统不支持 `VOP_SETEXTATTR`。

[`ENOSPC`] 文件系统空间不足。

[`EROFS`] 文件系统是只读的。

## 参见

[extattr(9)](extattr.9.md), [vnode(9)](vnode.9.md), [VOP_GETEXTATTR(9)](vop_getextattr.9.md), [VOP_LISTEXTATTR(9)](vop_listextattr.9.md)

## 作者

本手册页面由 Robert Watson 编写。
