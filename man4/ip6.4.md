# ip6(4)

`ip6` — Internet 协议版本 6（IPv6）网络层

## 名称

`ip6`

## 概要

`#include <sys/socket.h>`

`#include <netinet/in.h>`

`int socket(AF_INET6, SOCK_RAW, proto)`

## 描述

IPv6 协议族使用 IPv6 网络层传输数据。IPv6 数据包包含一个 IPv6 头，当传递给应用程序时，该头不作为载荷内容的一部分提供。IPv6 头选项影响此协议的行为，可被高层协议（如 [tcp(4)](tcp.4.md) 和 [udp(4)](udp.4.md) 协议）以及直接处理 IPv6 消息的“原始套接字”使用，后者在较低层级处理 IPv6 消息，对于开发新协议和特殊用途应用程序可能有用。

### 头

所有 IPv6 数据包均以 IPv6 头开始。当内核接收到的数据传递给应用程序时，即使使用原始套接字，该头也不包含在缓冲区中。同样，当应用程序将数据发送给内核进行传输时，不会检查缓冲区中的 IPv6 头：内核始终构造头。要从接收数据包中直接访问 IPv6 头，并将其指定为传递给内核的缓冲区的一部分，必须改用链路层访问（例如 [bpf(4)](bpf.4.md)）。

该头具有以下定义：

```sh
struct ip6_hdr {
     union {
          struct ip6_hdrctl {
               uint32_t ip6_un1_flow;	/* 20 位 flow ID */
               uint16_t ip6_un1_plen;	/* 载荷长度 */
               uint8_t  ip6_un1_nxt;	/* 下一头 */
               uint8_t  ip6_un1_hlim;	/* 跳数限制 */
          } ip6_un1;
          uint8_t ip6_un2_vfc;	/* 版本和类 */
     } ip6_ctlun;
     struct in6_addr ip6_src;	/* 源地址 */
     struct in6_addr ip6_dst;	/* 目的地址 */
} __packed;
#define ip6_vfc		ip6_ctlun.ip6_un2_vfc
#define ip6_flow	ip6_ctlun.ip6_un1.ip6_un1_flow
#define ip6_plen	ip6_ctlun.ip6_un1.ip6_un1_plen
#define ip6_nxt		ip6_ctlun.ip6_un1.ip6_un1_nxt
#define ip6_hlim	ip6_ctlun.ip6_un1.ip6_un1_hlim
#define ip6_hops	ip6_ctlun.ip6_un1.ip6_un1_hlim
```

所有字段均处于网络字节序。指定的任何选项（见下文“选项”小节）也必须以网络字节序指定。

`ip6_flow` 指定 flow ID。`ip6_plen` 指定载荷长度。`ip6_nxt` 指定下一头的类型。`ip6_hlim` 指定跳数限制。

`ip6_vfc` 的最高 4 位指定类，最低 4 位指定版本。

`ip6_src` 和 `ip6_dst` 指定源地址和目的地址。

IPv6 头后面可跟随任意数量的扩展头，这些扩展头以以下通用定义开始：

```sh
struct ip6_ext {
     uint8_t ip6e_nxt;
     uint8_t ip6e_len;
} __packed;
```

### 选项

IPv6 允许在数据包上使用头选项来操作协议行为。这些选项和其他控制请求通过 `IPPROTO_IPV6` 级别的 getsockopt(2) 和 setsockopt(2) 系统调用，以及 recvmsg(2) 和 sendmsg(2) 中的辅助数据访问。它们可用于访问 IPv6 头和扩展头中的大多数字段。

支持以下套接字选项：

```sh
struct ipv6_mreq {
	struct in6_addr	ipv6mr_multiaddr;
	unsigned int	ipv6mr_interface;
};
```

**`IPV6_PORTRANGE_DEFAULT`** 使用常规的非保留端口范围（可变，见 [ip(4)](ip.4.md)）。

**`IPV6_PORTRANGE_HIGH`** 使用高范围（可变，见 [ip(4)](ip.4.md)）。

