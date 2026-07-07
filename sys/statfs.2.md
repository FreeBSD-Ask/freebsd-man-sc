# statfs(2)

`statfs` — 获取文件系统统计信息

## 名称

`statfs`

## 库

Lb libc

## 概要

`#include <sys/param.h>`

`#include <sys/mount.h>`

```c
int
statfs(const char *path, struct statfs *buf);

int
fstatfs(int fd, struct statfs *buf);
```

## 描述

`statfs()` 系统调用返回关于已挂载文件系统的信息。`path` 参数是已挂载文件系统中任何文件的路径名。`buf` 参数是指向 `statfs` 结构的指针，定义如下：

```c
typedef struct fsid { int32_t val[2]; } fsid_t; /* 文件系统 id 类型 */
/*
 * 文件系统统计信息
 */
#define	MFSNAMELEN	16		/* 类型名长度，包含 null */
#define	MNAMELEN	1024		/* on/from 名称缓冲区大小 */
#define	STATFS_VERSION	0x20140518	/* 当前版本号 */
struct statfs {
uint32_t f_version;		/* 结构版本号 */
uint32_t f_type;		/* 文件系统类型 */
uint64_t f_flags;		/* 挂载导出标志的副本 */
uint64_t f_bsize;		/* 文件系统片段大小 */
uint64_t f_iosize;		/* 最佳传输块大小 */
uint64_t f_blocks;		/* 文件系统中总数据块数 */
uint64_t f_bfree;		/* 文件系统中空闲块数 */
int64_t	 f_bavail;		/* 非超级用户可用的空闲块数 */
uint64_t f_files;		/* 文件系统中总文件节点数 */
int64_t	 f_ffree;		/* 非超级用户可用的空闲节点数 */
uint64_t f_syncwrites;		/* 自挂载以来同步写入计数 */
uint64_t f_asyncwrites;		/* 自挂载以来异步写入计数 */
uint64_t f_syncreads;		/* 自挂载以来同步读取计数 */
uint64_t f_asyncreads;		/* 自挂载以来异步读取计数 */
uint64_t f_spare[10];		/* 未使用的备用字段 */
uint32_t f_namemax;		/* 最大文件名长度 */
uid_t	  f_owner;		/* 挂载该文件系统的用户 */
fsid_t	  f_fsid;		/* 文件系统 id */
char	  f_charspare[80];	    /* 备用字符串空间 */
char	  f_fstypename[MFSNAMELEN]; /* 文件系统类型名 */
char	  f_mntfromname[MNAMELEN];  /* 挂载的文件系统 */
char	  f_mntonname[MNAMELEN];    /* 挂载到的目录 */
};
```

可能返回的标志包括：

**`MNT_ACLS`** 启用了访问控制列表（ACL）支持。

**`MNT_ASYNC`** 不进行同步文件系统 I/O。

**`MNT_AUTOMOUNTED`** 该文件系统是自动挂载的，参见 [autofs(4)](../man4/autofs.4.md)。

**`MNT_DEFEXPORTED`** 该文件系统向任何 Internet 主机导出以进行读写。

**`MNT_GJOURNAL`** 启用了 gjournal 日志记录（参见 [gjournal(8)](../man8/gjournal.8.md)）。

**`MNT_EXKERB`** 该文件系统使用 Kerberos uid 映射导出。

**`MNT_EXPORTANON`** 该文件系统将所有远程访问映射到匿名用户。

**`MNT_EXPORTED`** 该文件系统导出以进行读写。

**`MNT_EXPUBLIC`** 该文件系统公开导出（WebNFS）。

**`MNT_EXRDONLY`** 该文件系统以只读方式导出。

**`MNT_IGNORE`** 该文件系统不应被列出，例如被 [df(1)](../man1/df.1.md)。

**`MNT_LOCAL`** 该文件系统位于本地。

**`MNT_MULTILABEL`** 对单个对象的强制访问控制（MAC）支持（参见 [mac(4)](../man4/mac.4.md)）。

**`MNT_NAMEDATTR`** 该文件系统支持如 [named_attribute(7)](../man7/named_attribute.7.md) 中所述的命名属性。

**`MNT_NFS4ACLS`** 支持 NFSv4 变体的 ACL。

**`MNT_NOATIME`** 禁用文件访问时间的更新。

**`MNT_NOCLUSTERR`** 禁用读取集群。

**`MNT_NOCLUSTERW`** 禁用写入集群。

**`MNT_NOEXEC`** 不能从该文件系统执行文件。

**`MNT_NOSUID`** 文件上的 setuid 和 setgid 位在执行时不被遵守。

**`MNT_NOSYMFOLLOW`** 不跟随符号链接。

**`MNT_SOFTDEP`** 正在进行软更新（参见 [ffs(4)](../man4/ffs.4.md)）。

**`MNT_SUIDDIR`** 对目录上的 SUID 位进行特殊处理。

**`MNT_SUJ`** 正在进行带日志的软更新。

**`MNT_SYNCHRONOUS`** 到该文件系统的所有 I/O 都同步进行。

**`MNT_QUOTA`** 该文件系统已启用配额。

**`MNT_RDONLY`** 该文件系统以只读方式挂载；即使是超级用户也不能在其上写入。

**`MNT_ROOTFS`** 标识根文件系统。

**`MNT_UNION`** 与底层文件系统联合。

**`MNT_UNTRUSTED`** 该文件系统以 `untrusted` 选项挂载，表示来源或完整性未知的介质。目前由 [ffs(4)](../man4/ffs.4.md) 遵守。

**`MNT_USER`** 该文件系统由用户挂载。

**`MNT_VERIFIED`** 该文件系统被标记为已验证，无需在 [execve(2)](execve.2.md) 时进行指纹检查，参见 mac_veriexec(4)。

对于特定文件系统未定义的字段设置为 -1。`fstatfs()` 系统调用返回由描述符 `fd` 引用的已打开文件的相同信息。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`statfs()` 系统调用在以下一个或多个条件成立时失败：

**[`ENOTDIR`]** `path` 路径前缀的某个组件不是目录。

**[`ENAMETOOLONG`]** `path` 某个组件的长度超过 255 个字符，或 `path` 的长度超过 1023 个字符。

**[`ENOENT`]** `path` 所引用的文件不存在。

**[`EACCES`]** `path` 路径前缀的某个组件的搜索权限被拒绝。

**[`ELOOP`]** 在转换 `path` 时遇到过多的符号链接。

**[`EFAULT`]** `buf` 或 `path` 参数指向无效地址。

**[`EIO`]** 在向文件系统读取或写入时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

`fstatfs()` 系统调用在以下一个或多个条件成立时失败：

**[`EBADF`]** `fd` 参数不是有效的打开文件描述符。

**[`EFAULT`]** `buf` 参数指向无效地址。

**[`EIO`]** 在向文件系统读取或写入时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

## 注释

`statfs` 结构中的字段被定义为提供与传统 UNIX 文件系统相关的参数。对于某些其他文件系统，可能返回具有类似但不完全相同语义的值。一个例子是 msdosfs，对于 FAT12 或 FAT16 文件系统，它报告可用的和空闲的根目录条目数而不是 inode（其中存储每个文件或目录名或磁盘标签需要 1 到 21 个这样的目录条目）。

## 参见

[fhstatfs(2)](fhopen.2.md), [getfsstat(2)](getfsstat.2.md), [named_attribute(7)](../man7/named_attribute.7.md)

## 历史

`statfs()` 系统调用首次出现于 4.4BSD。