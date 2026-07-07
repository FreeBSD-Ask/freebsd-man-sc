# vfs_unbusy(9)

`vfs_unbusy` — 解除挂载点的忙碌状态

## 名称

`vfs_unbusy`

## 概要

`#include <sys/param.h>`

`#include <sys/mount.h>`

`void vfs_unbusy(struct mount *mp)`

## 描述

`vfs_unbusy()` 函数通过递减挂载点的引用计数来解除其忙碌状态。引用计数通常在此调用之前通过调用 [vfs_busy(9)](vfs_busy.9.md) 递增。

其参数如下：

**`mp`** 要解除忙碌状态的挂载点。

## 参见

[vfs_busy(9)](vfs_busy.9.md)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
