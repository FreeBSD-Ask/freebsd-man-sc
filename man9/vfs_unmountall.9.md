# vfs_unmountall(9)

`vfs_unmountall` — 卸载所有文件系统

## 名称

`vfs_unmountall`

## 概要

`#include <sys/param.h>`

`#include <sys/mount.h>`

`void vfs_unmountall(void)`

## 描述

`vfs_unmountall()` 函数仅在系统关闭时运行，按从最新到最旧的顺序卸载所有已挂载的文件系统，以避免处理依赖关系。

## 参见

boot(9)
