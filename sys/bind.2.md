# bind.2

`bind` — 为套接字分配本地协议地址

## 名称

`bind`

## 库

Lb libc

## 概要

`#include <sys/socket.h>`

```c
int
bind(int s, const struct sockaddr *addr, socklen_t addrlen)
```

## 描述

`bind()` 系统调用将本地协议地址分配给套接字。当通过 [socket(2)](socket.2.md) 创建套接字时，它存在于地址族空间中，但未分配协议地址。`bind()` 系统调用请求将 `addr` 分配给该套接字。

## 注释

在 UNIX 域中绑定地址会在文件系统中创建一个套接字，当不再需要时，调用者必须将其删除（使用 [unlink(2)](unlink.2.md)）。

地址绑定所用的规则因通信域而异。详细信息请参见第 4 节中的手册页。

为获得最大可移植性，在填充套接字地址结构并将其传递给 `bind()` 之前，应始终将该结构清零。

## 返回值

成功完成时，`bind()` 函数返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`bind()` 系统调用将在以下情况下失败：

**[`EAGAIN`]** 完成请求所需的内核资源暂时不可用。

**[`EBADF`]** `s` 参数不是有效的描述符。

**[`EINVAL`]** 套接字已绑定到地址，且协议不支持绑定到新地址；或套接字已关闭。

**[`EINVAL`]** `addrlen` 参数对于该地址族不是有效长度。

**[`ENOTSOCK`]** `s` 参数不是套接字。

**[`EADDRNOTAVAIL`]** 指定的地址在本地机器上不可用。

**[`EADDRINUSE`]** 指定的地址已被使用。

**[`EAFNOSUPPORT`]** 指定地址族中的地址不能与此套接字一起使用。

**[`EACCES`]** 请求的地址受保护，当前用户没有足够的权限访问它。

**[`EFAULT`]** `addr` 参数不在用户地址空间的有效部分。

以下错误特定于在 UNIX 域中绑定地址。

**[`ENOTDIR`]** 路径前缀的某个组件不是目录。

**[`ENAMETOOLONG`]** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[`ENOENT`]** 路径名的前缀组件不存在。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`EIO`]** 在创建目录项或分配 inode 时发生 I/O 错误。

**[`EINTEGRITY`]** 从文件系统读取时检测到数据损坏。

**[`EROFS`]** 该名称将位于只读文件系统上。

**[`EISDIR`]** 指定了空路径名。

## 参见

[connect(2)](connect.2.md), [getsockname(2)](getsockname.2.md), [listen(2)](listen.2.md), [socket(2)](socket.2.md)

## 历史

`bind()` 系统调用出现于 4.2BSD。
