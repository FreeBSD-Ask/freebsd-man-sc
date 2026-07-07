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
| :------: | :------: | :--: |
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
| :------: | :------: | :--: |
| `CLSET_RETRY_TIMEOUT` | `struct timeval *` | 设置重试超时 |
| `CLGET_RETRY_TIMEOUT` | `struct timeval *` | 获取重试超时 |
| `CLSET_CONNECT` | `int *` | 使用 connect(2) |

重试超时是 RPC 在重新传输请求之前等待服务器回复的时间。`clnt_control` 函数成功时返回 `TRUE`，失败时返回 `FALSE`。

**`clnt_create`** 用于程序 `prognum` 和版本 `versnum` 的通用客户端创建例程。`host` 参数标识服务器所在的远程主机名。`nettype` 参数指示要使用的传输协议类别。传输按 `NETPATH` 环境变量中从左到右的顺序，或 netconfig 数据库中从上到下的顺序尝试。`clnt_create` 函数会尝试 `NETPATH` 环境变量和 netconfig 数据库中可用的所有 `nettype` 类传输，并选择第一个成功的。默认超时已设置，可使用 `clnt_control` 修改。该例程失败时返回 `NULL`。可使用 `clnt_pcreateerror` 例程打印失败原因。注意：即使提供给 `clnt_create` 的特定版本号未在 rpcbind(8) 服务中注册，`clnt_create` 也会返回有效的客户端句柄。这种不匹配会在稍后的 `clnt_call` 中被发现（参见 [rpc_clnt_calls(3)](rpc_clnt_calls.3.md)）。

**`clnt_create_timed`** 通用客户端创建例程，类似于 `clnt_create`，但增加了 `timeout` 参数，指定每次尝试传输类别所允许的最长时间。在其他所有方面，`clnt_create_timed` 调用的行为与 `clnt_create` 调用完全相同。

**`clnt_create_vers`** 通用客户端创建例程，类似于 `clnt_create`，但还会检查版本的可用性。`host` 参数标识服务器所在的远程主机名。`nettype` 参数指示要使用的传输协议类别。如果该例程成功，则返回为服务器支持的 `vers_low` 和 `vers_high` 之间最高版本创建的客户端句柄。`vers_outp` 参数被设置为该值。也就是说，成功返回后 `vers_low` <= `*vers_outp` <= `vers_high`。如果服务器不支持 `vers_low` 和 `vers_high` 之间的任何版本，则该例程失败并返回 `NULL`。默认超时已设置，可使用 `clnt_control` 修改。该例程失败时返回 `NULL`。可使用 `clnt_pcreateerror` 例程打印失败原因。注意：即使提供给 `clnt_create` 的特定版本号未在 rpcbind(8) 服务中注册，`clnt_create` 也会返回有效的客户端句柄。这种不匹配会在稍后的 `clnt_call` 中被发现（参见 [rpc_clnt_calls(3)](rpc_clnt_calls.3.md)）。但是，`clnt_create_vers` 会替你完成此检查，并且仅当服务器支持所提供范围内的版本时才返回有效句柄。

**`clnt_create_vers_timed`** 通用客户端创建例程，类似于 `clnt_create_vers`，但增加了 `timeout` 参数，指定每次尝试传输类别所允许的最长时间。在其他所有方面，`clnt_create_vers_timed` 调用的行为与 `clnt_create_vers` 调用完全相同。

**`clnt_destroy`** 一个函数宏，销毁客户端的 RPC 句柄。销毁通常涉及释放私有数据结构，包括 `clnt` 本身。调用 `clnt_destroy` 后，`clnt` 的使用是未定义的。如果 RPC 库打开了关联的文件描述符，或通过 `clnt_control` 设置了 `CLSET_FD_CLOSE`，则该文件描述符会被关闭。调用方应（在调用 `clnt_destroy` 之前）调用 `auth_destroy` `clnt->cl_auth` 以销毁关联的 `AUTH` 结构（参见 [rpc_clnt_auth(3)](rpc_clnt_auth.3.md)）。

**`clnt_dg_create`** 该例程为远程程序 `prognum` 和版本 `versnum` 创建 RPC 客户端；客户端使用无连接传输。远程程序位于地址 `svcaddr`。`fildes` 参数是一个已打开并绑定的文件描述符。该例程会每 15 秒重发一次调用消息，直到收到响应或调用超时。调用超时的总时间由 `clnt_call` 指定（参见 [rpc_clnt_calls(3)](rpc_clnt_calls.3.md) 中的 `clnt_call`）。重试超时和总超时时间可使用 `clnt_control` 修改。用户可通过 `sendsz` 和 `recvsz` 参数设置发送和接收缓冲区的大小；值为 0 时选择合适的默认值。该例程失败时返回 `NULL`。

