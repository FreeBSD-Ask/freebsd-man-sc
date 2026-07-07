# mkfifo(2)

`mkfifo` — 创建 fifo 文件

## 名称

`mkfifo`, `mkfifoat`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/stat.h>`

```c
int
mkfifo(const char *path, mode_t mode);

int
mkfifoat(int fd, const char *path, mode_t mode);
```

## 描述

`mkfifo()` 系统调用创建名为 `path` 的新 fifo 文件。访问权限由 `mode` 指定，并受调用进程的 [umask(2)](umask.2.md) 限制。

fifo 的所有者 ID 设置为进程的有效用户 ID。fifo 的组 ID 设置为其所在父目录的组 ID。

`mkfifoat()` 系统调用等价于 `mkfifo()`，不同之处在于 `path` 指定相对路径的情况。此时，新创建的 FIFO 相对于与文件描述符 `fd` 关联的目录创建，而非相对于当前工作目录。如果 `mkfifoat()` 的 `fd` 参数传入特殊值 `AT_FDCWD`，则使用当前工作目录，其行为与调用 `mkfifo()` 相同。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`mkfifo()` 系统调用在以下情况下会失败，且不会创建 fifo：

**[`ENOTSUP`]** 内核未配置为支持 fifo。

**[`ENOTDIR`]** 路径前缀的某个组件不是目录。

**[`ENAMETOOLONG`]** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[`ENOENT`]** 路径前缀的某个组件不存在。

**[`EACCES`]** 路径前缀的某个组件拒绝搜索权限，或要创建的 fifo 的父目录拒绝写权限。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`EROFS`]** 指定名称的文件将位于只读文件系统上。

**[`EEXIST`]** 指定名称的文件已存在。

**[`EPERM`]** 指定名称的文件的父目录设置了 immutable 标志，更多信息请参见 [chflags(2)](chflags.2.md) 手册页。

**[`ENOSPC`]** 无法扩展放置新 fifo 条目的目录，因为包含该目录的文件系统上没有剩余空间。

**[`ENOSPC`]** 创建 fifo 所在文件系统上没有空闲的 inode。

**[`EDQUOT`]** 无法扩展放置新 fifo 条目的目录，因为用户在包含该目录的文件系统上的磁盘块配额已用尽。

**[`EDQUOT`]** 创建 fifo 所在文件系统上用户的 inode 配额已用尽。

**[`EIO`]** 创建目录项或分配 inode 时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`EFAULT`]** `path` 参数指向进程分配地址空间之外。

除 `mkfifo()` 返回的错误外，`mkfifoat()` 还可能在以下情况下失败：

**[`EBADF`]** `path` 参数未指定绝对路径，且 `fd` 参数既不是 `AT_FDCWD`，也不是一个有效的、可搜索的已打开文件描述符。

**[`ENOTDIR`]** `path` 参数不是绝对路径，且 `fd` 既不是 `AT_FDCWD`，也不是与目录关联的文件描述符。

## 参见

[chflags(2)](chflags.2.md), [chmod(2)](chmod.2.md), [mknod(2)](mknod.2.md), [stat(2)](stat.2.md), [umask(2)](umask.2.md)

## 标准

`mkfifo()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1")。`mkfifoat()` 系统调用遵循 The Open Group Extended API Set 2 规范。

## 历史

`mkfifoat()` 系统调用出现于 FreeBSD 8.0。