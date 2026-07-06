# vnode\_pager\_purge\_range.9

`vnode_pager_purge_range` — 使给定字节范围内的缓存内容失效

## 名称

`vnode_pager_purge_range`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_extern.h>

void
vnode_pager_purge_range(struct vnode *vp, vm_ooffset_t start,
    vm_ooffset_t end)
```

## 描述

`vnode_pager_purge_range` 使指定 vnode `vp` 中给定字节范围内的缓存内容失效。要清除的范围是 [`start`, `end`)。如果 `end` 参数值为零，受影响的范围从 `start` 开始一直持续到对象末尾。指定范围内的页面将从对象的队列中移除。如果 `start` 或 `end` 未对齐到页边界，页面中失效的部分将被清零。此函数仅清除受影响区域中的驻留页面，调用者需确保读取支持存储时返回零。

如果 vnode `vp` 没有分配 VM 对象，调用此函数的效果是无操作。

## 锁

vnode 在入口处必须被锁定，在出口处仍保持锁定。

## 参见

[vnode(9)](vnode.9.md)

## 历史

`vnode_pager_purge_range` 手册页首次出现在 FreeBSD 14 中。

## 作者

本手册页由 Ka Ho Ng <khng@FreeBSD.org> 编写。
