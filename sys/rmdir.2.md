# rmdir(2)

`rmdir` — 删除目录文件

## 名称

`rmdir`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
rmdir(const char *path);
```

## 描述

`rmdir()` 系统调用删除由 `path` 指定名称的目录文件。该目录除 `.` 和 `..` 外不能有任何条目。

## 返回值

成功完成时，`rmdir()` 函数返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

除非出现以下情况，否则指定的文件将被删除：

**[`ENOTDIR`]** 路径的某个组件不是目录。

**[`ENAMETOOLONG`]** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[`ENOENT`]** 指定的目录不存在。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`ENOTEMPTY`]** 指定的目录中包含 `.` 和 `..` 以外的文件。

**[`EACCES`]** 对路径前缀的某个组件的搜索权限被拒绝。

**[`EACCES`]** 对包含要删除链接的目录的写权限被拒绝。

**[`EPERM`]** 要删除的目录设置了 immutable、undeletable 或 append-only 标志，更多信息请参见 [chflags(2)](chflags.2.md) 手册页。

**[`EPERM`]** 要删除目录的父目录设置了 immutable 或 append-only 标志。

**[`EPERM`]** 包含要删除目录的目录标记为 sticky，且包含目录和要删除的目录均非有效用户 ID 所拥有。

**[`EINVAL`]** 路径的最后一个组件是 `.` 或 `..`。

**[`EBUSY`]** 要删除的目录是已挂载文件系统的挂载点。

**[`EIO`]** 删除目录项或释放 inode 时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`EROFS`]** 要删除的目录项位于只读文件系统上。

**[`EFAULT`]** `path` 参数指向进程分配的地址空间之外。

## 参见

[mkdir(2)](mkdir.2.md), [unlink(2)](unlink.2.md)

## 历史

`rmdir()` 系统调用首次出现于 4.2BSD。