**`IPV6_PORTRANGE_LOW`** 使用低保留范围（600-1023，见 [ip(4)](ip.4.md)）。

```sh
struct in6_pktinfo {
	struct in6_addr ipi6_addr;    /* 源/目的 IPv6 地址 */
	unsigned int    ipi6_ifindex; /* 发送/接收接口索引 */
};
```

```sh
struct ip6_hbh {
	uint8_t ip6h_nxt;	/* 下一头 */
	uint8_t ip6h_len;	/* 长度，以 8 字节为单位 */
/* 后跟选项 */
} __packed;
```

```sh
struct ip6_dest {
	uint8_t ip6d_nxt;	/* 下一头 */
	uint8_t ip6d_len;	/* 长度，以 8 字节为单位 */
/* 后跟选项 */
} __packed;
```

```sh
struct ip6_rthdr {
	uint8_t ip6r_nxt;	/* 下一头 */
	uint8_t ip6r_len;	/* 长度，以 8 字节为单位 */
	uint8_t ip6r_type;	/* 路由类型 */
	uint8_t ip6r_segleft;	/* 剩余段数 */
/* 后跟路由类型特定数据 */
} __packed;
```

**`IPV6_UNICAST_HOPS`** `int *` 获取或设置此套接字上外出单播数据报的默认跳数限制头字段。

**`IPV6_MULTICAST_IF`** `u_int *` 获取或设置发送多播数据包的接口。对于具有多个接口的主机，每次多播传输都从主网络接口发送。接口以 if_nametoindex(3) 提供的索引指定。值为零指定默认接口。

**`IPV6_MULTICAST_HOPS`** `int *` 获取或设置此套接字上外出多播数据报的默认跳数限制头字段。此选项控制多播数据报传输的范围。跳数限制为 1 的数据报不会转发到本地网络之外。跳数限制为零的多播数据报不会在任何网络上传输，但如果发送主机属于目的组且发送套接字上未禁用多播环回（见下文），则可能在本地交付。跳数限制大于 1 的多播数据报可被转发到其他网络（如果本地网络连接了多播路由器，如 mrouted(8)（`ports/net/mrouted`））。

**`IPV6_MULTICAST_LOOP`** `u_int *` 获取或设置当多播数据报发送到发送主机所属的组时，多播数据报是否环回以进行本地交付的状态。此选项通过消除接收自身传输的开销，提高在单主机上可能只有一个实例的应用程序（如路由守护进程）的性能。对于单主机上可能有多个实例的应用程序（如会议程序）或发送方不属于目的组的应用程序（如时间查询程序），通常不应使用此选项。以大于 1 的初始跳数限制发送的多播数据报可能会在与发送接口不同的接口上交付给发送主机（如果该主机属于该其他接口上的目的组）。多播环回控制选项对此类交付无影响。

**`IPV6_JOINGROUP`** `struct ipv6_mreq *` 加入多播组。主机必须先成为多播组的成员，才能接收发送到该组的数据报。`ipv6mr_interface` 可设为零以选择默认多播接口，如果主机是多宿主的，则设为特定支持多播的接口的索引。成员资格与单个接口关联；在多宿主主机上运行的程序可能需要在一个以上的接口上加入同一组。如果多播地址未指定（即全零），则来自所有多播地址的消息都将被该组接受。注意，设置为此值需要超级用户特权。

**`IPV6_LEAVEGROUP`** `struct ipv6_mreq *` 从关联的多播组退出成员资格。当套接字关闭或进程退出时，成员资格会自动退出。

**`IPV6_ORIGDSTADDR`** `int *` 获取或设置是否在后续 recvmsg(2) 调用中连同载荷一起作为辅助数据返回数据报的原始目的地址和端口。信息以 sockaddr_in6 结构存储在辅助数据中。

**`IPV6_PORTRANGE`** `int *` 获取或设置当内核自动将本地地址绑定到此套接字时临时端口的分配策略。可用以下值：

