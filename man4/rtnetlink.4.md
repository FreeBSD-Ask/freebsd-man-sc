# rtnetlink(4)

`RTNetlink` — 网络配置专用的 Netlink 协议族

## 名称

`RTNetlink`

## 概要

`#include <netlink/netlink.h>`

`#include <netlink/netlink_route.h>`

`Ft int Fn socket AF_NETLINK SOCK_RAW NETLINK_ROUTE`

## 描述

`NETLINK_ROUTE` 协议族旨在成为所有网络相关任务的主要配置机制。目前它支持配置接口、接口地址、路由、下一跳（nexthop）以及 arp/ndp 邻居。

## 路由

所有路由配置消息共享通用头部：

```sh
struct rtmsg {
	unsigned char	rtm_family;	/* 地址族 */
	unsigned char	rtm_dst_len;	/* 前缀长度 */
	unsigned char	rtm_src_len;	/* 已弃用，设置为 0 */
	unsigned char	rtm_tos;	/* 服务类型（未使用） */
	unsigned char	rtm_table;	/* 已弃用，设置为 0 */
	unsigned char	rtm_protocol;	/* 路由协议 ID（RTPROT_） */
	unsigned char	rtm_scope;	/* 路由距离（RT_SCOPE_） */
	unsigned char	rtm_type;	/* 路由类型（RTN_） */
	unsigned 	rtm_flags;	/* 路由标志（不支持） */
};
```

`rtm_family` 指定要操作的路由族。目前仅支持 `AF_INET6` 和 `AF_INET`。路由前缀长度存储在 `rtm_dst_len` 中。调用方应在 `rtm_protocol` 中设置发起者身份（`RTPROT_` 值之一）。这对于用户和应用本身都很有用，可便于轻松识别自发起的路由。路由作用范围必须通过 `rtm_scope` 字段设置。支持的值有：

RT_SCOPE_UNIVERSE	全局作用范围
RT_SCOPE_LINK		链路作用范围

必须设置路由类型。已定义的值有：

RTN_UNICAST	单播路由
RTN_MULTICAST	多播路由
RTN_BLACKHOLE	丢弃发往目的地的流量
RTN_PROHIBIT	丢弃流量并发送拒绝

支持以下消息：

### RTM_NEWROUTE

添加新路由。支持所有 NL 标志。扩展多路径路由需要 NLM_F_APPEND 标志。

### RTM_DELROUTE

尝试删除路由。该路由通过 `RTA_DST` TLV 和 `rtm_dst_len` 的组合来指定。

### RTM_GETROUTE

获取单个路由或当前 VNET 中的所有路由，取决于 `NLM_F_DUMP` 标志。每条路由以 `RTM_NEWROUTE` 消息的形式报告。内核识别以下过滤器：

rtm_family	必需的族或 AF_UNSPEC
RTA_TABLE	fib 编号或 RT_TABLE_UNSPEC（返回所有 fib）

### TLV

```sh
struct rtnexthop {
	unsigned short		rtnh_len;
	unsigned char		rtnh_flags;
	unsigned char		rtnh_hops;	/* 下一跳权重 */
	int			rtnh_ifindex;
};
```

RTA_GATEWAY	网关的 IPv4/IPv6 下一跳地址
RTA_VIA		IPv4 路由的 IPv6 下一跳地址
RTA_KNH_ID	下一跳的内核专用索引

**`RTA_DST`** （二进制）IPv4/IPv6 地址，取决于 `rtm_family`。

**`RTA_OIF`** （uint32_t）发送接口索引。

**`RTA_GATEWAY`** （二进制）IPv4/IPv6 网关地址，取决于 `rtm_family`。

**`RTA_METRICS`** （嵌套）容器属性，列出路由属性。唯一支持的子属性为 `RTAX_MTU`，以 uint32_t 存储 path MTU。

**`RTA_MULTIPATH`** 此属性包含多路径路由的下一跳及其权重。这些下一跳表示为一系列 `rtnexthop` 结构，每个结构后跟 `RTA_GATEWAY` 或 `RTA_VIA` 属性。`rtnh_len` 字段指定下一跳信息的总长度，包括 `struct rtnexthop` 和随后的 TLV。`rtnh_hops` 字段存储相对下一跳权重，用于组成员间的负载均衡。`rtnh_ifindex` 字段包含发送接口的索引。该结构后可跟以下 TLV：

