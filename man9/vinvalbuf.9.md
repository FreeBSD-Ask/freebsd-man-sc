# vinvalbuf.9

`vinvalbuf` — 刷新并失效与 vnode 关联的所有缓冲区

## 名称

`vinvalbuf`

## 概要

`#include <sys/param.h>`

`#include <sys/vnode.h>`

`int vinvalbuf(struct vnode *vp, int flags, struct ucred *cred, int slpflag, int slptimeo)`

## 描述

`vinvalbuf()` 函数失效与给定 vnode 关联的所有缓冲区。这包括干净列表和脏列表上的缓冲区。如果指定了 `V_SAVE` 标志，则脏列表上的缓冲区在释放之前先同步。如果 vnode 关联有 VM 对象，则将其移除。

其参数如下：

**`vp`** 指向将失效其缓冲区的 vnode 的指针。

**`flags`** 唯一支持的标志是 `V_SAVE`，表示脏缓冲区应与磁盘同步。

**`cred`** 如果设置了 `V_SAVE`，用于 [VOP_FSYNC(9)](VOP_FSYNC.9.md) 缓冲区的用户凭证。

**`slpflag`** 用于函数中任何睡眠优先级的 slp 标志。

**`slptimeo`** 函数中任何睡眠的超时时间。

## 锁

调用前假定 vnode 已被锁定，返回时保持锁定。

调用前必须持有 `Giant`，返回时保持锁定。

## 返回值

成功时返回 0。

## 伪代码

```c
vn_lock(devvp, LK_EXCLUSIVE | LK_RETRY);
error = vinvalbuf(devvp, V_SAVE, cred, 0, 0);
VOP_UNLOCK(devvp, 0);
if (error)
	return (error);
```

## 错误

**[`ENOSPC`]** 文件系统已满。（使用 `V_SAVE`）

**[`EDQUOT`]** 磁盘配额超限。（使用 `V_SAVE`）

**[`EWOULDBLOCK`]** 睡眠操作超时。（参见 `slptimeo`）

**[`ERESTART`]** 需要传递信号，应重启系统调用。（在 `slpflag` 中设置 `PCATCH`）

**[`EINTR`]** 系统被信号中断。（在 `slpflag` 中设置 `PCATCH`）

## 参见

tsleep(9), [VOP_FSYNC(9)](VOP_FSYNC.9.md)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
