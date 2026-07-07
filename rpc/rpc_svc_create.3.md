# rpc_svc_create(3)

`rpc_svc_create` — 用于创建服务器句柄的库例程

## 名称

`rpc_svc_create`, `svc_control`, `svc_create`, `svc_destroy`, `svc_dg_create`, `svc_fd_create`, `svc_raw_create`, `svc_tli_create`, `svc_tp_create`, `svc_vc_create`

## 库

Lb libc

## 概要

`#include <rpc/rpc.h>`

```c
bool_t
svc_control(SVCXPRT *svc, const u_int req, void *info);

int
svc_create(void (*dispatch)(struct svc_req *, SVCXPRT *),
    const rpcprog_t prognum, const rpcvers_t versnum,
    const char *nettype);

SVCXPRT *
svc_dg_create(const int fildes, const u_int sendsz, const u_int recvsz);

void
svc_destroy(SVCXPRT *xprt);

SVCXPRT *
svc_fd_create(const int fildes, const u_int sendsz, const u_int recvsz);

SVCXPRT *
svc_raw_create(void);

SVCXPRT *
svc_tli_create(const int fildes, const struct netconfig *netconf,
    const struct t_bind *bindaddr, const u_int sendsz,
    const u_int recvsz);

SVCXPRT *
svc_tp_create(void (*dispatch)(struct svc_req *, SVCXPRT *),
    const rpcprog_t prognum, const rpcvers_t versnum,
    const struct netconfig *netconf);

SVCXPRT *
svc_vc_create(const int fildes, const u_int sendsz, const u_int recvsz);
```

## 描述

这些例程是 RPC 库的一部分，允许 C 语言程序通过网络在服务器上进行过程调用。这些例程处理服务句柄的创建。句柄创建后，可以通过调用 `svc_run` 来调用服务器。

## 例程

关于 `SVCXPRT` 数据结构的定义，参见 [rpc(3)](rpc.3.md)。

**`svc_control`** 一个用于更改或检索服务对象各种信息的函数。`req` 参数指示操作类型，`info` 是指向该信息的指针。`req` 支持的值、参数类型及其作用如下：

**`SVCGET_VERSQUIET`** 如果收到的请求针对此服务器服务的程序号，但版本号不在服务器注册的范围内，通常会返回 `RPC_PROGVERSMISMATCH` 错误。`info` 参数应是指向整数的指针。`SVCGET_VERSQUIET` 请求成功完成后，`*info` 包含一个描述服务器当前行为的整数：0 表示正常服务器行为（即返回 `RPC_PROGVERSMISMATCH` 错误）；1 表示将默默忽略超出范围的请求。

**`SVCSET_VERSQUIET`** 如果收到的请求针对此服务器服务的程序号，但版本号不在服务器注册的范围内，通常会返回 `RPC_PROGVERSMISMATCH` 错误。有时需要更改此行为。`info` 参数应是指向整数的指针，该整数要么为 0（表示正常服务器行为——返回 `RPC_PROGVERSMISMATCH` 错误），要么为 1（表示应默默忽略超出范围的请求）。

**`svc_create`** `svc_create` 函数为属于 `nettype` 类别的所有传输创建服务器句柄。`nettype` 参数定义可用于特定应用程序的传输类别。传输按 `NETPATH` 变量中从左到右的顺序，或 netconfig 数据库中从上到下的顺序尝试。如果 `nettype` 为 `NULL`，则默认为 "netpath"。`svc_create` 函数向 rpcbind 服务注册自身（参见 rpcbind(8)）。当收到针对给定 `prognum` 和 `versnum` 的远程过程调用时，调用 `dispatch` 函数；这需要调用 `svc_run`（参见 [rpc_svc_reg(3)](rpc_svc_reg.3.md) 中的 `svc_run`）。如果 `svc_create` 成功，返回它创建的服务器句柄数，否则返回 0 并记录错误消息。

