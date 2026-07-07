# sctp_getassocid(3)

`sctp_getassocid` — 返回指定套接字地址的关联 ID

## 名称

`sctp_getassocid`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/sctp.h>`

```c
sctp_assoc_t
sctp_getassocid(int s, struct sockaddr *addr);
```

## 描述

`sctp_getassocid` 调用尝试查找指定的套接字地址 `addr`，并找到相应的关联标识。

## 返回值

调用成功时返回关联 ID，失败时返回 0。

## 错误

`sctp_getassocid` 函数可能返回以下错误：

**`[ENOENT]`** 该地址未设置关联。

**`[EBADF]`** 参数 `s` 不是有效的描述符。

**`[ENOTSOCK]`** 参数 `s` 不是套接字。

## 参见

[sctp(4)](../man4/sctp.4.md)
