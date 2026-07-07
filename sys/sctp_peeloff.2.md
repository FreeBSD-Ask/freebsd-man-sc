# sctp_peeloff(2)

`sctp_peeloff` — 将关联从一对多套接字分离到其自身的文件描述符

## 名称

`sctp_peeloff`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/sctp.h>`

```c
int
sctp_peeloff(int s, sctp_assoc_t id);
```

## 描述

`sctp_peeloff()` 系统调用尝试将 `id` 指定的关联分离到其自身的独立套接字。

## 返回值

调用失败时返回 -1，成功时返回新的套接字描述符。

## 错误

`sctp_peeloff()` 系统调用可能返回以下错误：

**[`ENOTCONN`]** 传递给调用的 `id` 未映射到有效的关联。

**[`E2BIG`]** 地址列表的大小超过所提供的数据量。

**[`EBADF`]** 参数 `s` 不是有效的描述符。

**[`ENOTSOCK`]** 参数 `s` 不是套接字。

## 参见

[sctp(4)](../man4/sctp.4.md)

## 标准

`sctp_peeloff()` 函数遵循 RFC 6458。