**`svc_destroy`** 一个函数宏，销毁 RPC 服务句柄 `xprt`。销毁通常涉及释放私有数据结构，包括 `xprt` 本身。调用此例程后，`xprt` 的使用是未定义的。

**`svc_dg_create`** 该例程创建一个无连接 RPC 服务句柄，并返回指向它的指针。该例程失败时返回 `NULL`，并记录错误消息。`sendsz` 和 `recvsz` 参数用于指定缓冲区大小。如果为 0，则选择合适的默认值。文件描述符 `fildes` 应是已打开并绑定的。该服务器未向 rpcbind(8) 注册。警告：由于基于无连接的 RPC 消息只能容纳有限的编码数据，此传输不能用于接受大型参数或返回巨大结果的过程。

**`svc_fd_create`** 该例程在一个已打开并绑定的文件描述符之上创建服务，并返回其句柄。通常，此描述符是面向连接传输的已连接文件描述符。`sendsz` 和 `recvsz` 参数指示发送和接收缓冲区的大小。如果为 0，则选择合理的默认值。该例程失败时返回 `NULL`，并记录错误消息。

**`svc_raw_create`** 该例程创建一个 RPC 服务句柄并返回指向它的指针。传输实际上是进程地址空间内的一个缓冲区，因此对应的 RPC 客户端应位于同一地址空间（参见 [rpc_clnt_create(3)](rpc_clnt_create.3.md) 中的 `clnt_raw_create`）。此例程允许模拟 RPC 并获取 RPC 开销（如往返时间），而无需任何内核和网络干扰。该例程失败时返回 `NULL`，并记录错误消息。注意：使用原始接口时不应调用 `svc_run`。

**`svc_tli_create`** 该例程创建一个 RPC 服务器句柄，并返回指向它的指针。`fildes` 参数是服务正在监听的文件描述符。如果 `fildes` 为 `RPC_ANYFD`，则打开由 `netconf` 指定的传输上的文件描述符。如果文件描述符未绑定且 `bindaddr` 不为 `NULL`，则将 `fildes` 绑定到 `bindaddr` 指定的地址，否则将 `fildes` 绑定到由传输选择的默认地址。注意：`t_bind` 结构来自 TLI/XTI SysV 接口，NetBSD 不使用此接口。该结构在 `<rpc/types.h>` 中定义为兼容形式：

```c
struct t_bind {
    struct netbuf addr;	/* 网络地址，参见 rpc(3) */
    unsigned int  qlen;	/* 队列长度（用于 listen(2)） */
};
```

在选择默认地址的情况下，对于面向连接的传输，未决连接请求数设置为 8。用户可以通过 `sendsz` 和 `recvsz` 参数指定发送和接收缓冲区的大小；值为 0 时选择合适的默认值。该例程失败时返回 `NULL`，并记录错误消息。该服务器未向 rpcbind(8) 服务注册。

**`svc_tp_create`** `svc_tp_create` 函数为 `netconf` 指定的网络创建服务器句柄，并向 rpcbind 服务注册自身。当收到针对给定 `prognum` 和 `versnum` 的远程过程调用时，调用 `dispatch` 函数；这需要调用 `svc_run`。`svc_tp_create` 函数成功时返回服务句柄，否则返回 `NULL` 并记录错误消息。

**`svc_vc_create`** 该例程创建一个面向连接的 RPC 服务并返回指向它的指针。该例程失败时返回 `NULL`，并记录错误消息。用户可以通过 `sendsz` 和 `recvsz` 参数指定发送和接收缓冲区的大小；值为 0 时选择合适的默认值。文件描述符 `fildes` 应是已打开并绑定的。该服务器未向 rpcbind(8) 服务注册。

## 参见

[rpc(3)](rpc.3.md), [rpc_svc_calls(3)](rpc_svc_calls.3.md), [rpc_svc_err(3)](rpc_svc_err.3.md), [rpc_svc_reg(3)](rpc_svc_reg.3.md), rpcbind(8)
