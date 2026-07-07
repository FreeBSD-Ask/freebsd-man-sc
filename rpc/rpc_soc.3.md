# rpc_soc(3)

`rpc_soc` — 远程过程调用的库例程

## 名称

`rpc_soc`, `auth_destroy`, `authnone_create`, `authunix_create`, `authunix_create_default`, `callrpc`, `clnt_broadcast`, `clnt_call`, `clnt_control`, `clnt_create`, `clnt_destroy`, `clnt_freeres`, `clnt_geterr`, `clnt_pcreateerror`, `clnt_perrno`, `clnt_perror`, `clnt_spcreateerror`, `clnt_sperrno`, `clnt_sperror`, `clntraw_create`, `clnttcp_create`, `clntudp_bufcreate`, `clntudp_create`, `clntunix_create`, `get_myaddress`, `pmap_getmaps`, `pmap_getport`, `pmap_rmtcall`, `pmap_set`, `pmap_unset`, `registerrpc`, `rpc_createerr`, `svc_destroy`, `svc_fds`, `svc_fdset`, `svc_getargs`, `svc_getcaller`, `svc_getreq`, `svc_getreqset`, `svc_register`, `svc_run`, `svc_sendreply`, `svc_unregister`, `svcerr_auth`, `svcerr_decode`, `svcerr_noproc`, `svcerr_noprog`, `svcerr_progvers`, `svcerr_systemerr`, `svcerr_weakauth`, `svcfd_create`, `svcunixfd_create`, `svcraw_create`, `svcunix_create`, `xdr_accepted_reply`, `xdr_authunix_parms`, `xdr_callhdr`, `xdr_callmsg`, `xdr_opaque_auth`, `xdr_pmap`, `xdr_pmaplist`, `xdr_rejected_reply`, `xdr_replymsg`, `xprt_register`, `xprt_unregister`

## 库

Lb libc

## 概要

`#include <rpc/rpc.h>`

参见下文描述以获取函数声明。

## 描述

> 本页所述的 `svc_*` 和 `clnt_*` 函数是 XDR 和 RPC 库的旧版 TS-RPC 接口，仅为向后兼容而保留。新接口在 [rpc(3)](rpc.3.md) 所引用的页面中描述。

这些例程允许 C 程序通过网络在其他机器上进行过程调用。首先，客户端调用一个过程向服务器发送数据包。服务器收到数据包后，调用一个分发例程来执行所请求的服务，然后发回回复。最后，过程调用返回到客户端。

用于 Secure RPC（DES 认证）的例程在 [rpc_secure(3)](rpc_secure.3.md) 中描述。只有在 DES 加密可用时才能使用 Secure RPC。

```c
bool_t
eachresult(caddr_t out, struct sockaddr_in *addr);
```

对于 UDP 和 TCP，`clnt_control` 中 `req` 支持的值及其参数类型和作用如下：

| `req` 值 | 参数类型 | 说明 |
| :------: | :------: | :--: |
| `CLSET_TIMEOUT` | `struct timeval` | 设置总超时 |
| `CLGET_TIMEOUT` | `struct timeval` | 获取总超时 |
| `CLGET_SERVER_ADDR` | `struct sockaddr_in` | 获取服务器地址 |
| `CLSET_RETRY_TIMEOUT` | `struct timeval` | 设置重试超时 |
| `CLGET_RETRY_TIMEOUT` | `struct timeval` | 获取重试超时 |

```c
bool_t
dispatch(struct svc_req *request, SVCXPRT *xprt);
```

**`auth_destroy`** 一个宏，销毁与 `auth` 关联的认证信息。销毁通常涉及释放私有数据结构。调用 `auth_destroy` 后，`auth` 的使用是未定义的。

**`authnone_create`** 创建并返回一个 RPC 认证句柄，该句柄在每次远程过程调用时传递不可用的认证信息。这是 RPC 使用的默认认证。

**`authunix_create`** 创建并返回一个包含 UNIX 认证信息的 RPC 认证句柄。`host` 参数是创建该信息的机器名；`uid` 是用户的用户 ID；`gid` 是用户的当前组 ID；`len` 和 `aup_gids` 指向用户所属组的计数数组。很容易冒充用户。

