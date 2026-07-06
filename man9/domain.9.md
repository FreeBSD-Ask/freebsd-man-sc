# domain.9

`domain` — 内核套接字实现的编程接口

## 名称

`domain`, `protosw`

## 概要

```c
#include <sys/param.h>

#include <sys/kernel.h>

#include <sys/protosw.h>

#include <sys/domain.h>

void
domain_add(struct domain *dom)

void
domain_remove(struct domain *dom)

void
DOMAIN_SET(domain)

int
protosw_register(struct domain *dom, struct protosw *pr)

int
protosw_unregister(struct protosw *pr)
```

## 描述

`protosw` 子系统允许实现通过 socket(2) API 暴露给用户态的通信协议。当应用程序执行 `socket(domain, type, protocol)` 系统调用时，内核搜索与 `domain` 参数匹配的 `protosw`，然后在该域内搜索与 `type` 匹配的协议。如果第三个参数 `protocol` 不为 `0`，则该值也必须匹配。所找到的结构必须实现某些方法，以便 socket(2) API 能用于此种特定类型的套接字。

实现域的最小 `protosw` 结构应使用稀疏 C99 初始化器初始化，其公开字段如下：

```c
struct domain {
    /*
     * 必填字段。
     */
    int	dom_family;	/* PF_xxx，socket(2) 的第一个参数 */
    char	*dom_name;	/* 域的文本名称 */
    u_int	dom_nprotosw;	/* dom_protosw[] 的长度 */
    /*
     * 以下方法为可选。
     */
    int	(*dom_probe)(void);			/* 检查是否支持 */
    struct rib_head *(*dom_rtattach)(uint32_t);	/* 初始化路由表 */
    void (*dom_rtdetach)(struct rib_head *);	/* 清理表 */
    void *(*dom_ifattach)(struct ifnet *);	/* 接口附加 */
    void (*dom_ifdetach)(struct ifnet *, void *);/* 与分离回调 */
    int	(*dom_ifmtu)(struct ifnet *);		/* mtu 变更 */
    /*
     * 必填的变长 protosw 结构指针数组。
     */
    struct  protosw *dom_protosw[];
};
```

每个域包含协议切换结构（`struct protosw *`）的 `dom_protosw` 数组，每个支持的套接字类型对应一个。数组可针对可加载协议保留 `NULL` 间隔。应使用稀疏 C99 初始化器初始化 `protosw` 结构。该结构有必填字段 `pr_type` 和必填方法 `pr_attach`。其余方法为可选，但有意义的协议应实现其中一些。

```c
struct protosw {
    short	pr_type;	/* socket(2) 的第二个参数 */
    short	pr_protocol;	/* socket(2) 的第三个参数或 0 */
    short	pr_flags;	/* 见 protosw.h */
    pr_soreceive_t  *pr_soreceive;  /* recv(2) */
    pr_rcvd_t       *pr_rcvd;       /* 若 PR_WANTRCV 则为 soreceive_generic() */
    pr_sosend_t     *pr_sosend;     /* send(2) */
    pr_send_t       *pr_send;       /* 通过 sosend_generic() 的 send(2) */
    pr_ready_t      *pr_ready;      /* sendfile/ktls 就绪状态 */
    pr_sopoll_t     *pr_sopoll;     /* poll(2) */
    pr_attach_t     *pr_attach;     /* 创建：socreate()，sonewconn() */
    pr_detach_t     *pr_detach;     /* 销毁：sofree() */
    pr_connect_t    *pr_connect;    /* connect(2) */
    pr_disconnect_t *pr_disconnect; /* sodisconnect() */
    pr_close_t      *pr_close;      /* close(2) */
    pr_shutdown_t   *pr_shutdown;   /* shutdown(2) */
    pr_abort_t      *pr_abort;      /* 突然拆除：soabort() */
    pr_aio_queue_t  *pr_aio_queue;  /* aio(9) */
    pr_bind_t       *pr_bind;       /* bind(2) */
    pr_bindat_t     *pr_bindat;     /* bindat(2) */
    pr_listen_t     *pr_listen;     /* listen(2) */
    pr_accept_t     *pr_accept;     /* accept(2) */
    pr_connectat_t  *pr_connectat;  /* connectat(2) */
    pr_connect2_t   *pr_connect2;   /* socketpair(2) */
    pr_control_t    *pr_control;    /* ioctl(2) */
    pr_rcvoob_t     *pr_rcvoob;     /* soreceive_rcvoob() */
    pr_ctloutput_t  *pr_ctloutput;  /* 控制输出（来自上层） */
    pr_peeraddr_t   *pr_peeraddr;   /* getpeername(2) */
    pr_sockaddr_t   *pr_sockaddr;   /* getsockname(2) */
    pr_sense_t      *pr_sense;      /* stat(2) */
};
```

以下函数用于处理新域和协议的注册。

`domain_add` 向系统添加新的协议域。在大多数情况下，不直接调用 `domain_add`，而是使用 `DOMAIN_SET`，它是 `SYSINIT` 宏的包装。如果新域定义了 `dom_probe` 例程，则在 `domain_add` 中首先调用它以确定是否应在当前系统上支持该域。如果探测例程返回非 0 值，则不会添加该域。一旦添加了域，就无法完全卸载。这是因为没有适当的引用计数系统来确定该域内的套接字是否存在活动引用。但是，实验性的 `domain_remove` 存在，未来可能支持可卸载的域。

`protosw_register` 在域的 `dom_protosw` 有空槽时，动态地向域添加协议。动态添加的协议稍后可通过 `protosw_unregister` 卸载。

## 返回值

`domain_add` 永远不会失败，但如果其 `dom_probe` 失败，可能不会添加域。

`protosw_register` 函数可能在以下情况下失败：

**[`EEXIST`]** 域中已存在具有相同 `pr_type` 和 `pr_protocol` 值的协议。

**[`ENOMEM`]** 域的 `dom_protosw` 中没有任何 `NULL` 槽位。

## 参见

socket(2), [SYSINIT(9)](SYSINIT.9.md)

## 历史

`protosw` 子系统首次出现于 4.3BSD，作为最初的 socket(2) API 实现的一部分。

`protosw` 子系统及本手册页在 FreeBSD 14 中被显著重写。

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 和 Gleb Smirnoff <glebius@FreeBSD.org> 编写。
