# VOP_INOTIFY(9)

`VOP_INOTIFY` — vnode inotify 接口

## 名称

`VOP_INOTIFY`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
```

```c
int
VOP_INOTIFY(struct vnode *vp, struct vnode *dvp,
    struct componentname *cnp, int event, uint32_t cookie)

int
VOP_INOTIFY_ADD_WATCH(struct vnode *vp, struct inotify_softc *sc,
    uint32_t mask, uint32_t *wdp, struct thread *td)
```

## 描述

`VOP_INOTIFY` 操作用于通知 inotify(2) 子系统在 vnode 上发生的文件系统事件。`dvp` 和 `cnp` 参数是可选的，仅用于获取事件的文件名。如果省略这些参数，inotify 子系统将使用文件名缓存来查找 vnode 的名称，但这开销更大。

`VOP_INOTIFY_ADD_WATCH` 操作供 inotify 子系统内部使用，用于向 vnode 添加监视。

## 锁定

`VOP_INOTIFY` 操作不假定任何特定的 vnode 锁定状态。`VOP_INOTIFY_ADD_WATCH` 操作应在 vnode 已锁定时调用。

## 返回值

成功时返回零，否则返回错误代码。

## 参见

[inotify(2)](../man2/inotify.2.md), [vnode(9)](vnode.9.md)
