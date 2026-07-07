# getpeername(2)

`getpeername` — 获取已连接对端的名称

## 名称

`getpeername`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

```c
int
getpeername(int s, struct sockaddr * restrict name,
    socklen_t * restrict namelen);
```

## 描述

`getpeername()` 系统调用返回连接到套接字 `s` 的对端名称。`namelen` 参数应被初始化为指示 `name` 所指向空间的大小。返回时，它包含返回名称的实际大小（以字节为单位）。如果提供的缓冲区太小，名称会被截断。

## 返回值

成功完成时，`getpeername()` 函数返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

除非出现以下情况，否则调用成功：

**[`EBADF`]** `s` 参数不是有效的描述符。

**[`ECONNRESET`]** 连接已被对端重置。

**[`EINVAL`]** `namelen` 参数的值无效。

**[`ENOTSOCK`]** `s` 参数是文件，不是套接字。

**[`ENOTCONN`]** 套接字未连接。

**[`ENOBUFS`]** 系统中可用于执行该操作的资源不足。

**[`EFAULT`]** `name` 参数指向的内存不在进程地址空间的有效部分。

## 参见

[accept(2)](accept.2.md), [bind(2)](bind.2.md), [getsockname(2)](getsockname.2.md), [socket(2)](socket.2.md)

## 历史

`getpeername()` 系统调用首次出现于 4.2BSD。
