# vfs_mountedfrom(9)

`vfs_mountedfrom` — 设置挂载的来源名称

## 名称

`vfs_mountedfrom`

## 概要

`#include <sys/param.h>`

`#include <sys/mount.h>`

`void vfs_mountedfrom(struct mount *mp, const char *from)`

## 描述

`vfs_mountedfrom()` 函数设置挂载的来源名称。此值由 statfs(2) 用于填充 `f_mntfromname`。

在大多数情况下，`from` 是包含文件系统的设备，但对于伪文件系统，它可以是描述性名称，如 `devfs` 或 `procfs`。

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
