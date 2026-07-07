# VOP_DEALLOCATE(9)

`VOP_DEALLOCATE` — 将文件中的存储空间清零和/或释放

## 名称

`VOP_DEALLOCATE`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>

int
VOP_DEALLOCATE(struct vnode *vp, off_t *offset, off_t *len, int flags,
    int ioflag, struct ucred *cred)
```

## 描述

此 VOP 调用对文件中的偏移量范围清零/释放存储空间。它用于实现 [fspacectl(2)](../man2/fspacectl.2.md) 系统调用。

其参数为：

**`vp`** 文件的 vnode。

**`offset`** 文件中要释放存储空间的范围的起始位置。

**`len`** 文件中要释放存储空间的范围的长度。

**`flags`** 此调用的标志。目前应设置为 0。

**`ioflag`** 要给予文件系统的指令和提示。

**`cred`** 调用者的凭据。

`*offset` 和 `*len` 在返回时被更新以反映仍需清零/释放的范围部分。部分结果被视为成功操作。对于非部分成功完成，`*len` 被更新为值 0，并且 `*offset` 按文件末尾之前清零的字节数递增。

## 锁定

vnode 在入口时应被锁定，并在退出时仍将保持锁定状态。

## 返回值

如果调用成功则返回零，否则返回适当的错误代码。

## 错误

**[`EINVAL`]** 传递给此 VOP 调用的 `offset`、`len` 或 `flags` 参数无效。

**[`ENODEV`]** 此 VOP 调用不支持该 vnode 类型。

**[`ENOSPC`]** 文件系统已满。

**[`EPERM`]** 文件上设置了仅追加标志，但调用者试图在当前文件末尾之前清零。

## 参见

[vnode(9)](vnode.9.md)

## 作者

`VOP_DEALLOCATE` 和本手册页由 Ka Ho Ng <khng@FreeBSD.org> 编写，由 FreeBSD 基金会赞助。
