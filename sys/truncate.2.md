# truncate(2)

`truncate` — 将文件截断或扩展到指定长度

## 名称

`truncate`, `ftruncate`

## 库

Lb libc

## 概要

```c
#include <unistd.h>

int
truncate(const char *path, off_t length);

int
ftruncate(int fd, off_t length);
```

## 描述

`truncate()` 系统调用将 `path` 命名或 `fd` 引用的文件截断或扩展到 `length` 字节大小。如果文件原本大于此大小，多余的数据将丢失。如果文件原本小于此大小，将通过写入值为零的字节来扩展。

`ftruncate()` 系统调用将支撑文件描述符 `fd` 的文件或共享内存对象截断或扩展到 `length` 字节大小。该文件描述符必须是有效的、以写入方式打开的文件描述符。与文件描述符 `fd` 关联的文件位置指针不会被修改。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。如果要修改的文件不是目录或常规文件，`truncate()` 调用无效并返回值 0。

## 错误

`truncate()` 系统调用在以下情况下失败：

**[`ENOTDIR`]** 路径前缀的某个组件不是目录。

**[`ENAMETOOLONG`]** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[`ENOENT`]** 指定的文件不存在。

**[`EACCES`]** 路径前缀的某个组件拒绝搜索权限。

**[`EACCES`]** 指定的文件对用户不可写。

**[`ELOOP`]** 在翻译路径名时遇到过多的符号链接。

**[`EPERM`]** 指定的文件设置了不可变或仅追加标志，更多信息参见 [chflags(2)](chflags.2.md) 手册页。

**[`EISDIR`]** 指定的文件是目录。

**[`EROFS`]** 指定的文件位于只读文件系统上。

**[`ETXTBSY`]** 该文件是正在执行的纯过程（共享文本）文件。

**[`EFBIG`]** `length` 参数大于最大文件大小。

**[`EINVAL`]** `length` 参数小于 0。

**[`EIO`]** 更新 inode 时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到损坏的数据。

**[`EFAULT`]** `path` 参数指向进程分配地址空间之外。

`ftruncate()` 系统调用在以下情况下失败：

**[`EBADF`]** `fd` 参数不是有效的描述符。

**[`EINVAL`]** `fd` 参数引用的文件描述符不是常规文件或共享内存对象。

**[`EINVAL`]** `fd` 描述符未以写入方式打开。

## 参见

[chflags(2)](chflags.2.md), [open(2)](open.2.md), [shm_open(2)](shm_open.2.md)

## 历史

`truncate()` 和 `ftruncate()` 系统调用出现于 4.2BSD。

## 缺陷

这些调用应当泛化，以允许丢弃文件中字节范围的数据。

历史上，使用 `truncate()` 或 `ftruncate()` 扩展文件并不可移植，但此行为在 IEEE Std 1003.1-2008 ("POSIX.1") 中成为必需。