**`RTA_KNH_ID`** （uint32_t）（FreeBSD 专用）下一跳的内核自动分配索引。

**`RTA_RTFLAGS`** （uint32_t）（FreeBSD 专用）rtsock 路由标志。

**`RTA_TABLE`** （uint32_t）路由的 Fib 编号。默认路由表为 `RT_TABLE_MAIN`。要显式指定"所有表"，需将值设置为 `RT_TABLE_UNSPEC`。

**`RTA_PRIORITY`** （uint32_t）下一跳的度量。

**`RTA_EXPIRES`** （uint32_t）路径过期前的秒数。

**`RTA_NH_ID`** （uint32_t）用户空间使用的下一跳或下一跳组索引。

### 组

定义了以下组：

RTNLGRP_IPV4_ROUTE	通知 IPv4 路由的到达/移除/更改
RTNLGRP_IPV6_ROUTE	通知 IPv6 路由的到达/移除/更改

## 下一跳

所有下一跳/下一跳组配置消息共享通用头部：

```sh
struct nhmsg {
        unsigned char	nh_family;	/* 传输族 */
	unsigned char	nh_scope;	/* 接收时忽略，由内核填写 */
	unsigned char	nh_protocol;	/* 安装 nh 的路由协议 */
	unsigned char	resvd;
	unsigned int	nh_flags;	/* 来自 route.h 的 RTNH_F_* 标志 */
};
```

`nh_family` 指定网关地址族。对于带 IPv6 下一跳的 IPv4 路由，它可以不同于路由地址族。`nh_protocol` 类似于 `rtm_protocol` 字段，表示发起应用的身份。

支持以下消息：

### RTM_NEWNEXTHOP

创建新的下一跳或下一跳组。

### RTM_DELNEXTHOP

删除下一跳或下一跳组。所需对象由 `RTA_NH_ID` 属性指定。

### RTM_GETNEXTHOP

获取单个下一跳或所有下一跳/下一跳组，取决于 `NLM_F_DUMP` 标志。内核识别以下过滤器：

RTA_NH_ID	下一跳或下一跳组 ID
NHA_GROUPS	仅匹配下一跳组

### TLV

```sh
struct nexthop_grp {
	uint32_t	id;		/* 下一跳用户空间索引 */
	uint8_t		weight;         /* 此下一跳的权重 */
	uint8_t		resvd1;
	uint16_t	resvd2;
};
```

NEXTHOP_GRP_TYPE_MPATH	默认多路径组

**`RTA_NH_ID`** （uint32_t）用于标识特定下一跳或下一跳组的下一跳索引。应在创建下一跳时由用户空间提供。

**`NHA_GROUP`** 此属性标识下一跳组，包含其所有下一跳及其相对权重。该属性由一系列 `nexthop_grp` 结构组成：

**`NHA_GROUP_TYPE`** （uint16_t）下一跳组类型，设置为以下类型之一：

**`NHA_BLACKHOLE`** （标志）将下一跳标记为黑洞。

**`NHA_OIF`** （uint32_t）下一跳的发送接口索引。

**`NHA_GATEWAY`** （二进制）IPv4/IPv6 网关地址

**`NHA_GROUPS`** （标志）在 dump 期间匹配下一跳组。

### 组

定义了以下组：

RTNLGRP_NEXTHOP		通知下一跳/组的到达/移除/更改

## 接口

所有接口配置消息共享通用头部：

```sh
struct ifinfomsg {
	unsigned char	ifi_family;	/* 未使用，设置为 0 */
	unsigned char	__ifi_pad;
	unsigned short	ifi_type;	/* IFT_* */
	int		ifi_index;	/* 接口索引 */
	unsigned	ifi_flags;	/* IFF_* 标志 */
	unsigned	ifi_change;	/* IFF_* 变更掩码 */
};
```

**注意：** 在 FreeBSD 上，`ifi_type` 字段使用来自以下文件的 `IFT_*` 常量

`#include <net/if_types.h>`

而非 Linux 上的 `ARPHRD_*`。

### RTM_NEWLINK

创建新接口。唯一强制的 TLV 是 `IFLA_IFNAME`。以下属性在嵌套的 `NLMSGERR_ATTR_COOKIE` 中返回：

