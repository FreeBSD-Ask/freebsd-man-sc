# link(2)

`link` — 创建硬文件链接

## 名称

`link`, `linkat`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
link(const char *name1, const char *name2);

int
linkat(int fd1, const char *name1, int fd2,
    const char *name2, int flag);
```

## 描述

`link()` 系统调用以 `name1` 所指向底层对象的属性，原子地创建指定的目录项（硬链接）`name2`。如果链接成功：底层对象的链接计数递增；`name1` 和 `name2` 共享对底层对象的同等访问权和权限。

如果 `name1` 被删除，文件 `name2` 不会被删除，底层对象的链接计数递减。

`name1` 参数所指向的对象必须存在，硬链接才能成功，且 `name1` 和 `name2` 必须在同一文件系统中。`name1` 参数不能是目录。

`linkat()` 系统调用等价于 `link`，不同之处在于 `name1` 或 `name2` 或两者为相对路径的情况。此时，相对路径 `name1` 相对于与文件描述符 `fd1` 关联的目录解释，而非相对于当前工作目录；`name2` 和文件描述符 `fd2` 同理。

`flag` 的值由以下列表中标志的按位或构造，定义在 `<fcntl.h>` 中：

**`AT_SYMLINK_FOLLOW`** 如果 `name1` 命名了一个符号链接，则为该符号链接的目标创建新链接。

**`AT_RESOLVE_BENEATH`** 仅遍历 `fd1` 描述符所指定目录下方的路径。参见 [open(2)](open.2.md) 手册页中 `O_RESOLVE_BENEATH` 标志的描述。

**`AT_EMPTY_PATH`** 如果 `name1` 参数是空字符串，则链接描述符 `fd1` 所引用的文件。此操作要求调用进程具有 `PRIV_VFS_FHOPEN` 特权，实际上以有效用户 `root` 身份执行。

如果 `linkat()` 的 `fd1` 或 `fd2` 参数传入特殊值 `AT_FDCWD`，则相应的 `name` 参数使用当前工作目录。如果 `fd1` 和 `fd2` 的值均为 `AT_FDCWD`，其行为与调用 `link()` 相同。除非 `flag` 包含 `AT_SYMLINK_FOLLOW` 标志，否则如果 `name1` 命名了一个符号链接，则为该符号链接 `name1` 创建新链接，而非为其目标创建。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`link()` 系统调用在以下情况下会失败，且不会创建链接：

**[`ENOTDIR`]** 某个路径前缀的组件不是目录。

**[`ENAMETOOLONG`]** 某个路径名的组件超过 255 个字符，或某个路径名的总长度超过 1023 个字符。

**[`ENOENT`]** 某个路径前缀的组件不存在。

**[`EOPNOTSUPP`]** 包含 `name1` 所命名文件的文件系统不支持链接。

**[`EMLINK`]** `name1` 所命名文件的链接计数将超过 32767。

**[`EACCES`]** 某个路径前缀的组件拒绝搜索权限。

**[`EACCES`]** 请求的链接要求在一个模式拒绝写权限的目录中写入。

**[`ELOOP`]** 在转换某个路径名时遇到过多的符号链接。

**[`ENOENT`]** `name1` 所命名的文件不存在。

**[`EEXIST`]** `name2` 所命名的链接已存在。

**[`EPERM`]** `name1` 所命名的文件是目录。

**[`EPERM`]** `name1` 所命名的文件设置了 immutable 或 append-only 标志，更多信息请参见 [chflags(2)](chflags.2.md) 手册页。

**[`EPERM`]** `name2` 所命名文件的父目录设置了 immutable 标志。

**[`EXDEV`]** `name2` 所命名的链接与 `name1` 所命名的文件位于不同的文件系统上。

**[`ENOSPC`]** 无法扩展放置新链接条目的目录，因为包含该目录的文件系统上没有剩余空间。

**[`EDQUOT`]** 无法扩展放置新链接条目的目录，因为用户在包含该目录的文件系统上的磁盘块配额已用尽。

**[`EIO`]** 在读取或写入文件系统以创建目录项时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`EROFS`]** 请求的链接要求在只读文件系统上的目录中写入。

**[`EFAULT`]** 指定的某个路径名位于进程分配地址空间之外。

除 `link()` 返回的错误外，`linkat()` 系统调用还可能在以下情况下失败：

**[`EBADF`]** `name1` 或 `name2` 参数未指定绝对路径，且相应的 `fd1` 或 `fd2` 参数既不是 `AT_FDCWD`，也不是一个有效的、可搜索的已打开文件描述符。

**[`EINVAL`]** `flag` 参数的值无效。

**[`ENOTDIR`]** `name1` 或 `name2` 参数不是绝对路径，且相应的 `fd1` 或 `fd2` 既不是 `AT_FDCWD`，也不是与目录关联的文件描述符。

**[`ENOTCAPABLE`]** `name1` 不严格相对于起始目录。例如，`name1` 是绝对路径，或包含逃逸 `fd` 所指定目录层级的 ".." 组件，且进程处于 capability 模式或指定了 `AT_RESOLVE_BENEATH` 标志。

## 参见

[chflags(2)](chflags.2.md), [readlink(2)](readlink.2.md), [symlink(2)](symlink.2.md), [unlink(2)](unlink.2.md)

## 标准

`link()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1")。`linkat()` 系统调用遵循 The Open Group Extended API Set 2 规范。

## 历史

`link()` 函数出现于 Version 1 AT&T UNIX。`linkat()` 系统调用出现于 FreeBSD 8.0。

`link()` 系统调用传统上允许超级用户链接目录，这会破坏文件系统的一致性。本实现不再允许此操作。