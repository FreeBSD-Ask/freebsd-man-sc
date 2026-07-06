# vn\_deallocate.9

`vn_deallocate` — 对文件中的存储进行清零和/或释放

## 名称

`vn_deallocate`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>

int
vn_deallocate(struct vnode *vp, off_t *offset, off_t *length,
    int flags, int ioflag, struct ucred *active_cred,
    struct ucred *file_cred)
```

## 描述

`vn_deallocate` 函数对文件中的支持存储空间进行清零和/或释放。此函数仅适用于 `VREG` 类型的 vnode。

参数如下：

**`vp`** 文件的 vnode。

**`offset`** 操作范围的起始偏移量。

**`length`** 操作范围的长度。这必须大于 0。

**`flags`** 操作的控制标志。目前应设置为 0。

**`ioflag`** 给文件系统的指令和提示。

**`active_cred`** 调用线程的用户凭证。

**`file_cred`** 安装在指向 vnode 的文件描述上的凭证或 NOCRED。

`ioflag` 参数向文件系统提供指令和提示。它可以包含以下一个或多个标志：

**`IO_NODELOCKED`** vnode 在调用前已被锁定。

**`IO_RANGELOCKED`** 调用周围拥有范围锁。

**`IO_NOMACCHECK`** 在调用中跳过 MAC 检查。

**`IO_SYNC`** 同步执行 I/O。

**`IO_DIRECT`** 尝试绕过缓冲区缓存。

`*offset` 和 `*length` 被更新以反映调用中未处理的操作范围。成功完成时，`*length` 更新为值 0，`*offset` 增加文件结尾之前清零的字节数。

## 返回值

成功完成时返回值 0；否则返回相应的错误。

## 参见

[vnode(9)](vnode.9.md), [VOP_DEALLOCATE(9)](VOP_DEALLOCATE.9.md)

## 作者

`vn_deallocate` 和本手册页由 Ka Ho Ng <khng@FreeBSD.org> 在 FreeBSD Foundation 赞助下编写。
