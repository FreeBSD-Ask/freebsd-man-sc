# sctp_generic_recvmsg(2)

`sctp_generic_recvmsg` — 从对端接收数据

## 名称

`sctp_generic_recvmsg`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/sctp.h>`

```c
int
sctp_generic_recvmsg(int s, struct iovec *iov, int iovlen,
    struct sockaddr *from, socklen_t *fromlen,
    struct sctp_sndrcvinfo *sinfo, int *msgflags);
```

## 描述

`sctp_generic_recvmsg()` 是 [sctp_recvmsg(3)](../net/sctp_recvmsg.3.md) 函数调用所使用的真正系统调用。此调用更高效，因为它是真正的系统调用，但它是 FreeBSD 特有的，不能期望在其他操作系统上存在。详细用法请参见 [sctp_recvmsg(3)](../net/sctp_recvmsg.3.md) 函数调用。

## 返回值

调用成功时返回读取的字节数，失败时返回 -1。

## 错误

**[`EBADF`]** `s` 参数不是有效的描述符。

**[`ENOTSOCK`]** `s` 参数不是套接字。

## 参见

[sctp_recvmsg(3)](../net/sctp_recvmsg.3.md), [sctp(4)](../man4/sctp.4.md)
