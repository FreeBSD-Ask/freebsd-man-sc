# multicast(4)

`multicast` — 多播路由

## 名称

`multicast`

## 概要

`options MROUTING`

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/in.h>`

`#include <netinet/ip_mroute.h>`

`#include <netinet6/ip6_mroute.h>`

Ft int Fn getsockopt int s IPPROTO_IP MRT_INIT void *optval socklen_t*optlen Ft int Fn setsockopt int s IPPROTO_IP MRT_INIT const void *optval socklen_t optlen Ft int Fn getsockopt int s IPPROTO_IPV6 MRT6_INIT void*optval socklen_t *optlen Ft int Fn setsockopt int s IPPROTO_IPV6 MRT6_INIT const void*optval socklen_t optlen

## 描述

多播路由用于在多点网络中将数据包高效地传播给一组多播侦听者。如果使用单播将数据复制给所有侦听者，则某些网络链路可能携带同一数据包的多个副本。使用多播路由时，每条网络链路的开销至多减少为一个副本。

所有支持多播的路由器必须运行共同的多播路由协议。建议使用协议无关多播 - 稀疏模式（PIM-SM）或协议无关多播 - 密集模式（PIM-DM），因为它们是目前互联网社区中普遍接受的协议。Sx HISTORY 章节讨论了以前的多播路由协议。

要启动多播路由，用户必须在内核中启用多播转发（参见 Sx SYNOPSIS 中关于内核配置选项的说明），并且必须运行支持多播路由的用户级进程。从开发者的角度来看，应使用 Sx Programming Guide 章节中描述的编程指南来控制内核中的多播转发。

### 编程指南

本节提供关于基本多播路由 API 的信息。所谓的“高级多播 API”在 Sx Advanced Multicast API Programming Guide 章节中描述。

首先，必须打开一个多播路由套接字。该套接字将用于控制内核中的多播转发。注意，以下大多数操作需要特定权限（即 root 权限）：

```sh
/* IPv4 */
int mrouter_s4;
mrouter_s4 = socket(AF_INET, SOCK_RAW, IPPROTO_IGMP);
```

```sh
int mrouter_s6;
mrouter_s6 = socket(AF_INET6, SOCK_RAW, IPPROTO_ICMPV6);
```

注意，如果路由器需要打开 IGMP 或 ICMPv6 套接字（分别用于 IPv4 和 IPv6）以发送或接收 IGMP 或 MLD 多播组成员关系消息，则应使用同一个 `mrouter_s4` 或 `mrouter_s6` 套接字来分别发送和接收 IGMP 或 MLD 消息。在 BSD 派生的内核中，可能可以仅为 IGMP 或 MLD 消息打开单独的套接字。然而，其他一些内核（例如 Linux）要求多播路由套接字必须用于发送和接收 IGMP 或 MLD 消息。因此，出于可移植性原因，多播路由套接字也应复用于 IGMP 和 MLD 消息。

打开多播路由套接字后，可使用它在内核中启用多播转发：

```sh
/* IPv4 */
int v = 1;
setsockopt(mrouter_s4, IPPROTO_IP, MRT_INIT, (void *)&v, sizeof(v));
```

```sh
/* IPv6 */
int v = 1;
setsockopt(mrouter_s6, IPPROTO_IPV6, MRT6_INIT, (void *)&v, sizeof(v));
...
/* 如有必要，过滤所有 ICMPv6 消息 */
struct icmp6_filter filter;
ICMP6_FILTER_SETBLOCKALL(&filter);
setsockopt(mrouter_s6, IPPROTO_ICMPV6, ICMP6_FILTER, (void *)&filter,
           sizeof(filter));
```

当应用于多播路由套接字时，`MRT_DONE` 和 `MRT6_DONE` 套接字选项会禁用内核中的多播转发：

```sh
/* IPv4 */
int v = 1;
setsockopt(mrouter_s4, IPPROTO_IP, MRT_DONE, (void *)&v, sizeof(v));
```

