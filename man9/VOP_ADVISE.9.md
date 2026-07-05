# VOP_ADVISE.9

`VOP_ADVISE` — 应用关于文件数据使用的建议

## 名称

`VOP_ADVISE`

## 概要

```c
#include <sys/param.h>
#include <sys/vnode.h>

int
VOP_ADVISE(struct vnode *vp, off_t start, off_t end, int advice)
```

## 描述

此调用对文件数据的一个范围应用建议。它用于实现 [posix_fadvise(2)](../man2/posix_fadvise.2.md) 系统调用。

其参数为：

**`POSIX_FADV_WILLNEED`** 如果文件数据尚未驻留，则发起异步读取。

**`POSIX_FADV_DONTNEED`** 降低干净文件数据的内存优先级或丢弃干净文件数据。

**`vp`** 文件的 vnode。

**`start`** 文件数据范围的起始位置。

**`end`** 文件数据范围的结束位置。值为 `OFF_MAX` 表示建议将应用直到文件末尾。

**`advice`** 要应用于文件数据的操作类型。可能取值为：

如果 `start` 和 `end` 偏移量都为零，则操作应应用于整个文件。请注意，此调用仅为建议性质，并且可以在请求范围的子集上执行请求的操作（包括完全不执行），仍然返回成功。

## 锁定

文件在入口时应处于未锁定状态。

## 返回值

如果调用成功则返回零，否则返回适当的错误代码。

## 错误

**[`EINVAL`]** 为 `advice` 给出了无效值。

## 参见

[vnode(9)](vnode.9.md)
