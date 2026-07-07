# sctp_getaddrlen(3)

`sctp_getaddrlen` — 返回地址族的地址长度

## 名称

`sctp_getaddrlen`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/sctp.h>`

```c
int
sctp_getaddrlen(sa_family_t family);
```

## 描述

`sctp_getaddrlen` 函数返回特定地址族的大小。提供此函数是为了应用程序的二进制兼容性，因为它向应用程序提供了操作系统所认为的特定地址族的大小。注意，该函数实际上会创建一个 SCTP 套接字，然后通过 `getsockopt` 系统调用收集信息。如果由于某种原因无法创建 SCTP 套接字或 `getsockopt` 调用失败，将返回错误，并按照 `socket` 或 `getsockopt` 系统调用中的规定设置 `errno`。

## 返回值

调用返回操作系统期望的特定地址族的字节数，或 -1。

## 错误

`sctp_getaddrlen` 函数可能返回以下错误：

**`[EINVAL]`** 指定的地址族不存在。

## 参见

[getsockopt(2)](../sys/getsockopt.2.md), [socket(2)](../sys/socket.2.md), [sctp(4)](../man4/sctp.4.md)