```sh
/* IPv6 */
int v = 1;
setsockopt(mrouter_s6, IPPROTO_IPV6, MRT6_DONE, (void *)&v, sizeof(v));
```

关闭套接字具有相同的效果。

启用多播转发后，如果我们运行 PIM-SM 或 PIM-DM，则可以使用多播路由套接字在内核中启用 PIM 处理（参见 [pim(4)](pim.4.md)。

对于将用于多播转发的每个网络接口（例如物理接口或虚拟隧道），必须将相应的多播接口添加到内核中：

```sh
/* IPv4 */
struct vifctl vc;
memset(&vc, 0, sizeof(vc));
/* 适当地分配所有 vifctl 字段 */
vc.vifc_vifi = vif_index;
vc.vifc_flags = vif_flags;
vc.vifc_threshold = min_ttl_threshold;
vc.vifc_rate_limit = 0;
memcpy(&vc.vifc_lcl_addr, &vif_local_address, sizeof(vc.vifc_lcl_addr));
setsockopt(mrouter_s4, IPPROTO_IP, MRT_ADD_VIF, (void *)&vc,
           sizeof(vc));
```

`vif_index` 在每个 vif 中必须唯一。`vif_flags` 包含如下定义的 `VIFF_*` 标志

`#include <netinet/ip_mroute.h>`

FreeBSD 不再支持 `VIFF_TUNNEL` 标志。希望通过隧道转发多播数据报的用户应考虑配置 [gif(4)](gif.4.md) 或 [gre(4)](gre.4.md) 隧道，并将其用作物理接口。

`min_ttl_threshold` 包含多播数据包在该 vif 上转发所必须具有的最小 TTL。通常值为 1。

`max_rate_limit` 参数在 FreeBSD 中不再受支持，应设置为 0。希望对多播数据报进行速率限制的用户应考虑使用 [dummynet(4)](dummynet.4.md) 或 [altq(4)](altq.4.md)。

`vif_local_address` 包含相应本地接口的本地 IP 地址。在 DVMRP 多播隧道的情况下，`vif_remote_address` 包含远程 IP 地址。

```sh
/* IPv6 */
struct mif6ctl mc;
memset(&mc, 0, sizeof(mc));
/* 适当地分配所有 mif6ctl 字段 */
mc.mif6c_mifi = mif_index;
mc.mif6c_flags = mif_flags;
mc.mif6c_pifi = pif_index;
setsockopt(mrouter_s6, IPPROTO_IPV6, MRT6_ADD_MIF, (void *)&mc,
           sizeof(mc));
```

`mif_index` 在每个 vif 中必须唯一。`mif_flags` 包含如下定义的 `MIFF_*` 标志

`#include <netinet6/ip6_mroute.h>`

`pif_index` 是相应本地接口的物理接口索引。

删除多播接口的方式如下：

```sh
/* IPv4 */
vifi_t vifi = vif_index;
setsockopt(mrouter_s4, IPPROTO_IP, MRT_DEL_VIF, (void *)&vifi,
           sizeof(vifi));
```

```sh
/* IPv6 */
mifi_t mifi = mif_index;
setsockopt(mrouter_s6, IPPROTO_IPV6, MRT6_DEL_MIF, (void *)&mifi,
           sizeof(mifi));
```

启用多播转发并添加多播虚拟接口后，内核可能会在先前用 `MRT_INIT` 或 `MRT6_INIT` 打开的多播路由套接字上传递上 call 消息（在本文后文中也称为信号）。IPv4 上 call 具有 `struct igmpmsg` 头部（参见

`#include <netinet/ip_mroute.h>`

其中 `im_mbz` 字段设置为零。注意，此头部遵循 `struct ip` 的结构，协议字段 `ip_p` 设置为零。IPv6 上 call 具有 `struct mrt6msg` 头部（参见

`#include <netinet6/ip6_mroute.h>`

其中 `im6_mbz` 字段设置为零。注意，此头部遵循 `struct ip6_hdr` 的结构，下一个头部字段 `ip6_nxt` 设置为零。

