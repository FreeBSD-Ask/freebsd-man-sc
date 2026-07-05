# icmp6.4

`icmp6` — IPv6 的 Internet 控制报文协议

## 名称

`icmp6`

## 概要

`#include <sys/socket.h>`

`#include <netinet/in.h>`

`#include <netinet/icmp6.h>`

`Ft int Fn socket AF_INET6 SOCK_RAW IPPROTO_ICMPV6`

## 描述

ICMPv6 是 IPv6 及 IPv6 协议族（参见 [ip6(4)](ip6.4.md) 和 [inet6(4)](inet6.4.md)）使用的差错和控制报文协议。可通过“raw socket”访问它，用于网络监控和诊断功能。

创建 ICMPv6 套接字时，socket(2) 调用的 `proto` 参数可从 getprotobyname(3) 获取。ICMPv6 套接字是无连接的，通常与 sendto(2) 和 recvfrom(2) 调用一起使用，不过也可以使用 connect(2) 调用固定后续数据包的目的地（此时可使用 read(2) 或 recv(2) 以及 write(2) 或 send(2) 系统调用）。

发出的数据包会自动在前面加上 IPv6 头（基于目的地址）。套接字上接收到的数据包会去除 IPv6 头和任何扩展头。

### 类型

ICMPv6 报文根据 ICMPv6 头中的 type 和 code 字段进行分类。类型和代码的缩写可用于 [pf.conf(5)](../man5/pf.conf.5.md) 中的规则。已定义以下类型：

| **Num** | **Abbrev.** | **Description** |
| --- | --- | --- |
| 1 | unreach | Destination unreachable |
| 2 | toobig | Packet too big |
| 3 | timex | Time exceeded |
| 4 | paramprob | Invalid IPv6 header |
| 128 | echoreq | Echo service request |
| 129 | echorep | Echo service reply |
| 130 | groupqry | Group membership query |
| 130 | listqry | Multicast listener query |
| 131 | grouprep | Group membership report |
| 131 | listenrep | Multicast listener report |
| 132 | groupterm | Group membership termination |
| 132 | listendone | Multicast listener done |
| 133 | routersol | Router solicitation |
| 134 | routeradv | Router advertisement |
| 135 | neighbrsol | Neighbor solicitation |
| 136 | neighbradv | Neighbor advertisement |
| 137 | redir | Shorter route exists |
| 138 | routrrenum | Route renumbering |
| 139 | fqdnreq | FQDN query |
| 139 | niqry | Node information query |
| 139 | wrureq | Who-are-you request |
| 140 | fqdnrep | FQDN reply |
| 140 | nirep | Node information reply |
| 140 | wrurep | Who-are-you reply |
| 200 | mtraceresp | mtrace response |
| 201 | mtrace | mtrace messages |

已定义以下代码：

**Description**

| **Num** | **Abbrev.** | **Type** |  |
| --- | --- | --- | --- |
| 0 | noroute-unr | unreach | No route to destination |
| 1 | admin-unr | unreach | Administratively prohibited |
| 2 | beyond-unr | unreach | Beyond scope of source address |
| 2 | notnbr-unr | unreach | Not a neighbor (obsolete) |
| 3 | addr-unr | unreach | Address unreachable |
| 4 | port-unr | unreach | Port unreachable |
| 0 | transit | timex | Time exceeded in transit |
| 1 | reassemb | timex | Time exceeded in reassembly |
| 0 | badhead | paramprob | Erroneous header field |
| 1 | nxthdr | paramprob | Unrecognized next header |
| 2 |  | redir | Unrecognized option |
| 0 | redironlink | redir | Redirection to on-link node |
| 1 | redirrouter | redir | Redirection to better router |

### 头部

所有 ICMPv6 报文均以 ICMPv6 头为前缀。此头对应 `icmp6_hdr` 结构，定义如下：