**`authunix_create_default`** 使用适当的参数调用 `authunix_create`。

**`callrpc`** 调用机器 `host` 上与 `prognum`、`versnum` 和 `procnum` 关联的远程过程。`in` 参数是过程参数的地址，`out` 是放置结果的地址；`inproc` 用于编码过程参数，`outproc` 用于解码过程结果。该例程成功时返回零，失败时返回转换为整数的 `enum clnt_stat` 值。`clnt_perrno` 例程便于将失败状态转换为消息。警告：使用此例程调用远程过程时使用 UDP/IP 作为传输；有关限制，参见 `clntudp_create`。使用此例程时你无法控制超时或认证。

**`clnt_broadcast`** 类似于 `callrpc`，但调用消息会广播到所有本地连接的广播网络。每次收到响应时，该例程会调用 `eachresult`，其形式为：其中 `out` 与传递给 `clnt_broadcast` 的 `out` 相同，只是远程过程的输出在那里被解码；`addr` 指向发送结果的机器的地址。如果 `eachresult` 返回零，`clnt_broadcast` 会等待更多回复；否则以适当的状态返回。警告：广播套接字的大小受限于数据链路的最大传输单元。对于以太网，此值为 1500 字节。

**`clnt_call`** 一个宏，调用与客户端句柄 `clnt` 关联的远程过程 `procnum`，该句柄通过 RPC 客户端创建例程（如 `clnt_create`）获取。`in` 参数是过程参数的地址，`out` 是放置结果的地址；`inproc` 用于编码过程参数，`outproc` 用于解码过程结果；`tout` 是允许返回结果的时间。

**`clnt_destroy`** 一个宏，销毁客户端的 RPC 句柄。销毁通常涉及释放私有数据结构，包括 `clnt` 本身。调用 `clnt_destroy` 后，`clnt` 的使用是未定义的。如果 RPC 库打开了关联的套接字，它也会将其关闭。否则，套接字保持打开。

**`clnt_create`** 通用客户端创建例程。`host` 参数标识服务器所在的远程主机名。`proto` 参数指示要使用的传输协议类型。该字段当前支持的值为 `udp` 和 `tcp`。默认超时已设置，但可使用 `clnt_control` 修改。警告：使用 UDP 有其缺点。由于基于 UDP 的 RPC 消息最多只能容纳 8 KB 的编码数据，因此该传输不能用于接受大型参数或返回大量结果的过程。

**`clnt_control`** 一个宏，用于更改或检索客户端对象的各种信息。`req` 参数指示操作类型，`info` 是指向该信息的指针。对于 UDP 和 TCP，`req` 支持的值及其参数类型和作用见上表。注意：如果通过 `clnt_control` 设置超时，则在后续所有调用中，`clnt_call` 所传递的超时参数会被忽略。以下操作仅对 UDP 有效：重试超时是 UDP RPC 在重新传输请求之前等待服务器回复的时间。

**`clnt_freeres`** 一个宏，释放 RPC/XDR 系统在解码 RPC 调用结果时分配的所有数据。`out` 参数是结果的地址，`outproc` 是描述结果的 XDR 例程。该例程成功释放结果时返回 1，否则返回 0。

**`clnt_geterr`** 一个宏，将错误结构从客户端句柄复制到地址 `errp` 所指向的结构。

**`clnt_pcreateerror`** 向标准错误打印一条消息，指示为何无法创建客户端 RPC 句柄。消息前会加上字符串 `s` 和一个冒号。消息末尾会附加换行符。在 `clnt_create`、`clntraw_create`、`clnttcp_create` 或 `clntudp_create` 调用失败时使用。

**`clnt_perrno`** 向标准错误打印一条与 `stat` 所指示条件对应的消息。消息末尾会附加换行符。在 `callrpc` 之后使用。

**`clnt_perror`** 向标准错误打印一条消息，指示 RPC 调用失败的原因；`clnt` 是用于进行该调用的句柄。消息前会加上字符串 `s` 和一个冒号。消息末尾会附加换行符。在 `clnt_call` 之后使用。

