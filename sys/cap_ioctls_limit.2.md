# cap_ioctls_limit(2)

`cap_ioctls_limit` — 管理允许的 ioctl 命令

## 名称

`cap_ioctls_limit`, `cap_ioctls_get`

## 库

Lb libc

## 概要

`#include <sys/capsicum.h>`

```c
int
cap_ioctls_limit(int fd, const unsigned long *cmds, size_t ncmds);

ssize_t
cap_ioctls_get(int fd, unsigned long *cmds, size_t maxcmds);
```

## 描述

如果文件描述符被授予 `CAP_IOCTL` 能力权限，可以通过 `cap_ioctls_limit()` 系统调用选择性地缩减（但绝不会扩展）允许的 [ioctl(2)](ioctl.2.md) 命令列表。`cmds` 参数是一个 [ioctl(2)](ioctl.2.md) 命令数组，`ncmds` 参数指定数组中的元素数量。数组中最多可以有 `256` 个元素。包含已被撤销的元素将产生错误。成功调用后，仅可使用数组中列出的命令。

可以通过 `cap_ioctls_get()` 系统调用获取给定文件描述符允许的 ioctl 命令列表。`cmds` 参数指向最多可容纳 `maxcmds` 个值的内存。该函数用最多 `maxcmds` 个元素填充所提供的缓冲区，但始终返回给定文件描述符允许的 ioctl 命令总数。可以通过传入 `NULL` 作为 `cmds` 参数、`0` 作为 `maxcmds` 参数来获取给定文件描述符的 ioctl 命令总数。如果所有 ioctl 命令都被允许（即 `CAP_IOCTL` 能力权限已分配给文件描述符，且从未对此文件描述符调用过 `cap_ioctls_limit()` 系统调用），`cap_ioctls_get()` 系统调用将返回 `CAP_IOCTLS_ALL`，并且不会修改 `cmds` 参数所指向的缓冲区。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

`cap_ioctls_get()` 函数如果成功，返回允许的 ioctl 命令总数，如果所有 ioctl 命令都被允许则返回 `CAP_IOCTLS_ALL`。失败时返回值 `-1`，并设置全局变量 `errno` 以指示错误。

## 错误

`cap_ioctls_limit()` 和 `cap_ioctls_get()` 系统调用在以下情况下会失败：

**[`EBADF`]** `fd` 参数不是有效的描述符。

**[`EFAULT`]** `cmds` 参数指向无效地址。

**[`ENOSYS`]** 运行中的内核编译时未包含 `options CAPABILITY_MODE`。

`cap_ioctls_limit()` 系统调用还可能返回以下错误：

**[`EINVAL`]** `ncmds` 参数大于 `256`。

**[`ENOTCAPABLE`]** `cmds` 将扩展允许的 [ioctl(2)](ioctl.2.md) 命令列表。

## 参见

[cap_fcntls_limit(2)](cap_fcntls_limit.2.md), [cap_rights_limit(2)](cap_rights_limit.2.md), [ioctl(2)](ioctl.2.md)

## 历史

`cap_ioctls_get()` 和 `cap_ioctls_limit()` 系统调用首次出现于 FreeBSD 8.3。对能力和能力模式的支持作为 TrustedBSD 项目的一部分开发。

## 作者

此函数由 Pawel Jakub Dawidek <pawel@dawidek.net> 在 FreeBSD 基金会赞助下创建。