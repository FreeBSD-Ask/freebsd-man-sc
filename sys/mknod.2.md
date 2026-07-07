# mknod(2)

`mknod` — 创建特殊文件节点

## 名称

`mknod`, `mknodat`

## 库

Lb libc

## 概要

`#include <sys/stat.h>`

```c
int
mknod(const char *path, mode_t mode, dev_t dev);

int
mknodat(int fd, const char *path, mode_t mode, dev_t dev);
```

## 描述

文件系统节点 `path` 以 `mode` 中指定的文件类型和访问权限创建。访问权限由进程的 umask 值修改。

如果 `mode` 指示为块或字符特殊文件，`dev` 是一个依赖于配置的说明，表示系统上的特定设备。否则，`dev` 被忽略。

`mknod()` 系统调用需要超级用户权限。

`mknodat()` 系统调用等价于 `mknod()`，不同之处在于 `path` 指定相对路径的情况。此时，新创建的设备节点相对于与文件描述符 `fd` 关联的目录创建，而非相对于当前工作目录。如果 `mknodat()` 的 `fd` 参数传入特殊值 `AT_FDCWD`，则使用当前工作目录，其行为与调用 `mknod()` 相同。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`mknod()` 系统调用在以下情况下会失败，且不会创建文件：

**[`ENOTDIR`]** 路径前缀的某个组件不是目录。

**[`ENAMETOOLONG`]** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[`ENOENT`]** 路径前缀的某个组件不存在。

**[`EACCES`]** 路径前缀的某个组件拒绝搜索权限。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`EPERM`]** 进程的有效用户 ID 不是超级用户。

**[`EIO`]** 创建目录项或分配 inode 时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`ENOSPC`]** 无法扩展放置新节点条目的目录，因为包含该目录的文件系统上没有剩余空间。

**[`ENOSPC`]** 创建节点所在文件系统上没有空闲的 inode。

**[`EDQUOT`]** 无法扩展放置新节点条目的目录，因为用户在包含该目录的文件系统上的磁盘块配额已用尽。

**[`EDQUOT`]** 创建节点所在文件系统上用户的 inode 配额已用尽。

**[`EROFS`]** 指定名称的文件位于只读文件系统上。

**[`EEXIST`]** 指定名称的文件已存在。

**[`EFAULT`]** `path` 参数指向进程分配地址空间之外。

**[`EINVAL`]** 不支持创建块或字符特殊文件（或 *whiteout*）以外的任何内容。

除 `mknod()` 返回的错误外，`mknodat()` 还可能在以下情况下失败：

**[`EBADF`]** `path` 参数未指定绝对路径，且 `fd` 参数既不是 `AT_FDCWD`，也不是一个有效的、可搜索的已打开文件描述符。

**[`ENOTDIR`]** `path` 参数不是绝对路径，且 `fd` 既不是 `AT_FDCWD`，也不是与目录关联的文件描述符。

## 参见

[chmod(2)](chmod.2.md), [mkfifo(2)](mkfifo.2.md), [stat(2)](stat.2.md), [umask(2)](umask.2.md)

## 标准

`mknodat()` 系统调用遵循 The Open Group Extended API Set 2 规范。

## 历史

`mknod()` 函数出现于 Version 4 AT&T UNIX。`mknodat()` 系统调用出现于 FreeBSD 8.0。