**`IPV6_PKTINFO`** `int *` 获取或设置是否在后续 recvmsg(2) 调用中连同载荷一起作为辅助数据提供后续数据包的附加信息。信息存储在返回的辅助数据中的以下结构中：

**`IPV6_HOPLIMIT`** `int *` 获取或设置是否在后续 recvmsg(2) 调用中连同载荷一起作为辅助数据提供后续数据包的跳数限制头字段。该值在返回的辅助数据中作为 `int` 存储。

**`IPV6_HOPOPTS`** `int *` 获取或设置是否在后续 recvmsg(2) 调用中连同载荷一起作为辅助数据提供后续数据包的逐跳选项。该选项存储在返回的辅助数据中的以下结构中：可使用 `inet6_opt_init` 例程及其相关例程操作此数据。此选项需要超级用户特权。

**`IPV6_DSTOPTS`** `int *` 获取或设置是否在后续 recvmsg(2) 调用中连同载荷一起作为辅助数据提供后续数据包的目的选项。该选项存储在返回的辅助数据中的以下结构中：可使用 `inet6_opt_init` 例程及其相关例程操作此数据。此选项需要超级用户特权。

**`IPV6_TCLASS`** `int *` 获取或设置此套接字上外出数据报使用的流量类字段的值。该值必须在 -1 到 255 之间。值为 -1 重置为默认值。

**`IPV6_RECVTCLASS`** `int *` 获取或设置是否在后续 recvmsg(2) 调用中连同载荷一起作为辅助数据提供流量类头字段的状态。该头字段作为 `int` 类型的单个值存储。

**`IPV6_RTHDR`** `int *` 获取或设置是否在后续 recvmsg(2) 调用中连同载荷一起作为辅助数据提供后续数据包的路由头。该头存储在返回的辅助数据中的以下结构中：可使用 `inet6_opt_init` 例程及其相关例程操作此数据。此选项需要超级用户特权。

**`IPV6_PKTOPTIONS`** `struct cmsghdr *` 一次性获取或设置套接字上最后发送或接收的数据包上的所有头选项和扩展头。所有选项必须适合一个 mbuf 的大小（见 [mbuf(9)](../man9/mbuf.9.md)）。选项以一系列 `cmsghdr` 结构及其相应值指定。`cmsg_level` 设为 `IPPROTO_IPV6`，`cmsg_type` 设为此列表中的其他值之一，尾随数据为选项值。设置选项时，如果 setsockopt(2) 的长度 `optlen` 为零，则所有头选项将重置为默认值。否则，该长度应指定一系列控制消息所占用的大小。可使用作为 setsockopt(2) 参数提供的一系列控制消息中的控制消息直接指定对应所需头选项的辅助数据（这些数据本来在 sendmsg(2) 调用中使用），而无需使用 sendmsg(2) 指定选项值。

**`IPV6_CHECKSUM`** `int *` 获取或设置数据包中 16 位校验和所在的字节偏移量。设置后，此字节偏移量是进入数据包预期存储数据校验和的位置，也是外出数据包内核计算并存储数据校验和的位置。值为 -1 指定不检查进入数据包的校验和，也不计算或存储外出数据包的校验和。ICMPv6 套接字的校验和偏移量不能重定位或关闭。

**`IPV6_V6ONLY`** `int *` 获取或设置是否只能对此套接字进行 IPv6 连接。对于通配套接字，这可将连接限制为仅 IPv6。

**`IPV6_USE_MIN_MTU`** `int *` 获取或设置是否使用最小 IPv6 最大传输单元（MTU）大小以避免后续外出数据报发生分片。

**`IPV6_AUTH_LEVEL`** `int *` 获取或设置 [ipsec(4)](ipsec.4.md) 认证级别。

**`IPV6_ESP_TRANS_LEVEL`** `int *` 获取或设置 ESP 传输级别。

**`IPV6_ESP_NETWORK_LEVEL`** `int *` 获取或设置 ESP 封装级别。

**`IPV6_IPCOMP_LEVEL`** `int *` 获取或设置 ipcomp(4) 级别。

