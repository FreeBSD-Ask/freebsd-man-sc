# connect(2)

`connect` — 在套接字上发起连接

## 名称

`connect`

## 库

Lb libc

## 概要

`#include <sys/socket.h>`

```c
int
connect(int s, const struct sockaddr *name, socklen_t namelen);
```

## 描述

`s` 参数是一个套接字。如果它的类型为 `SOCK_DGRAM`，此调用指定套接字要关联的对端；此地址是数据报要发送到的地址，也是唯一可以从中接收数据报的地址。如果套接字的类型为 `SOCK_STREAM`，此调用尝试与另一个套接字建立连接。另一个套接字由 `name` 指定，它是套接字通信空间中的一个地址。`namelen` 指示 `name` 所指向空间的大小（以字节为单位）；`name` 的 `sa_len` 成员被忽略。每个通信空间以自己的方式解释 `name` 参数。通常，流套接字只能成功 `connect()` 一次；数据报套接字可以多次使用 `connect()` 来更改其关联。数据报套接字可以通过连接到一个无效地址（如空地址）来解除关联。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`connect()` 系统调用在以下情况下会失败：

**[`EBADF`]** `s` 参数不是有效的描述符。

**[`EINVAL`]** `namelen` 参数对于地址族不是有效长度。

**[`ENOTSOCK`]** `s` 参数是一个文件描述符，而非套接字。

**[`EADDRNOTAVAIL`]** 指定的地址在本机上不可用。

**[`EAFNOSUPPORT`]** 指定地址族中的地址不能与此套接字一起使用。

**[`EISCONN`]** 套接字已连接。

**[`ETIMEDOUT`]** 建立连接超时，未建立连接。

**[`ECONNREFUSED`]** 连接尝试被强制拒绝。

**[`ECONNRESET`]** 连接被远程主机重置。

**[`ENETUNREACH`]** 网络从本主机不可达。

**[`EHOSTUNREACH`]** 远程主机从本主机不可达。

**[`EADDRINUSE`]** 地址已被使用。

**[`EFAULT`]** `name` 参数指定了进程地址空间之外的区域。

**[`EINPROGRESS`]** 套接字是非阻塞的，且连接无法立即完成。可以通过对套接字进行写选择来 [select(2)](select.2.md) 完成检测。

**[`EINTR`]** 连接尝试被信号传递中断。连接将在后台建立，如同 `EINPROGRESS` 的情况。

**[`EALREADY`]** 先前的连接尝试尚未完成。

**[`EACCES`]** 试图通过不提供广播功能的套接字连接到广播地址（通过 `INADDR_BROADCAST` 常量或 `INADDR_NONE` 返回值获得）。

**[`EAGAIN`]** 请求了自动分配的端口号，但没有可用的自动分配端口。增大由 [sysctl(3)](../man3/sysctl.3.md) MIB 变量 `net.inet.ip.portrange.first` 和 `net.inet.ip.portrange.last` 指定的端口范围可能缓解此问题。

以下错误特定于在 UNIX 域中连接名称。这些错误在未来版本的 UNIX IPC 域中可能不适用。

**[`ENOTDIR`]** 路径前缀中的一个组件不是目录。

**[`ENAMETOOLONG`]** 路径名的一个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[`ENOENT`]** 命名的套接字不存在。

**[`EACCES`]** 对路径前缀的某个组件拒绝搜索权限。

**[`EACCES`]** 对命名的套接字拒绝写访问。

**[`ELOOP`]** 在转换路径名时遇到过多的符号链接。

**[`EPERM`]** 对命名的套接字拒绝写访问。

## 参见

[accept(2)](accept.2.md), [getpeername(2)](getpeername.2.md), [getsockname(2)](getsockname.2.md), [select(2)](select.2.md), [socket(2)](socket.2.md), [sysctl(3)](../man3/sysctl.3.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`connect()` 系统调用首次出现于 4.2BSD。