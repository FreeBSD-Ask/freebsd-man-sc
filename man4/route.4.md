# route.4

`route` — 内核数据包转发数据库

## 名称

`route`

## 概要

`#include <sys/types.h>`

`#include <sys/time.h>`

`#include <sys/socket.h>`

`#include <net/if.h>`

`#include <net/route.h>`

`Ft int Fn socket PF_ROUTE SOCK_RAW int family`

## 描述

FreeBSD 提供了一些数据包路由设施。内核维护着一个路由信息数据库，用于在传输数据包时选择合适的网络接口。

用户进程（或可能是多个协作的进程）通过在一种特殊套接字上发送消息来维护此数据库。这取代了早期版本中使用的固定大小 ioctl(2)。路由表更改只能由超级用户执行。

操作系统可能会自发地发出路由消息以响应外部事件，例如接收到重定向，或未能为请求找到合适的路由。各消息类型将在下文更详细地描述。

路由数据库条目有两种形式：针对特定主机的条目，或针对通用子网上所有主机的条目（由位掩码和掩码下的值指定）。通过使用全零掩码可实现通配或默认路由的效果，且可能存在层次化路由。

当系统引导并为网络接口分配地址时，每个协议族在每个接口准备好进行流量传输时都会为其安装一个路由表条目。通常，协议将通过每个接口的路由指定为到目的主机或网络的"直接"连接。如果路由是直接的，协议族的传输层通常请求数据包发送至数据包中指定的同一主机。否则，请求接口将数据包寻址到路由条目中列出的网关（即数据包被转发）。

在为数据包寻路时，内核将尝试找到与目的地匹配的最特定路由。（如果存在两组不同的掩码和掩码下值匹配对，则更特定的是掩码中位数更多的那个。到主机的路由被视为具有与目的地位数相同数量的全 1 掩码）。如果未找到条目，则宣布目的地不可达，并且如果下文所述路由控制套接字上存在监听者，则生成路由未命中消息。

通配路由条目通过零目的地址值和全零掩码指定。当系统未能找到与目的地匹配的其他路由时，将使用通配路由。通配路由和路由重定向的组合可提供一种经济高效的流量路由机制。

通过使用上文概要中所示的 socket 调用来打开传递路由控制消息的通道：

`family` 参数可为 `AF_UNSPEC`，将提供所有地址族的路由信息，也可通过指定所需地址族来限制为特定地址族。每个系统可打开多个路由套接字。

消息由一个头部和少量 sockaddrs（现在为可变长度，特别是在 ISO 情况下）组成，按位置解释，并由 sockaddr 中新的 length 项分隔。带有四个地址的消息示例可能是 ISO 重定向：Destination、Netmask、Gateway 和 Author of the redirect。哪些地址存在的解释由头部内的位掩码给出，序列从向量中最低有效位到最高有效位。

发送到内核的任何消息都会被返回，并且副本会发送给所有感兴趣的监听者。内核会提供发送方的进程 ID，发送方可使用附加的 sequence 字段来区分未完成的消息。但是，当内核缓冲区耗尽时，消息回复可能丢失。

内核可能会拒绝某些消息，并通过填写 `rtm_errno` 字段来指示。如果请求复制现有条目，路由代码会返回 Er EEXIST；如果请求删除不存在的条目，返回 Er ESRCH；如果安装新路由时资源不足，返回 Er ENOBUFS。在当前实现中，所有路由进程都在本地运行，即使路由回复消息丢失，`rtm_errno` 的值也可通过常规 *errno* 机制获得。

进程可通过发出 setsockopt(2) 调用关闭 `SOL_SOCKET` 层级的 `SO_USELOOPBACK` 选项，以避免读取自身消息回复的开销。进程可通过对进一步输入执行 shutdown(2) 系统调用来忽略来自路由套接字的所有消息。

如果某条路由在被删除时正在使用中，该路由条目将被标记为下线并从路由表中移除，但与之关联的资源要等到对它的所有引用都释放后才会被回收。用户进程可使用 `RTM_GET` 消息或通过调用 sysctl(3) 获取到特定目的地的路由条目信息。

消息包括：

```sh
#define	RTM_ADD		0x1    /* 添加路由 */
#define	RTM_DELETE	0x2    /* 删除路由 */
#define	RTM_CHANGE	0x3    /* 更改度量、标志或网关 */
#define	RTM_GET		0x4    /* 报告信息 */
#define	RTM_LOSING	0x5    /* 内核怀疑发生分区 */
#define	RTM_REDIRECT	0x6    /* 被告知使用不同路由 */
#define	RTM_MISS	0x7    /* 在此地址上的查找失败 */
#define	RTM_LOCK	0x8    /* 固定指定的度量 */
#define	RTM_RESOLVE	0xb    /* 请求将 dst 解析为 LL 地址 - 未使用 */
#define	RTM_NEWADDR	0xc    /* 地址正被添加到接口 */
#define	RTM_DELADDR	0xd    /* 地址正从接口移除 */
#define	RTM_IFINFO	0xe    /* 接口上线/下线等 */
#define	RTM_NEWMADDR	0xf    /* 多播组成员关系正被添加到接口 */
#define	RTM_DELMADDR	0x10   /* 多播组成员关系正被删除 */
#define	RTM_IFANNOUNCE	0x11   /* 接口到达/离开 */
#define	RTM_IEEE80211	0x12   /* IEEE80211 无线事件 */
```

