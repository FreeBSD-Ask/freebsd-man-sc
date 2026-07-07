# vflush(9)

`vflush` — 刷新挂载点的 vnode

## 名称

`vflush`

## 概要

`#include <sys/param.h>`

`#include <sys/vnode.h>`

`int vflush(struct mount *mp, int rootrefs, int flags, struct thread *td)`

## 描述

`vflush()` 函数移除 vnode 表中属于给定 `mount` 结构的所有 vnode。

其参数如下：

**`FORCECLOSE`** 如果设置，将强制关闭忙碌的 vnode。

**`SKIPSYSTEM`** 如果设置，将跳过设置了 `VV_SYSTEM` 标志的 vnode。

**`WRITECLOSE`** 如果设置，仅移除当前为写入而打开的常规文件。

**`mp`** 应移除其 vnode 的挂载点。

**`rootrefs`** 根 vnode 上预期的引用数。将在根 vnode 上调用 `rootrefs` 次 [vrele(9)](vrele.9.md)。

**`flags`** 指示如何处理 vnode 的标志。

**`td`** 调用线程。

## 返回值

如果刷新成功则返回 0；否则返回 `EBUSY`。

## 参见

[vgone(9)](vgone.9.md), [vrele(9)](vrele.9.md)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
