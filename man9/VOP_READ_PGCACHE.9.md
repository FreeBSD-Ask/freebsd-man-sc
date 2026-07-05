# VOP_READ_PGCACHE.9

`VOP_READ_PGCACHE` — 快速读取文件

## 名称

`VOP_READ_PGCACHE`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
#include <sys/uio.h>
```

```c
int
VOP_READ_PGCACHE(struct vnode *vp, struct uio *uio, int ioflag,
    struct ucred *cred)
```

## 描述

此入口点读取文件内容。其目的是从不需要昂贵操作或任何磁盘 I/O 的缓存中提供数据。例如，如果文件系统使用正常的 VM 页面缓存并维护 `v_object` 的生命周期，它可以使用 vn_read_from_obj(9) 辅助函数从驻留的 `vp->v_object` 页面返回数据。

文件系统通过在 `vp->v_irflag` 中设置 `VIRF_PGREAD` 标志来表示在特定 vnode 上支持 `VOP_READ_PGCACHE`。

该函数不需要满足整个请求；它也可以选择不提供任何数据。在这些情况下，`uio` 必须按已读数据量前进，`VOP_READ_PGCACHE` 应返回 `EJUSTRETURN`，VFS 将使用 VOP_READ(9) 处理读取操作的其余部分。

VFS 层为从 `VOP_READ_PGCACHE` 访问用户空间页面执行与 VOP_READ(9) 相同的死锁避免处理。

调用进入时 vnode 未锁定，返回时也不应锁定。对于需要 vnode 锁才能返回任何数据的文件系统，实现 `VOP_READ_PGCACHE`（并设置 `VIRF_PGREAD` 标志）没有意义，因为 VFS 会根据需要安排调用 VOP_READ(9)。

参数如下：

**`vp`** 文件的 vnode。

**`uio`** 要读取的数据位置。

**`ioflag`** 各种标志，列表见 VOP_READ(9)。

**`cred`** 调用者的凭证。

`VOP_READ_PGCACHE` 不处理非零的 `ioflag` 参数。

## 锁定

文件应在进入时已被引用，并在退出时仍保持引用。在调用周围应持有覆盖整个读取范围的范围锁。

## 返回值

当整个请求被满足且无法通过任何方式为其提供更多数据时，返回零表示成功。如果可以返回更多数据，但 `VOP_READ_PGCACHE` 无法提供，则必须返回 `EJUSTRETURN`。`uio` 记录应根据已完成的部分操作进行更新。

否则返回错误代码，与 VOP_READ(9) 相同。

## 参见

uiomove(9), [vnode(9)](vnode.9.md), [VOP_READ(9)](VOP_RDWR.9.md)