消息头部由以下之一构成：

```sh
struct rt_msghdr {
    u_short rtm_msglen;         /* 用于跳过未理解的消息 */
    u_char  rtm_version;        /* 未来的二进制兼容性 */
    u_char  rtm_type;           /* 消息类型 */
    u_short rtm_index;          /* 关联 ifp 的索引 */
    int     rtm_flags;          /* 标志，包括内核和消息，例如 DONE */
    int     rtm_addrs;          /* 标识消息中 sockaddrs 的位掩码 */
    pid_t   rtm_pid;            /* 标识发送方 */
    int     rtm_seq;            /* 供发送方标识操作 */
    int     rtm_errno;          /* 失败原因 */
    int     rtm_fmask;          /* RTM_CHANGE 消息中使用的位掩码 */
    u_long  rtm_inits;          /* 正在初始化哪些度量 */
    struct  rt_metrics rtm_rmx;	/* 度量本身 */
};
struct if_msghdr {
    u_short ifm_msglen;         /* 用于跳过未理解的消息 */
    u_char  ifm_version;        /* 未来的二进制兼容性 */
    u_char  ifm_type;           /* 消息类型 */
    int     ifm_addrs;          /* 类似于 rtm_addrs */
    int     ifm_flags;          /* if_flags 的值 */
    u_short ifm_index;          /* 关联 ifp 的索引 */
    struct  if_data ifm_data;   /* 关于接口的统计信息和其他数据 */
};
struct ifa_msghdr {
    u_short ifam_msglen;        /* 用于跳过未理解的消息 */
    u_char  ifam_version;       /* 未来的二进制兼容性 */
    u_char  ifam_type;          /* 消息类型 */
    int     ifam_addrs;         /* 类似于 rtm_addrs */
    int     ifam_flags;         /* ifa_flags 的值 */
    u_short ifam_index;         /* 关联 ifp 的索引 */
    int     ifam_metric;        /* ifa_metric 的值 */
};
struct ifma_msghdr {
    u_short ifmam_msglen;       /* 用于跳过未理解的消息 */
    u_char  ifmam_version;      /* 未来的二进制兼容性 */
    u_char  ifmam_type;         /* 消息类型 */
    int     ifmam_addrs;        /* 类似于 rtm_addrs */
    int     ifmam_flags;        /* ifa_flags 的值 */
    u_short ifmam_index;        /* 关联 ifp 的索引 */
};
struct if_announcemsghdr {
	u_short	ifan_msglen;	/* 用于跳过未理解的消息 */
	u_char	ifan_version;	/* 未来的二进制兼容性 */
	u_char	ifan_type;	/* 消息类型 */
	u_short	ifan_index;	/* 关联 ifp 的索引 */
	char	ifan_name[IFNAMSIZ]; /* 接口名，例如 "en0" */
	u_short	ifan_what;	/* 公告的类型 */
};
```

`RTM_IFINFO` 消息使用 `if_msghdr` 头部，`RTM_NEWADDR` 和 `RTM_DELADDR` 消息使用 `ifa_msghdr` 头部，`RTM_NEWMADDR` 和 `RTM_DELMADDR` 消息使用 `ifma_msghdr` 头部，`RTM_IFANNOUNCE` 消息使用 `if_announcemsghdr` 头部，所有其他消息使用 `rt_msghdr` 头部。

"`struct rt_metrics`" 和标志位的定义见 [rtentry(9)](../man9/rtentry.9.md)。

rmx_locks 和 rtm_inits 中度量值的说明符为：

```sh
#define	RTV_MTU       0x1    /* 初始化或锁定 _mtu */
#define	RTV_HOPCOUNT  0x2    /* 初始化或锁定 _hopcount */
#define	RTV_EXPIRE    0x4    /* 初始化或锁定 _expire */
#define	RTV_RPIPE     0x8    /* 初始化或锁定 _recvpipe */
#define	RTV_SPIPE     0x10   /* 初始化或锁定 _sendpipe */
#define	RTV_SSTHRESH  0x20   /* 初始化或锁定 _ssthresh */
#define	RTV_RTT       0x40   /* 初始化或锁定 _rtt */
#define	RTV_RTTVAR    0x80   /* 初始化或锁定 _rttvar */
#define	RTV_WEIGHT    0x100  /* 初始化或锁定 _weight */
```

消息中存在哪些地址的说明符为：

```sh
#define RTA_DST       0x1    /* 存在目的 sockaddr */
#define RTA_GATEWAY   0x2    /* 存在网关 sockaddr */
#define RTA_NETMASK   0x4    /* 存在网络掩码 sockaddr */
#define RTA_GENMASK   0x8    /* 存在克隆掩码 sockaddr - 未使用 */
#define RTA_IFP       0x10   /* 存在接口名 sockaddr */
#define RTA_IFA       0x20   /* 存在接口地址 sockaddr */
#define RTA_AUTHOR    0x40   /* 重定向作者的 sockaddr */
#define RTA_BRD       0x80   /* 对于 NEWADDR，广播或点对点目的地址 */
```

## 参见

sysctl(3), [route(8)](../man8/route.8.md), [rtentry(9)](../man9/rtentry.9.md)

`rtm_flags` 字段的常量记录在 [route(8)](../man8/route.8.md) 实用程序的手册页中。

## 历史

`PF_ROUTE` 协议族最早出现在 4.3BSD 中。
