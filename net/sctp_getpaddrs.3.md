# sctp_getpaddrs(3)

`sctp_getpaddrs` — 向调用者返回地址列表

## 名称

`sctp_getpaddrs`, `sctp_getladdrs`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/sctp.h>`

```c
int
sctp_getpaddrs(int s, sctp_assoc_t asocid, struct sockaddr **addrs);

int
sctp_getladdrs(int s, sctp_assoc_t asocid, struct sockaddr **addrs);
```

## 描述

`sctp_getpaddrs` 函数用于获取对端地址列表。`sctp_getladdrs` 函数用于获取本地地址列表。感兴趣的关联由 `asocid` 参数标识。成功时，地址在参数 `addrs` 中返回的一个新分配的套接字地址数组中。

调用者使用完毕后，应使用 `sctp_freepaddrs` 或 `sctp_freeladdrs` 函数释放这些调用所分配的内存。

## 返回值

失败时返回 -1，成功时返回 `addrs` 中返回的地址计数。

## 错误

这些函数可能返回以下错误：

**`[EINVAL]`** 所列地址的族无效，或未提供任何地址。

**`[ENOMEM]`** 调用无法分配内存来容纳套接字地址。

**`[EBADF]`** 参数 `s` 不是有效的描述符。

**`[ENOTSOCK]`** 参数 `s` 不是套接字。

## 参见

[getsockopt(2)](../sys/getsockopt.2.md), sctp_freeladdrs(3), [sctp_freepaddrs(3)](sctp_freepaddrs.3.md), [sctp(4)](../man4/sctp.4.md)

> R. Stewart, M. Tuexen, K. Poon, P. Lei, V. Yasevich, "Sockets API Extensions for the Stream Control Transmission Protocol (SCTP)", December 2011.

## 标准

`sctp_getpaddrs` 和 `sctp_getladdrs` 函数遵循 RFC 6458。
