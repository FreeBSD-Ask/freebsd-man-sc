# byteorder.3

`htonl` — 在主机与网络字节顺序之间转换值

## 名称

`htonl`, `htons`, `ntohl`, `ntohs`

## 库

libc

## 概要

`#include <arpa/inet.h>`

或

`#include <netinet/in.h>`

```c
uint32_t
htonl(uint32_t hostlong);

uint16_t
htons(uint16_t hostshort);

uint32_t
ntohl(uint32_t netlong);

uint16_t
ntohs(uint16_t netshort);
```

## 描述

这些例程在 16 和 32 位量的网络字节顺序与主机字节顺序之间进行转换。在字节顺序与网络顺序相同的机器上，这些例程定义为空宏。

这些例程最常与 [gethostbyname(3)](gethostbyname.3.md) 和 [getservent(3)](getservent.3.md) 返回的 Internet 地址和端口一起使用。

## 参见

[gethostbyname(3)](gethostbyname.3.md), [getservent(3)](getservent.3.md), [byteorder(9)](../man9/byteorder.9.md)

## 标准

`byteorder` 函数遵循 IEEE Std 1003.1-2001（"POSIX.1"）。

## 历史

`byteorder` 函数出现于 4.2BSD。

## 缺陷

在 VAX 上，字节的处理方式与世界上大多数其他系统相反。预计在近期不会修复此问题。
