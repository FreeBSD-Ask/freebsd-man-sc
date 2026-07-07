# copy_file_range(2)

`copy_file_range` — 在内核中将一个普通文件的字节范围复制到另一个普通文件或同一普通文件内

## 名称

`copy_file_range`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <unistd.h>`

```c
ssize_t
copy_file_range(int infd, off_t *inoffp, int outfd,
    off_t *outoffp, size_t len, unsigned int flags);
```

## 描述

`copy_file_range()` 系统调用在内核中从 `infd` 向 `outfd` 复制最多 `len` 字节。如果 `infd` 和 `outfd` 位于同一文件系统上，它可能使用文件系统特定的技术来完成此操作。如果 `infd` 和 `outfd` 引用同一文件，则由输入文件偏移量、输出文件偏移量和 `len` 定义的字节范围不能重叠。`infd` 参数必须以读取方式打开，`outfd` 参数必须以写入方式打开，但不能是 `O_APPEND`。

如果 `inoffp` 或 `outoffp` 为 `NULL`，则分别使用 `infd` 或 `outfd` 的文件偏移量，并按复制的字节数更新。如果 `inoffp` 或 `outoffp` 不为 `NULL`，则分别使用 `inoffp` 或 `outoffp` 所指向的字节偏移量并进行更新，而 `infd` 或 `outfd` 的文件偏移量分别不受影响。

当前定义的唯一 `flags` 参数是 `COPY_FILE_RANGE_CLONE`。设置此标志时，如果无法通过块克隆完成复制，`copy_file_range()` 将返回 `EOPNOTSUPP`。当 `flags` 为 0 时，文件系统可通过块克隆或数据复制来完成复制。仅当偏移量（如果未到输入文件末尾，还包括 `len`）按块对齐时，块克隆才可能实现。正确的块对齐通常可通过 [pathconf(2)](pathconf.2.md) 的 `_PC_CLONE_BLKSIZE` 查询获得。

此系统调用尝试在输出文件中为正在复制的字节范围保留空洞。然而，这并不总是能很好地工作。建议使用 [lseek(2)](lseek.2.md) 的 `SEEK_HOLE`、`SEEK_DATA` 参数以及此系统调用在一个循环中复制稀疏文件中找到的数据范围。

为获得最佳性能，应以尽可能大的 `len` 值调用 `copy_file_range()`。在大多数文件系统上它可被中断，因此使用非常大的 len 值（甚至 SSIZE_MAX）也不会有不利影响。

## 返回值

如果成功，该调用返回复制的字节数，可能少于 `len`。返回少于 `len` 的字节数并不一定表示已到达 EOF。然而，对于非零的 `len` 参数返回零表示 `infd` 的偏移量已到达或超过 EOF。应在循环中使用 `copy_file_range()`，直到完成所需字节范围的复制。如果发生错误，返回 -1，并将错误代码放入全局变量 `errno` 中。

## 错误

`copy_file_range()` 系统调用在以下情况下会失败：

**[`EBADF`]** `infd` 未以读取方式打开，或 `outfd` 未以写入方式打开，或以 `O_APPEND` 写入方式打开，或 `infd` 和 `outfd` 引用同一文件。

**[`EFBIG`]** 复制超出进程的文件大小限制或 `outfd` 所在文件系统的最大文件大小。

**[`EINTR`]** 系统调用在完成之前被信号中断。这可能发生在某些 NFS 挂载的文件上。发生此情况时，`inoffp` 和 `outoffp` 所指向的值将重置为该系统调用的初始值。

**[`EINVAL`]** `infd` 和 `outfd` 引用同一文件且字节范围重叠。

**[`EINVAL`]** `flags` 参数不为零。

**[`EINVAL`]** `infd` 或 `outfd` 引用的文件对象不是普通文件。

**[`EIO`]** 读取/写入文件时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`EISDIR`]** `infd` 或 `outfd` 引用的是目录。

**[`ENOSPC`]** 存储 `outfd` 的文件系统已满。

**[`EOPNOTSUPP`]** 无法通过块克隆完成复制，且指定了 `COPY_FILE_RANGE_CLONE` `flags` 参数。

## 参见

[lseek(2)](lseek.2.md), [pathconf(2)](pathconf.2.md)

## 标准

`copy_file_range()` 系统调用预期与同名的 Linux 系统调用兼容。

## 历史

`copy_file_range()` 函数出现于 FreeBSD 13.0。
