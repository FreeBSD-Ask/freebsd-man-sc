# VOP_RDWR.9

`VOP_READ` — 读取或写入文件

## 名称

`VOP_READ`, `VOP_WRITE`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
#include <sys/uio.h>
```

```c
int
VOP_READ(struct vnode *vp, struct uio *uio, int ioflag,
    struct ucred *cred)

int
VOP_WRITE(struct vnode *vp, struct uio *uio, int ioflag,
    struct ucred *cred)
```

## 描述

这些入口点用于读取或写入文件内容。

参数如下：

**`vp`** 文件的 vnode。

**`uio`** 要读取或写入的数据位置。

**`ioflag`** 各种标志。

**`cnp`** 调用者的凭证。

`ioflag` 参数用于向文件系统提供指令和提示。当尝试读取时，高 16 位用于提供预读提示（以文件系统块为单位），文件系统应尝试预读。低 16 位是一个位掩码，可以包含以下标志：

**`IO_UNIT`** 以原子单位执行 I/O。

**`IO_APPEND`** 追加写入到末尾。

**`IO_SYNC`** 同步执行 I/O。

**`IO_NODELOCKED`** 底层节点已锁定。

**`IO_NDELAY`** 文件表中设置了 `FNDELAY` 标志。

**`IO_VMIO`** 数据已在 VMIO 空间中。

## 锁定

文件应在进入时已锁定，并在退出时仍保持锁定。在调用周围应持有覆盖整个 I/O 范围的范围锁。

## 返回值

成功时返回零，否则返回错误代码。

## 错误

[`EFBIG`] 试图写入的文件超过了进程的文件大小限制或最大文件大小。

[`ENOSPC`] 文件系统已满。

[`EPERM`] 文件设置了仅追加标志，但调用者试图在当前文件末尾之前写入。

## 参见

uiomove(9), [vnode(9)](vnode.9.md)

## 作者

本手册页面由 Doug Rabson 编写。
