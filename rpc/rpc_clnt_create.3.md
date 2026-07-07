# rpc_clnt_create(3)

`rpc_clnt_create` — 用于创建和操作 `CLIENT` 句柄的库例程

## 名称

`rpc_clnt_create`, `clnt_control`, `clnt_create`, `clnt_create_timed`, `clnt_create_vers`, `clnt_create_vers_timed`, `clnt_destroy`, `clnt_dg_create`, `clnt_pcreateerror`, `clnt_raw_create`, `clnt_spcreateerror`, `clnt_tli_create`, `clnt_tp_create`, `clnt_tp_create_timed`, `clnt_vc_create`, `rpc_createerr` —— `CLIENT` 句柄

## 库

Lb libc

## 概要

`#include <rpc/rpc.h>`

```c
bool_t
clnt_control(CLIENT *clnt, const u_int req, char *info);

CLIENT *
clnt_create(const char *host, const rpcprog_t prognum,
    const rpcvers_t versnum, const char *nettype);

CLIENT *
clnt_create_timed(const char *host, const rpcprog_t prognum,
    const rpcvers_t versnum, const char *nettype,
    const struct timeval *timeout);

CLIENT *
clnt_create_vers(const char *host, const rpcprog_t prognum,
    rpcvers_t *vers_outp, const rpcvers_t vers_low,
    const rpcvers_t vers_high, const char *nettype);

CLIENT *
clnt_create_vers_timed(const char *host, const rpcprog_t prognum,
    rpcvers_t *vers_outp, const rpcvers_t vers_low,
    const rpcvers_t vers_high, const char *nettype,
    const struct timeval *timeout);

void
clnt_destroy(CLIENT *clnt);

CLIENT *
clnt_dg_create(const int fildes, const struct netbuf *svcaddr,
    const rpcprog_t prognum, const rpcvers_t versnum,
    const u_int sendsz, const u_int recvsz);

void
clnt_pcreateerror(const char *s);

char *
clnt_spcreateerror(const char *s);

CLIENT *
clnt_raw_create(const rpcprog_t prognum, const rpcvers_t versnum);

CLIENT *
clnt_tli_create(const int fildes, const struct netconfig *netconf,
    struct netbuf *svcaddr, const rpcprog_t prognum,
    const rpcvers_t versnum, const u_int sendsz, const u_int recvsz);

CLIENT *
clnt_tp_create(const char *host, const rpcprog_t prognum,
    const rpcvers_t versnum, const struct netconfig *netconf);

CLIENT *
clnt_tp_create_timed(const char *host, const rpcprog_t prognum,
    const rpcvers_t versnum, const struct netconfig *netconf,
    const struct timeval *timeout);

CLIENT *
clnt_vc_create(const int fildes, const struct netbuf *svcaddr,
    const rpcprog_t prognum, const rpcvers_t versnum,
    u_int sendsz, u_int recvsz);
```

## 描述

RPC 库例程允许 C 语言程序通过网络在其他机器上进行过程调用。首先创建一个 `CLIENT` 句柄，然后客户端调用一个过程向服务器发送请求。服务器收到请求后，调用一个分发例程来执行所请求的服务，然后发回回复。

## 例程

**`clnt_control`** 一个函数宏，用于更改或检索客户端对象的各种信息。`req` 参数指示操作类型，`info` 是指向该信息的指针。对于无连接和面向连接的传输，`req` 支持的值及其参数类型和作用如下：

| `req` 值 | 参数类型 | 说明 |
| :--- | :--- | :--- |
| `CLSET_TIMEOUT` | `struct timeval *` | 设置总超时 |
| `CLGET_TIMEOUT` | `struct timeval *` | 获取总超时 |
| `CLGET_SVC_ADDR` | `struct netbuf *` | 获取服务器地址 |
| `CLGET_FD` | `int *` | 从句柄获取文件描述符 |
| `CLSET_FD_CLOSE` | `void` | 销毁时关闭文件描述符 |
| `CLSET_FD_NCLOSE` | `void` | 销毁时不关闭文件描述符 |
| `CLGET_VERS` | `uint32_t *` | 获取 RPC 程序版本 |
| `CLSET_VERS` | `uint32_t *` | 设置 RPC 程序版本 |
| `CLGET_XID` | `uint32_t *` | 获取上次调用的 XID |
| `CLSET_XID` | `uint32_t *` | 设置下次调用的 XID |

注意：如果通过 `clnt_control` 设置超时，则在后续所有调用中，`clnt_call` 所传递的超时参数会被忽略。注意：如果将超时值设置为 0，`clnt_control` 会立即返回错误（`RPC_TIMEDOUT`）。对于批量调用，可将超时参数设置为 0。

以下操作仅适用于无连接传输：

| `req` 值 | 参数类型 | 说明 |
| :--- | :--- | :--- |
| `CLSET_RETRY_TIMEOUT` | `struct timeval *` | 设置重试超时 |
| `CLGET_RETRY_TIMEOUT` | `struct timeval *` | 获取重试超时 |
| `CLSET_CONNECT` | `int *` | 使用 connect(2) |

重试超时是 RPC 在重新传输请求之前等待服务器回复的时间。`clnt_control` 函数成功时返回 `TRUE`，失败时返回 `FALSE`。

**`clnt_create`** 用于程序 `prognum` 和版本 `versnum` 的通用客户端创建例程。`host` 参数标识服务器所在的远程主机名。`nettype` 参数指示要使用的传输协议类别。传输按 `NETPATH` 环境变量中从左到右的顺序，或 netconfig 数据库中从上到下的顺序尝试。`clnt_create` 函数会尝试 `NETPATH` 环境变量和 netconfig 数据库中可用的所有 `nettype` 类传输，并选择第一个成功的。默认超时已设置，可使用 `clnt_control` 修改。该例程失败时返回 `NULL`。可使用 `clnt_pcreateerror` 例程打印失败原因。注意：即使提供给 `clnt_create` 的特定版本号未在 rpcbind(8) 服务中注册，`clnt_create` 也会返回有效的客户端句柄。这种不匹配会在稍后的 `clnt_call` 中被发现（参见 [rpc_clnt_calls(3)](rpc_clnt_calls.3.md)）。

**`clnt_create_timed`** 通用客户端创建例程，类似于 `clnt_create`，但增加了 `timeout` 参数，指定每次尝试传输类别所允许的最长时间。在其他所有方面，`clnt_create_timed` 调用的行为与 `clnt_create` 调用完全相同。

**`clnt_create_vers`** 通用客户端创建例程，类似于 `clnt_create`，但还会检查版本的可用性。`host` 参数标识服务器所在的远程主机名。`nettype` 参数指示要使用的传输协议类别。如果该例程成功，则返回为服务器支持的 `vers_low` 和 `vers_high` 之间最高版本创建的客户端句柄。`vers_outp` 参数被设置为该值。也就是说，成功返回后 `vers_low` <= `*vers_outp` <= `vers_high`。如果服务器不支持 `vers_low` 和 `vers_high` 之间的任何版本，则该例程失败并返回 `NULL`。默认超时已设置，可使用 `clnt_control` 修改。该例程失败时返回 `NULL`。可使用 `clnt_pcreateerror` 例程打印失败原因。注意：即使提供给 `clnt_create` 的特定版本号未在 rpcbind(8) 服务中