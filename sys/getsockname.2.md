# getsockname(2)

`getsockname` — 获取套接字名称

## 名称

`getsockname`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

```c
int
getsockname(int s, struct sockaddr * restrict name,
    socklen_t * restrict namelen);
```

## 描述

`getsockname()` 系统调用返回指定套接字的当前 `name`。`namelen` 参数应被初始化以指示 `name` 所指向空间的大小。返回时，它包含返回名称的实际大小（以字节为单位）。

## 返回值

`getsockname()` 系统调用在成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

除非发生以下情况，否则调用将成功：

**[`EBADF`]** `s` 参数不是有效的描述符。

**[`ECONNRESET`]** 连接已被对端重置。

**[`EINVAL`]** `namelen` 参数的值无效。

**[`ENOTSOCK`]** `s` 参数是一个文件，而非套接字。

**[`ENOBUFS`]** 系统中没有足够的资源来执行该操作。

**[`EFAULT`]** `name` 参数指向的内存不在进程地址空间的有效部分。

## 参见

[bind(2)](bind.2.md), [getpeername(2)](getpeername.2.md), [socket(2)](socket.2.md)

## 历史

`getsockname()` 系统调用首次出现于 4.2BSD。

## 缺陷

在 UNIX 域中绑定到套接字的名称无法访问；`getsockname()` 返回长度为零的名称。