**`clnt_spcreateerror`** 类似于 `clnt_pcreateerror`，但返回字符串而非打印到标准错误。缺陷：返回指向静态数据的指针，该数据在每次调用时会被覆盖。

**`clnt_sperrno`** 接受与 `clnt_perrno` 相同的参数，但不向标准输出发送指示 RPC 调用失败原因的消息，而是返回指向包含该消息的字符串的指针。当程序没有标准错误（作为服务器运行的程序很可能没有），或者程序员不希望消息通过 `printf` 输出，或者要使用与 `clnt_perrno` 所支持格式不同的消息格式时，通常使用 `clnt_sperrno` 函数代替 `clnt_perrno`。注意：与 `clnt_sperror` 和 `clnt_spcreateerror` 不同，`clnt_sperrno` 返回指向静态数据的指针，但结果不会在每次调用时被覆盖。

**`clnt_sperror`** 类似于 `clnt_perror`，但（与 `clnt_sperrno` 一样）返回字符串而非打印到标准错误。缺陷：返回指向静态数据的指针，该数据在每次调用时会被覆盖。

**`clntraw_create`** 该例程为远程程序 `prognum`、版本 `versnum` 创建一个玩具 RPC 客户端。用于将消息传递给服务的传输实际上是进程地址空间内的一个缓冲区，因此对应的 RPC 服务器应位于同一地址空间；参见 `svcraw_create`。这允许在没有任何内核干扰的情况下模拟 RPC 并获取 RPC 开销（如往返时间）。该例程失败时返回 `NULL`。

**`clnttcp_create`** 该例程为远程程序 `prognum`、版本 `versnum` 创建 RPC 客户端；客户端使用 TCP/IP 作为传输。远程程序位于 Internet 地址 `addr`。如果 `addr->sin_port` 为零，则将其设置为远程程序正在监听的实际端口（为此信息会查询远程 rpcbind(8) 服务）。`sockp` 参数是一个套接字；如果为 `RPC_ANYSOCK`，则该例程打开一个新套接字并设置 `sockp`。由于基于 TCP 的 RPC 使用缓冲 I/O，用户可通过 `sendsz` 和 `recvsz` 参数指定发送和接收缓冲区的大小；值为零时选择合适的默认值。该例程失败时返回 `NULL`。

**`clntudp_create`** 该例程为远程程序 `prognum`、版本 `versnum` 创建 RPC 客户端；客户端使用 UDP/IP 作为传输。远程程序位于 Internet 地址 `addr`。如果 `addr->sin_port` 为零，则将其设置为远程程序正在监听的实际端口（为此信息会查询远程 rpcbind(8) 服务）。`sockp` 参数是一个套接字；如果为 `RPC_ANYSOCK`，则该例程打开一个新套接字并设置 `sockp`。UDP 传输以 `wait` 时间间隔重发调用消息，直到收到响应或调用超时。调用超时的总时间由 `clnt_call` 指定。警告：由于基于 UDP 的 RPC 消息最多只能容纳 8 KB 的编码数据，因此该传输不能用于接受大型参数或返回大量结果的过程。

**`clntudp_bufcreate`** 该例程为远程程序 `prognum`、版本 `versnum` 创建 RPC 客户端；客户端使用 UDP/IP 作为传输。远程程序位于 Internet 地址 `addr`。如果 `addr->sin_port` 为零，则将其设置为远程程序正在监听的实际端口（为此信息会查询远程 rpcbind(8) 服务）。`sockp` 参数是一个套接字；如果为 `RPC_ANYSOCK`，则该例程打开一个新套接字并设置 `sockp`。UDP 传输以 `wait` 时间间隔重发调用消息，直到收到响应或调用超时。调用超时的总时间由 `clnt_call` 指定。这允许用户指定发送和接收基于 UDP 的 RPC 消息的最大数据包大小。