上 call 头部包含 `im_msgtype` 和 `im6_msgtype` 字段，分别用于 IPv4 和 IPv6 的上 call 类型 `IGMPMSG_*` 和 `MRT6MSG_*`。上 call 头部其余字段的值以及上 call 消息的主体取决于特定的上 call 类型。

如果上 call 消息类型为 `IGMPMSG_NOCACHE` 或 `MRT6MSG_NOCACHE`，则表示多播数据包已到达多播路由器，但路由器没有该数据包的转发状态。通常，上 call 会作为信号通知多播路由用户级进程在内核中安装相应的多播转发缓存（MFC）条目。

添加 MFC 条目的方式如下：

```sh
/* IPv4 */
struct mfcctl mc;
memset(&mc, 0, sizeof(mc));
memcpy(&mc.mfcc_origin, &source_addr, sizeof(mc.mfcc_origin));
memcpy(&mc.mfcc_mcastgrp, &group_addr, sizeof(mc.mfcc_mcastgrp));
mc.mfcc_parent = iif_index;
for (i = 0; i < maxvifs; i++)
    mc.mfcc_ttls[i] = oifs_ttl[i];
setsockopt(mrouter_s4, IPPROTO_IP, MRT_ADD_MFC,
           (void *)&mc, sizeof(mc));
```

```sh
/* IPv6 */
struct mf6cctl mc;
memset(&mc, 0, sizeof(mc));
memcpy(&mc.mf6cc_origin, &source_addr, sizeof(mc.mf6cc_origin));
memcpy(&mc.mf6cc_mcastgrp, &group_addr, sizeof(mf6cc_mcastgrp));
mc.mf6cc_parent = iif_index;
for (i = 0; i < maxvifs; i++)
    if (oifs_ttl[i] > 0)
        IF_SET(i, &mc.mf6cc_ifset);
setsockopt(mrouter_s6, IPPROTO_IPV6, MRT6_ADD_MFC,
           (void *)&mc, sizeof(mc));
```

`source_addr` 和 `group_addr` 是多播数据包的源地址和组地址（如上 call 消息中所设）。`iif_index` 是用于接收此特定源和组地址多播数据包的多播接口的虚拟接口索引。`oifs_ttl[]` 数组包含多播数据包在出接口上转发所必须具有的最小 TTL（按接口）。如果 TTL 值为零，则相应接口不包含在出接口集合中。注意，对于 IPv6，只能指定出接口集合。

删除 MFC 条目的方式如下：

```sh
/* IPv4 */
struct mfcctl mc;
memset(&mc, 0, sizeof(mc));
memcpy(&mc.mfcc_origin, &source_addr, sizeof(mc.mfcc_origin));
memcpy(&mc.mfcc_mcastgrp, &group_addr, sizeof(mc.mfcc_mcastgrp));
setsockopt(mrouter_s4, IPPROTO_IP, MRT_DEL_MFC,
           (void *)&mc, sizeof(mc));
```

```sh
/* IPv6 */
struct mf6cctl mc;
memset(&mc, 0, sizeof(mc));
memcpy(&mc.mf6cc_origin, &source_addr, sizeof(mc.mf6cc_origin));
memcpy(&mc.mf6cc_mcastgrp, &group_addr, sizeof(mf6cc_mcastgrp));
setsockopt(mrouter_s6, IPPROTO_IPV6, MRT6_DEL_MFC,
           (void *)&mc, sizeof(mc));
```

可以使用以下方法获取内核中已安装的每个 MFC 条目的各种统计信息（例如，每个源和组地址的转发数据包数）：

```sh
/* IPv4 */
struct sioc_sg_req sgreq;
memset(&sgreq, 0, sizeof(sgreq));
memcpy(&sgreq.src, &source_addr, sizeof(sgreq.src));
memcpy(&sgreq.grp, &group_addr, sizeof(sgreq.grp));
ioctl(mrouter_s4, SIOCGETSGCNT, &sgreq);
```

