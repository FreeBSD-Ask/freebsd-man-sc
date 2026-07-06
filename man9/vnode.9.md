# vnode.9

`vnode` — 文件或目录的内部表示

## 名称

`vnode`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
```

## 描述

vnode 是 Unix 中所有文件活动的焦点。vnode 由 `struct vnode` 描述。每个活动文件、每个当前目录、每个被挂载的文件、文本文件和根目录都分配有一个唯一的 vnode。

每个 vnode 有三个引用计数：`v_usecount`、`v_holdcnt` 和 `v_writecount`。第一个是内核中使用此 vnode 的客户端数量。此计数由 [vref(9)](vref.9.md)、[vrele(9)](vrele.9.md) 和 `vput` 维护。第二个是内核中否决回收此 vnode 的客户端数量。此计数由 `vhold` 和 `vdrop` 维护。当 vnode 的 `v_usecount` 和 `v_holdcnt` 都达到零时，vnode 将被放入空闲列表，并可能被重新用于另一个文件（可能在另一个文件系统中）。从空闲列表的转换由 [getnewvnode(9)](getnewvnode.9.md) 处理。第三个是写入该文件的客户端数量计数。它由 [open(2)](../man2/open.2.md) 和 [close(2)](../man2/close.2.md) 系统调用维护。

任何返回 vnode 的调用（如 [vget(9)](vget.9.md)、[VOP_LOOKUP(9)](VOP_LOOKUP.9.md) 等）都会将 vnode 的 `v_usecount` 增加一。当调用者完成使用 vnode 时，应通过调用 [vrele(9)](vrele.9.md)（如果 vnode 被锁定则用 `vput`）释放此引用。

vnode 结构的其他常用成员包括：`v_id` 用于维护名称缓存的一致性，`v_mount` 指向拥有该 vnode 的文件系统，`v_type` 包含 vnode 表示的对象类型，`v_data` 供文件系统用于存储与 vnode 相关的文件系统特定数据。`v_op` 字段由 `VOP_*` 函数使用，以调用实现 vnode 功能的文件系统中的函数。

`VOP_*` 函数声明和定义由 **sys/tools/vnode_if.awk** 脚本从 **sys/kern/vnode_if.src** 生成。这些接口记录在各自的手册页中，如 [VOP_READ](VOP_READ.9.md) 和 [VOP_WRITE](VOP_WRITE.9.md)。

## VNODE 类型

**`VNON`** 无类型。

**`VREG`** 常规文件；可以有或没有 VM 对象支持。如果要确保获得支持对象，调用 `vnode_create_vobject`。

**`VDIR`** 目录。

**`VBLK`** 块设备；可以有或没有 VM 对象支持。如果要确保获得支持对象，调用 `vnode_create_vobject`。

**`VCHR`** 字符设备。

**`VLNK`** 符号链接。

**`VSOCK`** 套接字。建议性锁定在此上不起作用。

**`VFIFO`** FIFO（命名管道）。建议性锁定在此上不起作用。

**`VBAD`** 指示 vnode 已被回收。

## 实现说明

VFIFO 使用 **/sys/kern/sys_pipe.c** 中的 "struct fileops"。VSOCK 使用 **/sys/kern/sys_socket.c** 中的 "struct fileops"。其他所有类型使用 **/sys/kern/vfs_vnops.c** 中的。

VFIFO/VSOCK 代码（即使用 "struct fileops" 的原因）是 VFS 代码集成到内核中不完整的产物。

在持有 `vnode` 互锁时调用 [malloc(9)](malloc.9.md) 或 [free(9)](free.9.md) 会由于 VM 对象和 Vnode 的交织而导致 LOR（锁顺序反转）。

## 文件

**sys/kern/vnode_if.src** **sys/tools/vnode_if.awk** 的输入文件。

**sys/tools/vnode_if.awk** 生成 `VOP_*` 函数源代码的脚本。

## 参见

[malloc(9)](malloc.9.md), [VFS(9)](VFS.9.md), [VOP_LOOKUP(9)](VOP_LOOKUP.9.md), [VOP_INACTIVE(9)](VOP_INACTIVE.9.md), [VOP_LOCK(9)](VOP_LOCK.9.md), [VOP_READ(9)](VOP_READ.9.md), [VOP_WRITE(9)](VOP_WRITE.9.md)

## 作者

本手册页由 Doug Rabson 编写。
