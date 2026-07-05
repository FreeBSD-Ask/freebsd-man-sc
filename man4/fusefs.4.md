# fusefs.4

`fusefs` — 用户空间文件系统

## 名称

`fusefs`

## 概要

`链接进内核：`

> options FUSEFS

`作为可加载内核模块加载：`

```sh
kldload fusefs
```

## 描述

`fusefs` 驱动程序实现了由用户空间程序提供服务的文件系统。

`fusefs` 有许多用途。例如，用户空间守护进程可以访问无法在内核模式下运行的库或编程语言。`fusefs` 也适用于开发和调试文件系统，因为守护进程崩溃不会导致整个操作系统崩溃。最后，`fusefs` API 是可移植的。许多守护进程只需最少的修改即可在多个操作系统上运行。

## SYSCTL 变量

以下 [sysctl(8)](../man8/sysctl.8.md) 变量可用：

**`vfs.fusefs.kernelabi_major`** 本驱动程序支持的 FUSE 内核 ABI 主版本号。

**`vfs.fusefs.kernelabi_minor`** 本驱动程序支持的 FUSE 内核 ABI 次版本号。

**`vfs.fusefs.data_cache_mode`** 控制 `fusefs` 如何为 7.23 之前的文件系统缓存文件数据。值为 0 时完全禁用缓存。每次数据访问都将转发到守护进程。值为 1 时选择写穿缓存。读取将照常在 VFS 层缓存。写入将立即转发到守护进程，并同时添加到缓存。值为 2 时选择写回缓存。读取和写入都将被缓存，写入偶尔会由页面守护进程刷新到守护进程。写回缓存通常是不安全的，特别是对于需要网络访问的 FUSE 文件系统。使用 7.23 或更高版本协议的 FUSE 文件系统按每个挂载点指定其缓存行为，忽略此 sysctl。

**`vfs.fusefs.stats.filehandle_count`** 当前打开的 FUSE 文件句柄数量。

**`vfs.fusefs.stats.lookup_cache_hits`** 查找缓存命中总数。

**`vfs.fusefs.stats.lookup_cache_misses`** 查找缓存未命中总数。

**`vfs.fusefs.stats.node_count`** 当前已分配的 FUSE vnode 数量。

**`vfs.fusefs.stats.ticket_count`** 当前已分配的 FUSE 票据数量，大致等于守护进程当前正在处理的 FUSE 操作数量。

## 参见

mount_fusefs(8)

## 历史

`fuse` 驱动程序作为 FreeBSD 实现 FUSE 用户空间文件系统框架（参见 <https://github.com/libfuse/libfuse> ）的一部分编写，首次出现于 `sysutils/fusefs-kmod` port，支持 FreeBSD 6.0。在 FreeBSD 10.0 中被添加到基本系统，并在 FreeBSD 12.1 中重命名为 `fuse`。

## 作者

`fuse` 驱动程序最初由 Csaba Henk 在 2005 年作为 Google Summer of Code 项目编写。Ilya Putsikau 在 2011 年 Google Summer of Code 期间对其进行了进一步开发，该版本由 Attilio Rao <attilio@FreeBSD.org> 集成到基本系统中。

本手册页由 Alan Somers <asomers@FreeBSD.org> 编写。
