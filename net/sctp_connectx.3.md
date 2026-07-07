# sctp_connectx(3)

`sctp_connectx` — 使用多个目的地址连接 SCTP 套接字

## 名称

`sctp_connectx`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/sctp.h>`

```c
int
sctp_connectx(int sd, struct sockaddr *addrs, int addrcnt,
    sctp_assoc_t *id);
```

## 描述

`sctp_connectx` 调用尝试向对端 SCTP 端点发起关联。该调用的操作类似于 `connect`，但它还提供了为对端指定多个目的地址的能力。这允许使用容错的方法发起关联。当对端的一个地址不可达时，所列的后续地址也将用于与对端建立关联。

用户还需要考虑，在 `sctp_connectx` 调用中列出的任何地址都被视为"已确认"。已确认地址是 SCTP 传输层将信任其为关联一部分的地址，并且不会向其发送带有随机 nonce 的确认心跳。

如果对端 SCTP 协议栈在其响应消息中未列出所提供的一个或多个地址，则在 `sctp_connectx` 调用中发送的额外地址将从关联中静默丢弃。成功完成后，所提供的 `id` 将填充为正在新建关联的关联标识。

## 返回值

调用成功时返回 0，失败时返回 -1。

## 错误

`sctp_connectx` 函数可能返回以下错误：

**`[EINVAL]`** 所列地址的族无效，或未提供任何地址。

**`[E2BIG]`** 地址列表的大小超出所提供的数据量。

**`[EBADF]`** 参数 `s` 不是有效的描述符。

**`[ENOTSOCK]`** 参数 `s` 不是套接字。

## 参见

[connect(2)](../sys/connect.2.md), [sctp(4)](../man4/sctp.4.md)

> R. Stewart, M. Tuexen, K. Poon, P. Lei, V. Yasevich, "Sockets API Extensions for the Stream Control Transmission Protocol (SCTP)", December 2011.

## 标准

`sctp_connectx` 函数遵循 RFC 6458。
