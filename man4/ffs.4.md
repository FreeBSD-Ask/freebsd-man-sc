# ffs.4

`ffs` — Berkeley 快速文件系统

## 名称

`ffs`, `ufs`

## 概要

`在内核配置文件中： options FFS options QUOTA options SOFTUPDATES options SUIDDIR options UFS_ACL options UFS_DIRHASH options UFS_EXTATTR options UFS_EXTATTR_AUTOSTART options UFS_GJOURNAL`

`在 fstab(5) 中：`

/dev/disk0a	/mnt ufs rw 1 1

## 描述

Berkeley 快速文件系统提供将文件系统数据存储到磁盘设备上的功能。`ufs` 多年来在速度和可靠性方面不断优化，是 FreeBSD 的默认文件系统。

### 配额

**`options QUOTA`** 此选项允许系统管理员按用户设置磁盘使用限制。配额只能在以 `quota` 选项挂载的文件系统上使用；参见 quota(1) 和 edquota(8)。

### 软更新

> `newfs` `-U` `fs`

> `tunefs` `-n` `enable` `fs`

> `newfs` `-j` `fs`

> `tunefs` `-j` `enable` `fs`

**`options SOFTUPDATES`** 软更新功能跟踪对磁盘的写入，并强制执行元数据更新依赖关系（例如更新空闲块映射），以确保文件系统保持一致。要创建启用软更新的新文件系统，使用 newfs(8) 命令：`fs` 可以是 [fstab(5)](../man5/fstab.5.md) 中列出的挂载点（例如 **/usr**），也可以是磁盘设备（例如 **/dev/da0a**）。可以通过 tunefs(8) 命令在*未挂载*的文件系统上启用软更新：软更新还可以添加日志功能，将 fsck_ffs(8) 在崩溃后清理文件系统所花费的时间从数分钟减少到数秒。日志存放在名为 `.sujournal` 的 inode 中，以循环日志的形式保存包含描述元数据操作记录的段。要创建同时启用软更新和软更新日志的新文件系统，使用以下命令：这会在带 `-U` 标志的 newfs(8) 命令之后运行 tunefs(8) 命令。可以通过 tunefs(8) 命令在*未挂载*的文件系统上启用软更新日志：当未启用软更新功能时，此标志会自动启用软更新功能。注意，如果在启用软更新日志之前已存在文件 `.sujournal`，则此 tunefs(8) 命令将失败。

### 文件属主继承

**`options SUIDDIR`** 用于包含 Microsoft Windows 和 Apple Macintosh 计算机在内的网络文件共享环境，此选项允许以 `suiddir` 选项挂载的文件系统上的文件继承其所在目录的属主，即“如果这是我的目录，那么其中的文件也必须是我的”。

### 访问控制列表

**`options UFS_ACL`** 访问控制列表允许将细粒度的自主访问控制信息与文件和目录关联。此选项需要 `UFS_EXTATTR` 选项的存在，并建议同时包含 `UFS_EXTATTR_AUTOSTART`，以便在挂载文件系统时原子地启用 ACL。

为启用 ACL 支持，必须在 `EXTATTR_NAMESPACE_SYSTEM` 命名空间中提供两个扩展属性：`posix1e.acl_access`（保存访问 ACL）和 `posix1e.acl_default`（保存目录的默认 ACL）。如果使用文件系统扩展属性，可以使用以下命令在每个文件系统根目录中为 ACL 分配空间并创建必要的 EA 后备文件。这些示例中使用根文件系统；详见扩展属性章节。

```sh
mkdir -p /.attribute/system
cd /.attribute/system
extattrctl initattr -p / 388 posix1e.acl_access
extattrctl initattr -p / 388 posix1e.acl_default
```

在下一次挂载根文件系统时，如果内核配置中包含 `UFS_EXTATTR_AUTOSTART`，这些属性将自动启动，ACL 也将被启用。

### 目录哈希

**`options UFS_DIRHASH`** 对目录实现基于哈希的查找方案，以加速对超大目录的访问。

### 扩展属性

**`options UFS_EXTATTR`** 扩展属性允许将额外的任意元数据与文件和目录关联，这些属性可以在用户态和内核中分配和检索；参见 extattrctl(8)。

**`options UFS_EXTATTR_AUTOSTART`** 如果定义了此选项，`tunefs` 将在挂载操作期间搜索文件系统根目录下的 `.attribute` 子目录。如果找到，将自动为该文件系统启动扩展属性支持。

### 基于 GEOM 的日志

> `gjournal` `da0`

> `newfs` `-J` `/dev/da0.journal`

> `mount` `-o` `async` `/dev/da0.journal` `/mnt`

> `gjournal` `da0`

> `tunefs` `-J` `enable` `/dev/da0.journal`

> `mount` `-o` `async` `/dev/da0.journal` `/mnt`

**`options UFS_GJOURNAL`** 实现 UFS 文件系统的块级日志，同时覆盖数据和元数据。要启用此功能，使用以下命令为块设备创建 gjournal(8) GEOM 提供程序：在此示例中，**/dev/da0** 用作目标块设备，并创建 **/dev/da0.journal**。然后使用带块级日志标志的 newfs(8) 创建新文件系统并挂载：`async` 选项并非必需，但建议使用以获得更好的性能，因为日志功能保证了 `async` 挂载的一致性。也可以在现有文件系统上启用块级日志。为此，使用 gjournal(8) 工具为底层块设备加标签，并使用 tunefs(8) 工具启用块级日志标志：

### sysctl 8 MIB

以下 [sysctl(8)](../man8/sysctl.8.md) MIB 用于 `mount`：

**`vfs.ffs.doasyncfree`** 在重新分配文件系统块以使其连续时，异步写出已修改的 inode 和间接块。（默认值：1）。

**`vfs.ffs.doreallocblks`** 启用对块进行重新排列以使其连续的支持。（默认值：1）。

**`vfs.ffs.prttimechgs`** 当发现 UFS1 文件系统的时间戳为未来时间并将其更改为当前时间时，打印控制台消息。（默认值：0）。

## 历史

`mount` 手册页首次出现于 FreeBSD 4.5。

## 参见

quota(1), acl(3), extattr(3), edquota(8), extattrctl(8), fsck_ffs(8), [sysctl(8)](../man8/sysctl.8.md), tunefs(8)

> M. McKusick, W. Joy, S. Leffler, R. Fabry, "A Fast File System for UNIX", *ACM Transactions on Computer Systems*, 3, 2, pp. 181-197, August 1984.

> M. McKusick, "Soft Updates: A Technique for Eliminating Most Synchronous Writes in the Fast Filesystem", *Proceedings of the Freenix Track at the 1999 Usenix Annual Technical Conference*, pp. 71-84, June 2000.

> M. McKusick, J. Roberson, "Journaled Soft-updates", *BSD Canada Conference 2010 (BSDCan)*, May 2010.