```sh
/* IPv6 */
struct sioc_sg_req6 sgreq;
memset(&sgreq, 0, sizeof(sgreq));
memcpy(&sgreq.src, &source_addr, sizeof(sgreq.src));
memcpy(&sgreq.grp, &group_addr, sizeof(sgreq.grp));
ioctl(mrouter_s6, SIOCGETSGCNT_IN6, &sgreq);
```

可以使用以下方法获取内核中每个多播虚拟接口的各种统计信息（例如，每个接口的转发数据包数）：

```sh
/* IPv4 */
struct sioc_vif_req vreq;
memset(&vreq, 0, sizeof(vreq));
vreq.vifi = vif_index;
ioctl(mrouter_s4, SIOCGETVIFCNT, &vreq);
```

```sh
/* IPv6 */
struct sioc_mif_req6 mreq;
memset(&mreq, 0, sizeof(mreq));
mreq.mifi = vif_index;
ioctl(mrouter_s6, SIOCGETMIFCNT_IN6, &mreq);
```

### 高级多播 API 编程指南

如果要在内核中添加新功能，同时保持向后兼容性（二进制和 API），并同时允许用户级进程利用新功能（如果内核支持），就会变得困难。

允许我们保持向后兼容性的机制之一是用户级进程与内核之间的一种协商：

- 用户级进程尝试在内核中启用它希望使用的一组新功能（以及相应的 API）。
- 内核返回它知道并愿意启用的（子）功能集。
- 用户级进程仅使用内核已同意的那组功能。

为支持向后兼容性，如果用户级进程不请求任何新功能，内核默认使用基本多播 API（参见 Sx Programming Guide 章节）。目前，高级多播 API 仅存在于 IPv4 中；未来也会有 IPv6 支持。

以下是可扩展 API 解决方案的摘要。注意，除非另有说明，所有新选项和结构都定义在

`#include <netinet/ip_mroute.h>`

和

`#include <netinet6/ip6_mroute.h>`

中。

用户级进程使用新的 Fn getsockopt/Fn setsockopt 选项与内核执行 API 功能协商。此协商必须在多播路由套接字打开后立即进行。所需/允许的功能集存储在一个位集（目前为 `uint32_t`；即最多 32 个新功能）中。新的 Fn getsockopt/Fn setsockopt 选项为 `MRT_API_SUPPORT` 和 `MRT_API_CONFIG`。示例：

```sh
uint32_t v;
getsockopt(sock, IPPROTO_IP, MRT_API_SUPPORT, (void *)&v, sizeof(v));
```

会在 `v` 中设置内核 API 支持的预定义位。`uint32_t` 中八个最低有效位与可在 `mfcc_flags` 中使用的八个可能的 `MRT_MFC_FLAGS_*` 标志相同，作为 `struct mfcctl` 新定义的一部分（关于这些标志见下文），这为其他新功能留下了 24 个标志。Fn getsockopt MRT_API_SUPPORT 返回的值是只读的；换句话说，Fn setsockopt MRT_API_SUPPORT 将失败。

要修改 API 并在内核中设置某些特定功能，则：

```sh
uint32_t v = MRT_MFC_FLAGS_DISABLE_WRONGVIF;
if (setsockopt(sock, IPPROTO_IP, MRT_API_CONFIG, (void *)&v, sizeof(v))
    != 0) {
    return (ERROR);
}
if (v & MRT_MFC_FLAGS_DISABLE_WRONGVIF)
    return (OK);	/* 成功 */
else
    return (ERROR);
```

换句话说，当调用 Fn setsockopt MRT_API_CONFIG 时，其参数指定了要在 API 和内核中启用的所需功能集。`v` 中返回的值是内核中实际启用的（子）功能集。要稍后获取已启用的相同功能集，则：

```sh
getsockopt(sock, IPPROTO_IP, MRT_API_CONFIG, (void *)&v, sizeof(v));
```

