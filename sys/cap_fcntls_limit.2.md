# cap_fcntls_limit(2)

`cap_fcntls_limit` — 管理允许的 fcntl 命令

## 名称

`cap_fcntls_limit`, `cap_fcntls_get`

## 库

Lb libc

## 概要

`#include <sys/capsicum.h>`

```c
int
cap_fcntls_limit(int fd, uint32_t fcntlrights);

int
cap_fcntls_get(int fd, uint32_t *fcntlrightsp);
```

## 描述

如果文件描述符被授予 `CAP_FCNTL` 能力权限，可以通过 `cap_fcntls_limit()` 系统调用选择性地缩减（但绝不会扩展）允许的 [fcntl(2)](fcntl.2.md) 命令列表。

可以通过 `cap_fcntls_get()` 系统调用获取给定文件描述符允许的 fcntl 命令的位掩码。

## 标志

以下标志可以在 `fcntlrights` 参数中指定，或在 `fcntlrightsp` 参数中返回：

**`CAP_FCNTL_GETFL`** 允许 `F_GETFL` 命令。

**`CAP_FCNTL_SETFL`** 允许 `F_SETFL` 命令。

**`CAP_FCNTL_GETOWN`** 允许 `F_GETOWN` 命令。

**`CAP_FCNTL_SETOWN`** 允许 `F_SETOWN` 命令。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`cap_fcntls_limit()` 在以下情况下不会成功：

**[`EBADF`]** `fd` 参数不是有效的描述符。

**[`EINVAL`]** `fcntlrights` 中传入了无效的标志。

**[`ENOTCAPABLE`]** `fcntlrights` 将扩展允许的 [fcntl(2)](fcntl.2.md) 命令列表。

`cap_fcntls_get()` 在以下情况下不会成功：

**[`EBADF`]** `fd` 参数不是有效的描述符。

**[`EFAULT`]** `fcntlrightsp` 参数指向无效地址。

**[`ENOSYS`]** 运行中的内核编译时未包含 `options CAPABILITY_MODE`。

## 参见

[cap_ioctls_limit(2)](cap_ioctls_limit.2.md), [cap_rights_limit(2)](cap_rights_limit.2.md), [fcntl(2)](fcntl.2.md)

## 历史

`cap_fcntls_get()` 和 `cap_fcntls_limit()` 系统调用首次出现于 FreeBSD 8.3。对能力和能力模式的支持作为 TrustedBSD 项目的一部分开发。

## 作者

此函数由 Pawel Jakub Dawidek <pawel@dawidek.net> 在 FreeBSD 基金会赞助下创建。