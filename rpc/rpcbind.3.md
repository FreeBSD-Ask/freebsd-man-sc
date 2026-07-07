# rpcbind(3)

`rpcbind` — RPC 绑定服务的库例程

## 名称

`rpcb_getmaps`, `rpcb_getaddr`, `rpcb_gettime`, `rpcb_rmtcall`, `rpcb_set`, `rpcb_unset`

## 库

Lb libc

## 概要

`#include <rpc/rpc.h>`

```c
rpcblist *
rpcb_getmaps(const struct netconfig *netconf, const char *host);

bool_t
rpcb_getaddr(const rpcprog_t prognum, const rpcvers_t versnum,
    const struct netconfig *netconf, struct netbuf *svcaddr,
    const char *host);

bool_t
rpcb_gettime(const char *host, time_t *timep);

enum clnt_stat
rpcb_rmtcall(const struct netconfig *netconf, const char *host,
    const rpcprog_t prognum, const rpcvers_t versnum,
    const rpcproc_t procnum, const xdrproc_t inproc,
    const caddr_t in, const xdrproc_t outproc, const caddr_t out,
    const struct timeval tout, const struct netbuf *svcaddr);

bool_t
rpcb_set(const rpcprog_t prognum, const rpcvers_t versnum,
    const struct netconfig *netconf, const struct netbuf *svcaddr);

bool_t
rpcb_unset(const rpcprog_t prognum, const rpcvers_t versnum,
    const struct netconfig *netconf);
```

## 描述

这些例程允许客户端 C 程序向 RPC 绑定服务发起过程调用。（参见 rpcbind(8)）维护着程序与其通用地址之间的映射列表。

## 例程

**`rpcb_getmaps`** rpcbind 服务的接口，返回 `host` 上当前 RPC 程序到地址的映射列表。它使用通过 `netconf` 指定的传输来联系 `host` 上的远程 rpcbind 服务。如果无法联系远程 rpcbind，该例程将返回 `NULL`。

**`rpcb_getaddr`** rpcbind 服务的接口，查找 `host` 上注册了程序号 `prognum`、版本 `versnum` 且使用与 `netconf` 关联的传输协议的服务的地址。找到的地址在 `svcaddr` 中返回。`svcaddr` 参数应预先分配。该例程成功时返回 `TRUE`。返回值为 `FALSE` 表示映射不存在或 RPC 系统未能联系远程 rpcbind 服务。在后一种情况下，全局变量 `rpc_createerr`（参见 [rpc_clnt_create(3)](rpc_clnt_create.3.md)）包含 RPC 状态。

**`rpcb_gettime`** 该例程在 `timep` 中返回 `host` 上的时间。如果 `host` 为 `NULL`，`rpcb_gettime` 返回本机的时间。该例程成功时返回 `TRUE`，失败时返回 `FALSE`。`rpcb_gettime` 函数可用于同步客户端和远程服务器之间的时间。

**`rpcb_rmtcall`** rpcbind 服务的接口，指示 `host` 上的 rpcbind 代你向该主机上的某个过程发起 RPC 调用。`netconfig` 结构应对应于无连接传输。如果过程成功，`svcaddr` 参数将被修改为服务器的地址（其他参数的定义参见 [rpc_clnt_calls(3)](rpc_clnt_calls.3.md) 中的 `rpc_call` 和 `clnt_call`）。此过程通常仅用于“ping”且仅用于此目的。此例程允许程序一步完成查找和调用。注意：即使服务器未运行，`rpcb_rmtcall` 也不会向调用方返回任何错误消息。在这种情况下，调用方会超时。注意：`rpcb_rmtcall` 仅适用于无连接传输。

**`rpcb_set`** rpcbind 服务的接口，在机器的 rpcbind 服务上建立三元组 [`prognum`, `versnum`, `netconf->nc_netid`] 与 `svcaddr` 之间的映射。`nc_netid` 的值必须对应于由 netconfig 数据库定义的网络标识符。该例程成功时返回 `TRUE`，否则返回 `FALSE`。（另见 [rpc_svc_calls(3)](rpc_svc_calls.3.md) 中的 `svc_reg`）如果 rpcbind 中已存在这样的条目，`rpcb_set` 将失败。

**`rpcb_unset`** rpcbind 服务的接口，销毁机器的 rpcbind 服务上三元组 [`prognum`, `versnum`, `netconf->nc_netid`] 与地址之间的映射。如果 `netconf` 为 `NULL`，`rpcb_unset` 销毁机器的 rpcbind 服务上三元组 [`prognum`, `versnum`, 所有传输] 与地址之间的所有映射。该例程成功时返回 `TRUE`，否则返回 `FALSE`。只有服务的所有者或超级用户才能销毁映射。（另见 [rpc_svc_calls(3)](rpc_svc_calls.3.md) 中的 `svc_unreg`）

## 参见

[rpc_clnt_calls(3)](rpc_clnt_calls.3.md), [rpc_svc_calls(3)](rpc_svc_calls.3.md), rpcbind(8), rpcinfo(8)
