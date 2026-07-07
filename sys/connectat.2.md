# connectat(2)

`connectat` — 在套接字上发起连接

## 名称

`connectat`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <fcntl.h>`

```c
int
connectat(int fd, int s, const struct sockaddr *name,
    socklen_t namelen);
```

## 描述

`connectat()` 系统调用在套接字 `s` 上发起连接。当在 `fd` 参数中传入特殊值 `AT_FDCWD` 时，其行为与调用 [connect(2)](connect.2.md) 相同。否则，`connectat()` 的工作方式类似于 [connect(2)](connect.2.md) 系统调用，但有两个例外：

1. 它仅限于 PF_LOCAL 域中的套接字。
2. 如果存储在 sockaddr_un 结构的 `sun_path` 字段中的文件路径是相对路径，则该路径相对于与文件描述符 `fd` 关联的目录来定位。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`connectat()` 系统调用可能因与 [connect(2)](connect.2.md) 系统调用相同的错误而失败，或因以下错误而失败：

**[`EBADF`]** `sun_path` 字段未指定绝对路径，且 `fd` 参数既不是 `AT_FDCWD` 也不是有效的文件描述符。

**[`ENOTDIR`]** `sun_path` 字段不是绝对路径，且 `fd` 既不是 `AT_FDCWD` 也不是与目录关联的文件描述符。

## 参见

[bindat(2)](bindat.2.md), [connect(2)](connect.2.md), [socket(2)](socket.2.md), [unix(4)](../man4/unix.4.md)

## 作者

`connectat` 由 Pawel Jakub Dawidek <pawel@dawidek.net> 在 FreeBSD 基金会赞助下开发。