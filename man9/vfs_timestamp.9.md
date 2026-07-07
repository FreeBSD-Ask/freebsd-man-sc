# vfs_timestamp(9)

`vfs_timestamp` — 生成当前时间戳

## 名称

`vfs_timestamp`

## 概要

`#include <sys/param.h>`

`#include <sys/vnode.h>`

`void vfs_timestamp(struct timespec *tsp)`

## 描述

`vfs_timestamp()` 函数用当前时间填充 `tsp`。

精度基于 `vfs.timestamp_precision` sysctl 变量的值：

**0** 仅秒；纳秒为零。

**1** 秒和纳秒，精度在 1/HZ 以内。

**2** 秒和纳秒，截断为微秒。

**（>=3）** 秒和纳秒，最高精度。

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
