# symlink(2)

`symlink` — 创建指向文件的符号链接

## 名称

`symlink`, `symlinkat`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
symlink(const char *name1, const char *name2);

int
symlinkat(const char *name1, int fd, const char *name2);
```

## 描述

创建指向 `name1` 的符号链接 `name2`（`name2` 是所创建文件的名称，`name1` 是创建符号链接时使用的字符串）。任一名称都可以是任意路径名；文件不必位于同一文件系统上。

`symlinkat()` 系统调用等价于 `symlink()`，不同之处在于 `name2` 指定相对路径的情况。此时，符号链接相对于与文件描述符 `fd` 关联的目录创建，而非相对于当前工作目录。如果 `symlinkat()` 的 `fd` 参数传入特殊值 `AT_FDCWD`，则使用当前工作目录，其行为与调用 `symlink()` 相同。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

符号链接在以下情况下不会成功创建：

**[`ENOTDIR`]** `name2` 路径前缀的某个组件不是目录。

**[`ENAMETOOLONG`]** `name2` 路径名的某个组件超过 255 个字符，或任一路径名的总长度超过 1023 个字符。

**[`ENOENT`]** `name2` 路径前缀的某个组件不存在。

**[`EOPNOTSUPP`]** 包含 `name2` 所命名文件的文件系统不支持符号链接。

**[`EACCES`]** `name2` 路径前缀的某个组件拒绝搜索权限，或要创建文件的父目录拒绝写权限。

**[`ELOOP`]** 在转换 `name2` 路径名时遇到过多的符号链接。

**[`EEXIST`]** `name2` 参数所指向的路径名已存在。

**[`EPERM`]** `name2` 所命名文件的父目录设置了 immutable 标志，更多信息请参见 [chflags(2)](chflags.2.md) 手册页。

**[`EIO`]** 为 `name2` 创建目录项、为 `name2` 分配 inode 或写出 `name2` 的链接内容时发生 I/O 错误。

**[`EROFS`]** 文件 `name2` 将位于只读文件系统上。

**[`ENOSPC`]** 无法扩展放置新符号链接条目的目录，因为包含该目录的文件系统上没有剩余空间。

**[`ENOSPC`]** 无法创建新符号链接，因为将包含该符号链接的文件系统上没有剩余空间。

**[`ENOSPC`]** 创建符号链接所在文件系统上没有空闲的 inode。

**[`EDQUOT`]** 无法扩展放置新符号链接条目的目录，因为用户在包含该目录的文件系统上的磁盘块配额已用尽。

**[`EDQUOT`]** 无法创建新符号链接，因为用户在将包含该符号链接的文件系统上的磁盘块配额已用尽。

**[`EDQUOT`]** 创建符号链接所在文件系统上用户的 inode 配额已用尽。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`EFAULT`]** `name1` 或 `name2` 参数指向进程分配地址空间之外。

除 `symlink()` 返回的错误外，`symlinkat()` 还可能在以下情况下失败：

**[`EBADF`]** `name2` 参数未指定绝对路径，且 `fd` 参数既不是 `AT_FDCWD`，也不是一个有效的、可搜索的已打开文件描述符。

**[`ENOTDIR`]** `name2` 参数不是绝对路径，且 `fd` 既不是 `AT_FDCWD`，也不是与目录关联的文件描述符。

## 参见

[ln(1)](../man1/ln.1.md), [chflags(2)](chflags.2.md), [link(2)](link.2.md), [lstat(2)](lstat.2.md), [readlink(2)](readlink.2.md), [unlink(2)](unlink.2.md), [symlink(7)](../man7/symlink.7.md)

## 标准

`symlinkat()` 系统调用遵循 The Open Group Extended API Set 2 规范。

## 历史

`symlink()` 系统调用出现于 4.2BSD。`symlinkat()` 系统调用出现于 FreeBSD 8.0。