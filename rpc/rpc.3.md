# rpc(3)

`rpc` — 远程过程调用的库例程

## 名称

`rpc`

## 库

Lb libc

## 概要

`#include <rpc/rpc.h>`

`#include <netconfig.h>`

## 描述

这些例程允许 C 语言程序通过网络在其他机器上进行过程调用。首先，客户端向服务器发送请求。服务器收到请求后，调用一个分发例程来执行所请求的服务，然后发回回复。

所有 RPC 例程都需要头文件：

`#include <rpc/rpc.h>`

接受 `struct netconfig` 的例程还需要：

`#include <netconfig.h>`

## Nettype

部分高级 RPC 接口例程接受 `nettype` 字符串作为参数之一（例如 `clnt_create`、`svc_create`、`rpc_reg`、`rpc_call`）。此字符串定义了可用于特定应用程序的传输类别。

`nettype` 参数可以是以下之一：

**netpath** 从 `NETPATH` 环境变量中由其令牌名指示的传输中选择。如果 `NETPATH` 未设置或为 `NULL`，则默认为 "visible"。"netpath" 是默认的 `nettype`。

**visible** 选择在 **/etc/netconfig** 文件中设置了 visible 标志 (v) 的传输。

**circuit_v** 与 "visible" 相同，但仅从 **/etc/netconfig** 文件中的条目中选择面向连接的传输（语义为 "tpi_cots" 或 "tpi_cots_ord"）。

**datagram_v** 与 "visible" 相同，但仅从 **/etc/netconfig** 文件中的条目中选择无连接数据报传输（语义为 "tpi_clts"）。

**circuit_n** 与 "netpath" 相同，但仅选择面向连接的数据报传输（语义为 "tpi_cots" 或 "tpi_cots_ord"）。

**datagram_n** 与 "netpath" 相同，但仅选择无连接数据报传输（语义为 "tpi_clts"）。

**udp** 指 Internet UDP，包括版本 4 和 6。

**tcp** 指 Internet TCP，包括版本 4 和 6。

如果 `nettype` 为 `NULL`，则默认为 "netpath"。传输按 `NETPATH` 变量中从左到右的顺序，或 **/etc/netconfig** 文件中从上到下的顺序尝试。

## 派生类型

RPC 接口中使用的派生类型定义如下：

```c
typedef uint32_t rpcprog_t;
typedef uint32_t rpcvers_t;
typedef uint32_t rpcproc_t;
typedef uint32_t rpcprot_t;
typedef uint32_t rpcport_t;
typedef int32_t  rpc_inline_t;
```

## 数据结构

RPC 包使用的部分数据结构如下所示。

## AUTH 结构

```c
/*
 * 认证信息。对客户端不透明。
 */
struct opaque_auth {
    enum_t    oa_flavor;    /* 认证风格 */
    caddr_t    oa_base;    /* 更多认证内容的地址 */
    u_int    oa_length;    /* 不超过 MAX_AUTH_BYTES */
};
/*
 * 认证句柄，客户端认证器的接口。
 */
typedef struct {
    struct    opaque_auth    ah_cred;
    struct    opaque_auth    ah_verf;
    struct auth_ops {
        void    (*ah_nextverf)();
        int    (*ah_marshal)();    /* nextverf 与序列化 */
        int    (*ah_validate)();    /* 验证验证器 */
        int    (*ah_refresh)();    /* 刷新凭据 */
        void    (*ah_destroy)();    /* 销毁此结构 */
    } *ah_ops;
    caddr_t ah_private;
} AUTH;
```

## CLIENT 结构

