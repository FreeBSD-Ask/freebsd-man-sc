# rpc_clnt_calls(3)

`rpc_clnt_calls` — 客户端调用的库例程

## 名称

`rpc_clnt_calls`, `clnt_call`, `clnt_freeres`, `clnt_geterr`, `clnt_perrno`, `clnt_perror`, `clnt_sperrno`, `clnt_sperror`, `rpc_broadcast`, `rpc_broadcast_exp`, `rpc_call`

## 库

Lb libc

## 概要

`#include <rpc/rpc.h>`

```c
enum clnt_stat
clnt_call(CLIENT *clnt, const rpcproc_t procnum, const xdrproc_t inproc,
    const caddr_t in, const xdrproc_t outproc, caddr_t out,
    const struct timeval tout);

bool_t
clnt_freeres(CLIENT *clnt, const xdrproc_t outproc, caddr_t out);

void
clnt_geterr(const CLIENT *clnt, struct rpc_err *errp);

void
clnt_perrno(const enum clnt_stat stat);

void
clnt_perror(CLIENT *clnt, const char *s);

char *
clnt_sperrno(const enum clnt_stat stat);

char *
clnt_sperror(CLIENT *clnt, const char *s);

enum clnt_stat
rpc_broadcast(const rpcprog_t prognum, const rpcvers_t versnum,
    const rpcproc_t procnum, const xdrproc_t inproc, const caddr_t in,
    const xdrproc_t outproc, caddr_t out, const resultproc_t eachresult,
    const char *nettype);

enum clnt_stat
rpc_broadcast_exp(const rpcprog_t prognum, const rpcvers_t versnum,
    const rpcproc_t procnum, const xdrproc_t xargs, caddr_t argsp,
    const xdrproc_t xresults, caddr_t resultsp,
    const resultproc_t eachresult, const int inittime,
    const int waittime, const char *nettype);

enum clnt_stat
rpc_call(const char *host, const rpcprog_t prognum, const rpcvers_t versnum,
    const rpcproc_t procnum, const xdrproc_t inproc, const char *in,
    const xdrproc_t outproc, char *out, const char *nettype);
```

## 描述

RPC 库例程允许 C 语言程序通过网络在其他机器上进行过程调用。首先，客户端调用一个过程向服务器发送请求。服务器收到请求后，调用一个分发例程来执行所请求的服务，然后发回回复。

`clnt_call`、`rpc_call` 和 `rpc_broadcast` 例程处理过程调用的客户端部分。其余例程用于在出现错误时进行错误处理。

部分例程将 `CLIENT` 句柄作为参数之一。`CLIENT` 句柄可由 RPC 创建例程（如 `clnt_create`）创建（参见 [rpc_clnt_create(3)](rpc_clnt_create.3.md)）。

这些例程可安全用于多线程应用程序。`CLIENT` 句柄可以在线程间共享，但在本实现中，不同线程的请求会被串行化（即第一个请求会在第二个请求发送之前收到其结果）。

## 例程

关于 `CLIENT` 数据结构的定义，参见 [rpc(3)](rpc.3.md)。

**`clnt_call`** 一个函数宏，调用与客户端句柄 `clnt` 关联的远程过程 `procnum`，该句柄通过 RPC 客户端创建例程（如 `clnt_create`）获取（参见 [rpc_clnt_create(3)](rpc_clnt_create.3.md)）。`inproc` 参数是用于编码过程参数的 XDR 函数，`outproc` 是用于解码过程结果的 XDR 函数；`in` 是过程参数的地址，`out` 是放置结果的地址。`tout` 参数是允许返回结果的时间，该值会被通过 `clnt_control` 显式设置的超时覆盖，参见 [rpc_clnt_create(3)](rpc_clnt_create.3.md)。如果远程调用成功，返回状态为 `RPC_SUCCESS`，否则返回适当的状态。

**`clnt_freeres`** 一个函数宏，释放 RPC/XDR 系统在解码 RPC 调用结果时分配的所有数据。`out` 参数是结果的地址，`outproc` 是描述结果的 XDR 例程。如果结果成功释放，该例程返回 1，否则返回 0。

