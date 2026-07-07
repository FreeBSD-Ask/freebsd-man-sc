# sctp\_bindx.3

`sctp_bindx` — 将 SCTP 套接字绑定到地址列表或从中解绑

## 名称

`sctp_bindx`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/sctp.h>`

```c
int
sctp_bindx(int s, struct sockaddr *addrs, int num, int type);
```

## 描述

`sctp_bindx` 调用将一个地址或一组地址绑定到 SCTP 端点，或从中解绑。这允许用户绑定地址的一个子集。`sctp_bindx` 调用的操作类似于 `bind`，但允许使用地址列表，并且允许绑定或解绑。参数 `s` 必须是有效的 SCTP 套接字描述符。参数 `addrs` 是用户希望绑定到套接字或从套接字解绑的地址列表（列表长度可以仅为 1）。参数 `type` 必须是以下值之一。

`SCTP_BINDX_ADD_ADDR` 此值指示需要将所列地址添加到端点。

`SCTP_BINDX_REM_ADDR` 此值指示需要从端点移除所列地址。

注意，当用户向关联添加或删除地址时，如果启用了动态地址标志 `net.inet.sctp.auto_asconf`，端点中的任何关联都将尝试将地址动态添加到现有关联。

## 返回值

调用成功时返回 0，失败时返回 -1。

## 错误

`sctp_bindx` 函数可能返回以下错误：

**`[EINVAL]`** 如果 `type` 字段不是允许的值之一（见上文），则返回此值。

**`[ENOMEM]`** 如果所添加的地址数量导致调用中的内存分配失败，则返回此值。

**`[EBADF]`** 参数 `s` 不是有效的描述符。

**`[ENOTSOCK]`** 参数 `s` 不是套接字。

## 参见

[bind(2)](../sys/bind.2.md), [sctp(4)](../man4/sctp.4.md)

> R. Stewart, M. Tuexen, K. Poon, P. Lei, V. Yasevich, "Sockets API Extensions for the Stream Control Transmission Protocol (SCTP)", December 2011.

## 标准

`sctp_bindx` 函数遵循 RFC 6458。
