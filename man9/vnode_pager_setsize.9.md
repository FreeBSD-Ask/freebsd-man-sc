# vnode_pager_setsize(9)

`vnode_pager_setsize` — 通知 VM 系统文件大小的更新

## 名称

`vnode_pager_setsize`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_extern.h>

void
vnode_pager_setsize(struct vnode *vp, vm_ooffset_t nsize)
```

## 描述

`vnode_pager_setsize` 让 VM 系统知道文件大小的变化，并用 `nsize` 更新 `vp` 中 vm 对象的对象大小和 vnode pager 大小。偏移量超过新对象大小的对象映射上的页错误将导致 `SIGBUS`。

如果文件大小缩小，旧 EOF 和新 EOF 之间的页面将从对象队列中移除。如果 `nsize` 参数指定的新 EOF 未对齐到页边界，则从 EOF 开始的部分页区域被清零并标记为无效（如果页面存在驻留）。

如果 vnode `vp` 没有分配 VM 对象，调用此函数的效果是无操作。

如果文件系统为 vnode 分配 vm 对象，则必须使用此函数在文件系统代码内实现截断。

## 锁

vnode 在入口处应以独占方式锁定，在出口处仍保持锁定。

## 参见

[vnode(9)](vnode.9.md)

## 历史

`vnode_pager_setsize` 手册页首次出现在 FreeBSD 14 中。

## 作者

本手册页由 Ka Ho Ng <khng@FreeBSD.org> 编写。
