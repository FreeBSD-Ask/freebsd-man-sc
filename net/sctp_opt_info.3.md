# sctp_opt_info(3)

`sctp_opt_info` — 获取 SCTP 套接字信息

## 名称

`sctp_opt_info`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/sctp.h>`

`Ft int Fn sctp_opt_info int sd sctp_assoc_t id int opt void *arg socklen_t *size`

## 描述

`sctp_opt_info` 调用提供了一种多操作系统兼容的方法，用于获取需要将关联标识传入操作系统的特定 `getsockopt` 数据。对于 FreeBSD，可以直接使用 `getsockopt`，因为 FreeBSD 能够在 `getsockopt` 调用时将信息传入操作系统。其他操作系统可能不具备此能力。对于希望在多个操作系统之间编写可移植代码的用户，应对以下 SCTP 套接字选项使用此调用。

`SCTP_RTOINFO`

`SCTP_ASSOCINFO`

`SCTP_PRIMARY_ADDR`

`SCTP_PEER_ADDR_PARAMS`

`SCTP_DEFAULT_SEND_PARAM`

`SCTP_MAX_SEG`

`SCTP_AUTH_ACTIVE_KEY`

`SCTP_DELAYED_SACK`

`SCTP_MAX_BURST`

`SCTP_CONTEXT`

`SCTP_EVENT`

`SCTP_DEFAULT_SNDINFO`

`SCTP_DEFAULT_PRINFO`

`SCTP_STATUS`

`SCTP_GET_PEER_ADDR_INFO`

`SCTP_PEER_AUTH_CHUNKS`

`SCTP_LOCAL_AUTH_CHUNKS`

## 返回值

该调用成功时返回 0，出错时返回 -1。

## 错误

`sctp_opt_info` 函数可能返回以下错误：

**`[EINVAL]`** 参数 `arg` 的值无效。

**`[EOPNOTSUPP]`** 参数 `opt` 不是上述列出的 SCTP 套接字选项之一。

**`[EBADF]`** 参数 `s` 不是有效的描述符。

**`[ENOTSOCK]`** 参数 `s` 不是套接字。

## 参见

[getsockopt(2)](../sys/getsockopt.2.md), [sctp(4)](../man4/sctp.4.md)

## 缺陷

由于 `SCTP_MAX_BURST` 套接字选项的 `arg` 所用结构在 FreeBSD 9.0 及更高版本中已更改，将 `SCTP_MAX_BURST` 用作 `opt` 仅在 FreeBSD 9.0 及更高版本中受支持。
