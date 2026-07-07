# rpc_svc_reg(3)

`rpc_svc_reg` — 用于注册服务器的库例程

## 名称

`rpc_svc_reg`, `rpc_reg`, `svc_reg`, `svc_unreg`, `svc_auth_reg`, `xprt_register`, `xprt_unregister`

## 库

Lb libc

## 概要

`#include <rpc/rpc.h>`

```c
int
rpc_reg(const rpcprog_t prognum, const rpcvers_t versnum,
    const rpcproc_t procnum, char *(*procname)(),
    const xdrproc_t inproc, const xdrproc_t outproc,
    const char *nettype);

bool_t
svc_reg(SVCXPRT *xprt, const rpcprog_t prognum,
    const rpcvers_t versnum,
    void (*dispatch)(struct svc_req *, SVCXPRT *),
    const struct netconfig *netconf);

void
svc_unreg(const rpcprog_t prognum, const rpcvers_t versnum);

int
svc_auth_reg(int cred_flavor,
    enum auth_stat (*handler)(struct svc_req *, struct rpc_msg *));

void
xprt_register(SVCXPRT *xprt);

void
xprt_unregister(SVCXPRT *xprt);
```

## 描述

这些例程是 RPC 库的一部分，允许 RPC 服务器向 rpcbind 注册自身（参见 rpcbind(8)），并将给定的程序和版本号与分发函数关联。当 RPC 服务器收到 RPC 请求时，库会以适当的参数调用分发例程。

## 例程

关于 `SVCXPRT` 数据结构的定义，参见 [rpc(3)](rpc.3.md)。

**`rpc_reg`** 向 RPC 服务包注册程序 `prognum`、过程 `procname` 和版本 `versnum`。如果收到针对程序 `prognum`、版本 `versnum` 和过程 `procnum` 的请求，则会以指向其参数的指针调用 `procname`；`procname` 应返回指向其静态结果的指针；`inproc` 是用于解码参数的 XDR 函数，`outproc` 是用于编码结果的 XDR 函数。过程在 `nettype` 类别的所有可用传输上注册。参见 [rpc(3)](rpc.3.md)。该例程成功时返回 0，否则返回 -1。

**`svc_reg`** 将 `prognum` 和 `versnum` 与服务分发过程 `dispatch` 关联。如果 `netconf` 为 `NULL`，则不会向 rpcbind(8) 服务注册该服务。如果 `netconf` 非零，则向本地 rpcbind 服务建立三元组 [`prognum`, `versnum`, `netconf->nc_netid`] 到 `xprt->xp_ltaddr` 的映射。`svc_reg` 例程成功时返回 1，否则返回 0。

**`svc_unreg`** 从 rpcbind 服务中删除所有三元组 [`prognum`, `versnum`, 所有传输] 到网络地址的映射，以及 RPC 服务包内所有二元组 [`prognum`, `versnum`] 到分发例程的映射。

**`svc_auth_reg`** 向分发机制注册服务认证例程 `handler`，以便在收到带有认证类型 `cred_flavor` 的 RPC 请求时调用它进行认证。此接口允许开发者向其 RPC 应用程序添加新的认证类型，而无需修改库。服务实现者通常不需要此例程。典型的服务应用程序会在注册服务之后、调用 `svc_run` 之前调用 `svc_auth_reg`。当需要处理类型为 `cred_flavor` 的 RPC 凭据时，将以两个参数 `struct svc_req *rqst` 和 `struct rpc_msg *msg` 调用 `handler` 过程，并期望返回有效的 `enum auth_stat` 值。一旦注册，没有机制可以更改或删除认证处理程序。`svc_auth_reg` 例程成功时返回 0，如果 `cred_flavor` 已注册了认证处理程序则返回 1，否则返回 -1。

**`xprt_register`** 在 RPC 服务传输句柄 `xprt` 创建后，将其注册到 RPC 服务包。该例程修改全局变量 `svc_fdset`（参见 [rpc_svc_calls(3)](rpc_svc_calls.3.md)）。服务实现者通常不需要此例程。

**`xprt_unregister`** 在 RPC 服务传输句柄 `xprt` 销毁之前，将其从 RPC 服务包中注销。该例程修改全局变量 `svc_fdset`（参见 [rpc_svc_calls(3)](rpc_svc_calls.3.md)）。服务实现者通常不需要此例程。

## 参见

select(2), [rpc(3)](rpc.3.md), [rpc_svc_calls(3)](rpc_svc_calls.3.md), [rpc_svc_create(3)](rpc_svc_create.3.md), [rpc_svc_err(3)](rpc_svc_err.3.md), [rpcbind(3)](rpcbind.3.md), rpcbind(8)