**`clnt_geterr`** 一个函数宏，将错误结构从客户端句柄复制到地址 `errp` 所指向的结构。

**`clnt_perrno`** 向标准错误打印一条与 `stat` 所指示条件对应的消息。消息末尾会附加一个换行符。通常在过程调用失败后使用，适用于不需要客户端句柄的例程，例如 `rpc_call`。

**`clnt_perror`** 向标准错误打印一条消息，指示 RPC 调用失败的原因；`clnt` 是用于进行该调用的句柄。消息前会加上字符串 `s` 和一个冒号。消息末尾会附加一个换行符。通常在远程过程调用失败后使用，适用于需要客户端句柄的例程，例如 `clnt_call`。

**`clnt_sperrno`** 接受与 `clnt_perrno` 相同的参数，但不向标准输出发送指示 RPC 调用失败原因的消息，而是返回指向包含该消息的字符串的指针。当程序没有标准错误（作为服务器运行的程序很可能没有），或者程序员不希望消息通过 `printf` 输出（参见 printf(3)），或者要使用与 `clnt_perrno` 所支持格式不同的消息格式时，通常使用 `clnt_sperrno` 函数代替 `clnt_perrno`。注意：与 `clnt_sperror` 和 `clnt_spcreateerror`（参见 [rpc_clnt_create(3)](rpc_clnt_create.3.md)）不同，`clnt_sperrno` 不返回指向静态数据的指针，因此结果不会在每次调用时被覆盖。

**`clnt_sperror`** 类似于 `clnt_perror`，但（与 `clnt_sperrno` 一样）返回字符串而非打印到标准错误。但是，`clnt_sperror` 不会在消息末尾附加换行符。警告：返回指向缓冲区的指针，该缓冲区在每次调用时会被覆盖。

**`rpc_broadcast`** 类似于 `rpc_call`，但调用消息会广播到由 `nettype` 指定的所有无连接传输。如果 `nettype` 为 `NULL`，则默认为“netpath”。每次收到响应时，该例程会调用 `eachresult`，其形式为：

```c
bool_t
eachresult(caddr_t out, const struct netbuf *addr,
    const struct netconfig *netconf);
```

其中 `out` 与传递给 `rpc_broadcast` 的 `out` 相同，只是远程过程的输出在那里被解码；`addr` 指向发送结果的机器的地址，`netconf` 是远程服务器响应所在传输的 netconfig 结构。如果 `eachresult` 返回 0，`rpc_broadcast` 会等待更多回复；否则以适当的状态返回。警告：广播文件描述符的大小受限于该传输的最大传输大小。对于以太网，此值为 1500 字节。`rpc_broadcast` 函数默认使用 `AUTH_SYS` 凭据（参见 [rpc_clnt_auth(3)](rpc_clnt_auth.3.md)）。

**`rpc_broadcast_exp`** 类似于 `rpc_broadcast`，但初始超时 `inittime` 和最大超时 `waittime` 以毫秒为单位指定。`inittime` 参数是 `rpc_broadcast_exp` 在重新发送请求前等待的初始时间。首次重发后，重传间隔会呈指数增长，直到超过 `waittime`。

**`rpc_call`** 调用机器 `host` 上与 `prognum`、`versnum` 和 `procnum` 关联的远程过程。`inproc` 参数用于编码过程的参数，`outproc` 用于解码过程的结果；`in` 是过程参数的地址，`out` 是放置结果的地址。`nettype` 参数可以是 [rpc(3)](rpc.3.md) 中列出的任何值。该例程成功时返回 `RPC_SUCCESS`，否则返回适当的状态。使用 `clnt_perrno` 例程可将失败状态转换为错误消息。警告：`rpc_call` 使用 `nettype` 类别下可创建连接的第一个可用传输。使用该例程时你无法控制超时或认证。

## 参见

printf(3), [rpc(3)](rpc.3.md), [rpc_clnt_auth(3)](rpc_clnt_auth.3.md), [rpc_clnt_create(3)](rpc_clnt_create.3.md)
