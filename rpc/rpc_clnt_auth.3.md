# auth_destroy(3)

`auth_destroy` — 客户端远程过程调用认证的库例程

## 名称

`auth_destroy`, `authnone_create`, `authsys_create`, `authsys_create_default`

## 库

Lb libc

## 概要

`#include <rpc/rpc.h>`

```c
void
auth_destroy(AUTH *auth);

AUTH *
authnone_create(void);

AUTH *
authsys_create(const char *host, const uid_t uid, const gid_t gid,
    const int len, const gid_t *aup_gids);

AUTH *
authsys_create_default(void);
```

## 描述

这些例程是 RPC 库的一部分，允许 C 语言程序通过网络在其他机器上进行过程调用，并提供所需的认证。

这些例程通常在创建 `CLIENT` 句柄之后调用。`CLIENT` 结构的 `cl_auth` 字段应由以下某些例程返回的 `AUTH` 结构初始化。客户端的认证信息在进行 RPC 调用时传递给服务器。

此处仅讨论 `NULL` 和 `SYS` 风格的认证。

## 例程

**`auth_destroy`** 一个函数宏，销毁与 `auth` 关联的认证信息。销毁通常涉及释放私有数据结构。调用 `auth_destroy` 后，`auth` 的使用是未定义的。

**`authnone_create`** 创建并返回一个 RPC 认证句柄，该句柄在每次远程过程调用时传递不可用的认证信息。这是 RPC 使用的默认认证。

**`authsys_create`** 创建并返回一个包含 `AUTH_SYS` 认证信息的 RPC 认证句柄。`host` 参数是创建该信息的机器名；`uid` 是用户的用户 ID；`gid` 是用户的当前组 ID；`len` 和 `aup_gids` 指向用户所属组的计数数组。

**`authsys_create_default`** 使用适当的参数调用 `authsys_create`。

## 参见

[rpc(3)](rpc.3.md), [rpc_clnt_calls(3)](rpc_clnt_calls.3.md), [rpc_clnt_create(3)](rpc_clnt_create.3.md)
