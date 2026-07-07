# unlink(2)

`unlink` — 删除目录项

## 名称

`unlink`, `unlinkat`, `funlinkat`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
unlink(const char *path);

int
unlinkat(int dfd, const char *path, int flag);

int
funlinkat(int dfd, const char *path, int fd, int flag);
```

## 描述

`unlink()` 系统调用从其目录中删除由 `path` 命名的链接，并将该链接所引用文件的链接计数减一。如果该递减操作将文件的链接计数减为零，且没有进程打开该文件，则会回收与该文件关联的所有资源。如果在删除最后一个链接时有一个或多个进程打开了该文件，则链接会被删除，但文件的删除会延迟到对该文件的所有引用都关闭之后。`path` 参数不能是目录。

`unlinkat()` 系统调用等效于 `unlink()` 或 `rmdir()`，不同之处在于 `path` 指定相对路径的情况。此时，要删除的目录项是相对于与文件描述符 `dfd` 关联的目录来确定，而非相对于当前工作目录。

`flag` 的值由以下列表中标志的按位或运算构成，定义在 `<fcntl.h>` 中：

**`AT_REMOVEDIR`** 将由 `fd` 和 `path` 指定的目录项作为目录而非普通文件删除。

**`AT_RESOLVE_BENEATH`** 仅遍历 `fd` 描述符所指定目录下方的路径。参见 [open(2)](open.2.md) 手册页中 `O_RESOLVE_BENEATH` 标志的描述。

如果 `unlinkat()` 的 `fd` 参数传入特殊值 `AT_FDCWD`，则使用当前工作目录，其行为与调用 `unlink()` 或 `rmdir()` 相同，具体取决于 `flag` 中是否设置了 `AT_REMOVEDIR` 位。

`funlinkat()` 系统调用可用于删除已打开的文件，除非该文件在打开后已被替换。当 `path` 已经作为文件描述符 `fd` 打开时，它等效于 `unlinkat()`。否则，路径不会被删除，并返回错误。`fd` 可以设置为 `FD_NONE`。在这种情况下，`funlinkat()` 的行为与 `unlinkat()` 完全相同。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`unlink()` 系统调用在以下情况下会失败：

**[`ENOTDIR`]** 路径前缀的某个组件不是目录。

**[`EISDIR`]** 指定文件是目录。

**[`ENAMETOOLONG`]** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[`ENOENT`]** 指定文件不存在。

**[`EACCES`]** 拒绝对路径前缀某个组件的搜索权限。

**[`EACCES`]** 拒绝对包含待删除链接的目录的写权限。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`EPERM`]** 指定文件是目录。

**[`EPERM`]** 指定文件设置了 immutable、undeletable 或 append-only 标志，更多信息请参见 [chflags(2)](chflags.2.md) 手册页。

**[`EPERM`]** 指定文件的父目录设置了 immutable 或 append-only 标志。

**[`EPERM`]** 包含该文件的目录被标记为 sticky，且包含目录和待删除文件均非有效用户 ID 所拥有。

**[`EIO`]** 在删除目录项或释放 inode 时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`EROFS`]** 指定文件位于只读文件系统上。

**[`EFAULT`]** `path` 参数指向进程分配地址空间之外。

**[`ENOSPC`]** 在支持写时复制或快照的文件系统上，没有足够的可用空间来记录文件删除操作的元数据。

除 `unlink()` 返回的错误外，`unlinkat()` 还可能在以下情况下失败：

**[`EBADF`]** `path` 参数未指定绝对路径，且 `fd` 参数既不是 `AT_FDCWD` 也不是有效的、可搜索的已打开文件描述符。

**[`ENOTEMPTY`]** `flag` 参数设置了 `AT_REMOVEDIR` 位，且 `path` 参数命名的目录不是空目录，或该目录有除 dot 或 dot-dot 中的单个条目以外的硬链接。

**[`ENOTDIR`]** `flag` 参数设置了 `AT_REMOVEDIR` 位，且 `path` 未命名目录。

**[`EINVAL`]** `flag` 参数的值无效。

**[`ENOTDIR`]** `path` 参数不是绝对路径，且 `fd` 既不是 `AT_FDCWD` 也不是与目录关联的文件描述符。

**[`ENOTCAPABLE`]** `path` 是绝对路径，或包含导致超出 `fd` 所指定目录层级的 `".."` 组件，且进程处于 capability 模式或指定了 `AT_RESOLVE_BENEATH` 标志。

除 `unlinkat()` 返回的错误外，`funlinkat()` 还可能在以下情况下失败：

**[`EDEADLK`]** 文件描述符未与该路径关联。

## 参见

[chflags(2)](chflags.2.md), [close(2)](close.2.md), [link(2)](link.2.md), [rmdir(2)](rmdir.2.md), [symlink(7)](../man7/symlink.7.md)

## 标准

`unlinkat()` 系统调用遵循 The Open Group Extended API Set 2 规范。

## 历史

`unlink()` 函数出现于 Version 1 AT&T UNIX。`unlinkat()` 系统调用出现于 FreeBSD 8.0。`funlinkat()` 系统调用出现于 FreeBSD 13.0。

`unlink()` 系统调用在传统上允许超级用户删除目录，这会破坏文件系统的一致性。本实现不再允许此操作。
