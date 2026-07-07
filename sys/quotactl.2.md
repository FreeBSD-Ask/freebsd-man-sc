# quotactl(2)

`quotactl` — 操作文件系统配额

## 名称

`quotactl`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <ufs/ufs/quota.h>`

```c
int
quotactl(const char *path, int cmd, int id, void *addr);
```

## 描述

`quotactl()` 系统调用启用、禁用和操作文件系统配额。由 `cmd` 给出的配额控制命令对给定的文件名 `path` 进行操作，针对给定的用户或组 `id`。（注意：应使用 `#include <ufs/ufs/quota.h>` 中定义的 QCMD 宏来构造 `cmd` 的值。）可以提供一个可选的命令特定数据结构的地址 `addr`；其解释在下面每个命令中讨论。

对于使用 `id` 标识符的命令，它必须是 -1 或任何正值。值 -1 表示应使用当前 UID 或 GID。任何其他负值将返回错误。

目前仅支持"ufs"文件系统的配额。对于"ufs"，命令由一个主命令（见下文）和一个用于解释 `id` 的命令类型组成。支持用于解释用户标识符（USRQUOTA）和组标识符（GRPQUOTA）的类型。"ufs"特定命令如下：

**`Q_QUOTAON`** 为 `path` 指定的文件系统启用磁盘配额。命令类型指定要启用的配额类型。`addr` 参数指定一个用于获取配额的文件。配额文件必须存在；通常由 quotacheck(8) 程序创建。`id` 参数未使用。只有超级用户可以启用配额。

**`Q_QUOTAOFF`** 为 `path` 指定的文件系统禁用磁盘配额。命令类型指定要禁用的配额类型。`addr` 和 `id` 参数未使用。只有超级用户可以禁用配额。

**`Q_GETQUOTASIZE`** 获取用于表示用户或组配额的字长（由命令类型决定）。可能的值为 32（旧式配额文件）和 64（新式配额文件）。`addr` 参数是一个指向整数的指针，大小存储在该整数中。标识符 `id` 未使用。

**`Q_GETQUOTA`** 获取标识符为 `id` 的用户或组（由命令类型决定）的磁盘配额限制和当前使用量。`addr` 参数是一个指向 `struct dqblk` 结构的指针（定义在 `#include <ufs/ufs/quota.h>` 中）。

**`Q_SETQUOTA`** 设置标识符为 `id` 的用户或组（由命令类型决定）的磁盘配额限制。`addr` 参数是一个指向 `struct dqblk` 结构的指针（定义在 `#include <ufs/ufs/quota.h>` 中）。`dqblk` 结构的使用量字段被忽略。此系统调用仅限超级用户使用。

**`Q_SETUSE`** 设置标识符为 `id` 的用户或组（由命令类型决定）的磁盘使用量限制。`addr` 参数是一个指向 `struct dqblk` 结构的指针（定义在 `#include <ufs/ufs/quota.h>` 中）。仅使用使用量字段。此系统调用仅限超级用户使用。

**`Q_SYNC`** 更新磁盘上的配额使用量副本。命令类型指定要更新的配额类型。`id` 和 `addr` 参数被忽略。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 errno 以指示错误。

## 错误

`quotactl()` 系统调用在以下情况下会失败：

**[`EOPNOTSUPP`]** 内核未编译 `QUOTA` 选项。

**[`EUSERS`]** 配额表无法扩展。

**[`EINVAL`]** `cmd` 参数或命令类型无效。在 `Q_GETQUOTASIZE`、`Q_GETQUOTA`、`Q_SETQUOTA` 和 `Q_SETUSE` 中，此文件系统当前未启用配额。传给 `Q_GETQUOTA`、`Q_SETQUOTA` 或 `Q_SETUSE` 的 `id` 参数为负值。

**[`EACCES`]** 在 `Q_QUOTAON` 中，配额文件不是普通文件。

**[`EACCES`]** 路径前缀的某个组件被拒绝搜索权限。

**[`ENOTDIR`]** 路径前缀的某个组件不是目录。

**[`ENAMETOOLONG`]** 任一路径名的某个组件超过 255 个字符，或任一路径名的总长度超过 1023 个字符。

**[`ENOENT`]** 文件名不存在。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`EROFS`]** 在 `Q_QUOTAON` 中，要启用配额的文件系统以只读方式挂载，或配额文件位于只读文件系统上。

**[`EIO`]** 在对包含配额的文件进行读写时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取数据时检测到损坏的数据。

**[`EFAULT`]** 提供了无效的 `addr`；关联的结构无法复制进或出内核。

**[`EFAULT`]** `path` 参数指向进程分配地址空间之外。

**[`EPERM`]** 该调用需要特权，且调用者不是超级用户。

## 参见

[quota(1)](../man1/quota.1.md), [fstab(5)](../man5/fstab.5.md), [edquota(8)](../man8/edquota.8.md), [quotacheck(8)](../man8/quotacheck.8.md), [quotaon(8)](../man8/quotaon.8.md), [repquota(8)](../man8/repquota.8.md)

## 历史

`quotactl()` 系统调用出现于 4.3BSD-Reno。

## 缺陷

应该有某种方式将此调用与 [setrlimit(2)](getrlimit.2.md) 和 [getrlimit(2)](getrlimit.2.md) 提供的资源限制接口集成。