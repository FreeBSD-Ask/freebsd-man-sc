# VOP_GETEXTATTR.9

`VOP_GETEXTATTR` — 从 vnode 检索命名的扩展属性

## 名称

`VOP_GETEXTATTR`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
#include <sys/extattr.h>

int
VOP_GETEXTATTR(struct vnode *vp, int attrnamespace, const char *name,
    struct uio *uio, size_t *size, struct ucred *cred, struct thread *td)
```

## 描述

此 vnode 调用可用于从文件或目录检索特定的命名扩展属性。

其参数为：

**`vp`** 文件或目录的 vnode。

**`attrnamespace`** 指示属性名存在于哪个扩展属性命名空间的整数常量。

**`name`** 指向以 null 结尾的包含属性名的字符串的指针。

**`uio`** 要读取的数据的位置。

**`size`** 如果不为 `NULL`，则在返回时将包含读取所有属性数据所需的字节数。在大多数情况下，当 `size` 不为 `NULL` 时 `uio` 将为 `NULL`，反之亦然。

**`cred`** 用于授权请求的用户凭据。

**`td`** 请求扩展属性的线程。

`cred` 指针可以为 `NULL`，以指示在可能的情况下不执行访问控制检查。此 `cred` 设置可用于允许内核授权活动进程可能不被允许执行的扩展属性检索。

扩展属性语义可能因实现该调用的文件系统而异。关于扩展属性的更多信息，请参见 [extattr(9)](extattr.9.md)。

## 锁定

vnode 在入口时将被锁定，并在返回时应保持锁定状态。

## 返回值

成功时返回零，并且 uio 结构将被更新以反映读取的数据。否则，返回适当的错误代码。

## 错误

**[`ENOATTR`]** 请求的属性未为此 vnode 定义。

**[`EACCES`]** 调用者没有适当的权限。

**[`ENXIO`]** 对于指定的 vnode 和属性名，该请求在此文件系统中无效。

**[`ENOMEM`]** 没有足够的内存来满足请求。

**[`EFAULT`]** uio 结构引用了无效的用户空间地址。

**[`EINVAL`]** `name`、`namespace` 或 `uio` 参数无效。

**[`EOPNOTSUPP`]** 文件系统不支持 `VOP_GETEXTATTR`。

## 参见

[extattr(9)](extattr.9.md), [vnode(9)](vnode.9.md), [VOP_LISTEXTATTR(9)](vop_listextattr.9.md), [VOP_SETEXTATTR(9)](vop_setextattr.9.md)

## 缺陷

通过传入空字符串作为属性名，某些文件系统将返回目标 vnode 上请求命名空间中已定义名称的列表。这是一个糟糕的 API，将被显式的 VOP 替换。
