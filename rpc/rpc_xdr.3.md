# rpc_xdr(3)

`rpc_xdr` — 用于远程过程调用的 XDR 库例程

## 名称

`xdr_accepted_reply`, `xdr_authsys_parms`, `xdr_callhdr`, `xdr_callmsg`, `xdr_opaque_auth`, `xdr_rejected_reply`, `xdr_replymsg`

## 库

Lb libc

## 概要

`#include <rpc/rpc.h>`

```c
bool_t
xdr_accepted_reply(XDR *xdrs, struct accepted_reply *ar);

bool_t
xdr_authsys_parms(XDR *xdrs, struct authsys_parms *aupp);

bool_t
xdr_callhdr(XDR *xdrs, struct rpc_msg *chdr);

bool_t
xdr_callmsg(XDR *xdrs, struct rpc_msg *cmsg);

bool_t
xdr_opaque_auth(XDR *xdrs, struct opaque_auth *ap);

bool_t
xdr_rejected_reply(XDR *xdrs, struct rejected_reply *rr);

bool_t
xdr_replymsg(XDR *xdrs, struct rpc_msg *rmsg);
```

## 描述

这些例程用于以 XDR 语言描述 RPC 消息。通常由那些不希望直接使用 RPC 包的用户使用。这些例程成功时返回 `TRUE`，否则返回 `FALSE`。

## 例程

关于 `XDR` 数据结构的定义，参见 [rpc(3)](rpc.3.md)。

**`xdr_accepted_reply`** 用于在 RPC 应答消息及其外部表示之间转换。它以 XDR 语言格式包含 RPC 调用的状态。成功时，还包括调用结果。

**`xdr_authsys_parms`** 用于描述 UNIX 操作系统凭据。它包括机器名、uid、gid 列表等。

**`xdr_callhdr`** 用于描述 RPC 调用头消息。它以 XDR 语言格式编码调用消息头的静态部分。它包括事务 ID、RPC 版本号、程序和版本号等信息。

**`xdr_callmsg`** 用于描述 RPC 调用消息。这包括所有 RPC 调用信息，如事务 ID、RPC 版本号、程序号、版本号、认证信息等。通常由服务器用于确定关于客户端 RPC 调用的信息。

**`xdr_opaque_auth`** 用于描述 RPC 不透明认证信息消息。

**`xdr_rejected_reply`** 用于描述 RPC 应答消息。它以 XDR 语言格式编码被拒绝的 RPC 消息。消息可能因版本号不匹配或认证错误而被拒绝。

**`xdr_replymsg`** 用于描述 RPC 应答消息。它在 RPC 应答消息及其外部表示之间转换。此应答可以是接受、拒绝或 `NULL`。

## 参见

[rpc(3)](rpc.3.md), [xdr(3)](xdr.3.md)