`IPV6_PKTINFO`、`IPV6_HOPLIMIT`、`IPV6_HOPOPTS`、`IPV6_DSTOPTS`、`IPV6_RTHDR` 和 `IPV6_ORIGDSTADDR` 选项将在后续 recvmsg(2) 调用中连同载荷内容一起返回辅助数据，`cmsg_level` 设为 `IPPROTO_IPV6`，`cmsg_type` 设为相应的选项名值（例如 `IPV6_HOPTLIMIT`）。其中某些选项也可在 sendmsg(2) 中直接用作辅助 `cmsg_type` 值，以在该调用传输的数据包上设置选项。`cmsg_level` 值必须为 `IPPROTO_IPV6`。对于这些选项，辅助数据对象值格式与 recvmsg(2) 接收时返回的值格式相同（如各自说明中所述）。

注意，使用 sendmsg(2) 在特定数据包上指定选项仅适用于 UDP 和原始套接字。要操作 TCP 套接字上数据包的头选项，只能使用套接字选项。

在某些情况下，定义了多个 API 用于操作 IPv6 头字段。一个很好的例子是多播数据报的外出接口，可通过 `IPV6_MULTICAST_IF` 套接字选项、`IPV6_PKTINFO` 选项以及传递给 sendto(2) 系统调用的套接字地址的 `sin6_scope_id` 字段设置。

解决这些冲突的方式取决于实现。此实现按以下方式确定值：首先考虑使用辅助数据指定的选项（即 sendmsg(2)），其次考虑使用 `IPV6_PKTOPTIONS` 设置“粘性”选项，第三考虑使用单独的、基本的和直接的套接字选项（例如 `IPV6_UNICAST_HOPS`）指定的选项，最后考虑传递给 sendto(2) 的套接字地址中指定的选项。

### 多播

仅在 `AF_INET6` 类型为 `SOCK_DGRAM` 和 `SOCK_RAW` 的套接字上以及接口驱动程序支持多播的网络上支持 IPv6 多播。操作多播组成员资格和其他多播选项的套接字选项（见上文）包括 `IPV6_MULTICAST_IF`、`IPV6_MULTICAST_HOPS`、`IPV6_MULTICAST_LOOP`、`IPV6_LEAVE_GROUP` 和 `IPV6_JOIN_GROUP`。

### 原始套接字

原始 IPv6 套接字是无连接的，通常与 sendto(2) 和 recvfrom(2) 调用一起使用，虽然可使用 connect(2) 调用来固定后续外出数据包的目的地址，以便改用 send(2)，且可使用 bind(2) 调用来固定后续外出数据包的源地址，而非由内核选择源地址。

通过使用 connect(2) 或 bind(2)，原始套接字输入被限制为仅接收其源地址与套接字目的地址匹配（如果使用了 connect(2)）的数据包，或其目的地址与套接字源地址匹配（如果使用了 bind(2)）的数据包。

如果 socket(2) 的 `proto` 参数为零，外出数据包使用默认协议（`IPPROTO_RAW`）。对于进入数据包，内核识别的协议**不**会传递给应用程序套接字（例如 [tcp(4)](tcp.4.md) 和 [udp(4)](udp.4.md)），某些 ICMPv6 消息除外。不传递给原始套接字的 ICMPv6 消息包括回显、时间戳和地址掩码请求。如果 `proto` 非零，则只有该协议的数据包会传递给套接字。

IPv6 分片在重新组装之前也不会传递给应用程序套接字。如果需要接收所有数据包，必须改用链路层访问（例如 [bpf(4)](bpf.4.md)）。

外出数据包会自动在前面加上 IPv6 头（基于目的地址和创建套接字时使用的协议号）。应用程序接收进入数据包时不带 IPv6 头或任何扩展头。

如果外出数据包过大，内核会自动将其分片。进入数据包在发送到原始套接字之前会被重新组装，因此原始套接字上永远不会看到数据包分片或分片头。

## 实例

以下示例确定下一个接收数据包的跳数限制：