**`clntunix_create`** 该例程为本地程序 `prognum`、版本 `versnum` 创建 RPC 客户端；客户端使用 UNIX 域套接字作为传输。本地程序位于 `*raddr`。`sockp` 参数是一个套接字；如果为 `RPC_ANYSOCK`，则该例程打开一个新套接字并设置 `sockp`。由于基于 UNIX 的 RPC 使用缓冲 I/O，用户可通过 `sendsz` 和 `recvsz` 参数指定发送和接收缓冲区的大小；值为零时选择合适的默认值。该例程失败时返回 `NULL`。

**`get_myaddress`** 将机器的 IP 地址填入 `addr`，不查询处理 **/etc/hosts** 的库例程。端口号始终设置为 `htons` `PMAPPORT`。成功时返回零，失败时返回非零。

**`pmap_getmaps`** rpcbind(8) 服务的用户接口，返回位于 IP 地址 `addr` 的主机上当前 RPC 程序到端口的映射列表。该例程可能返回 `NULL`。命令“`rpcinfo` `-p`”使用此例程。

**`pmap_getport`** rpcbind(8) 服务的用户接口，返回支持程序号 `prognum`、版本 `versnum` 且使用与 `protocol` 关联的传输协议的服务所等待的端口号。`protocol` 的值很可能是 `IPPROTO_UDP` 或 `IPPROTO_TCP`。返回值为零表示映射不存在或 RPC 系统未能联系远程 rpcbind(8) 服务。在后一种情况下，全局变量 `rpc_createerr` 包含 RPC 状态。

**`pmap_rmtcall`** rpcbind(8) 服务的用户接口，指示位于 IP 地址 `addr` 的主机上的 rpcbind(8) 代你向该主机上的某个过程发起 RPC 调用。如果过程成功，`portp` 参数将被修改为该程序的端口号。其他参数的定义参见 `callrpc` 和 `clnt_call`。此过程应用于“ping”且仅用于此目的。另见 `clnt_broadcast`。

**`pmap_set`** rpcbind(8) 服务的用户接口，在机器的 rpcbind(8) 服务上建立三元组 (`prognum`, `versnum`, `protocol`) 与 `port` 之间的映射。`protocol` 的值很可能是 `IPPROTO_UDP` 或 `IPPROTO_TCP`。该例程成功时返回 1，否则返回 0。由 `svc_register` 自动完成。

**`pmap_unset`** rpcbind(8) 服务的用户接口，销毁机器的 rpcbind(8) 服务上三元组 (`prognum`, `versnum`, `*`) 与 `ports` 之间的所有映射。该例程成功时返回 1，否则返回 0。

**`registerrpc`** 向 RPC 服务包注册过程 `procname`。如果收到针对程序 `prognum`、版本 `versnum` 和过程 `procnum` 的请求，则以指向其参数的指针调用 `procname`；`progname` 应返回指向其静态结果的指针；`inproc` 用于解码参数，`outproc` 用于编码结果。该例程成功时返回零，否则返回 -1。警告：以这种形式注册的远程过程使用 UDP/IP 传输访问；有关限制，参见 `svcudp_create`。

`struct rpc_createerr rpc_createerr` 一个全局变量，其值由任何未成功的 RPC 客户端创建例程设置。使用 `clnt_pcreateerror` 例程打印失败原因。

**`svc_destroy`** 一个宏，销毁 RPC 服务传输句柄 `xprt`。销毁通常涉及释放私有数据结构，包括 `xprt` 本身。调用此例程后，`xprt` 的使用是未定义的。

`fd_set svc_fdset` 一个全局变量，反映 RPC 服务端的读取文件描述符位掩码；它适合作为 select(2) 系统调用的模板参数。仅当服务实现者不调用 `svc_run`，而是自行实现异步事件处理时才有意义。该变量是只读的（不要将其地址传递给 select(2)），但在调用 `svc_getreqset` 或任何创建例程后它可能会更改。此外，请注意，如果进程的描述符限制扩展到 `FD_SETSIZE` 之外，则该变量仅可用于前 `FD_SETSIZE` 个描述符。

`int svc_fds` 类似于 `svc_fdset`，但限于 32 个描述符。此接口已被 `svc_fdset` 取代。

**`svc_freeargs`** 一个宏，释放 RPC/XDR 系统在使用 `svc_getargs` 解码服务过程参数时分配的所有数据。该例程成功释放结果时返回 1，否则返回 0。

