# inet6(4)

`inet6` — Internet 协议版本 6 协议族

## 名称

`inet6`

## 概要

`#include <sys/types.h>`

`#include <netinet/in.h>`

## 描述

`inet6` 协议族是 [inet(4)](inet.4.md) 协议族的更新版本。[inet(4)](inet.4.md) 实现 Internet 协议版本 4，而 `inet6` 实现 Internet 协议版本 6。

`inet6` 是一组叠加在 *Internet Protocol version 6*（IPv6）传输层之上并使用 IPv6 地址格式的协议集合。`inet6` 协议族为 `SOCK_STREAM`、`SOCK_DGRAM` 和 `SOCK_RAW` 套接字类型提供协议支持；`SOCK_RAW` 接口提供对 IPv6 协议的访问。

## 寻址

IPv6 地址为 16 字节数据，按网络标准字节序存储。头文件

`#include <netinet/in.h>`

将该地址定义为判别联合。

绑定到 `inet6` 协议族的套接字使用以下寻址结构：

```sh
struct sockaddr_in6 {
	uint8_t		sin6_len;
	sa_family_t	sin6_family;
	in_port_t	sin6_port;
	uint32_t	sin6_flowinfo;
	struct in6_addr	sin6_addr;
	uint32_t	sin6_scope_id;
};
```

可使用本地地址“`::`”（等于 IPv6 地址 `0:0:0:0:0:0:0:0`）创建套接字，以对进入的消息实现“通配”匹配。

IPv6 规范定义了带作用域的地址，例如链路本地地址或站点本地地址。如果在不指定作用域标识符的情况下指定带作用域的地址，则该地址对内核而言是歧义的。要从用户空间正确操作带作用域的地址，程序必须使用 RFC2292 中定义的高级 API。在 [ip6(4)](ip6.4.md) 中有该高级 API 的简要说明。如果在未显式指定作用域的情况下指定带作用域的地址，内核可能会报错。注意，无论从规范还是实现角度看，带作用域的地址目前都不适合日常使用。

KAME 实现支持对链路本地地址的扩展数字 IPv6 地址表示法，例如“`fe80::1%de0`”表示“`de0` 接口上的 `fe80::1`”。getaddrinfo(3) 和 getnameinfo(3) 支持此表示法。某些普通用户空间程序，如 [telnet(1)](../man1/telnet.1.md) 或 [ftp(1)](../man1/ftp.1.md)，能够使用此表示法。对于 [ping(8)](../man8/ping.8.md) 等特殊程序，可通过额外的命令行选项指定外出接口，以消除带作用域地址的歧义。

带作用域的地址在内核中作特殊处理。在路由表或接口结构等内核结构中，带作用域的地址会将接口索引嵌入到地址中。因此，某些内核结构中的地址与链路上的地址不同。嵌入的索引会通过 `PF_ROUTE` 套接字、通过 kvm(3) 访问内核内存以及某些其他场合可见。然而，用户**不应**使用嵌入形式。详情请参阅 KAME 套件中提供的 `IMPLEMENTATION` 文档。

## 协议

`inet6` 协议族由 IPv6 网络协议、Internet 控制报文协议版本 6（ICMPv6）、传输控制协议（TCP）和用户数据报协议（UDP）组成。TCP 用于支持 `SOCK_STREAM` 抽象，UDP 用于支持 `SOCK_DGRAM` 抽象。注意，TCP 和 UDP 在 [inet(4)](inet.4.md) 和 `inet6` 中通用。可通过创建 `SOCK_RAW` 类型的 Internet 套接字获得 IPv6 的原始接口。可通过原始套接字访问 ICMPv6 报文协议。

### MIB 变量

在 sysctl(3) MIB 的 `net.inet6` 分支中实现了若干变量。除了传输协议支持的变量（请参阅相应手册页）之外，还定义了以下通用变量：

**`IPV6CTL_FORWARDING`** (ip6.forwarding) 布尔值：启用/禁用 IPv6 数据包转发。同时标识节点是否充当路由器。默认为关闭。

**`IPV6CTL_SENDREDIRECTS`** (ip6.redirect) 布尔值：启用/禁用响应不可转发的 IPv6 数据包而发送 ICMPv6 重定向。除非节点正在路由 IPv6 数据包，否则此选项会被忽略；通常应在所有系统上启用。默认为开启。