已启用的功能集是全局的。换句话说，Fn setsockopt MRT_API_CONFIG 应在 Fn setsockopt MRT_INIT 之后立即调用。

目前，定义了以下新功能集：

```sh
#define	MRT_MFC_FLAGS_DISABLE_WRONGVIF (1 << 0) /* 禁用 WRONGVIF 信号 */
#define	MRT_MFC_FLAGS_BORDER_VIF   (1 << 1)  /* 边界 vif              */
#define MRT_MFC_RP                 (1 << 8)  /* 启用 RP 地址	*/
#define MRT_MFC_BW_UPCALL          (1 << 9)  /* 启用带宽上 call	*/
```

高级多播 API 使用新定义的 `struct mfcctl2`，而非传统的 `struct mfcctl`。原始的 `struct mfcctl` 保持不变。新的 `struct mfcctl2` 为：

```sh
/*
 * MRT_ADD_MFC 和 MRT_DEL_MFC 的新参数结构
 * 覆盖并扩展了旧的 struct mfcctl。
 */
struct mfcctl2 {
        /* mfcctl 字段 */
        struct in_addr  mfcc_origin;       /* mcast 的 ip 源地址       */
        struct in_addr  mfcc_mcastgrp;     /* 关联的多播组            */
        vifi_t          mfcc_parent;       /* 入 vif                  */
        u_char          mfcc_ttls[MAXVIFS];/* vif 上的转发 ttl         */
        /* 扩展字段 */
        uint8_t         mfcc_flags[MAXVIFS];/* MRT_MFC_FLAGS_* 标志    */
        struct in_addr  mfcc_rp;            /* RP 地址                 */
};
```

新字段为 `mfcc_flags[MAXVIFS]` 和 `mfcc_rp`。注意，出于兼容性原因，它们被添加在末尾。

`mfcc_flags[MAXVIFS]` 字段用于按接口按 (S,G) 条目设置各种标志。当前定义的标志为：

```sh
#define	MRT_MFC_FLAGS_DISABLE_WRONGVIF (1 << 0) /* 禁用 WRONGVIF 信号 */
#define	MRT_MFC_FLAGS_BORDER_VIF       (1 << 1) /* 边界 vif          */
```

`MRT_MFC_FLAGS_DISABLE_WRONGVIF` 标志用于在多播数据包到达错误接口时，以 (S,G) 粒度显式禁用 `IGMPMSG_WRONGVIF` 内核信号。通常，此信号用于在 PIM-SM 多播路由中完成最短路径切换，或触发 PIM assert 消息。然而，对于不在出接口集合中且不期望成为入接口的接口，不应传递此信号。因此，如果为某些接口设置了 `MRT_MFC_FLAGS_DISABLE_WRONGVIF` 标志，则在该接口上为该 MFC 条目到达的数据包不会触发 WRONGVIF 信号。如果未设置该标志，则触发信号（默认行为）。

`MRT_MFC_FLAGS_BORDER_VIF` 标志用于指定是否应在 PIM Register 消息中设置 Border 位（在内核内执行 Register 封装的情况下）。如果为特殊的 PIM Register 内核虚拟接口设置了此标志（参见 [pim(4)](pim.4.md)），则发送给 RP 的 Register 消息中将设置 Border 位。

其余六位保留供未来使用。

`mfcc_rp` 字段用于指定多播组 G 的 RP 地址（在 PIM-SM 多播路由的情况下），以便我们执行内核级 PIM Register 封装。仅当 `MRT_MFC_RP` 高级 API 标志/功能已通过 Fn setsockopt MRT_API_CONFIG 成功设置时，才使用 `mfcc_rp` 字段。

如果 `MRT_MFC_RP` 标志已通过 Fn setsockopt MRT_API_CONFIG 成功设置，则内核将尝试自行执行 PIM Register 封装，而不是将多播数据包发送到用户级（通过 `IGMPMSG_WHOLEPKT` 上 call）进行用户级封装。RP 地址取自新 `struct mfcctl2` 中的 `mfcc_rp` 字段。然而，即使 `MRT_MFC_RP` 标志已成功设置，如果 `mfcc_rp` 字段设置为 `INADDR_ANY`，内核仍会向用户级进程传递带有该多播数据包的 `IGMPMSG_WHOLEPKT` 上 call。

