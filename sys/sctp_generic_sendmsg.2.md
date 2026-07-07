# sctp_generic_sendmsg(2)

`sctp_generic_sendmsg` — 向对端发送数据

## 名称

`sctp_generic_sendmsg`, `sctp_generic_sendmsg_iov`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/sctp.h>`

```c
int
sctp_generic_sendmsg(int s, void *msg, int msglen,
    struct sockaddr *to, socklen_t len,
    struct sctp_sndrcvinfo *sinfo, int flags);

int
sctp_generic_sendmsg_iov(int s, struct iovec *iov, int iovlen,
    struct sockaddr *to, struct sctp_sndrcvinfo *sinfo, int flags);
```

## 描述

`sctp_generic_sendmsg()` 和 `sctp_generic_sendmsg_iov()` 是 [sctp_sendmsg(3)](../net/sctp_sendmsg.3.md) 和 [sctp_send(3)](../net/sctp_send.3.md) 函数调用所使用的真正系统调用。由于它们是真正的系统调用，因此效率更高，但它们是 FreeBSD 特有的，不应期望在其他任何操作系统上存在。有关详细用法，请参见 [sctp_send(3)](../net/sctp_send.3.md) 或 [sctp_sendmsg(3)](../net/sctp_sendmsg.3.md) 函数调用。

## 返回值

调用成功时返回写入的字节数，失败时返回 -1。

## 错误

**[EBADF]** 参数 `s` 不是有效的描述符。

**[ENOTSOCK]** 参数 `s` 不是套接字。

## 参见

[sctp_send(3)](../net/sctp_send.3.md), [sctp_sendmsg(3)](../net/sctp_sendmsg.3.md), [sctp_sendmsgx(3)](../net/sctp_sendmsg.3.md), [sctp_sendx(3)](../net/sctp_send.3.md), [sctp(4)](../man4/sctp.4.md)
