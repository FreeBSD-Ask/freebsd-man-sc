# VOP_RENAME.9

`VOP_RENAME` — 重命名文件

## 名称

`VOP_RENAME`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>
```

```c
int
VOP_RENAME(struct vnode *fdvp, struct vnode *fvp,
    struct componentname *fcnp, struct vnode *tdvp,
    struct vnode *tvp, struct componentname *tcnp)
```

## 描述

此操作重命名文件，并可能更改其父目录。如果目标对象存在，将先将其删除。

参数如下：

**`fdvp`** 旧父目录的 vnode。

**`fvp`** 要重命名的文件的 vnode。

**`fcnp`** 文件当前名称的路径名信息。

**`tdvp`** 新父目录的 vnode。

**`tvp`** 目标文件的 vnode（如果存在）。

**`tcnp`** 文件新名称的路径名信息。

## 锁定

源目录和文件已解锁，但预期在进入时其引用计数已增加。VOP 例程预期在返回前对两者调用 [vrele(9)](vrele.9.md)。

目标目录和文件已锁定且引用计数已增加。VOP 例程预期在返回前对两者调用 vput(9)。

## 错误

[`EPERM`] 文件是不可变的。

[`EXDEV`] 不能在不同文件系统之间重命名文件。

[`EINVAL`] 试图重命名 `.` 或 `..`，或执行会破坏目录树结构的操作。

[`ENOTDIR`] 试图将目录重命名为文件，或反之。

[`ENOTEMPTY`] 试图删除一个非空目录。

## 参见

[vnode(9)](vnode.9.md)

## 作者

本手册页面由 Doug Rabson 编写。