此外，如果多播数据包在 PIM Register 封装后太大，无法放入单个 IP 数据包（例如，其大小约为 65500 字节），则数据包将被分片，然后每个分片将单独封装。注意，通常多播数据包只有在源自执行封装的同一主机时才可能那么大；否则，例如通过以太网传输多播数据包时会将其分片成小得多的片段。

通常，多播路由用户级进程需要知道某些数据流的转发带宽。例如，多播路由进程可能希望让空闲的 MFC 条目超时，或者在 PIM-SM 的情况下，如果带宽速率超过阈值，则可以发起 (S,G) 最短路径切换。

测量数据流带宽的原始解决方案是用户级进程定期查询内核关于每个 (S,G) 转发的数据包/字节数，然后根据这些数字估计某个源是否空闲，或者源的传输带宽是否超过阈值。该解决方案远不具备可扩展性，因此需要一种新的带宽监控机制。

以下是带宽监控机制的描述。

- 如果数据流的带宽满足某个预定义过滤器，内核会向安装了该过滤器的多播路由进程在多播路由套接字上传递一个上 call。
- 带宽上 call 过滤器按 (S,G) 安装。每个 (S,G) 可以有多个过滤器。
- 不支持所有可能的比较操作（即 < <= == != > >= ），仅支持 <= 和 >= 操作，因为这使得内核级实现更简单，而且实际上我们只需要这两个。此外，缺失的操作可以通过对这些 <= 和 >= 过滤器的辅助用户级过滤来模拟。例如，要模拟 !=，则需要安装过滤器“bw <= 0xffffffff”，并在收到上 call 后检查“measured_bw != expected_bw”。
- 带宽上 call 机制通过为 `MRT_MFC_BW_UPCALL` 标志调用 Fn setsockopt MRT_API_CONFIG 来启用。
- 带宽上 call 过滤器分别通过新的 Fn setsockopt MRT_ADD_BW_UPCALL 和 Fn setsockopt MRT_DEL_BW_UPCALL 来添加/删除（当然需要带相应的 `struct bw_upcall` 参数）。

从应用程序的角度来看，开发者需要了解以下内容：

```sh
/*
 * 用于安装或传递上 call 的结构，当
 * 测量的带宽高于或低于阈值时。
 *
 * 用户程序（例如守护进程）可能需要知道何时
 * 某些数据流使用的带宽高于或低于某个阈值。
 * 此接口允许用户态指定阈值（以
 * 字节和/或数据包为单位）和测量间隔。流是
 * 具有相同源和目的 IP 地址的所有数据包。
 * 目前此代码仅用于多播目的地，
 * 但没有任何东西阻止其用于单播。
 *
 * 测量间隔不能短于某个 Tmin（目前为 3 秒）。
 * 阈值以每间隔的数据包和/或字节为单位设置。
 *
 * 测量工作方式如下：
 *
 * 对于 >= 测量：
 * 第一个数据包标记测量间隔的开始。
 * 在一个间隔内，我们计数数据包和字节，当
 * 超过阈值时，我们传递一个上 call，然后完成。
 * 间隔结束后的第一个数据包重置
 * 计数并重新开始测量。
 *
 * 对于 <= 测量：
 * 我们启动一个定时器在间隔结束时触发，
 * 然后对于每个传入数据包，我们计数数据包和字节。
 * 当定时器触发时，我们将值与阈值比较，
 * 如果低于则安排一个上 call，并重新开始测量
 * （重新安排定时器并清零计数器）。
 */
struct bw_data {
        struct timeval  b_time;
        uint64_t        b_packets;
        uint64_t        b_bytes;
};
struct bw_upcall {
        struct in_addr  bu_src;         /* 源地址            */
        struct in_addr  bu_dst;         /* 目的地址           */
        uint32_t        bu_flags;       /* 杂项标志（见下文）    */
#define BW_UPCALL_UNIT_PACKETS (1 << 0) /* 阈值（以数据包为单位）    */
#define BW_UPCALL_UNIT_BYTES   (1 << 1) /* 阈值（以字节为单位）      */
#define BW_UPCALL_GEQ          (1 << 2) /* 如果 bw >= 阈值则上 call */
#define BW_UPCALL_LEQ          (1 << 3) /* 如果 bw <= 阈值则上 call */
#define BW_UPCALL_DELETE_ALL   (1 << 4) /* 删除 s,d 的所有上 call */
        struct bw_data  bu_threshold;   /* 带宽阈值          */
        struct bw_data  bu_measured;    /* 测量的带宽           */
};
/* 一起传递的最大上 call 数 */
#define BW_UPCALLS_MAX				128
/* 带宽测量的最小阈值时间间隔 */
#define BW_UPCALL_THRESHOLD_INTERVAL_MIN_SEC	3
#define BW_UPCALL_THRESHOLD_INTERVAL_MIN_USEC	0
```

