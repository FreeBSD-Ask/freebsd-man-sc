# chown(2)

`chown` — 更改文件的所有者和组

## 名称

`chown`, `fchown`, `lchown`, `fchownat`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
chown(const char *path, uid_t owner, gid_t group);

int
fchown(int fd, uid_t owner, gid_t group);

int
lchown(const char *path, uid_t owner, gid_t group);

int
fchownat(int fd, const char *path, uid_t owner, gid_t group, int flag);
```

## 描述

由 `path` 指定名称或由 `fd` 引用的文件的所有者 ID 和组 ID 将按照 `owner` 和 `group` 参数的指定进行更改。文件的所有者可以将 `group` 更改为其所属的组，但更改 `owner` 的能力仅限于超级用户。

`chown()` 系统调用会清除文件上的 set-user-id 和 set-group-id 位，以防止在非超级用户执行时意外或恶意创建 set-user-id 和 set-group-id 程序。`chown()` 系统调用会跟随符号链接，以操作链接所指向的目标而非链接本身。

`fchown()` 系统调用在与文件锁定原语配合使用时特别有用（参见 [flock(2)](flock.2.md)）。

`lchown()` 系统调用类似于 `chown()`，但不跟随符号链接。

`fchownat()` 系统调用等效于 `chown()` 和 `lchown()`，但当 `path` 指定相对路径时除外。在此情况下，要更改的文件是相对于与文件描述符 `fd` 关联的目录来确定，而不是相对于当前工作目录。

`flag` 的值由以下列表中定义的标志按位或运算构成，定义于

`#include <fcntl.h>`

**`AT_SYMLINK_NOFOLLOW`** 如果 `path` 命名一个符号链接，则更改该符号链接的所有权。

**`AT_RESOLVE_BENEATH`** 仅遍历由 `fd` 描述符指定目录之下的路径。参见 [open(2)](open.2.md) 手册页中对 `O_RESOLVE_BENEATH` 标志的描述。

**`AT_EMPTY_PATH`** 如果 `path` 参数为空字符串，则对描述符 `fd` 所引用的文件或目录进行操作。如果 `fd` 等于 `AT_FDCWD`，则对当前工作目录进行操作。

如果 `fchownat()` 在 `fd` 参数中传入特殊值 `AT_FDCWD`，则使用当前工作目录，其行为分别与调用 `chown()` 或 `lchown()` 相同，具体取决于 `flag` 参数中是否设置了 `AT_SYMLINK_NOFOLLOW` 位。

可以通过将 `owner` 或 `group` 中的一个指定为 -1 来保持其不变。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

如果以下条件成立，`chown()` 和 `lchown()` 将失败，且文件保持不变：

**[`ENOTDIR`]** 路径前缀的某个组件不是目录。

**[`ENAMETOOLONG`]** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[`ENOENT`]** 指定的文件不存在。

**[`EACCES`]** 路径前缀的某个组件的搜索权限被拒绝。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`EPERM`]** 该操作会更改所有权，但有效用户 ID 不是超级用户。

**[`EPERM`]** 指定文件设置了不可变或仅追加标志，更多信息请参见 [chflags(2)](chflags.2.md) 手册页。

**[`EROFS`]** 指定文件位于只读文件系统上。

**[`EFAULT`]** `path` 参数指向进程所分配地址空间之外。

**[`EIO`]** 在向文件系统读取或写入时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

`fchown()` 系统调用在以下情况下会失败：

**[`EBADF`]** `fd` 参数未引用有效描述符。

**[`EINVAL`]** `fd` 参数引用的是套接字，而非文件。

**[`EPERM`]** 有效用户 ID 不是超级用户。

**[`EROFS`]** 指定文件位于只读文件系统上。

**[`EIO`]** 在向文件系统读取或写入时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

除为 `chown()` 和 `lchown()` 指定的错误外，`fchownat()` 系统调用还可能在以下情况下失败：

**[`EBADF`]** `path` 参数未指定绝对路径，且 `fd` 参数既不是 `AT_FDCWD` 也不是一个有效的可用于搜索的文件描述符。

**[`EINVAL`]** `flag` 参数的值无效。

**[`ENOTDIR`]** `path` 参数不是绝对路径，且 `fd` 既不是 `AT_FDCWD` 也不是与目录关联的文件描述符。

**[`ENOTCAPABLE`]** `path` 是绝对路径，或包含导致超出 `fd` 所指定目录层级的“..”组件，且进程处于 capability mode 或指定了 `AT_RESOLVE_BENEATH` 标志。

## 参见

[chgrp(1)](../man1/chgrp.1.md), [chflags(2)](chflags.2.md), [chmod(2)](chmod.2.md), [flock(2)](flock.2.md), [chown(8)](../man8/chown.8.md)

## 标准

`chown()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1")。`fchownat()` 系统调用遵循 The Open Group Extended API Set 2 规范。

## 历史

`chown()` 函数出现于 Version 1 AT&T UNIX。`fchown()` 系统调用出现于 4.2BSD。

`chown()` 系统调用在 4.4BSD 中改为跟随符号链接。`lchown()` 系统调用在 FreeBSD 3.0 中添加，以补偿由此丧失的功能。

`fchownat()` 系统调用出现于 FreeBSD 8.0。