**`IPV6CTL_DEFHLIM`** (ip6.hlim) 整数：用于外出 IPv6 数据包的默认跳数值。此值适用于 IPv6 之上的所有传输协议。存在 API 可覆盖此值。

**`IPV6CTL_MAXFRAGS`** (ip6.maxfrags) 整数：主机在所有 VNET 中所有重组队列中接受并同时保留的分片的最大数量。设为 0 则禁用分片重组。设为 -1 则不应用此限制。当 mbuf cluster 数量变化时，会重新计算此限制。这是全局限制。

**`IPV6CTL_MAXFRAGPACKETS`** (ip6.maxfragpackets) 整数：节点为特定 VNET 接受并同时保留在重组队列中的分片数据包的最大数量。0 表示该节点不为该 VNET 接受任何分片数据包。-1 表示该节点不为该 VNET 应用此限制。当 mbuf cluster 数量变化时，会重新计算此限制。这是每 VNET 限制。

**`IPV6CTL_MAXFRAGBUCKETSIZE`** (ip6.maxfragbucketsize) 整数：每个桶中重组队列的最大数量。分片数据包被哈希到桶中。每个桶包含一个重组队列列表。系统必须将进入的数据包与桶中现有的重组队列进行比较，以找到匹配的重组队列。为节省系统资源，系统限制每个桶中允许的重组队列数量。当 mbuf cluster 数量变化或 `ip6.maxfragpackets` 的值变化时，会重新计算此限制。这是每 VNET 限制。

**`IPV6CTL_MAXFRAGSPERPACKET`** (ip6.maxfragsperpacket) 整数：主机为单个数据包接受并保留在重组队列中的分片的最大数量。这是每 VNET 限制。

**`IPV6CTL_ACCEPT_RTADV`** (ip6.accept_rtadv) 布尔值：每接口标志的默认值，用于启用/禁用接收 ICMPv6 路由器通告数据包，以及地址前缀和默认路由器的自动配置。节点必须是主机（而非路由器）此选项才有意义。默认为关闭。

**`IPV6CTL_AUTO_LINKLOCAL`** (ip6.auto_linklocal) 布尔值：每接口标志的默认值，用于启用/禁用执行自动链路本地地址配置。默认为开启。

**`IPV6CTL_LOG_INTERVAL`** (ip6.log_interval) 整数：IPv6 数据包转发引擎日志输出之间的默认间隔（秒）。

**`IPV6CTL_HDRNESTLIMIT`** (ip6.hdrnestlimit) 整数：进入 IPv6 数据包上允许的 IPv6 扩展头的默认最大数量。设为 0 表示节点接受尽可能多的扩展头。

**`IPV6CTL_DAD_COUNT`** (ip6.dad_count) 整数：IPv6 DAD（重复地址检测）探测数据包的默认数量。在配置 IPv6 接口地址时将生成这些数据包。

**`IPV6CTL_GRAND_COUNT`** (ip6.grand_count) 整数：IPv6 GRAND（无偿邻居发现）非请求 NA 数据包的默认数量。在配置 IPv6 接口地址或链路层接口地址发生变化时将生成这些数据包。

**`IPV6CTL_AUTO_FLOWLABEL`** (ip6.auto_flowlabel) 布尔值：启用/禁用对未完成的已连接传输协议数据包自动填充 IPv6 流标签字段。中间路由器可能使用此字段识别数据包流。默认为开启。

**`IPV6CTL_DEFMCASTHLIM`** (ip6.defmcasthlim) 整数：由该节点发起的 IPv6 多播数据包的默认跳数值。此值适用于 IPv6 之上的所有传输协议。如 [ip6(4)](ip6.4.md) 中所述，存在 API 可覆盖此值。

**`IPV6CTL_GIF_HLIM`** (ip6.gifhlim) 整数：由 [gif(4)](gif.4.md) 隧道接口生成的 IPv6 数据包的默认最大跳数值。

**`IPV6CTL_KAME_VERSION`** (ip6.kame_version) 字符串：标识内核中实现的 KAME IPv6 协议栈版本。

**`IPV6CTL_USE_DEPRECATED`** (ip6.use_deprecated) 布尔值：启用/禁用使用已弃用地址，按 RFC2462 5.5.4 规定。默认为开启。