`bw_upcall` 结构用作 Fn setsockopt MRT_ADD_BW_UPCALL 和 Fn setsockopt MRT_DEL_BW_UPCALL 的参数。每次 Fn setsockopt MRT_ADD_BW_UPCALL 会在内核中为 `bw_upcall` 参数中的源和目的地址安装一个过滤器，该过滤器将根据以下伪算法触发上 call：

```sh
 if (bw_upcall_oper IS ">=") {
    if (((bw_upcall_unit & PACKETS == PACKETS) &&
         (measured_packets >= threshold_packets)) ||
        ((bw_upcall_unit & BYTES == BYTES) &&
         (measured_bytes >= threshold_bytes)))
       SEND_UPCALL("测量的带宽 >= 阈值");
  }
  if (bw_upcall_oper IS "<=" && measured_interval >= threshold_interval) {
    if (((bw_upcall_unit & PACKETS == PACKETS) &&
         (measured_packets <= threshold_packets)) ||
        ((bw_upcall_unit & BYTES == BYTES) &&
         (measured_bytes <= threshold_bytes)))
       SEND_UPCALL("测量的带宽 <= 阈值");
  }
```

在同一个 `bw_upcall` 中，单位可以同时以 BYTES 和 PACKETS 指定。然而，GEQ 和 LEQ 标志是互斥的。

基本上，如果测量的带宽 >= 或 <= 阈值带宽（在指定的测量间隔内），则传递上 call。出于实际原因，测量间隔的最小值为 3 秒。如果允许更小的值，则带宽估计可能不太准确，或者生成的上 call 的潜在非常高的频率可能引入过多开销。对于 >= 操作，答案可能在 `threshold_interval` 结束之前已知，因此上 call 可能更早传递。然而，对于 <= 操作，我们必须等待阈值间隔到期才能知道答案。

使用示例：

```sh
struct bw_upcall bw_upcall;
/* 适当地分配所有 bw_upcall 字段 */
memset(&bw_upcall, 0, sizeof(bw_upcall));
memcpy(&bw_upcall.bu_src, &source, sizeof(bw_upcall.bu_src));
memcpy(&bw_upcall.bu_dst, &group, sizeof(bw_upcall.bu_dst));
bw_upcall.bu_threshold.b_data = threshold_interval;
bw_upcall.bu_threshold.b_packets = threshold_packets;
bw_upcall.bu_threshold.b_bytes = threshold_bytes;
if (is_threshold_in_packets)
    bw_upcall.bu_flags |= BW_UPCALL_UNIT_PACKETS;
if (is_threshold_in_bytes)
    bw_upcall.bu_flags |= BW_UPCALL_UNIT_BYTES;
do {
    if (is_geq_upcall) {
        bw_upcall.bu_flags |= BW_UPCALL_GEQ;
        break;
    }
    if (is_leq_upcall) {
        bw_upcall.bu_flags |= BW_UPCALL_LEQ;
        break;
    }
    return (ERROR);
} while (0);
setsockopt(mrouter_s4, IPPROTO_IP, MRT_ADD_BW_UPCALL,
          (void *)&bw_upcall, sizeof(bw_upcall));
```