```sh
struct iovec iov[2];
u_char buf[BUFSIZ];
struct cmsghdr *cm;
struct msghdr m;
int optval;
bool found;
u_char data[2048];
/* 创建套接字。 */
(void)memset(&m, 0, sizeof(m));
(void)memset(&iov, 0, sizeof(iov));
iov[0].iov_base = data;		/* 数据包载荷的缓冲区 */
iov[0].iov_len = sizeof(data);	/* 预期数据包长度 */
m.msg_name = &from;		/* 对端的 sockaddr_in6 */
m.msg_namelen = sizeof(from);
m.msg_iov = iov;
m.msg_iovlen = 1;
m.msg_control = (caddr_t)buf;	/* 控制消息的缓冲区 */
m.msg_controllen = sizeof(buf);
/*
 * 启用接收数据包的跳数限制值随载荷一起返回。
 */
optval = 1;
if (setsockopt(s, IPPROTO_IPV6, IPV6_HOPLIMIT, &optval,
    sizeof(optval)) == -1)
	err(1, "setsockopt");
found = false;
do {
	if (recvmsg(s, &m, 0) == -1)
		err(1, "recvmsg");
	for (cm = CMSG_FIRSTHDR(&m); cm != NULL;
	     cm = CMSG_NXTHDR(&m, cm)) {
		if (cm->cmsg_level == IPPROTO_IPV6 &&
		    cm->cmsg_type == IPV6_HOPLIMIT &&
		    cm->cmsg_len == CMSG_LEN(sizeof(int))) {
			found = true;
			(void)printf("hop limit: %d\n",
			    *(int *)CMSG_DATA(cm));
			break;
		}
	}
} while (!found);
```

## 诊断

套接字操作可能失败并返回以下错误之一：

**[EISCONN]** 当尝试在已建立连接的套接字上再次建立连接，或尝试在套接字已连接时指定目的地址发送数据报时。

**[ENOTCONN]** 当尝试发送数据报，但未指定目的地址且套接字未连接时。

**[ENOBUFS]** 当系统为内部数据结构耗尽内存时。

**[EADDRNOTAVAIL]** 当尝试创建一个网络地址对应的网络接口不存在的套接字时。

**[EACCES]** 当非特权进程尝试创建原始 IPv6 套接字时。

设置或获取头选项时可能发生以下 IPv6 特定错误：

**[EINVAL]** 给定了未知的套接字选项名。

**[EINVAL]** 辅助数据对象格式不正确。

## 参见

getsockopt(2), recv(2), send(2), setsockopt(2), socket(2), [CMSG_DATA(3)](../man3/cmsg_data.3.md), if_nametoindex(3), inet6_opt_init(3), [bpf(4)](bpf.4.md), [icmp6(4)](icmp6.4.md), [inet6(4)](inet6.4.md), [ip(4)](ip.4.md), [netintro(4)](netintro.4.md), [tcp(4)](tcp.4.md), [udp(4)](udp.4.md)

> W. Stevens, M. Thomas, "Advanced Sockets API for IPv6", February 1998.

> S. Deering, R. Hinden, "Internet Protocol, Version 6 (IPv6) Specification", December 1998.

> R. Gilligan, S. Thomson, J. Bound, W. Stevens, "Basic Socket Interface Extensions for IPv6", March 1999.

> R. Gilligan, S. Thomson, J. Bound, J. McCann, W. Stevens, "Basic Socket Interface Extensions for IPv6", February 2003.

> W. Stevens, M. Thomas, E. Nordmark, T. Jinmei, "Advanced Sockets Application Program Interface (API) for IPv6", May 2003.

> S. Deering, R. Hinden, "Internet Protocol, Version 6 (IPv6) Specification", July 2017.

> W. Stevens, B. Fenner, A. Rudoff, "UNIX Network Programming, 3rd Edition", Addison-Wesley Professional, November 2003.

## 标准

大多数套接字选项定义于 RFC 2292 / 3542 或 RFC 2553 / 3493。`IPV6_PORTRANGE` 套接字选项和冲突解决规则未在 RFC 中定义，应视为实现相关。