**`IPV6CTL_RR_PRUNE`** (ip6.rr_prune) 整数：IPv6 路由器重编号前缀看护之间的默认间隔（秒）。

**`IPV6CTL_V6ONLY`** (ip6.v6only) 布尔值：启用/禁用在 `AF_INET6` 套接字上禁止使用 IPv4 映射地址。默认为开启。

**`ip6.log_cannot_forward`** 布尔值：记录无法转发的数据包，原因包括源地址未指定或目的地址超出源地址作用域，如 RFC4443 所述。默认启用。

**`ip6.source_address_validation`** 布尔值：对发往本地主机的数据包执行源地址验证。可视为遵循 RFC3704/BCP84 第 3.2 节，将本地主机视为我们自己的基础设施。这对要转发的数据包无影响，因此不应将其视为路由器的反欺骗功能。默认启用。

### IPv4/v6 套接字之间的交互

默认情况下，FreeBSD 不会将 IPv4 流量路由到 `AF_INET6` 套接字。出于安全原因，此默认行为有意违反 RFC2553。如果想同时接受 IPv4 和 IPv6 流量，请监听两个套接字。可以通过某些每套接字/每节点配置将 IPv4 流量路由到 `AF_INET6` 套接字，但不建议这么做。详情请参阅 [ip6(4)](ip6.4.md)。

`AF_INET6` TCP/UDP 套接字的行为在 RFC2553 中有说明。基本上规定如下：

- 在 `AF_INET6` 套接字上进行特定绑定（即绑定到指定地址）时，应仅接受到该地址的 IPv6 流量。
- 如果在 `AF_INET6` 套接字上执行通配绑定（即绑定到 IPv6 地址 `::`），且在该 TCP/UDP 端口上没有通配绑定的 `AF_INET` 套接字，则 IPv6 流量和 IPv4 流量都应路由到该 `AF_INET6` 套接字。IPv4 流量应被视为来自形如 `::ffff:10.1.1.1` 的 IPv6 地址。这称为 IPv4 映射地址。
- 如果在一个 TCP/UDP 端口上同时存在通配绑定的 `AF_INET` 套接字和通配绑定的 `AF_INET6` 套接字，它们应分别运作。IPv4 流量应路由到 `AF_INET` 套接字，IPv6 流量应路由到 `AF_INET6` 套接字。

然而，RFC2553 并未定义 bind(2) 调用之间的顺序约束，也未定义 IPv4 TCP/UDP 端口号与 IPv6 TCP/UDP 端口号之间的关系（应整合还是分离）。不同内核之间的实现行为差异很大。因此，过于依赖 `AF_INET6` 通配绑定套接字的行为是不明智的。如果想同时接受 IPv4 和 IPv6 流量，建议监听两个套接字，一个用于 `AF_INET`，另一个用于 `AF_INET6`。

还应注意的是，恶意方可利用上述复杂性绕过访问控制，前提是目标节点将 IPv4 流量路由到 `AF_INET6` 套接字。建议用户谨慎处理来自 IPv4 映射地址到 `AF_INET6` 套接字的连接。

## 参见

ioctl(2), socket(2), sysctl(3), [icmp6(4)](icmp6.4.md), [intro(4)](intro.4.md), [ip6(4)](ip6.4.md), [tcp(4)](tcp.4.md), [udp(4)](udp.4.md)

"Protocol Version 6 (IPv6) Specification"

> A. Conta, S. Deering, M. Gupta, "Internet Control Message Protocol (ICMPv6) for the Internet \", March 2006.

## 标准

> Tatsuya Jinmei, Atsushi Onoe, "An Extension of Format for IPv6 Scoped Addresses", draft-ietf-ipngwg-scopedaddr-format-02.txt, June 2000, work in progress material.

## 历史

`inet6` 协议接口定义于 RFC2553 和 RFC2292。此处描述的实现出现于 WIDE/KAME 项目。

## 缺陷

IPv6 支持会随着 Internet 协议的发展而变化。用户不应依赖当前实现的细节，而应依赖其导出的服务。

建议用户尽可能实现“版本无关”的代码，因为你将需要同时支持 [inet(4)](inet.4.md) 和 `inet6`。
