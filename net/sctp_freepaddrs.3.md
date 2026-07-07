# sctp_freepaddrs(3)

`sctp_freepaddrs` — 释放前一次调用所返回的内存

## 名称

`sctp_freepaddrs`, `sctp_freeladdrs`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/sctp.h>`

```c
void
sctp_freepaddrs(struct sockaddr *);

void
sctp_freeladdrs(struct sockaddr *);
```

## 描述

`sctp_freepaddrs` 和 `sctp_freeladdrs` 函数用于释放之前调用 `sctp_getpaddrs` 或 `sctp_getladdrs` 所分配的内存。

## 返回值

无。

## 参见

sctp_getladdrs(3), [sctp_getpaddrs(3)](sctp_getpaddrs.3.md), [sctp(4)](../man4/sctp.4.md)

> R. Stewart, M. Tuexen, K. Poon, P. Lei, V. Yasevich, "Sockets API Extensions for the Stream Control Transmission Protocol (SCTP)", December 2011.

## 标准

`sctp_freepaddrs` 和 `sctp_freeladdrs` 函数遵循 RFC 6458。
