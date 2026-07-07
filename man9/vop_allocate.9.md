# VOP_ALLOCATE(9)

`VOP_ALLOCATE` — 为文件分配存储空间

## 名称

`VOP_ALLOCATE`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>

int
VOP_ALLOCATE(struct vnode *vp, off_t *offset, off_t *len, int ioflag,
    struct ucred *cred)
```

## 描述

此调用为文件中一个偏移量范围分配存储空间。它用于实现 [posix_fallocate(2)](../sys/posix_fallocate.2.md) 系统调用。

其参数为：

**`vp`** 文件的 vnode。

**`offset`** 文件中要分配存储空间的范围的起始位置。

**`len`** 文件中要分配存储空间的范围的长度。

**`ioflag`** 要给予文件系统的指令和提示。

**`cred`** 调用者的凭据。

`offset` 和 `len` 参数在返回时被更新以反映仍需分配的范围部分。部分分配被视为成功操作。文件内容不会改变。

## 锁定

文件在入口时应被独占锁定，并在退出时仍将保持锁定状态。

## 返回值

如果调用成功则返回零，否则返回适当的错误代码。

## 错误

**[`EFBIG`]** 试图写入的文件超过了进程的文件大小限制或最大文件大小。

**[`ENOSPC`]** 文件系统已满。

**[`EPERM`]** 文件上设置了仅追加标志，但调用者试图在当前文件末尾之前写入。

## 参见

[vnode(9)](vnode.9.md), VOP_READ(9), VOP_WRITE(9)
