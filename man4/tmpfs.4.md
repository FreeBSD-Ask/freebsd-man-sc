# tmpfs.4

`tmpfs` — 内存文件系统

## 名称

`tmpfs`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> options TMPFS

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
tmpfs_load="YES"
```

## 描述

`tmpfs` 驱动实现内存中（或 `tmpfs`）文件系统。该文件系统将文件元数据和数据都存储在主内存中。这允许非常快速、低延迟地访问数据。数据是易失的。卸载或系统重启会使其失效。这些特性使该文件系统的挂载适合用作快速临时存储，如 **`/tmp`** 。

如果系统内存不足且配置了交换空间（参见 swapon(8)），系统可以将文件数据传输到交换空间，为其他需要释放内存。当前实现中，元数据（包括目录内容）从不换出。在规划挂载限制时请记住这一点，特别是当预期在 tmpfs 挂载上放置许多小文件时。

当对 tmpfs 挂载上的文件使用 mmap(2) 时，管理文件页面的交换 VM 对象用于实现映射并避免文件数据的双重拷贝。这种特性导致进程检查工具（如 procstat(1)）报告匿名内存映射而非文件映射。

## 选项

挂载 `tmpfs` 文件系统时，以下选项可用：

**`easize`** 设置扩展属性使用的最大内存大小（字节）。默认为 16 兆字节。

**`export`** 接受 `export` 选项以与 nfsv4(4) 兼容。此选项无效。

**`gid`** 设置文件系统根 inode 的组 ID。默认为挂载点的 GID。

**`inodes`** 设置文件系统可用的最大节点数。如果未指定，文件系统会根据文件系统大小选择合理的最大值，该大小可使用 `size` 选项限制。

**`maxfilesize`** 设置最大文件大小（字节）。默认为最大可能值。

**`mode`** 设置文件系统根 inode 的模式（八进制表示）。默认为挂载点的模式。

**`nomtime`** 禁用跟踪由对 `tmpfs` 文件支撑的共享映射区域的写入引起的 mtime 更新。此选项移除定期扫描，该扫描将读写映射页降级为只读以记录写入。

**`nonc`** 不使用 namecache 将名称解析为所创建挂载的文件。这节省了内存，但目前可能会损害大型机器上高度使用的挂载的可伸缩性。

**`nosymfollow`** 在挂载的文件系统上不遵循 symlink(7)。

**`pgread`** 为挂载启用 pgcache 读取。

**`size`** 设置总文件系统大小（字节），除非后缀 k、m、g、t 或 p 之一，分别表示字节、千字节、兆字节、千兆字节、太字节和拍字节。如果给出零（默认）或大于 SIZE_MAX - PAGE_SIZE 的值，将使用可用内存量（包括主内存和交换空间）。

**`uid`** 设置文件系统根 inode 的用户 ID。默认为挂载点的 UID。

**`union`** 参见 [mount(8)](../man8/mount.8.md)。

## SYSCTL 变量

以下 [sysctl(8)](../man8/sysctl.8.md) 变量可用：

**`vfs.tmpfs.memory_percent`** 在内核文件系统初始化时可用的内存加交换空间百分比，可供大小为 0 的文件系统使用。当使用的空间达到此数量时，无法创建新文件且无法扩展文件。默认为 95%。更改此值也会更改 `vfs.tmpfs.memory_reserved`。

**`vfs.tmpfs.memory_reserved`** 基于内存百分比当前保留的内存加交换空间量。最小值编译到系统中，默认为 4 MB。

## 实例

挂载 `tmpfs` 内存文件系统：

```sh
mount -t tmpfs tmpfs /tmp
```

通过 [fstab(5)](../man5/fstab.5.md) 配置 `tmpfs` 挂载：

```sh
tmpfs /tmp tmpfs rw 0 0
```

## 参见

procstat(1), mmap(2), nmount(2), unmount(2), [fstab(5)](../man5/fstab.5.md), mdmfs(8), [mount(8)](../man8/mount.8.md), swapinfo(8), swapon(8)

## 历史

`tmpfs` 驱动首次出现于 FreeBSD 7.0。

## 作者

`tmpfs` 内核实现由 Julio M. Merino Vidal <jmmv@NetBSD.org> 作为 Google Summer of Code 项目编写。

Rohit Jalan 等人将其从 NetBSD 移植到 FreeBSD。

本手册页由 Xin LI <delphij@FreeBSD.org> 编写。
