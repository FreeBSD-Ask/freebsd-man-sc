# socketpair(2)

`socketpair` — 创建一对已连接的套接字

## 名称

`socketpair`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

```c
int
socketpair(int domain, int type, int protocol, int *sv);
```

## 描述

`socketpair()` 系统调用在指定通信 `domain` 中创建一对未命名的已连接套接字，使用指定的 `type` 和可选指定的 `protocol`。引用新套接字所用的描述符在 `sv`[0] 和 `sv`[1] 中返回。这两个套接字无法区分。

`type` 参数中的 `SOCK_CLOEXEC`、`SOCK_CLOFORK` 和 `SOCK_NONBLOCK` 标志适用于两个描述符。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

除非出现以下情况，否则调用成功：

**[`EMFILE`]** 该进程使用了过多的描述符。

**[`EAFNOSUPPORT`]** 本机不支持指定的地址族。

**[`EPROTONOSUPPORT`]** 本机不支持指定的协议。

**[`EOPNOTSUPP`]** 指定的协议不支持创建套接字对。

**[`EFAULT`]** 地址 `sv` 未指定进程地址空间的有效部分。

## 参见

[pipe(2)](pipe.2.md), [read(2)](read.2.md), [socket(2)](socket.2.md), [write(2)](write.2.md)

## 标准

`socketpair()` 系统调用遵循 IEEE Std 1003.1-2001 ("POSIX.1") 和 IEEE Std 1003.1-2008 ("POSIX.1")。

## 历史

`socketpair()` 系统调用出现于 4.2BSD。

## 缺陷

此调用目前仅针对 UNIX 域实现。
