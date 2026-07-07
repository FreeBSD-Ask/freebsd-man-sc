# mkdir(2)

`mkdir` — 创建目录文件

## 名称

`mkdir`, `mkdirat`

## 库

Lb libc

## 概要

`#include <sys/stat.h>`

```c
int
mkdir(const char *path, mode_t mode);

int
mkdirat(int fd, const char *path, mode_t mode);
```

## 描述

目录 `path` 以 `mode` 指定的访问权限创建，并受调用进程的 [umask(2)](umask.2.md) 限制。

目录的所有者 ID 设置为进程的有效用户 ID。目录的组 ID 设置为其所在父目录的组 ID。

`mkdirat()` 系统调用等价于 `mkdir()`，不同之处在于 `path` 指定相对路径的情况。此时，新创建的目录相对于与文件描述符 `fd` 关联的目录创建，而非相对于当前工作目录。如果 `mkdirat()` 的 `fd` 参数传入特殊值 `AT_FDCWD`，则使用当前工作目录，其行为与调用 `mkdir()` 相同。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`mkdir()` 系统调用在以下情况下会失败，且不会创建目录：

**[`ENOTDIR`]** 路径前缀的某个组件不是目录。

**[`ENAMETOOLONG`]** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[`ENOENT`]** 路径前缀的某个组件不存在。

**[`EACCES`]** 路径前缀的某个组件拒绝搜索权限，或要创建的目录的父目录拒绝写权限。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`EPERM`]** 要创建的目录的父目录设置了 immutable 标志，更多信息请参见 [chflags(2)](chflags.2.md) 手册页。

**[`EROFS`]** 指定的目录将位于只读文件系统上。

**[`EMLINK`]** 无法创建新目录，因为父目录包含的子目录过多。

**[`EEXIST`]** 指定名称的文件已存在。

**[`ENOSPC`]** 无法创建新目录，因为将包含该目录的文件系统上没有剩余空间。

**[`ENOSPC`]** 创建目录所在文件系统上没有空闲的 inode。

**[`EDQUOT`]** 无法创建新目录，因为用户在将包含该目录的文件系统上的磁盘块配额已用尽。

**[`EDQUOT`]** 创建目录所在文件系统上用户的 inode 配额已用尽。

**[`EIO`]** 创建目录项或分配 inode 时发生 I/O 错误。

**[`EIO`]** 从文件系统读取或向其写入时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`EFAULT`]** `path` 参数指向进程分配地址空间之外。

除 `mkdir()` 返回的错误外，`mkdirat()` 还可能在以下情况下失败：

**[`EBADF`]** `path` 参数未指定绝对路径，且 `fd` 参数既不是 `AT_FDCWD`，也不是一个有效的、可搜索的已打开文件描述符。

**[`ENOTDIR`]** `path` 参数不是绝对路径，且 `fd` 既不是 `AT_FDCWD`，也不是与目录关联的文件描述符。

## 参见

[chflags(2)](chflags.2.md), [chmod(2)](chmod.2.md), [stat(2)](stat.2.md), [umask(2)](umask.2.md)

## 标准

`mkdir()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1")。`mkdirat()` 系统调用遵循 The Open Group Extended API Set 2 规范。

## 历史

`mkdirat()` 系统调用出现于 FreeBSD 8.0。`mkdir()` 系统调用出现于 4.2BSD。