**`clnt_pcreateerror`** 向标准错误打印一条消息，指示为何无法创建客户端 RPC 句柄。消息前会加上字符串 `s` 和一个冒号，末尾附加换行符。

**`clnt_spcreateerror`** 类似于 `clnt_pcreateerror`，但返回字符串而非打印到标准错误。此时消息末尾不附加换行符。警告：返回指向缓冲区的指针，该缓冲区在每次调用时会被覆盖。

**`clnt_raw_create`** 该例程为远程程序 `prognum` 和版本 `versnum` 创建 RPC 客户端句柄。用于将消息传递给服务的传输实际上是进程地址空间内的一个缓冲区，因此对应的 RPC 服务器应位于同一地址空间（参见 [rpc_svc_create(3)](rpc_svc_create.3.md) 中的 `svc_raw_create`）。这允许在没有任何内核或网络干扰的情况下模拟 RPC 并测量 RPC 开销（如往返时间）。该例程失败时返回 `NULL`。应在 `svc_raw_create` 之后调用 `clnt_raw_create`。

**`clnt_tli_create`** 该例程为远程程序 `prognum` 和版本 `versnum` 创建 RPC 客户端句柄。远程程序位于地址 `svcaddr`。如果 `svcaddr` 为 `NULL` 且为面向连接的传输，则假定文件描述符已连接。对于无连接传输，如果 `svcaddr` 为 `NULL`，则设置 `RPC_UNKNOWNADDR` 错误。`fildes` 参数是一个文件描述符，可以是已打开、已绑定和已连接的。如果为 `RPC_ANYFD`，则打开由 `netconf` 指定的传输上的文件描述符。如果 `fildes` 为 `RPC_ANYFD` 且 `netconf` 为 `NULL`，则设置 `RPC_UNKNOWNPROTO` 错误。如果 `fildes` 未绑定，则尝试绑定该描述符。用户可通过 `sendsz` 和 `recvsz` 参数指定缓冲区大小；值为 0 时选择合适的默认值。根据传输类型（面向连接或无连接），`clnt_tli_create` 调用适当的客户端创建例程。该例程失败时返回 `NULL`。可使用 `clnt_pcreateerror` 例程打印失败原因。不会查询远程 rpcbind 服务（参见 rpcbind(8)）以获取远程服务的地址。

**`clnt_tp_create`** 类似于 `clnt_create`，但 `clnt_tp_create` 仅尝试通过 `netconf` 指定的单一传输。`clnt_tp_create` 函数为程序 `prognum`、版本 `versnum` 以及由 `netconf` 指定的传输创建客户端句柄。设置默认选项，可使用 `clnt_control` 调用更改。会查询主机 `host` 上的远程 rpcbind 服务以获取远程服务的地址。该例程失败时返回 `NULL`。可使用 `clnt_pcreateerror` 例程打印失败原因。

**`clnt_tp_create_timed`** 类似于 `clnt_tp_create`，但 `clnt_tp_create_timed` 增加了 `timeout` 参数，指定创建尝试成功所允许的最长时间。在其他所有方面，`clnt_tp_create_timed` 调用的行为与 `clnt_tp_create` 调用完全相同。

**`clnt_vc_create`** 该例程为远程程序 `prognum` 和版本 `versnum` 创建 RPC 客户端；客户端使用面向连接的传输。远程程序位于地址 `svcaddr`。`fildes` 参数是一个已打开并绑定的文件描述符。用户可通过 `sendsz` 和 `recvsz` 参数指定发送和接收缓冲区的大小；值为 0 时选择合适的默认值。该例程失败时返回 `NULL`。地址 `svcaddr` 不应为 `NULL`，应指向远程程序的实际地址。`clnt_vc_create` 函数不会查询远程 rpcbind 服务以获取此信息。

`struct rpc_createerr rpc_createerr` 一个全局变量，其值由任何失败的 RPC 客户端句柄创建例程设置。`clnt_pcreateerror` 例程使用它打印失败原因。

## 参见

[rpc(3)](rpc.3.md), [rpc_clnt_auth(3)](rpc_clnt_auth.3.md), [rpc_clnt_calls(3)](rpc_clnt_calls.3.md), rpcbind(8)
