# deadfs.9

`deadfs` — 拥有已回收 vnode 的伪文件系统

## 名称

`deadfs`

## 描述

`deadfs` 文件系统实现的操作不修改任何数据，而是返回指示无效 IO 的信号。其作用是为已回收的 [vnode(9)](vnode.9.md) 提供一个回退的 vnode 操作向量。

它是一个仅内核的伪文件系统，因此无法从用户态挂载。

## 参见

[insmntque(9)](insmntque.9.md), [vnode(9)](vnode.9.md), VOP_RECLAIM(9)

## 历史

4.4BSD 的 UNIX 系统管理员手册（SMM）将 `deadfs` 描述为"被拒绝的 vnode 去死亡"的文件系统。

## 作者

`deadfs` 手册页由 Mateusz Piotrowski <0mp@FreeBSD.org> 编写。