```c
/*
 * 客户端 rpc 句柄。
 * 由各个实现创建。
 * 客户端负责初始化认证。
 */
typedef struct {
    AUTH    *cl_auth;    /* 认证器 */
    struct clnt_ops {
        enum clnt_stat    (*cl_call)();    /* 调用远程过程 */
        void    (*cl_abort)();        /* 中止调用 */
        void    (*cl_geterr)();        /* 获取特定错误代码 */
        bool_t    (*cl_freeres)();    /* 释放结果 */
        void    (*cl_destroy)();    /* 销毁此结构 */
        bool_t    (*cl_control)();    /* rpc 的 ioctl() */
    } *cl_ops;
    caddr_t    cl_private;    /* 私有内容 */
    char    *cl_netid;    /* 网络标识符 */
    char    *cl_tp;        /* 设备名 */
} CLIENT;
```

## SVCXPRT 结构

```c
enum xprt_stat {
    XPRT_DIED,
    XPRT_MOREREQS,
    XPRT_IDLE
};
/*
 * 服务器端传输句柄
 */
typedef struct {
    int    xp_fd;    /* 服务器句柄的文件描述符 */
    u_short    xp_port;    /* 已过时 */
    const struct xp_ops {
        bool_t    (*xp_recv)();    /* 接收传入请求 */
        enum xprt_stat    (*xp_stat)();    /* 获取传输状态 */
        bool_t    (*xp_getargs)();    /* 获取参数 */
        bool_t    (*xp_reply)();      /* 发送回复 */
        bool_t    (*xp_freeargs)(); /* 释放为参数分配的内存 */
        void    (*xp_destroy)();    /* 销毁此结构 */
    } *xp_ops;
    int    xp_addrlen;    /* 远程地址长度。已过时 */
    struct sockaddr_in    xp_raddr; /* 已过时 */
    const struct xp_ops2 {
        bool_t    (*xp_control)();    /* 万能函数 */
    } *xp_ops2;
    char    *xp_tp;    /* 传输提供者设备名 */
    char    *xp_netid;    /* 网络标识符 */
    struct netbuf    xp_ltaddr;    /* 本地传输地址 */
    struct netbuf    xp_rtaddr;    /* 远程传输地址 */
    struct opaque_auth    xp_verf;    /* 原始响应验证器 */
    caddr_t    xp_p1;    /* 私有：供 svc 操作使用 */
    caddr_t    xp_p2;    /* 私有：供 svc 操作使用 */
    caddr_t    xp_p3;    /* 私有：供 svc 库使用 */
    int    xp_type    /* 传输类型 */
} SVCXPRT;
```

## svc_reg 结构

```c
struct svc_req {
    rpcprog_t    rq_prog;    /* 服务程序号 */
    rpcvers_t    rq_vers;    /* 服务协议版本 */
    rpcproc_t    rq_proc;    /* 所需过程 */
    struct opaque_auth    rq_cred;    /* 来自线路的原始凭据 */
    caddr_t    rq_clntcred;    /* 只读的已处理凭据 */
    SVCXPRT    *rq_xprt;    /* 关联的传输 */
};
```

## XDR 结构

