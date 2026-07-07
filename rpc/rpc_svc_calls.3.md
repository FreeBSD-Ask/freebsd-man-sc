# rpc_svc_calls(3)

`rpc_svc_calls` — 用于 RPC 服务器的库例程

## 名称

`svc_dg_enablecache`, `svc_exit`, `svc_fdset`, `svc_freeargs`, `svc_getargs`, `svc_getreq_common`, `svc_getreq_poll`, `svc_getreqset`, `svc_getrpccaller`, `svc_pollset`, `svc_run`, `svc_sendreply`

## 库

Lb libc

## 概要

`#include <rpc/rpc.h>`

```c
int
svc_dg_enablecache(SVCXPRT *xprt, const unsigned cache_size);

void
svc_exit(void);

bool_t
svc_freeargs(const SVCXPRT *xprt, const xdrproc_t inproc, caddr_t in);

bool_t
svc_getargs(const SVCXPRT *xprt, const xdrproc_t inproc, caddr_t in);

void
svc_getreq_common(const int fd);

void
svc_getreq_poll(struct pollfd *pfdp, const int pollretval);

void
svc_getreqset(fd_set *rdfds);

struct netbuf *
svc_getrpccaller(const SVCXPRT *xprt);

struct cmsgcred *
__svc_getcallercreds(const SVCXPRT *xprt);

struct pollfd svc_pollset[FD_SETSIZE];

void
svc_run(void);

bool_t
svc_sendreply(SVCXPRT *xprt, xdrproc_t outproc, void *out);
```

## 描述

这些例程是 RPC 库的一部分，允许 C 语言程序通过网络在其他机器上进行过程调用。

这些例程与 RPC 机制的服务器端相关。其中一些由服务器端的分发函数调用，另一些（如 `svc_run`）在服务器启动时调用。

## 例程

关于 `SVCXPRT` 数据结构的定义，参见 [rpc(3)](rpc.3.md)。

**`svc_dg_enablecache`** 该函数为服务端点 `xprt` 分配一个重复请求缓存，大小足以容纳 `cache_size` 个条目。一旦启用，无法禁用缓存。如果成功分配了给定大小缓存所需的空间，该例程返回 0，否则返回 1。

**`svc_exit`** 该函数被任何 RPC 服务器过程或其他方式调用时，会导致 `svc_run` 返回。在当前实现中，`svc_exit` 将全局变量 `svc_fdset` 清零。如果要恢复 RPC 服务器活动，必须通过 [rpc_svc_create(3)](rpc_svc_create.3.md) 函数之一或使用 `xprt_register` 重新向 RPC 库注册服务。`svc_exit` 函数具有全局作用域，会终止所有 RPC 服务器活动。

**`fd_set` `svc_fdset`** 一个全局变量，反映 RPC 服务器的读文件描述符位掩码；它适合作为 [select(2)](../man2/select.2.md) 系统调用的参数。仅在服务实现者不调用 `svc_run` 而是自行实现异步事件处理时才有意义。此变量是只读的（不要将其地址传递给 [select(2)](../man2/select.2.md)），但在调用 `svc_getreqset` 或任何创建例程后它可能会发生变化。

**`svc_freeargs`** 一个函数宏，释放 RPC/XDR 系统在使用 `svc_getargs` 解码服务过程参数时分配的任何数据。如果成功释放结果，该例程返回 `TRUE`，否则返回 `FALSE`。

**`svc_getargs`** 一个函数宏，解码与 RPC 服务传输句柄 `xprt` 关联的 RPC 请求的参数。`in` 参数是放置参数的地址；`inproc` 是用于解码参数的 XDR 例程。如果解码成功，该例程返回 `TRUE`，否则返回 `FALSE`。

**`svc_getreq_common`** 调用以处理给定文件描述符上的请求。

**`svc_getreq_poll`** 仅在服务实现者不调用 `svc_run` 而是实现自定义异步事件处理时才有意义。当 [poll(2)](../man2/poll.2.md) 确定 RPC 请求到达某些 RPC 文件描述符时调用；`pollretval` 是 [poll(2)](../man2/poll.2.md) 的返回值，`pfdp` 是进行 [poll(2)](../man2/poll.2.md) 操作的 `pollfd` 结构数组。假定数组足够大，可以容纳允许的最大描述符数。

**`svc_getreqset`** 仅在服务实现者不调用 `svc_run` 而是实现自定义异步事件处理时才有意义。当 [poll(2)](../man2/poll.2.md) 确定 RPC 请求到达某些 RPC 文件描述符时调用；`rdfds` 是结果读文件描述符位掩码。该例程在与 `rdfds` 值关联的所有文件描述符被服务后返回。

**`svc_getrpccaller`** 获取与 RPC 服务传输句柄 `xprt` 关联的过程调用方的网络地址的推荐方式。

**`__svc_getcallercreds`** *警告：*此宏是 FreeBSD 特有的，因此不可移植。此宏返回指向 `cmsgcred` 结构的指针（该结构定义于 `<sys/socket.h>`），用于标识调用客户端。仅当客户端通过 `AF_LOCAL` 套接字调用服务器时才有效。

**`struct pollfd` `svc_pollset[FD_SETSIZE]`** `svc_pollset` 是从 `svc_fdset[]` 派生的 `pollfd` 结构数组。它适合作为 [poll(2)](../man2/poll.2.md) 系统调用的参数。在当前实现中，`svc_pollset` 从 `svc_fdset` 的派生在 `svc_run` 中完成。不调用 `svc_run` 但希望使用此数组的服务实现者必须自行执行此派生。

**`svc_run`** 此例程永不返回。它等待 RPC 请求到达，并在请求到达时调用 `svc_getreq_poll` 调用适当的服务过程。此过程通常等待 [poll(2)](../man2/poll.2.md) 系统调用返回。

**`svc_sendreply`** 由 RPC 服务的分发例程调用，以发送远程过程调用的结果。`xprt` 参数是请求关联的传输句柄；`outproc` 是用于编码结果的 XDR 例程；`out` 是结果的地址。该例程成功时返回 `TRUE`，否则返回 `FALSE`。

## 参见

[poll(2)](../man2/poll.2.md), [select(2)](../man2/select.2.md), [rpc(3)](rpc.3.md), [rpc_svc_create(3)](rpc_svc_create.3.md), [rpc_svc_err(3)](rpc_svc_err.3.md), [rpc_svc_reg(3)](rpc_svc_reg.3.md)