**`svc_getargs`** 一个宏，解码与 RPC 服务传输句柄 `xprt` 关联的 RPC 请求的参数。`in` 参数是放置参数的地址；`inproc` 是用于解码参数的 XDR 例程。该例程成功解码时返回 1，否则返回 0。

**`svc_getcaller`** 获取与 RPC 服务传输句柄 `xprt` 关联的过程调用方网络地址的推荐方式。

**`svc_getreqset`** 仅当服务实现者不调用 `svc_run`，而是自行实现自定义异步事件处理时才有意义。当 select(2) 系统调用确定某个 RPC 套接字上已到达 RPC 请求时调用它；`rdfds` 是生成的读取文件描述符位掩码。该例程在所有与 `rdfds` 值关联的套接字都被服务后返回。

**`svc_getreq`** 类似于 `svc_getreqset`，但限于 32 个描述符。此接口已被 `svc_getreqset` 取代。

**`svc_register`** 将 `prognum` 和 `versnum` 与服务分发过程 `dispatch` 关联。如果 `protocol` 为零，则不会向 rpcbind(8) 服务注册该服务。如果 `protocol` 非零，则向本地 rpcbind(8) 服务建立三元组 (`prognum`, `versnum`, `protocol`) 到 `xprt->xp_port` 的映射（通常 `protocol` 为零、`IPPROTO_UDP` 或 `IPPROTO_TCP`）。`dispatch` 过程具有以下形式：`svc_register` 例程成功时返回 1，否则返回 0。

**`svc_run`** 此例程永不返回。它等待 RPC 请求到达，并在请求到达时使用 `svc_getreq` 调用适当的服务过程。此过程通常等待 select(2) 系统调用返回。

**`svc_sendreply`** 由 RPC 服务的分发例程调用，以发送远程过程调用的结果。`xprt` 参数是请求关联的传输句柄；`outproc` 是用于编码结果的 XDR 例程；`out` 是结果的地址。该例程成功时返回 1，否则返回 0。

**`svc_unregister`** 删除二元组 (`prognum`, `versnum`) 到分发例程的所有映射，以及三元组 (`prognum`, `versnum`, `*`) 到端口号的所有映射。

**`svcerr_auth`** 由拒绝由于认证错误而执行远程过程调用的服务分发例程调用。

**`svcerr_decode`** 由无法成功解码其参数的服务分发例程调用。另见 `svc_getargs`。

**`svcerr_noproc`** 由不实现调用方请求的过程号的服务分发例程调用。

**`svcerr_noprog`** 当所需程序未向 RPC 包注册时调用。服务实现者通常不需要此例程。

**`svcerr_progvers`** 当所需程序版本未向 RPC 包注册时调用。服务实现者通常不需要此例程。

**`svcerr_systemerr`** 由服务分发例程在检测到任何特定协议未涵盖的系统错误时调用。例如，如果服务无法再分配存储，它可以调用此例程。

**`svcerr_weakauth`** 由拒绝由于认证参数不足而执行远程过程调用的服务分发例程调用。该例程调用 `svcerr_auth` `xprt` `AUTH_TOOWEAK`。

**`svcraw_create`** 该例程创建一个玩具 RPC 服务传输，并返回指向它的指针。该传输实际上是进程地址空间内的一个缓冲区，因此对应的 RPC 客户端应位于同一地址空间；参见 `clntraw_create`。此例程允许在没有任何内核干扰的情况下模拟 RPC 并获取 RPC 开销（如往返时间）。该例程失败时返回 `NULL`。

**`svctcp_create`** 该例程创建一个基于 TCP/IP 的 RPC 服务传输，并返回指向它的指针。该传输与套接字 `sock` 关联，`sock` 可以是 `RPC_ANYSOCK`，在这种情况下会创建一个新套接字。如果套接字未绑定到本地 TCP 端口，则该例程将其绑定到任意端口。完成后，`xprt->xp_fd` 是传输的套接字描述符，`xprt->xp_port` 是传输的端口号。该例程失败时返回 `NULL`。由于基于 TCP 的 RPC 使用缓冲 I/O，用户可指定缓冲区大小；值为零时选择合适的默认值。