```c
/*
 * XDR 操作。
 * XDR_ENCODE 导致类型被编码到流中。
 * XDR_DECODE 导致类型从流中提取。
 * XDR_FREE 可用于释放由 XDR_DECODE 请求分配的空间。
 */
enum xdr_op {
    XDR_ENCODE=0,
    XDR_DECODE=1,
    XDR_FREE=2
};
/*
 * 每单位外部数据的字节数。
 */
#define BYTES_PER_XDR_UNIT    (4)
#define RNDUP(x)  ((((x) + BYTES_PER_XDR_UNIT - 1) /
                   BYTES_PER_XDR_UNIT) * BYTES_PER_XDR_UNIT)
/*
 * 每个要被编码或解码的数据类型都有一个 xdrproc_t。
 * xdrproc_t 的第二个参数是指向不透明指针的指针。
 * 该不透明指针通常指向要解码的数据类型的结构。
 * 如果它指向 0，则类型例程应分配适当大小的动态存储并返回。
 * bool_t  (*xdrproc_t)(XDR *, void *);
 */
typedef  bool_t (*xdrproc_t)(XDR *, void *);
/*
 * XDR 句柄。
 * 包含正应用于流的操作，以及特定实现的操作向量
 */
typedef struct {
    enum xdr_op    x_op;    /* 操作；快速附加参数 */
    struct xdr_ops {
        bool_t    (*x_getlong)();    /* 从底层流获取 long */
        bool_t    (*x_putlong)();    /* 向底层流放入 long */
        bool_t    (*x_getbytes)(); /* 从底层流获取字节 */
        bool_t    (*x_putbytes)(); /* 向底层流放入字节 */
        u_int    (*x_getpostn)(); /* 返回从开头的偏移字节数 */
        bool_t    (*x_setpostn)(); /* 让你重新定位流 */
        long *    (*x_inline)();    /* 缓冲数据的快速指针 */
        void    (*x_destroy)();    /* 释放此 xdr_stream 的私有数据 */
    } *x_ops;
    caddr_t    x_public;    /* 用户数据 */
    caddr_t    x_private;    /* 指向私有数据的指针 */
    caddr_t    x_base;    /* 私有，用于位置信息 */
    u_int    x_handy;    /* 额外的私有字 */
} XDR;
/*
 * netbuf 结构。此结构在 SysV 系统上定义于 <xti.h>，
 * 但 NetBSD / FreeBSD 不使用 XTI。
 *
 * 通常，buf 将指向 struct sockaddr，len 和 maxlen
 * 分别包含该套接字地址的长度和最大长度。
 */
struct netbuf {
	unsigned int maxlen;
	unsigned int len;
	void *buf;
};
/*
 * XTI t_bind 调用的地址和选项参数的格式。
 * 仅出于兼容性提供，不应使用，除了作为
 * svc_tli_create() 的参数。
 */
struct t_bind {
	struct netbuf   addr;
	unsigned int    qlen;
};
```

## 例程索引

下表列出了 RPC 例程及其所在的手册参考页：

