# VOP_LISTEXTATTR.9

`VOP_LISTEXTATTR` — 从 vnode 中检索命名扩展属性列表

## 名称

`VOP_LISTEXTATTR`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
#include <sys/extattr.h>
```

```c
int
VOP_LISTEXTATTR(struct vnode *vp, int attrnamespace, struct uio *uio,
    size_t *size, struct ucred *cred, struct thread *td)
```

## 描述

此 vnode 调用可用于从文件或目录的指定命名空间中检索命名扩展属性列表。

参数如下：

**`vp`** 文件或目录的 vnode。

**`attrnamespace`** 整数常量，指示属性名所在的扩展属性命名空间。

**`uio`** 要读取数据的位置。结果数据将是属性名列表。每个列表条目由一个包含属性名长度的单字节及其后的属性名组成。属性名不以 ASCII `NUL` 结尾。

**`size`** 如果不为 `NULL`，则在返回时将包含读取列表所需的字节数。在大多数情况下，当 `size` 不为 `NULL` 时 `uio` 将为 `NULL`，反之亦然。

**`cred`** 用于授权请求的用户凭证。

**`td`** 请求扩展属性的线程。

`cred` 指针可以为 `NULL`，表示如果可能的话不执行访问控制检查。此 `cred` 设置可用于允许内核授权当前进程可能无权执行的扩展属性检索。

扩展属性语义可能因实现该调用的文件系统而异。有关扩展属性的更多信息，请参见 [extattr(9)](extattr.9.md)。

## 锁定

vnode 在进入时将被锁定，并在返回时应保持锁定状态。

## 返回值

成功时返回零，并且 `uio` 结构将被更新以反映已读取的列表。否则，返回适当的错误代码。

## 错误

[`EACCES`] 调用者没有适当的权限。

[`ENXIO`] 对于指定的 vnode 和属性名，此请求在该文件系统中无效。

[`ENOMEM`] 没有足够的内存来满足请求。

[`EFAULT`] `uio` 结构引用了无效的用户空间地址。

[`EINVAL`] `namespace` 或 `uio` 参数无效。

[`EOPNOTSUPP`] 文件系统不支持 `VOP_LISTEXTATTR`。

## 参见

[extattr(9)](extattr.9.md), [vnode(9)](vnode.9.md), [VOP_GETEXTATTR(9)](vop_getextattr.9.md), [VOP_SETEXTATTR(9)](vop_setextattr.9.md)
