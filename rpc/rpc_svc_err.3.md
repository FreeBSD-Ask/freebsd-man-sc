# rpc_svc_err(3)

`rpc_svc_err` — 用于服务器端远程过程调用错误的库例程

## 名称

`rpc_svc_err`, `svcerr_auth`, `svcerr_decode`, `svcerr_noproc`, `svcerr_noprog`, `svcerr_progvers`, `svcerr_systemerr`, `svcerr_weakauth`

## 库

Lb libc

## 概要

`#include <rpc/rpc.h>`

```c
void
svcerr_auth(SVCXPRT *xprt, enum auth_stat why);

void
svcerr_decode(SVCXPRT *xprt);

void
svcerr_noproc(SVCXPRT *xprt);

void
svcerr_noprog(SVCXPRT *xprt);

void
svcerr_progvers(SVCXPRT *xprt, rpcvers_t low_vers, rpcvers_t high_vers);

void
svcerr_systemerr(SVCXPRT *xprt);

void
svcerr_weakauth(SVCXPRT *xprt);
```

## 描述

这些例程是 RPC 库的一部分，允许 C 语言程序通过网络在其他机器上进行过程调用。

在与客户端的事务中出现任何错误时，服务器端的分发函数可以调用这些例程。

## 例程

关于 `SVCXPRT` 数据结构的定义，参见 [rpc(3)](rpc.3.md)。

**`svcerr_auth`** 由因认证错误而拒绝执行远程过程调用的服务分发例程调用。

**`svcerr_decode`** 由无法成功解码远程参数的服务分发例程调用（参见 [rpc_svc_reg(3)](rpc_svc_reg.3.md) 中的 `svc_getargs`）。

**`svcerr_noproc`** 由未实现调用方请求的过程号的服务分发例程调用。

**`svcerr_noprog`** 当所需的程序未向 RPC 包注册时调用。服务实现者通常不需要此例程。

**`svcerr_progvers`** 当所需的程序版本未向 RPC 包注册时调用。`low_vers` 参数是最低版本号，`high_vers` 是最高版本号。服务实现者通常不需要此例程。

**`svcerr_systemerr`** 由服务分发例程在检测到任何特定协议未涵盖的系统错误时调用。例如，如果服务无法再分配存储空间，可以调用此例程。

**`svcerr_weakauth`** 由因认证参数不足（但正确）而拒绝执行远程过程调用的服务分发例程调用。该例程调用 `svcerr_auth(xprt, AUTH_TOOWEAK)`。

## 参见

[rpc(3)](rpc.3.md), [rpc_svc_calls(3)](rpc_svc_calls.3.md), [rpc_svc_create(3)](rpc_svc_create.3.md), [rpc_svc_reg(3)](rpc_svc_reg.3.md)