**`svcunix_create`** 该例程创建一个基于 UNIX 的 RPC 服务传输，并返回指向它的指针。该传输与套接字 `sock` 关联，`sock` 可以是 `RPC_ANYSOCK`，在这种情况下会创建一个新套接字。`*path` 参数是最多 104 个字符的可变长度文件系统路径名。当套接字关闭时，此文件 *不会* 被删除。必须使用 unlink(2) 系统调用来删除该文件。完成后，`xprt->xp_fd` 是传输的套接字描述符。该例程失败时返回 `NULL`。由于基于 UNIX 的 RPC 使用缓冲 I/O，用户可指定缓冲区大小；值为零时选择合适的默认值。

**`svcunixfd_create`** 在任何打开的描述符之上创建服务。`sendsize` 和 `recvsize` 参数指示发送和接收缓冲区的大小。如果它们为零，则选择合理的默认值。

**`svcfd_create`** 在任何打开的描述符之上创建服务。通常，此描述符是流协议（如 TCP）的已连接套接字。`sendsize` 和 `recvsize` 参数指示发送和接收缓冲区的大小。如果它们为零，则选择合理的默认值。

**`svcudp_bufcreate`** 该例程创建一个基于 UDP/IP 的 RPC 服务传输，并返回指向它的指针。该传输与套接字 `sock` 关联，`sock` 可以是 `RPC_ANYSOCK`，在这种情况下会创建一个新套接字。如果套接字未绑定到本地 UDP 端口，则该例程将其绑定到任意端口。完成后，`xprt->xp_fd` 是传输的套接字描述符，`xprt->xp_port` 是传输的端口号。该例程失败时返回 `NULL`。这允许用户指定发送和接收基于 UDP 的 RPC 消息的最大数据包大小。

**`xdr_accepted_reply`** 用于编码 RPC 回复消息。此例程适用于希望在不使用 RPC 包的情况下生成 RPC 风格消息的用户。

**`xdr_authunix_parms`** 用于描述 UNIX 凭据。此例程适用于希望在不使用 RPC 认证包的情况下生成这些凭据的用户。

**`xdr_callhdr`** 用于描述 RPC 调用头消息。此例程适用于希望在不使用 RPC 包的情况下生成 RPC 风格消息的用户。

**`xdr_callmsg`** 用于描述 RPC 调用消息。此例程适用于希望在不使用 RPC 包的情况下生成 RPC 风格消息的用户。

**`xdr_opaque_auth`** 用于描述 RPC 认证信息消息。此例程适用于希望在不使用 RPC 包的情况下生成 RPC 风格消息的用户。

**`xdr_pmap`** 用于向各种 rpcbind(8) 过程外部描述参数（`struct pmap`）。此例程适用于希望在不使用 `pmap_*` 接口的情况下生成这些参数的用户。

**`xdr_pmaplist`** 用于外部描述端口映射列表。此例程适用于希望在不使用 `pmap_*` 接口的情况下生成这些参数的用户。

**`xdr_rejected_reply`** 用于描述 RPC 回复消息。此例程适用于希望在不使用 RPC 包的情况下生成 RPC 风格消息的用户。

**`xdr_replymsg`** 用于描述 RPC 回复消息。此例程适用于希望在不使用 RPC 包的情况下生成 RPC 风格消息的用户。

**`xprt_register`** 在 RPC 服务传输句柄创建后，应将其注册到 RPC 服务包。该例程修改全局变量 `svc_fds`。服务实现者通常不需要此例程。

**`xprt_unregister`** 在 RPC 服务传输句柄销毁之前，应将其从 RPC 服务包中注销。该例程修改全局变量 `svc_fds`。服务实现者通常不需要此例程。

## 参见

[rpc_secure(3)](rpc_secure.3.md), [xdr(3)](../man3/xdr.3.md)

> “Remote Procedure Calls: Protocol Specification”.

> “Remote Procedure Call Programming Guide”.

> “rpcgen Programming Guide”.

> “RPC: Remote Procedure Call Protocol Specification”, RFC1050.
