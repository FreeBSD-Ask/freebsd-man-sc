# VOP_COPY_FILE_RANGE.9

`VOP_COPY_FILE_RANGE` — 在单个文件系统内或多个文件系统之间复制文件内或文件之间的字节范围

## 名称

`VOP_COPY_FILE_RANGE`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>

int
VOP_COPY_FILE_RANGE(struct vnode *invp, off_t *inoff,
    struct vnode *outvp, off_t *outoff, size_t *len, unsigned int flags,
    struct ucred *incred, struct ucred *outcred, struct thread *fsize_td)
```

## 描述

此入口点在单个文件系统中从一个常规文件复制字节范围到另一个文件，或在同一文件内复制。`invp` 和 `outvp` 可以引用同一文件。对于这种情况，由 `*inoff`、`*outoff` 和 `*len` 定义的字节范围不会重叠。

参数为：

**`invp`** 输入文件的 vnode。

**`inoff`** 指向输入文件偏移量的指针。

**`outvp`** 输出文件的 vnode。

**`outoff`** 指向输出文件偏移量的指针。

**`len`** 指向复制字节计数的指针。

**`flags`** 标志，目前应设置为 0。

**`incred`** 用于读取 `invp` 的凭据。

**`outcred`** 用于写入 `outvp` 的凭据。

**`fsize_td`** 要传递给 vn_rlimit_fsize() 的线程指针。对于没有限制的服务器线程（如 NFS 服务器），此值为 `NULL`，否则为 `curthread`。

在入口和返回时，`inoff` 和 `outoff` 参数指向文件偏移量的位置。这些文件偏移量应根据复制的字节数更新。`len` 参数指向存储要复制的字节数的位置。成功返回时，`len` 将被更新为实际复制的字节数。通常，这将等于请求复制的字节数，但是允许复制少于请求的字节数。这不一定表示复制已到达输入文件的 EOF。但是，如果成功返回时 `len` 参数指向的值为零，则表示 `inoff` 指向的偏移量位于或超过输入文件的 EOF。

## 锁定

vnode 在入口时未锁定，在返回时必须未锁定。当此调用完成时，`invp` 和 `outvp` 的字节范围都应被范围锁定。

## 返回值

成功时返回零，否则返回错误代码。

## 错误

**[`EFBIG`]** 如果复制超过了进程的文件大小限制或 `invp` 和 `outvp` 所在文件系统的最大文件大小。

**[`EINTR`]** 在 VOP 调用完成之前信号中断了它。

**[`EIO`]** 读写文件时发生 I/O 错误。

**[`EINTEGRITY`]** 读写文件时检测到损坏的数据。

**[`ENOSPC`]** 文件系统已满。

## 参见

vn_rdwr(9), [vnode(9)](vnode.9.md)