要删除单个过滤器，则使用 `MRT_DEL_BW_UPCALL`，并且 bw_upcall 的字段必须与调用 `MRT_ADD_BW_UPCALL` 时完全相同。

要删除给定 (S,G) 的所有带宽过滤器，则只需设置 `struct bw_upcall` 中的 `bu_src` 和 `bu_dst` 字段，然后只需在 `bw_upcall.bu_flags` 字段中设置 `BW_UPCALL_DELETE_ALL` 标志。

带宽上 call 通过将其聚合在新的上 call 消息中来接收：

```sh
#define IGMPMSG_BW_UPCALL  4  /* 带宽监控上 call */
```

此消息是一个 `struct bw_upcall` 元素数组（最多 `BW_UPCALLS_MAX` = 128 个）。当有 128 个待处理的上 call，或自上次上 call 以来已过 1 秒（以先到者为准）时，传递上 call。在 `struct upcall` 元素中，`bu_measured` 字段被填充以指示特定的测量值。然而，由于特定间隔的测量方式，用户应谨慎使用 `bu_measured.b_time`。例如，如果过滤器被安装为在数据包数 >= 1 时触发上 call，则 `bu_measured` 在第一次之后的上 call 中可能值为零，因为 >= 过滤器的测量间隔由转发的数据包“计时”。因此，此上 call 机制不应用于测量转发数据的确切带宽值。要测量确切带宽，用户需要使用 Fn ioctl SIOCGETSGCNT 机制获取转发数据包统计信息（参见 Sx Programming Guide 章节）。

注意，过滤器的上 call 会一直传递，直到特定过滤器被删除，但频率不高于每个 `bu_threshold.b_time` 一次。例如，如果过滤器指定为在 bw >= 1 个数据包时传递信号，则第一个数据包将触发信号，但下一个上 call 不会早于上一次上 call 之后的 `bu_threshold.b_time` 触发。

## 参见

getsockopt(2), recvfrom(2), recvmsg(2), setsockopt(2), socket(2), sourcefilter(3), [altq(4)](altq.4.md), [dummynet(4)](dummynet.4.md), [gif(4)](gif.4.md), [gre(4)](gre.4.md), [icmp6(4)](icmp6.4.md), [igmp(4)](igmp.4.md), [inet(4)](inet.4.md), [inet6(4)](inet6.4.md), [intro(4)](intro.4.md), [ip(4)](ip.4.md), [ip6(4)](ip6.4.md), [mld(4)](mld.4.md), [pim(4)](pim.4.md)

## 历史

距离向量多播路由协议（DVMRP）是最早开发的多播路由协议。后来，还开发了其他协议，如 OSPF 的多播扩展（MOSPF）和核心基于树（CBT）。自治系统边界处的路由器现在可以通过边界网关协议（BGP）与对等方交换多播路由。许多其他路由协议能够重新分发多播路由以用于 `PIM-SM` 和 `PIM-DM`。

## 作者

原始多播代码由 David Waitzman (BBN Labs) 编写，后来由以下人员修改：Steve Deering (Stanford)、Mark J. Steiglitz (Stanford)、Van Jacobson (LBL)、Ajit Thyagarajan (PARC)、Bill Fenner (PARC)。IPv6 多播支持由 KAME 项目（`https://www.kame.net`）实现，并基于 IPv4 多播代码。高级多播 API 和多播带宽监控由 Pavlin Radoslavov (ICSI) 与 Chris Brown (NextHop) 合作实现。IGMPv3 和 MLDv2 多播支持由 Bruce Simpson 实现。

本手册页由 Pavlin Radoslavov (ICSI) 编写。
