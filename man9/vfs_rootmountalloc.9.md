# vfs\_rootmountalloc.9

`vfs_rootmountalloc` — 分配根 `mount` 结构

## 名称

`vfs_rootmountalloc` `mount` 结构

## 概要

`#include <sys/param.h>`

`#include <sys/mount.h>`

`int vfs_rootmountalloc(char *fstypename, char *devname, struct mount **mpp)`

## 描述

`vfs_rootmountalloc()` 分配一个从与 `fstypename` 匹配的 `vfsconf` 类型初始化的 `mount` 结构。

## 返回值

成功时返回 0，`mpp` 指向新分配的 `mount` 结构。如果 `fstypename` 为 `NULL` 或无效，则返回 `ENODEV`。

## 参见

[vfsconf(9)](vfsconf.9.md)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