IFLA_NEW_IFINDEX	（uint32）已创建接口的索引
IFLA_IFNAME		（字符串）已创建接口的名称

### RTM_DELLINK

删除由 `IFLA_IFNAME` 指定的接口。

### RTM_GETLINK

获取单个接口或当前 VNET 中的所有接口，取决于 `NLM_F_DUMP` 标志。每个接口以 `RTM_NEWLINK` 消息的形式报告。内核识别以下过滤器：

ifi_index	接口索引
IFLA_IFNAME	接口名
IFLA_ALT_IFNAME	接口名

### TLV

IFLA_INFO_KIND		（字符串）接口类型（"vlan"）
IFLA_INFO_DATA		（嵌套）自定义属性

IFLA_VLAN_ID		（uint16_t）802.1Q vlan ID
IFLA_VLAN_PROTOCOL	（uint16_t）协议：ETHERTYPE_VLAN 或 ETHERTYPE_QINQ

**`vlan`**

IF_OPER_UNKNOWN	无法确定状态
IF_OPER_NOTPRESENT	某些（硬件）组件不存在
IF_OPER_DOWN		下线
IF_OPER_LOWERLAYERDOWN	某些下层接口下线
IF_OPER_TESTING		处于某种测试模式
IF_OPER_DORMANT		"上线"但等待某些条件（802.1X）
IF_OPER_UP		准备好传递数据包

```sh
struct rtnl_link_stats64 {
	uint64_t rx_packets;	/* 总 RX 数据包（IFCOUNTER_IPACKETS） */
	uint64_t tx_packets;	/* 总 TX 数据包（IFCOUNTER_OPACKETS） */
	uint64_t rx_bytes;	/* 总 RX 字节（IFCOUNTER_IBYTES） */
	uint64_t tx_bytes;	/* 总 TX 字节（IFCOUNTER_OBYTES） */
	uint64_t rx_errors;	/* RX 错误（IFCOUNTER_IERRORS） */
	uint64_t tx_errors;	/* RX 错误（IFCOUNTER_OERRORS） */
	uint64_t rx_dropped;	/* RX 丢弃（环中无空间/无缓冲区）（IFCOUNTER_IQDROPS） */
	uint64_t tx_dropped;	/* TX 丢弃（IFCOUNTER_OQDROPS） */
	uint64_t multicast;	/* RX 多播数据包（IFCOUNTER_IMCASTS） */
	uint64_t collisions;	/* 不支持 */
	uint64_t rx_length_errors;	/* 不支持 */
	uint64_t rx_over_errors;	/* 不支持 */
	uint64_t rx_crc_errors;		/* 不支持 */
	uint64_t rx_frame_errors;	/* 不支持 */
	uint64_t rx_fifo_errors;	/* 不支持 */
	uint64_t rx_missed_errors;	/* 不支持 */
	uint64_t tx_aborted_errors;	/* 不支持 */
	uint64_t tx_carrier_errors;	/* 不支持 */
	uint64_t tx_fifo_errors;	/* 不支持 */
	uint64_t tx_heartbeat_errors;	/* 不支持 */
	uint64_t tx_window_errors;	/* 不支持 */
	uint64_t rx_compressed;		/* 不支持 */
	uint64_t tx_compressed;		/* 不支持 */
	uint64_t rx_nohandler;	/* 因无协议处理程序而丢弃（IFCOUNTER_NOPROTO） */
};
```

**`IFLA_ADDRESS`** （二进制）链路层接口地址（MAC）。

**`IFLA_BROADCAST`** （二进制）（只读）链路层广播地址。

**`IFLA_IFNAME`** （字符串）新接口名。

**`IFLA_IFALIAS`** （字符串）接口描述。

**`IFLA_LINK`** （uint32_t）（只读）接口索引。

**`IFLA_MASTER`** （uint32_t）父接口索引。

**`IFLA_LINKINFO`** （嵌套）接口类型特定属性：支持以下类型和属性：

**`IFLA_OPERSTATE`** （uint8_t）依据 RFC 2863 的接口操作状态。可为以下之一：

**`IFLA_STATS64`** （只读）由以下 64 位计数器结构组成：

### 组

定义了以下组：

RTNLGRP_LINK		通知接口的到达/移除/更改

## 接口地址

所有接口地址配置消息共享通用头部：

