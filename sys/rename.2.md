# rename(2)

`rename` — 更改文件名

## 名称

`rename`

## 库

Lb libc

## 概要

`#include <stdio.h>`

```c
int
rename(const char *from, const char *to);

int
renameat(int fromfd, const char *from, int tofd, const char *to);
```

`#include <sys/fcntl.h>`

`#include <stdio.h>`

```c
int
renameat2(int fromfd, const char *from, int tofd,
    const char *to, unsigned int flags);
```

## 描述

`rename()` 系统调用将名为 `from` 的链接重命名为 `to`。如果 `to` 存在，则首先将其删除。`from` 和 `to` 必须为相同类型（即同为目录或同为非目录），并且必须位于同一文件系统上。

`rename()` 系统调用保证，如果 `to` 已经存在，则 `to` 的一个实例将始终存在，即使系统在操作过程中崩溃。

如果 `from` 的最后一个组件是符号链接，则重命名的是该符号链接，而非它所指向的文件或目录。

如果 `from` 和 `to` 解析为同一目录项，或解析为同一现有文件的不同目录项，`rename()` 返回成功，且不采取任何进一步操作。

`renameat()` 系统调用等效于 `rename()`，但当 `from` 或 `to` 指定相对路径时除外。如果 `from` 是相对路径，则要重命名的文件是相对于与文件描述符 `fromfd` 关联的目录来定位，而不是相对于当前工作目录。如果 `to` 是相对路径，则同样相对于与 `tofd` 关联的目录来定位。如果 `renameat()` 在 `fromfd` 或 `tofd` 参数中传入特殊值 `AT_FDCWD`，则在确定相应路径参数的文件时使用当前工作目录。

`renameat2()` 系统调用接受一个额外的 `flags` 参数。如果 `flags` 为零，`renameat2()` 调用的行为与 `renameat()` 相同。此外，还可以指定以下标志：

**`AT_RENAME_NOREPLACE`** 如果由 `tofd` 和 `to` 指定的路径已存在，则请求失败并返回错误 `EEXIST`。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

如果以下条件成立，`rename()` 系统调用将失败，且两个参数文件都不会受影响：

**[`ENAMETOOLONG`]** 任一路径名的某个组件超过 255 个字符，或任一路径名的总长度超过 1023 个字符。

**[`ENOENT`]** `from` 路径的某个组件不存在，或 `to` 的路径前缀不存在。

**[`EACCES`]** 任一路径前缀的某个组件拒绝搜索权限。

**[`EACCES`]** 请求的链接要求在一个模式拒绝写权限的目录中进行写入。

**[`EACCES`]** `from` 参数所指向的目录拒绝写权限，且该操作会将其移动到另一个父目录。

**[`EPERM`]** `from` 参数所指向的文件设置了不可变、不可删除或仅追加标志，更多信息请参见 [chflags(2)](chflags.2.md) 手册页。

**[`EPERM`]** `from` 参数所指向文件的父目录设置了不可变或仅追加标志。

**[`EPERM`]** `to` 参数所指向文件的父目录设置了不可变标志。

**[`EPERM`]** 包含 `from` 的目录被标记为粘滞，且包含目录和 `from` 都不属于有效用户 ID 的所有者。

**[`EPERM`]** `to` 参数所指向的文件存在，包含 `to` 的目录被标记为粘滞，且包含目录和 `to` 都不属于有效用户 ID 的所有者。

**[`ELOOP`]** 在转换任一路径名时遇到过多的符号链接。

**[`ENOTDIR`]** 任一路径前缀的某个组件不是目录。

**[`ENOTDIR`]** `from` 参数是目录，但 `to` 不是目录。

**[`EISDIR`]** `to` 参数是目录，但 `from` 不是目录。

**[`EXDEV`]** `to` 命名的链接和 `from` 命名的文件位于不同的逻辑设备（文件系统）上。注意，如果实现允许跨设备链接，则不会返回此错误代码。

**[`ENOSPC`]** 由于包含该目录的文件系统上没有剩余空间，无法扩展放置新名称条目的目录。

**[`EDQUOT`]** 由于包含该目录的文件系统上用户的磁盘块配额已用尽，无法扩展放置新名称条目的目录。

**[`EIO`]** 在创建或更新目录项时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`EROFS`]** 请求的链接要求在只读文件系统上的目录中进行写入。

**[`EFAULT`]** 路径指向进程所分配地址空间之外。

**[`EINVAL`]** `from` 参数是 `to` 的父目录，或试图重命名 `.` 或 `..`。

**[`EINVAL`]** `to` 路径的最后一个组件在目标文件系统上无效。

**[`ENOTEMPTY`]** `to` 参数是目录且不为空。

**[`ECAPMODE`]** 调用了 `rename()` 且进程处于 capability mode。

除 `rename()` 返回的错误外，`renameat()` 还可能在以下情况下失败：

**[`EBADF`]** `from` 参数未指定绝对路径且 `fromfd` 参数既不是 `AT_FDCWD` 也不是一个有效的可用于搜索的文件描述符，或 `to` 参数未指定绝对路径且 `tofd` 参数既不是 `AT_FDCWD` 也不是一个有效的可用于搜索的文件描述符。

**[`ENOTDIR`]** `from` 参数不是绝对路径且 `fromfd` 既不是 `AT_FDCWD` 也不是与目录关联的文件描述符，或 `to` 参数不是绝对路径且 `tofd` 既不是 `AT_FDCWD` 也不是与目录关联的文件描述符。

**[`ECAPMODE`]** 指定了 `AT_FDCWD` 且进程处于 capability mode。

**[`ENOTCAPABLE`]** `path` 是绝对路径或包含导致超出 `fromfd` 或 `tofd` 所指定目录层级的“..”组件。

**[`ENOTCAPABLE`]** `fromfd` 文件描述符缺少 `CAP_RENAMEAT_SOURCE` 权限，或 `tofd` 文件描述符缺少 `CAP_RENAMEAT_TARGET` 权限。

除 `renameat()` 系统调用返回的错误外，`renameat2()` 系统调用还可能在以下情况下失败：

**[`EEXIST`]** 提供了 `AT_RENAME_NOREPLACE` 标志，且在 `to` 指定的路径上存在文件。

**[`EOPNOTSUPP`]** 指定的某个 `flags` 不被待重命名文件所在文件系统支持。

## 注意事项

如果拥有待重命名文件的文件系统未实现 `AT_RENAME_NOREPLACE` 标志，则由于与目标文件创建的竞争，`renameat2()` 系统调用返回的错误可能不确定地为 `EEXIST` 或 `EOPNOTSUPP`。

## 参见

[chflags(2)](chflags.2.md), [open(2)](open.2.md), symlink(7)

## 标准

`rename()` 系统调用预期符合 ISO/IEC 9945-1:1996 ("POSIX.1")。`renameat()` 系统调用遵循 The Open Group Extended API Set 2 规范。

## 历史

`renameat()` 系统调用出现于 FreeBSD 8.0。`renameat2()` 系统调用出现于 FreeBSD 16.0。