```sh
struct icmp6_hdr {
	uint8_t  icmp6_type;	/* type field */
	uint8_t  icmp6_code;	/* code field */
	uint16_t icmp6_cksum;	/* checksum field */
	union {
		uint32_t icmp6_un_data32[1]; /* type-specific */
		uint16_t icmp6_un_data16[2]; /* type-specific */
		uint8_t  icmp6_un_data8[4];  /* type-specific */
	} icmp6_dataun;
} __packed;
#define icmp6_data32	icmp6_dataun.icmp6_un_data32
#define icmp6_data16	icmp6_dataun.icmp6_un_data16
#define icmp6_data8	icmp6_dataun.icmp6_un_data8
#define icmp6_pptr	icmp6_data32[0]	/* parameter prob */
#define icmp6_mtu	icmp6_data32[0]	/* packet too big */
#define icmp6_id	icmp6_data16[0]	/* echo request/reply */
#define icmp6_seq	icmp6_data16[1]	/* echo request/reply */
#define icmp6_maxdelay	icmp6_data16[0]	/* mcast group membership*/
```

`icmp6_type` 描述报文的类型。合适的值定义在 <`netinet/icmp6.h`> 中。`icmp6_code` 描述报文的子类型，并取决于 `icmp6_type`。`icmp6_cksum` 包含报文的校验和，由内核在发出报文时填入。其他字段用于类型特定的目的。

### 过滤器

由于 ICMPv6 相较 ICMPv4 具有额外的功能，在 ICMPv6 套接字上可能潜在接收到更多报文。因此可使用输入过滤器将输入限制为入站 ICMPv6 报文的一个子集，使得 recv(2) 系列调用仅向应用程序返回感兴趣的报文。

`icmp6_filter` 结构可用于根据 ICMPv6 类型精炼输入报文集合。默认情况下，新创建的 raw ICMPv6 套接字上允许所有消息类型。可使用以下宏精炼输入集合：

**Ft** void Fn ICMP6_FILTER_SETPASSALL struct icmp6_filter *filterp 允许所有入站报文。`filterp` 被修改为允许所有消息类型。

**Ft** void Fn ICMP6_FILTER_SETBLOCKALL struct icmp6_filter *filterp 忽略所有入站报文。`filterp` 被修改为忽略所有消息类型。

**Xo** Ft void Fn ICMP6_FILTER_SETPASS int type struct icmp6_filter *filterp Xc 允许指定 `type` 的 ICMPv6 报文。`filterp` 被修改为允许此类报文。

**Xo** Ft void Fn ICMP6_FILTER_SETBLOCK int type struct icmp6_filter *filterp Xc 忽略指定 `type` 的 ICMPv6 报文。`filterp` 被修改为忽略此类报文。

**Xo** Ft int Fn ICMP6_FILTER_WILLPASS int type const struct icmp6_filter *filterp Xc 判断给定过滤器是否会允许指定类型的 ICMPv6 报文。

**Xo** Ft int Fn ICMP6_FILTER_WILLBLOCK int type const struct icmp6_filter *filterp Xc 判断给定过滤器是否会忽略指定类型的 ICMPv6 报文。

可使用 getsockopt(2) 和 setsockopt(2) 调用在 ICMPv6 套接字上获取并安装过滤器，选项级别为 `IPPROTO_ICMPV6`，名称为 `ICMP6_FILTER`，选项值为指向 `icmp6_filter` 结构的指针。

## 参见

getsockopt(2), recv(2), send(2), setsockopt(2), socket(2), getprotobyname(3), [dtrace_mib(4)](dtrace_mib.4.md), [inet6(4)](inet6.4.md), [ip6(4)](ip6.4.md), [netintro(4)](netintro.4.md)

> W. Stevens, M. Thomas, "Advanced Sockets API for IPv6", RFC 2292, February 1998.

"Protocol Version 6 (IPv6) Specification"

> A. Conta, S. Deering, "Internet Control Message Protocol (ICMPv6) for the Internet", RFC 2463, December 1998.

> W. Stevens, M. Thomas, E. Nordmark, T. Jinmei, "Advanced Sockets Application Program Interface (API) for IPv6", May 2003.

"Protocol Version 6 (IPv6) Specification"

> A. Conta, S. Deering, M. Gupta, "Internet Control Message Protocol (ICMPv6) for the Internet", March 2006.
