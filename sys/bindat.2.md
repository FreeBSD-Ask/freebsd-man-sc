# bindat(2)

`bindat` — 为套接字分配本地协议地址

## 名称

`bindat`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <fcntl.h>`

```c
int
bindat(int fd, int s, const struct sockaddr *addr, socklen_t addrlen)
```

## 描述

`bindat()` 系统调用将本地协议地址分配给套接字。当在 `fd` 参数中传递特殊值 `AT_FDCWD` 时，其行为与调用 [bind(2)](bind.2.md) 相同。否则，`bindat()` 的工作方式与 [bind(2)](bind.2.md) 系统调用相同，但有以下两点例外：

- 它仅限于 `PF_LOCAL` 域中的套接字。
- 如果存储在 `sockaddr_un` 结构的 `sun_path` 字段中的文件路径是相对路径，则相对于与文件描述符 `fd` 关联的目录来定位。

## 返回值

成功完成时，`bindat()` 函数返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`bindat()` 系统调用可能失败，返回与 [bind(2)](bind.2.md) 系统调用相同的错误，或返回以下错误：

**[`EBADF`]** `sun_path` 字段未指定绝对路径，且 `fd` 参数既不是 `AT_FDCWD` 也不是有效的文件描述符。

**[`ENOTDIR`]** `sun_path` 字段不是绝对路径，且 `fd` 既不是 `AT_FDCWD` 也不是与目录关联的文件描述符。

## 参见

[bind(2)](bind.2.md), [connectat(2)](connectat.2.md), [socket(2)](socket.2.md), [unix(4)](../man4/unix.4.md)

## 作者

`bindat` 由 Pawel Jakub Dawidek <pawel@dawidek.net> 在 FreeBSD 基金会赞助下开发。
