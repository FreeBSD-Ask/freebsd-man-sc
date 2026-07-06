# vn\_isdisk.9

`vn_isdisk` — 检查 vnode 是否表示磁盘

## 名称

`vn_isdisk`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>

bool
vn_isdisk(struct vnode *vp)

bool
vn_isdisk_error(struct vnode *vp, int *errp)
```

## 描述

`vn_isdisk` 和 `vn_isdisk_error` 函数检查 `vp` 是否表示磁盘。要使 `vp` 成为磁盘，它必须是字符设备，`v_rdev` 必须有效，且 `cdevsw` 条目的 `flags` 必须设置了 `D_DISK`。

参数如下：

**`vp`** 要检查的 vnode。

**`errp`** 用于在调用失败时存储错误号的整数指针。

## 返回值

如果 vnode 表示磁盘，返回 true；否则返回 false 且 `errp` 将包含错误号。

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
