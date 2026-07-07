# posix_fallocate(2)

`posix_fallocate` — 为文件中的某个范围预分配存储空间

## 名称

`posix_fallocate`

## 库

Lb libc

## 概要

```c
#include <fcntl.h>

int
posix_fallocate(int fd, off_t offset, off_t len);
```

## 描述

成功返回时，保证为 `fd` 所引用文件中 `offset` 到 `offset +` `len` 范围分配所需的存储空间。即如果 `posix_fallocate()` 成功返回，后续对指定文件数据的写入不会因文件系统存储介质上缺乏空闲空间而失败。指定范围内的任何现有文件数据不会被修改。如果 `offset +` `len` 超过当前文件大小，`posix_fallocate()` 将文件大小调整为 `offset +` `len`。否则，文件大小不会改变。

通过 `posix_fallocate()` 分配的空间会在成功调用 [creat(2)](creat.2.md) 或 [open(2)](open.2.md) 截断文件大小时被释放。通过 `posix_fallocate()` 分配的空间可能会在成功调用 [ftruncate(2)](ftruncate.2.md) 将文件大小减小到小于 `offset +` `len` 时被释放。

## 返回值

如果成功，`posix_fallocate()` 返回零。失败时返回错误码，不设置 `errno`。

## 错误

可能的失败情况：

**[EBADF]** `fd` 参数不是有效的文件描述符。

**[EBADF]** `fd` 参数引用的文件以无写权限方式打开。

**[EFBIG]** `offset +` `len` 的值大于最大文件大小。

**[EINTR]** 执行期间捕获到信号。

**[EINVAL]** `len` 参数小于或等于零，或 `offset` 参数小于零。

**[EIO]** 从文件系统读取或向文件系统写入时发生 I/O 错误。

**[EINTEGRITY]** 从文件系统读取数据时检测到损坏的数据。

**[ENODEV]** `fd` 参数不引用支持 `posix_fallocate()` 的文件。

**[ENOSPC]** 文件系统存储介质上剩余的空闲空间不足。

**[ENOTCAPABLE]** 文件描述符 `fd` 权限不足。

**[EOPNOTSUPP]** 文件系统不支持此操作。

**[ESPIPE]** `fd` 参数与管道或 FIFO 关联。

## 参见

[creat(2)](creat.2.md), [ftruncate(2)](ftruncate.2.md), [open(2)](open.2.md), [unlink(2)](unlink.2.md)

## 标准

`posix_fallocate()` 系统调用遵循 -p1003.1-2024。

## 历史

`posix_fallocate()` 函数首次出现于 FreeBSD 9.0。

早期版本的 `posix_fallocate` 使用 EINVAL 指示文件系统不支持此操作，如 IEEE Std 1003.1 ("POSIX.1") Base Specifications, Issue 7 所规定。IEEE Std 1003.1 ("POSIX.1") Base Specifications, Issue 8 改为要求对此错误情况使用 EOPNOTSUPP。ZFS 在 FreeBSD 15.0 中采用了后一种约定，base 中的其余文件系统在 FreeBSD 15.1 中采用。

## 作者

`posix_fallocate()` 及本手册页最初由 Matthew Fleming <mdf@FreeBSD.org> 编写。