```sh
struct ifaddrmsg {
	uint8_t		ifa_family;	/* 地址族 */
	uint8_t		ifa_prefixlen;	/* 前缀长度 */
	uint8_t		ifa_flags;	/* 地址特定标志 */
	uint8_t		ifa_scope;	/* 地址作用范围 */
	uint32_t	ifa_index;	/* 链路 ifindex */
};
```

`ifa_family` 指定接口地址的地址族。`ifa_prefixlen` 指定前缀长度（如对该地址族适用）。`ifa_index` 指定目标接口的接口索引。

### RTM_NEWADDR

不支持

### RTM_DELADDR

不支持

### RTM_GETADDR

获取当前 VNET 中匹配条件的接口地址。每个地址以 `RTM_NEWADDR` 消息的形式报告。内核识别以下过滤器：

ifa_family	必需的族或 AF_UNSPEC
ifa_index	匹配的接口索引或 0

### TLV

**`IFA_ADDRESS`** （二进制）掩码后的接口地址，或 p2p 接口的目的地址。

**`IFA_LOCAL`** （二进制）本地接口地址。为 IPv4 和 p2p 地址设置。

**`IFA_LABEL`** （字符串）接口名。

**`IFA_BROADCAST`** （二进制）广播接口地址。

### 组

定义了以下组：

RTNLGRP_IPV4_IFADDR	通知 IPv4 ifaddr 的到达/移除/更改
RTNLGRP_IPV6_IFADDR	通知 IPv6 ifaddr 的到达/移除/更改

## 邻居

所有邻居配置消息共享通用头部：

```sh
struct ndmsg {
	uint8_t		ndm_family;
	uint8_t		ndm_pad1;
	uint16_t	ndm_pad2;
	int32_t		ndm_ifindex;
	uint16_t	ndm_state;
	uint8_t		ndm_flags;
	uint8_t		ndm_type;
};
```

`ndm_family` 字段指定邻居的地址族（IPv4 或 IPv6）。`ndm_ifindex` 指定要操作的接口。`ndm_state` 根据邻居模型表示条目状态。状态可为以下之一：

NUD_INCOMPLETE		无 lladdr，地址解析进行中
NUD_REACHABLE		可达且最近解析过
NUD_STALE		有 lladdr 但已陈旧
NUD_DELAY		有 lladdr，已陈旧，探测已延迟
NUD_PROBE		有 lladdr，已陈旧，已发送探测
NUD_FAILED		未使用

`ndm_flags` 字段存储特定于此条目的选项。可用标志：

NTF_SELF		本地站（LLE_IFADDR）
NTF_PROXY		代理条目（LLE_PUB）
NTF_STICKY		永久条目（LLE_STATIC）
NTF_ROUTER		目的地表明自身为路由器

### RTM_NEWNEIGH

创建新邻居条目。必需选项为 `NDA_DST`、`NDA_LLADDR` 和 `NDA_IFINDEX`。

### RTM_DELNEIGH

删除邻居条目。该条目由 `NDA_DST` 和 `NDA_IFINDEX` 的组合指定。

### RTM_GETNEIGH

获取单个邻居或当前 VNET 中的所有邻居，取决于 `NLM_F_DUMP` 标志。每个条目以 `RTM_NEWNEIGH` 消息的形式报告。内核识别以下过滤器：

ndm_family	必需的族或 AF_UNSPEC
ndm_ifindex	目标 ifindex
NDA_IFINDEX	目标 ifindex

### TLV

**`NDA_DST`** （二进制）邻居 IPv4/IPv6 地址。

**`NDA_LLADDR`** （二进制）邻居链路层地址。

**`NDA_IFINDEX`** （uint32_t）接口索引。

**`NDA_FLAGS_EXT`** （uint32_t）`ndm_flags` 的扩展版本。

### 组

定义了以下组：

RTNLGRP_NEIGH	通知 ARP/NDP 邻居的到达/移除/更改

## 参见

[snl(3)](../man3/snl.3.md), [netlink(4)](netlink.4.md), [route(4)](route.4.md)

## 历史

`NETLINK_ROUTE` 协议族出现在 FreeBSD 13.2 中。

## 作者

netlink 由 Alexander Chernikov <melifaro@FreeBSD.org> 实现。它源自 Ng Peng Nam Sean 在 2021 年 Google Summer of Code 中的项目。
