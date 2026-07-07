# VOP_SETLABEL(9)

`VOP_SETLABEL` — 在 vnode 上持久存储更新的 MAC 标签

## 名称

`VOP_SETLABEL`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
#include <security/mac.h>
```

```c
int
VOP_SETLABEL(struct vnode *vp, label *label)
```

## 描述

此 vnode 调用由 [mac(9)](mac.9.md) 在文件重新标记操作已被授权后调用，此时必须更新文件系统。

### 单标签与多标签文件系统

不实现每文件标签的文件系统（即单标签文件系统）可以直接不定义 [vnode(9)](vnode.9.md) 操作。这些文件系统不得在其 `struct mount` 中设置 `MNT_MULTLABEL` 标志。

实现每 vnode 标签存储的文件系统（即多标签文件系统）将在其 `struct mount` 中设置 `MNT_MULTILABEL` 标志。UFS 文件系统使用超级块标志来持久配置特定文件系统是否为每个 [vnode(9)](vnode.9.md) 实现标签，然后根据该标志是否设置来控制各种行为。

### 扩展属性

如果文件系统实现了扩展属性，则可以使用 MAC 框架的 `vop_stdsetlabel_ea` 函数，该函数将操作映射为一系列 VOP_OPENEXTATTR(9)、VOP_WRITEEXTATTR(9) 和 VOP_CLOSEEXTATTR(9)。

文件系统还需要在创建新文件系统对象时调用 `mac_vnode_create_extattr`，以便写出合适的扩展属性；并在 [vnode(9)](vnode.9.md) 首次与文件系统对象关联时调用 `mac_vnode_associate_extattr`。这些实用函数会根据需要使用 VOP_OPENEXTATTR(9)、VOP_READEXTATTR(9)、VOP_WRITEEXTATTR(9) 和 VOP_CLOSEEXTATTR(9)。

### 锁定与崩溃安全性

在所有情况下，重要的是持有独占的 [vnode(9)](vnode.9.md) 锁以防止在 MAC 标签可能尚未初始化时的并发访问。同样重要的是，操作的顺序应确保系统崩溃不会导致文件标记不正确。例如，新创建文件的扩展属性必须在文件被其父目录链接之前写入磁盘，以确保不会因崩溃而导致文件未标记。

## 锁定

vnode 在进入时将被锁定，并在返回时应保持锁定状态。

## 返回值

如果 MAC 标签成功设置，则返回零。否则，返回适当的错误代码。

## 错误

[`EOPNOTSUPP`] 文件系统不支持 `VOP_SETLABEL`。

[`ENOSPC`] 文件系统空间不足。

[`EROFS`] 文件系统是只读的。

根据 `VOP_SETLABEL` 的底层实现，其他错误也可能发生。

## 参见

[mac(9)](mac.9.md), mount(9), [vnode(9)](vnode.9.md), VOP_CLOSEEXTATTR(9), VOP_OPENEXTATTR(9), VOP_READEXTATTR(9), VOP_WRITEXTATTR(9)

## 作者

本手册页面由 Robert Watson 编写。
