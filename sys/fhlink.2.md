# fhlink(2)

`fhlink` — 创建硬文件链接

## 名称

`fhlink`, `fhlinkat`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
fhlink(fhandle_t *fhp, const char *to);

int
fhlinkat(fhandle_t *fhp, int tofd, const char *to);
```

## 描述

`fhlink()` 系统调用以 `fhp` 所指向底层对象的属性，原子地创建指定的目录项（硬链接）`to`。如果链接成功：底层对象的链接计数递增；`fhp` 和 `to` 共享对底层对象的同等访问权和权限。

如果 `fhp` 被删除，文件 `to` 不会被删除，底层对象的链接计数递减。

`fhp` 参数所指向的对象必须存在，硬链接才能成功，且 `fhp` 和 `to` 必须在同一文件系统中。`fhp` 参数不能是目录。

`fhlinkat()` 系统调用等价于 `fhlink`，不同之处在于 `to` 为相对路径的情况。此时，相对路径 `to` 相对于与文件描述符 `tofd` 关联的目录解释，而非相对于当前工作目录。

如果 `fhlinkat()` 的 `tofd` 参数传入特殊值 `AT_FDCWD`，则 `to` 参数使用当前工作目录。如果 `tofd` 的值为 `AT_FDCWD`，其行为与调用 `link()` 相同。除非 `flag` 包含 `AT_SYMLINK_FOLLOW` 标志，否则如果 `fhp` 命名了一个符号链接，则为该符号链接 `fhp` 创建新链接，而非为其目标创建。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`fhlink()` 系统调用在以下情况下会失败，且不会创建链接：

**[`ENOTDIR`]** `to` 前缀的某个组件不是目录。

**[`ENAMETOOLONG`]** `to` 的某个组件超过 255 个字符，或 `to` 名称的总长度超过 1023 个字符。

**[`ENOENT`]** `to` 前缀的某个组件不存在。

**[`EOPNOTSUPP`]** 包含 `fhp` 所指向文件的文件系统不支持链接。

**[`EMLINK`]** `fhp` 所指向文件的链接计数将超过 32767。

**[`EACCES`]** `to` 前缀的某个组件拒绝搜索权限。

**[`EACCES`]** 请求的链接要求在一个模式拒绝写权限的目录中写入。

**[`ELOOP`]** 在转换某个路径名时遇到过多的符号链接。

**[`ENOENT`]** `fhp` 所指向的文件不存在。

**[`EEXIST`]** `to` 所命名的链接已存在。

**[`EPERM`]** `fhp` 所指向的文件是目录。

**[`EPERM`]** `fhp` 所指向的文件设置了 immutable 或 append-only 标志，更多信息请参见 [chflags(2)](chflags.2.md) 手册页。

**[`EPERM`]** `to` 所命名文件的父目录设置了 immutable 标志。

**[`EXDEV`]** `to` 所命名的链接与 `fhp` 所指向的文件位于不同的文件系统上。

**[`ENOSPC`]** 无法扩展放置新链接条目的目录，因为包含该目录的文件系统上没有剩余空间。

**[`EDQUOT`]** 无法扩展放置新链接条目的目录，因为用户在包含该目录的文件系统上的磁盘块配额已用尽。

**[`EIO`]** 在读取或写入文件系统以创建目录项时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`EROFS`]** 请求的链接要求在只读文件系统上的目录中写入。

**[`EFAULT`]** 指定的某个路径名位于进程分配地址空间之外。

**[`ESTALE`]** 文件句柄 `fhp` 已不再有效。

除 `fhlink()` 返回的错误外，`fhlinkat()` 系统调用还可能在以下情况下失败：

**[`EBADF`]** `fhp` 或 `to` 参数未指定绝对路径，且 `tofd` 参数既不是 `AT_FDCWD`，也不是一个有效的、可搜索的已打开文件描述符。

**[`EINVAL`]** `flag` 参数的值无效。

**[`ENOTDIR`]** `fhp` 或 `to` 参数不是绝对路径，且 `tofd` 既不是 `AT_FDCWD`，也不是与目录关联的文件描述符。

## 参见

[fhopen(2)](fhopen.2.md), [fhreadlink(2)](fhreadlink.2.md), [fhstat(2)](fhopen.2.md)

## 历史

`fhlink()` 和 `fhlinkat()` 系统调用首次出现于 FreeBSD 12.1。