| RPC 例程 | 手册参考页 |
| :------: | :--------: |
| `auth_destroy` | [rpc_clnt_auth(3)](rpc_clnt_auth.3.md) |
| `authdes_create` | [rpc_soc(3)](rpc_soc.3.md) |
| `authnone_create` | [rpc_clnt_auth(3)](rpc_clnt_auth.3.md) |
| `authsys_create` | [rpc_clnt_auth(3)](rpc_clnt_auth.3.md) |
| `authsys_create_default` | [rpc_clnt_auth(3)](rpc_clnt_auth.3.md) |
| `authunix_create` | [rpc_soc(3)](rpc_soc.3.md) |
| `authunix_create_default` | [rpc_soc(3)](rpc_soc.3.md) |
| `callrpc` | [rpc_soc(3)](rpc_soc.3.md) |
| `clnt_broadcast` | [rpc_soc(3)](rpc_soc.3.md) |
| `clnt_call` | [rpc_clnt_calls(3)](rpc_clnt_calls.3.md) |
| `clnt_control` | [rpc_clnt_create(3)](rpc_clnt_create.3.md) |
| `clnt_create` | [rpc_clnt_create(3)](rpc_clnt_create.3.md) |
| `clnt_create_timed` | [rpc_clnt_create(3)](rpc_clnt_create.3.md) |
| `clnt_create_vers` | [rpc_clnt_create(3)](rpc_clnt_create.3.md) |
| `clnt_create_vers_timed` | [rpc_clnt_create(3)](rpc_clnt_create.3.md) |
| `clnt_destroy` | [rpc_clnt_create(3)](rpc_clnt_create.3.md) |
| `clnt_dg_create` | [rpc_clnt_create(3)](rpc_clnt_create.3.md) |
| `clnt_freeres` | [rpc_clnt_calls(3)](rpc_clnt_calls.3.md) |
| `clnt_geterr` | [rpc_clnt_calls(3)](rpc_clnt_calls.3.md) |
| `clnt_pcreateerror` | [rpc_clnt_create(3)](rpc_clnt_create.3.md) |
| `clnt_perrno` | [rpc_clnt_calls(3)](rpc_clnt_calls.3.md) |
| `clnt_perror` | [rpc_clnt_calls(3)](rpc_clnt_calls.3.md) |
| `clnt_raw_create` | [rpc_clnt_create(3)](rpc_clnt_create.3.md) |
| `clnt_spcreateerror` | [rpc_clnt_create(3)](rpc_clnt_create.3.md) |
| `clnt_sperrno` | [rpc_clnt_calls(3)](rpc_clnt_calls.3.md) |
| `clnt_sperror` | [rpc_clnt_calls(3)](rpc_clnt_calls.3.md) |
| `clnt_tli_create` | [rpc_clnt_create(3)](rpc_clnt_create.3.md) |
| `clnt_tp_create` | [rpc_clnt_create(3)](rpc_clnt_create.3.md) |
| `clnt_tp_create_timed` | [rpc_clnt_create(3)](rpc_clnt_create.3.md) |
| `clnt_udpcreate` | [rpc_soc(3)](rpc_soc.3.md) |
| `clnt_vc_create` | [rpc_clnt_create(3)](rpc_clnt_create.3.md) |
| `clntraw_create` | [rpc_soc(3)](rpc_soc.3.md) |
| `clnttcp_create` | [rpc_soc(3)](rpc_soc.3.md) |
| `clntudp_bufcreate` | [rpc_soc(3)](rpc_soc.3.md) |
| `get_myaddress` | [rpc_soc(3)](rpc_soc.3.md) |
| `pmap_getmaps` | [rpc_soc(3)](rpc_soc.3.md) |
| `pmap_getport` | [rpc_soc(3)](rpc_soc.3.md) |
| `pmap_rmtcall` | [rpc_soc(3)](rpc_soc.3.md) |
| `pmap_set` | [rpc_soc(3)](rpc_soc.3.md) |
| `pmap_unset` | [rpc_soc(3)](rpc_soc.3.md) |
| `registerrpc` | [rpc_soc(3)](rpc_soc.3.md) |
| `rpc_broadcast` | [rpc_clnt_calls(3)](rpc_clnt_calls.3.md) |
| `rpc_broadcast_exp` | [rpc_clnt_calls(3)](rpc_clnt_calls.3.md) |
| `rpc_call` | [rpc_clnt_calls(3)](rpc_clnt_calls.3.md) |
| `rpc_reg` | [rpc_svc_calls(3)](rpc_svc_calls.3.md) |
| `svc_create` | [rpc_svc_create(3)](rpc_svc_create.3.md) |
| `svc_destroy` | [rpc_svc_create(3)](rpc_svc_create.3.md) |
| `svc_dg_create` | [rpc_svc_create(3)](rpc_svc_create.3.md) |
| `svc_dg_enablecache` | [rpc_svc_calls(3)](rpc_svc_calls.3.md) |
| `svc_fd_create` | [rpc_svc_create(3)](rpc_svc_create.3.md) |
| `svc_fds` | [rpc_soc(3)](rpc_soc.3.md) |
| `svc_freeargs` | [rpc_svc_reg(3)](rpc_svc_reg.3.md) |
| `svc_getargs` | [rpc_svc_reg(3)](rpc_svc_reg.3.md) |
| `svc_getcaller` | [rpc_soc(3)](rpc_soc.3.md) |
| `svc_getreq` | [rpc_soc(3)](rpc_soc.3.md) |
| `svc_getreqset` | [rpc_svc_calls(3)](rpc_svc_calls.3.md) |
| `svc_getrpccaller` | [rpc_svc_calls(3)](rpc_svc_calls.3.md) |
| `svc_kerb_reg` | kerberos_rpc(3) |
| `svc_raw_create` | [rpc_svc_create(3)](rpc_svc_create.3.md) |
| `svc_reg` | [rpc_svc_calls(3)](rpc_svc_calls.3.md) |
| `svc_register` | [rpc_soc(3)](rpc_soc.3.md) |
| `svc_run` | [rpc_svc_reg(3)](rpc_svc_reg.3.md) |
| `svc_sendreply` | [rpc_svc_reg(3)](rpc_svc_reg.3.md) |
| `svc_tli_create` | [rpc_svc_create(3)](rpc_svc_create.3.md) |
| `svc_tp_create` | [rpc_svc_create(3)](rpc_svc_create.3.md) |
| `svc_unreg` | [rpc_svc_calls(3)](rpc_svc_calls.3.md) |
| `svc_unregister` | [rpc_soc(3)](rpc_soc.3.md) |
| `svc_vc_create` | [rpc_svc_create(3)](rpc_svc_create.3.md) |
| `svcerr_auth` | [rpc_svc_err(3)](rpc_svc_err.3.md) |
| `svcerr_decode` | [rpc_svc_err(3)](rpc_svc_err.3.md) |
| `svcerr_noproc` | [rpc_svc_err(3)](rpc_svc_err.3.md) |
| `svcerr_noprog` | [rpc_svc_err(3)](rpc_svc_err.3.md) |
| `svcerr_progvers` | [rpc_svc_err(3)](rpc_svc_err.3.md) |
| `svcerr_systemerr` | [rpc_svc_err(3)](rpc_svc_err.3.md) |
| `svcerr_weakauth` | [rpc_svc_err(3)](rpc_svc_err.3.md) |
| `svcfd_create` | [rpc_soc(3)](rpc_soc.3.md) |
| `svcraw_create` | [rpc_soc(3)](rpc_soc.3.md) |
| `svctcp_create` | [rpc_soc(3)](rpc_soc.3.md) |
| `svcudp_bufcreate` | [rpc_soc(3)](rpc_soc.3.md) |
| `svcudp_create` | [rpc_soc(3)](rpc_soc.3.md) |
| `xdr_accepted_reply` | [rpc_xdr(3)](rpc_xdr.3.md) |
| `xdr_authsys_parms` | [rpc_xdr(3)](rpc_xdr.3.md) |
| `xdr_authunix_parms` | [rpc_soc(3)](rpc_soc.3.md) |
| `xdr_callhdr` | [rpc_xdr(3)](rpc_xdr.3.md) |
| `xdr_callmsg` | [rpc_xdr(3)](rpc_xdr.3.md) |
| `xdr_opaque_auth` | [rpc_xdr(3)](rpc_xdr.3.md) |
| `xdr_rejected_reply` | [rpc_xdr(3)](rpc_xdr.3.md) |
| `xdr_replymsg` | [rpc_xdr(3)](rpc_xdr.3.md) |
| `xprt_register` | [rpc_svc_calls(3)](rpc_svc_calls.3.md) |
| `xprt_unregister` | [rpc_svc_calls(3)](rpc_svc_calls.3.md) |

## 文件

**/etc/netconfig**

## 参见

[getnetconfig(3)](getnetconfig.3.md), [getnetpath(3)](getnetpath.3.md), [rpc_clnt_auth(3)](rpc_clnt_auth.3.md), [rpc_clnt_calls(3)](rpc_clnt_calls.3.md), [rpc_clnt_create(3)](rpc_clnt_create.3.md), [rpc_svc_calls(3)](rpc_svc_calls.3.md), [rpc_svc_create(3)](rpc_svc_create.3.md), [rpc_svc_err(3)](rpc_svc_err.3.md), [rpc_svc_reg(3)](rpc_svc_reg.3.md), [rpc_xdr(3)](rpc_xdr.3.md), [rpcbind(3)](rpcbind.3.md), [xdr(3)](../man3/xdr.3.md), netconfig(5)
