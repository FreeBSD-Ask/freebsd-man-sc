# gai_strerror(3)

`gai_strerror` — 从 EAI_xxx 错误代码获取错误消息字符串

## 名称

`gai_strerror`

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netdb.h>`

```c
const char *
gai_strerror(int ecode);
```

## 描述

`gai_strerror` 函数返回与 [getaddrinfo(3)](getaddrinfo.3.md) 或 [getnameinfo(3)](getnameinfo.3.md) 所返回错误代码对应的错误消息字符串。

以下错误代码及其含义定义于

`#include <netdb.h>`

**`EAI_ADDRFAMILY`** 不支持主机名的地址族

**`EAI_AGAIN`** 此时无法解析名称

**`EAI_BADFLAGS`** flags 参数具有无效值

**`EAI_BADHINTS`** `hints` 的值无效

**`EAI_FAIL`** 名称解析中出现不可恢复的失败

**`EAI_FAMILY`** 未识别地址族

**`EAI_MEMORY`** 内存分配失败

**`EAI_NODATA`** 主机名未关联地址

**`EAI_NONAME`** 名称无法解析

**`EAI_OVERFLOW`** 参数缓冲区溢出

**`EAI_PROTOCOL`** 解析的协议未知

**`EAI_SERVICE`** 未识别该套接字类型的服务

**`EAI_SOCKTYPE`** 未识别预期的套接字类型

**`EAI_SYSTEM`** 系统错误在 `errno` 中返回

## 返回值

`gai_strerror` 函数返回指向与 `ecode` 对应的错误消息字符串的指针。如果 `ecode` 超出范围，返回实现定义的错误消息字符串。

## 参见

[getaddrinfo(3)](getaddrinfo.3.md), [getnameinfo(3)](getnameinfo.3.md)

## 标准

**RFC** 3493 IPv6 的基本套接字接口扩展

EAI_ADDRFAMILY 和 EAI_NODATA 出现于早期的 RFC，但不在 RFC 3493 中。它们不在 POSIX（IEEE Std 1003.1-2017）中。它们曾在 FreeBSD 5.2 之前存在，并在 14.0 中重新加入。EAI_BADHINTS、EAI_OVERFLOW 和 EAI_PROTOCOL 不在 RFC 3493 或 POSIX 中。
