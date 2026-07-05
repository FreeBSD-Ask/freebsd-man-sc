# insmntque.9

`insmntque` — 将 vnode 与挂载关联

## 名称

`insmntque`, `insmntque1`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/vnode.h>
```

```c
int
insmntque(struct vnode *vp, struct mount *mp)

int
insmntque1(struct vnode *vp, struct mount *mp)
```

## 描述

`insmntque` 函数将一个 vnode 与一个挂载关联。这包括更新 vnode 的 `v_mount`，并将该 vnode 插入到挂载的 vnode 列表中。

间接挂载引用计数（以它所拥有的 vnode 数量维护）会因每个添加到挂载的 vnode 而递增，该引用由 [vgone(9)](vgone.9.md) 递减。

在插入 vnode 时持有挂载的互斥锁。该 vnode 必须被独占锁定。

失败时，`insmntque` 会将 vnode 的操作向量重置为 [deadfs(9)](deadfs.9.md) 的向量，清除 `v_data`，然后调用 [vgone(9)](vgone.9.md) 和 vput(9)。如果需要在 `insmntque` 失败后进行更复杂的清理工作，可以改用 `insmntque1` 函数。它在失败后不执行任何清理，将所有工作留给调用者。特别是，vnode 的操作向量 `v_op` 和 `v_data` 字段会保持不变。

## 返回值

`insmntque` 函数将始终返回 0，除非文件系统当前正在被卸载，在这种情况下它可能返回 `EBUSY`。此外，即使在文件系统正在被卸载时，也可以通过在 vnode 的 `v_flag` 中设置 `VV_FORCEINSMQ` 标志来强制 `insmntque` 将 vnode 插入到挂载的 vnode 列表中。

## 参见

[vgone(9)](vgone.9.md)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
