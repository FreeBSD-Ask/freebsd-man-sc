# getdirentries(2)

`getdirentries` — 以文件系统无关的格式获取目录项

## 名称

`getdirentries`, `getdents`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <dirent.h>`

```c
ssize_t
getdirentries(int fd, char *buf, size_t nbytes, off_t *basep);

ssize_t
getdents(int fd, char *buf, size_t nbytes);
```

## 描述

`getdirentries()` 和 `getdents()` 系统调用以文件系统无关的格式，从文件描述符 `fd` 所引用的目录中读取目录项到 `buf` 所指向的缓冲区。最多将传输 `nbytes` 字节的数据。`nbytes` 参数必须大于或等于与该文件关联的块大小，参见 [stat(2)](stat.2.md)。某些文件系统可能不支持使用小于此大小的缓冲区进行这些系统调用。

缓冲区中的数据是一系列 `dirent` 结构，每个结构包含以下条目：

```c
ino_t     d_fileno;
off_t     d_off;
uint16_t  d_reclen;
uint8_t   d_type;
uint16_t  d_namlen;
char      d_name[MAXNAMLEN + 1];	/* 见下文 */
```

`d_fileno` 条目是文件系统中每个不同文件唯一的编号。通过硬链接链接的文件（参见 [link(2)](link.2.md)）具有相同的 `d_fileno`。`d_off` 字段返回一个 cookie，如果非零，可与 [lseek(2)](lseek.2.md) 一起使用以将目录描述符定位到下一个条目。`d_reclen` 条目是目录记录的长度（以字节为单位）。`d_type` 条目是目录记录所指向文件的类型。文件类型值定义在 `<sys/dirent.h>` 中。`d_name` 条目包含一个以 null 结尾的文件名。`d_namlen` 条目指定文件名长度，不包括 null 字节。因此 `d_name` 的实际大小可能从 1 到 `MAXNAMLEN` + 1 不等。

条目之间可能由额外空间分隔。`d_reclen` 条目可用作从一个 `dirent` 结构起始处到下一个结构（如果有）的偏移量。

返回实际传输的字节数。与 `fd` 关联的当前位置指针被设置为指向下一个条目块。该指针可能不会按 `getdirentries()` 或 `getdents()` 返回的字节数前进。当到达目录末尾时返回零值。

如果 `basep` 指针值非 NULL，`getdirentries()` 系统调用将所读取块的位置写入 `basep` 所指向的位置。或者，当前位置指针可通过 [lseek(2)](lseek.2.md) 设置和获取。当前位置指针仅应设置为 [lseek(2)](lseek.2.md) 返回的值、`basep` 所指向位置返回的值（仅 `getdirentries()`）、非零时 `d_off` 字段返回的值，或零。

## 实现说明

`d_off` 字段目前由 NFS 客户端设置为 0，因为 NFS 服务器返回的目录偏移 cookie 此时无法被 [lseek(2)](lseek.2.md) 使用。

## 返回值

如果成功，返回实际传输的字节数。否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`getdirentries()` 系统调用在以下情况下会失败：

**[`EBADF`]** `fd` 参数不是为读取打开的有效文件描述符。

**[`EFAULT`]** `buf` 或非 NULL 的 `basep` 指向已分配地址空间之外。

**[`EINVAL`]** `nbytes` 的值对于返回目录条目或条目块太小，或当前位置指针无效。

**[`EIO`]** 在向文件系统读取或写入时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`ENOENT`]** 目录已被取消链接但仍然打开。

**[`ENOTDIR`]** `fd` 所引用的文件不是目录。

## 参见

[lseek(2)](lseek.2.md), [open(2)](open.2.md), [directory(3)](../man3/directory.3.md), [dir(5)](../man5/dir.5.md)

## 历史

`getdirentries()` 系统调用首次出现于 4.4BSD。`getdents()` 系统调用首次出现于 FreeBSD 3.0。