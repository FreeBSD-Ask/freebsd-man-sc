# shutdown(2)

`shutdown` — 禁用套接字上的发送和/或接收

## 名称

`shutdown`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

```c
int
shutdown(int s, int how);
```

## 描述

`shutdown()` 系统调用禁用套接字上的发送或接收。`how` 参数指定关闭的类型。可能的值有：

**`SHUT_RD`** 禁止进一步接收。

**`SHUT_WR`** 禁止进一步发送。这可能引发与套接字 `s` 的协议族相关的特定操作；参见[实现说明](#实现说明)。

**`SHUT_RDWR`** 禁止进一步发送和接收。隐含 `SHUT_WR`。

如果文件描述符 `s` 关联的是 `SOCK_STREAM` 套接字，全双工连接的全部或部分将被关闭。

## 实现说明

根据与文件描述符 `s` 关联的套接字属性，以下协议特定操作适用于 `SHUT_WR`（可能也包括 `SHUT_RDWR`）的使用。

| 域 | 类型 | 协议 | 动作 |
| --- | --- | --- | --- |
| `PF_INET` | `SOCK_DGRAM` | `IPPROTO_SCTP` | 失败，因为套接字未连接。 |
| `PF_INET` | `SOCK_DGRAM` | `IPPROTO_UDP` | 失败，因为套接字未连接。 |
| `PF_INET` | `SOCK_STREAM` | `IPPROTO_SCTP` | 发送排队数据并拆除关联。 |
| `PF_INET` | `SOCK_STREAM` | `IPPROTO_TCP` | 发送排队数据，等待 ACK，然后发送 FIN。 |
| `PF_INET6` | `SOCK_DGRAM` | `IPPROTO_SCTP` | 失败，因为套接字未连接。 |
| `PF_INET6` | `SOCK_DGRAM` | `IPPROTO_UDP` | 失败，因为套接字未连接。 |
| `PF_INET6` | `SOCK_STREAM` | `IPPROTO_SCTP` | 发送排队数据并拆除关联。 |
| `PF_INET6` | `SOCK_STREAM` | `IPPROTO_TCP` | 发送排队数据，等待 ACK，然后发送 FIN。 |

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`shutdown()` 系统调用在以下情况下会失败：

**[`EBADF`]** `s` 参数不是有效的文件描述符。

**[`EINVAL`]** `how` 参数无效。

**[`ENOTCONN`]** `s` 参数指定了一个未连接的套接字。

**[`ENOTSOCK`]** `s` 参数不引用套接字。

## 参见

[connect(2)](connect.2.md), [socket(2)](socket.2.md), [inet(4)](../man4/inet.4.md), [inet6(4)](../man4/inet6.4.md)

## 标准

`shutdown()` 系统调用预期在最终定稿时遵循 -p1003.1g-2000。

## 历史

`shutdown()` 系统调用出现于 4.2BSD。`SHUT_RD`、`SHUT_WR` 和 `SHUT_RDWR` 常量出现于 -p1003.1g-2000。

## 作者

本手册页由 Bruce M. Simpson <bms@FreeBSD.org> 更新，以反映 `shutdown()` 在 `PF_INET` 和 `PF_INET6` 套接字上的行为。

## 缺陷

在 `shutdown()` 被调用后，对于 `s` 所绑定的本地端口上接收到的数据报，应生成 ICMP “`port unreachable`” 消息作为响应。
