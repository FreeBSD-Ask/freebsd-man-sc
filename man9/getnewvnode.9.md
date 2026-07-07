# getnewvnode(9)

`getnewvnode` — 获取新 vnode

## 名称

`getnewvnode`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/vnode.h>
```

```c
#include <sys/mount.h>
```

```c
int
getnewvnode(const char *tag, struct mount *mp, struct vop_vector *vops,
    struct vnode **vpp)
```

## 描述

`getnewvnode` 函数初始化一个新 vnode，将 `vops` 中传递的 vnode 操作分配给它。

`getnewvnode` 的参数为：

**`tag`** 文件系统类型字符串。此字段仅应引用于调试或用户空间工具。

**`mp`** 要将新 vnode 添加到的挂载点。

**`vops`** 要分配给新 vnode 的 vnode 操作。

**`vpp`** 成功完成后指向新 vnode。

## 返回值

`getnewvnode` 成功时返回 0。

## 缺陷

它从不返回错误，要么成功要么无限阻塞。

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
