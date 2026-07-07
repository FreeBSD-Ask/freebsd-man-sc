# VOP_REVOKE(9)

`VOP_REVOKE` — 撤销对设备及其别名的访问

## 名称

`VOP_REVOKE`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
```

```c
int
VOP_REVOKE(struct vnode *vp, int flags)
```

## 描述

`VOP_REVOKE` 将以管理方式撤销对由 `vp` 指定的设备以及通过 make_dev_alias(9) 创建的任何别名的访问。打开这些设备的进程对此类设备的进一步文件操作通常会失败。`flags` 必须设置为 `REVOKEALL`，表示所有访问都将被撤销；任何其他值都是无效的。

## 锁定

`vp` 必须在进入时以独占方式锁定，并在返回时保持锁定状态。

## 参见

make_dev_alias(9), [vnode(9)](vnode.9.md)

## 作者

本手册页面由 Brian Fundakowski Feldman 编写。
