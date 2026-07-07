# ip(4)

`ip` — Internet 协议

## 名称

`ip`

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/in.h>`

`int socket(AF_INET, SOCK_RAW, proto)`

## 描述

IP 是 Internet 协议族使用的传输层协议。当使用基于 IP 的更高层协议（如 TCP 和 UDP）时，可在 IP 层设置选项。在开发新协议或特殊用途应用程序时，也可通过“原始套接字”访问 IP。

有若干 IP 层的 setsockopt(2) 和 getsockopt(2) 选项。`IP_OPTIONS` 可用于提供要在每个外出数据包的 IP 头中传输的 IP 选项，或检查进入数据包头上的选项。IP 选项可与 Internet 协议族中的任何套接字类型一起使用。要发送的 IP 选项格式由 IP 协议规范（RFC-791）规定，但有一例外：源路由选项的地址列表必须在网关列表的开头包含首跳网关。首跳网关地址将从选项列表中提取，并在使用前相应调整大小。要禁用先前指定的选项，使用零长度缓冲区：

```sh
setsockopt(s, IPPROTO_IP, IP_OPTIONS, NULL, 0);
```

`IP_TOS` 可用于设置差异化服务代码点（DSCP）和显式拥塞通知（ECN）代码点。在使用实现 ECN 的传输协议的套接字上设置 ECN 代码点（最低两位）无效。

`IP_TTL` 配置 `SOCK_STREAM`、`SOCK_DGRAM` 以及某些类型的 `SOCK_RAW` 套接字的 IP 头中的生存时间（TTL）字段。例如：

```sh
int tos = IPTOS_DSCP_EF;       /* 见 <netinet/ip.h> */
setsockopt(s, IPPROTO_IP, IP_TOS, &tos, sizeof(tos));
int ttl = 60;                   /* 最大 = 255 */
setsockopt(s, IPPROTO_IP, IP_TTL, &ttl, sizeof(ttl));
```

`IP_IPSEC_POLICY` 控制套接字的 IPSec 策略。例如：

```sh
const char *policy = "in ipsec ah/transport//require";
char *buf = ipsec_set_policy(policy, strlen(policy));
setsockopt(s, IPPROTO_IP, IP_IPSEC_POLICY, buf, ipsec_get_policylen(buf));
```

`IP_MINTTL` 可用于设置套接字接收数据包时必须具有的最低可接受 TTL。所有 TTL 较低的数据包都将被静默丢弃。此选项仅在设置为 255 时才真正有用，可防止来自直接连接网络之外的数据包到达套接字上的本地监听器。

`IP_DONTFRAG` 可用于在 IP 数据包上设置 Don't Fragment 标志。除非已设置 `IP_HDRINCL` 选项，否则当前仅在 [udp(4)](udp.4.md) 和原始 `ip` 套接字上遵守此选项。在 [tcp(4)](tcp.4.md) 套接字上，Don't Fragment 标志由路径 MTU 发现选项控制。发送大于由目的地址确定的出口接口 MTU 大小的数据包会返回 `EMSGSIZE` 错误。

如果在 `SOCK_DGRAM` 套接字上启用了 `IP_ORIGDSTADDR` 选项，recvmsg(2) 调用将返回 UDP 数据报的目的 IP 地址和目的端口。`msghdr` 结构中的 `msg_control` 字段指向一个缓冲区，其中包含 `cmsghdr` 结构，后跟 sockaddr_in 结构。`cmsghdr` 字段具有以下值：

```sh
cmsg_len = CMSG_LEN(sizeof(struct sockaddr_in))
cmsg_level = IPPROTO_IP
cmsg_type = IP_ORIGDSTADDR
```

如果在 `SOCK_DGRAM` 套接字上启用了 `IP_RECVDSTADDR` 选项，recvmsg(2) 调用将返回 UDP 数据报的目的 IP 地址。`msghdr` 结构中的 `msg_control` 字段指向一个缓冲区，其中包含 `cmsghdr` 结构，后跟 IP 地址。`cmsghdr` 字段具有以下值：

```sh
cmsg_len = CMSG_LEN(sizeof(struct in_addr))
cmsg_level = IPPROTO_IP
cmsg_type = IP_RECVDSTADDR
```

套接字上外出 UDP 数据报的源地址可作为类型代码为 `IP_SENDSRCADDR` 的辅助数据指定。msghdr 结构中的 msg_control 字段应指向一个缓冲区，其中包含 `cmsghdr` 结构，后跟 IP 地址。cmsghdr 字段应具有以下值：

```sh
cmsg_len = CMSG_LEN(sizeof(struct in_addr))
cmsg_level = IPPROTO_IP
cmsg_type = IP_SENDSRCADDR
```

套接字应绑定到 `INADDR_ANY` 和一个本地端口，且通过 `IP_SENDSRCADDR` 提供的地址不应为 `INADDR_ANY`；或者套接字应绑定到本地地址，且通过 `IP_SENDSRCADDR` 提供的地址应为 `INADDR_ANY`。在后一种情况下，绑定的地址通过通用源地址选择逻辑被覆盖，该逻辑将选择最接近目的地的接口的 IP 地址。

为方便起见，`IP_SENDSRCADDR` 定义为与 `IP_RECVDSTADDR` 具有相同的值，因此来自 recvmsg(2) 的 `IP_RECVDSTADDR` 控制消息可直接用作 sendmsg(2) 的控制消息。

如果在 `SOCK_DGRAM` 或 `SOCK_RAW` 套接字上启用了 `IP_ONESBCAST` 选项，则该套接字上外出广播数据报的目的地址在传输前将被强制为无向广播地址 `INADDR_BROADCAST`。这与系统的默认行为不同，默认行为是通过设置了 `IFF_BROADCAST` 标志的第一个网络接口传输无向广播。

此选项允许应用程序选择使用哪个接口传输无向广播数据报。例如，以下代码将强制通过配置了广播地址 192.168.2.255 的接口传输无向广播：

```sh
char msg[512];
struct sockaddr_in sin;
int onesbcast = 1;	/* 0 = 禁用（默认），1 = 启用 */
setsockopt(s, IPPROTO_IP, IP_ONESBCAST, &onesbcast, sizeof(onesbcast));
sin.sin_addr.s_addr = inet_addr("192.168.2.255");
sin.sin_port = htons(1234);
sendto(s, msg, sizeof(msg), 0, &sin, sizeof(sin));
```

应用程序有责任将 `IP_TTL` 选项设置为适当的值以防止广播风暴。应用程序必须具有足够的凭据才能设置 `SO_BROADCAST` 套接字级选项，否则 `IP_ONESBCAST` 选项无效。

如果在 `SOCK_STREAM`、`SOCK_DGRAM` 或 `SOCK_RAW` 套接字上启用了 `IP_BINDANY` 选项，则可以 bind(2) 到任何地址，甚至系统中未绑定到任何可用网络接口的地址。此功能（结合特殊防火墙规则）可用于实现透明代理。设置此选项需要 `PRIV_NETINET_BINDANY` 特权。

如果在 `SOCK_DGRAM` 套接字上启用了 `IP_RECVTTL` 选项，recvmsg(2) 调用将返回 UDP 数据报的 IP TTL（生存时间）字段。msghdr 结构中的 msg_control 字段指向一个缓冲区，其中包含 cmsghdr 结构，后跟 TTL。cmsghdr 字段具有以下值：

```sh
cmsg_len = CMSG_LEN(sizeof(u_char))
cmsg_level = IPPROTO_IP
cmsg_type = IP_RECVTTL
```

如果在 `SOCK_DGRAM` 套接字上启用了 `IP_RECVTOS` 选项，recvmsg(2) 调用将返回 UDP 数据报的 IP TOS（服务类型）字段。msghdr 结构中的 msg_control 字段指向一个缓冲区，其中包含 cmsghdr 结构，后跟 TOS。cmsghdr 字段具有以下值：

```sh
cmsg_len = CMSG_LEN(sizeof(u_char))
cmsg_level = IPPROTO_IP
cmsg_type = IP_RECVTOS
```

如果在 `SOCK_DGRAM` 套接字上启用了 `IP_RECVIF` 选项，recvmsg(2) 调用将返回与接收数据包的接口对应的 `struct sockaddr_dl`。`msghdr` 结构中的 `msg_control` 字段指向一个缓冲区，其中包含 `cmsghdr` 结构，后跟 `struct sockaddr_dl`。`cmsghdr` 字段具有以下值：

```sh
cmsg_len = CMSG_LEN(sizeof(struct sockaddr_dl))
cmsg_level = IPPROTO_IP
cmsg_type = IP_RECVIF
```

`IP_PORTRANGE` 可用于在套接字上指定未指定（零）端口号时用于选择本地端口号的端口范围。其可能值如下：

**`IP_PORTRANGE_DEFAULT`** 使用默认值范围，通常为 `IPPORT_HIFIRSTAUTO` 到 `IPPORT_HILASTAUTO`。可通过 sysctl 设置 `net.inet.ip.portrange.first` 和 `net.inet.ip.portrange.last` 调整。

**`IP_PORTRANGE_HIGH`** 使用高值范围，通常为 `IPPORT_HIFIRSTAUTO` 到 `IPPORT_HILASTAUTO`。可通过 sysctl 设置 `net.inet.ip.portrange.hifirst` 和 `net.inet.ip.portrange.hilast` 调整。

**`IP_PORTRANGE_LOW`** 使用低端口范围，在 UNIX 系统上通常仅限于特权进程。范围通常从 `IPPORT_RESERVED` - 1 降序到 `IPPORT_RESERVEDSTART`。可通过 sysctl 设置 `net.inet.ip.portrange.lowfirst` 和 `net.inet.ip.portrange.lowlast` 调整。

仅由 root 拥有的进程才能打开的特权端口范围可通过 `net.inet.ip.portrange.reservedlow` 和 `net.inet.ip.portrange.reservedhigh` sysctl 设置修改。默认值为传统范围，分别为 0 到 `IPPORT_RESERVED` - 1（0 到 1023）。注意，这些设置不影响也不计入上述其他 `net.inet.ip.portrange` 值的使用或计算。更改这些值偏离 UNIX 传统，并具有管理员在修改这些设置前应仔细评估的安全后果。

在指定端口范围内随机分配端口，以增加随机欺骗攻击的难度。在基准测试等场景中，此行为可能是不希望出现的。在这些情况下，可使用 `net.inet.ip.portrange.randomized` 关闭随机化。

### 多播选项

仅在 `AF_INET` 类型为 `SOCK_DGRAM` 和 `SOCK_RAW` 的套接字上以及接口驱动程序支持多播的网络上支持 IP 多播。

`IP_MULTICAST_TTL` 选项更改外出多播数据报的生存时间（TTL），以控制多播的范围：

```sh
u_char ttl;	/* 范围：0 到 255，默认 = 1 */
setsockopt(s, IPPROTO_IP, IP_MULTICAST_TTL, &ttl, sizeof(ttl));
```

TTL 为 1 的数据报不会转发到本地网络之外。TTL 为 0 的多播数据报不会在任何网络上传输，但如果发送主机属于目的组且发送套接字上未禁用多播环回（见下文），则可能在本地交付。TTL 大于 1 的多播数据报可被转发到其他网络（如果本地网络连接了多播路由器）。

对于具有多个接口且未为多播组成员资格指定接口的主机，每次多播传输都从主网络接口发送。`IP_MULTICAST_IF` 选项覆盖给定套接字后续传输的默认值：

```sh
struct in_addr addr;
setsockopt(s, IPPROTO_IP, IP_MULTICAST_IF, &addr, sizeof(addr));
```

其中 "addr" 是所需接口的本地 IP 地址，或 `INADDR_ANY` 指定默认接口。

要按索引指定接口，可改为传递 `ip_mreqn` 实例。`imr_ifindex` 成员应设置为所需接口的索引，或 0 指定默认接口。内核通过大小来区分这两种结构。

*不建议*使用 `IP_MULTICAST_IF`，因为多播成员资格以每个接口为单位限定作用域。它仅为传统应用程序（如路由守护进程）支持，这些应用程序期望能够在多个接口上传输链路本地 IPv4 多播数据报（224.0.0.0/24），而无需为每个接口请求单独的成员资格。

可通过 `SIOCGIFCONF` 和 `SIOCGIFFLAGS` ioctl 获取接口的本地 IP 地址和多播能力。普通应用程序不应需要使用此选项。

如果多播数据报发送到发送主机本身所属的组（在出口接口上），默认情况下，IP 层会为本地交付环回该数据报的副本。`IP_MULTICAST_LOOP` 选项使发送方能够显式控制后续数据报是否环回：

```sh
u_char loop;	/* 0 = 禁用，1 = 启用（默认） */
setsockopt(s, IPPROTO_IP, IP_MULTICAST_LOOP, &loop, sizeof(loop));
```

此选项通过消除接收自身传输的开销，提高在单主机上可能只有一个实例的应用程序（如路由守护进程）的性能。对于单主机上可能有多个实例的应用程序（如会议程序）或发送方不属于目的组的应用程序（如时间查询程序），通常不应使用此选项。

sysctl 设置 `net.inet.ip.mcast.loop` 控制新套接字的 `IP_MULTICAST_LOOP` 套接字选项的默认设置。

以大于 1 的初始 TTL 发送的多播数据报可能会在与发送接口不同的接口上交付给发送主机（如果该主机属于该其他接口上的目的组）。环回控制选项对此类交付无影响。

主机必须先成为多播组的成员，才能接收发送到该组的数据报。要加入多播组，使用 `IP_ADD_MEMBERSHIP` 选项：

```sh
struct ip_mreqn mreqn;
setsockopt(s, IPPROTO_IP, IP_ADD_MEMBERSHIP, &mreqn, sizeof(mreqn));
```

其中 `mreqn` 是以下结构：

```sh
struct ip_mreqn {
    struct in_addr imr_multiaddr; /* 组的 IP 多播地址 */
    struct in_addr imr_address;   /* 接口的本地 IP 地址 */
    int            imr_ifindex;   /* 接口索引 */
}
```

如果主机是多宿主的，应将 `imr_ifindex` 设置为特定支持多播的接口的索引。如果 `imr_ifindex` 非零，则忽略 `imr_interface` 的值。否则，如果 `imr_ifindex` 为 0，内核将使用 `imr_interface` 中的 IP 地址查找接口。`imr_interface` 的值可设为 `INADDR_ANY` 选择默认接口，但不建议这么做；这被视为与默认路由对应的第一个接口。否则，将使用系统中配置的第一个支持多播的接口。

`IP_ADD_MEMBERSHIP` setsockopt 也支持缺少 `imr_ifindex` 字段的传统 `struct ip_mreq`。在这种情况下，内核的行为就如同 `imr_ifindex` 设为零：`imr_interface` 将用于查找接口。

在 FreeBSD 7.0 之前，如果 `imr_interface` 成员位于 `0.0.0.0/8` 网络范围内，则按 RIP Version 2 MIB Extension（RFC-1724）将其视为系统接口 MIB 中的接口索引。在 FreeBSD 7.0 之后的版本中，不再支持此行为。开发者应改用 RFC 3678 多播源过滤 API；特别是 `MCAST_JOIN_GROUP`。

单个套接字上最多可添加 `IP_MAX_MEMBERSHIPS` 个成员资格。成员资格与单个接口关联；在多宿主主机上运行的程序可能需要在一个以上的接口上加入同一组。

要退出成员资格，使用：

```sh
struct ip_mreq mreq;
setsockopt(s, IPPROTO_IP, IP_DROP_MEMBERSHIP, &mreq, sizeof(mreq));
```

其中 `mreq` 包含与添加成员资格时相同的值。当套接字关闭或进程退出时，成员资格将被退出。

IGMP 协议使用接口的主 IP 地址作为其组成员资格的标识符。这是在接口上配置的第一个 IP 地址。如果此地址被删除或更改，结果未定义，因为 IGMP 成员资格状态将不一致。如果在同一接口上配置了多个 IP 别名，它们将被忽略。

此缺陷在 IPv6 中得到解决；MLDv2 要求使用接口的唯一链路本地地址来标识 MLDv2 监听者。

### 特定源多播选项

自 FreeBSD 8.0 起，支持使用特定源多播（SSM）。这些扩展需要 IGMPv3 多播路由器才能充分利用。如果链路上存在传统多播路由器，FreeBSD 将简单降级到路由器所说的 IGMP 版本，并且上游链路上的源过滤优势将不存在，但内核将继续抑制来自被阻止源的传输。

套接字上的每个组成员资格现在都有一个过滤模式：

**`MCAST_EXCLUDE`** 接受发送到此组的数据报，除非源在被阻止源地址列表中。

**`MCAST_INCLUDE`** 仅当源在已接受源地址列表中时，才接受发送到此组的数据报。

使用传统 `IP_ADD_MEMBERSHIP` 选项加入的组被置于独占模式，并可请求阻止或允许某些源。这称为*基于增量的 API*。

要阻止现有组成员资格上的多播源：

```sh
struct ip_mreq_source mreqs;
setsockopt(s, IPPROTO_IP, IP_BLOCK_SOURCE, &mreqs, sizeof(mreqs));
```

其中 `mreqs` 是以下结构：

```sh
struct ip_mreq_source {
    struct in_addr imr_multiaddr; /* 组的 IP 多播地址 */
    struct in_addr imr_sourceaddr; /* 源的 IP 地址 */
    struct in_addr imr_interface; /* 接口的本地 IP 地址 */
}
```

`imr_sourceaddr` 应设置为要阻止的源的地址。

要解除阻止现有组上的多播源：

```sh
struct ip_mreq_source mreqs;
setsockopt(s, IPPROTO_IP, IP_UNBLOCK_SOURCE, &mreqs, sizeof(mreqs));
```

`IP_BLOCK_SOURCE` 和 `IP_UNBLOCK_SOURCE` 选项*不允许*用于包含模式组成员资格。

要以 `MCAST_INCLUDE` 模式加入具有单个源的多播组，或向现有包含模式成员资格添加另一个源：

```sh
struct ip_mreq_source mreqs;
setsockopt(s, IPPROTO_IP, IP_ADD_SOURCE_MEMBERSHIP, &mreqs, sizeof(mreqs));
```

要从包含模式下的现有组退出单个源：

```sh
struct ip_mreq_source mreqs;
setsockopt(s, IPPROTO_IP, IP_DROP_SOURCE_MEMBERSHIP, &mreqs, sizeof(mreqs));
```

如果这是该组的最后一个已接受源，则成员资格将被退出。

`IP_ADD_SOURCE_MEMBERSHIP` 和 `IP_DROP_SOURCE_MEMBERSHIP` 选项*不接受*用于独占模式组成员资格。但是，独占和包含模式成员资格都支持使用 RFC 3678 中记载的*完整状态 API*。有关使用此 API 管理源过滤列表的信息，请参阅 sourcefilter(3)。

sysctl 设置 `net.inet.ip.mcast.maxsocksrc` 和 `net.inet.ip.mcast.maxgrpsrc` 用于指定内核可分配的每套接字和每组的源过滤条目的上限。

### 原始 IP 套接字

原始 IP 套接字是无连接的，通常与 sendto(2) 和 recvfrom(2) 调用一起使用，但也可使用 connect(2) 调用来固定后续数据包的目的地（此时可使用 read(2) 或 recv(2) 以及 write(2) 或 send(2) 系统调用）。

如果 `proto` 为 0，外出数据包使用默认协议 `IPPROTO_RAW`，且仅接收发往该协议的进入数据包。如果 `proto` 非零，外出数据包将使用该协议号，并用于过滤进入数据包。

除非已设置 `IP_HDRINCL` 选项，否则外出数据包会自动在前面加上 IP 头（基于目的地址和创建套接字时使用的协议号）。与之前的 BSD 版本不同，进入数据包在接收时保留 IP 头和选项不变，所有字段保持网络字节序。

`IP_HDRINCL` 表示完整 IP 头包含在数据中，仅可用于 `SOCK_RAW` 类型。

```sh
#include <netinet/in_systm.h>
#include <netinet/ip.h>
int hincl = 1;                  /* 1 = 开启，0 = 关闭 */
setsockopt(s, IPPROTO_IP, IP_HDRINCL, &hincl, sizeof(hincl));
```

与之前的 BSD 版本不同，程序必须设置 IP 头的所有字段，包括以下内容：

```sh
ip->ip_v = IPVERSION;
ip->ip_hl = hlen >> 2;
ip->ip_id = 0;  /* 0 表示内核设置适当值 */
ip->ip_off = htons(offset);
ip->ip_len = htons(len);
```

数据包应原样提供以在线路上发送。这意味着所有字段（包括 `ip_len` 和 `ip_off`）都应处于网络字节序。有关网络字节序的更多信息，请参见 byteorder(3)。如果 `ip_id` 字段设为 0，内核将选择适当的值。如果头源地址设为 `INADDR_ANY`，内核将选择适当的地址。

## 错误

套接字操作可能失败并返回以下错误之一：

**[EISCONN]** 当尝试在已建立连接的套接字上再次建立连接，或尝试在套接字已连接时指定目的地址发送数据报时；

**[ENOTCONN]** 当尝试发送数据报，但未指定目的地址且套接字未连接时；

**[ENOBUFS]** 当系统为内部数据结构耗尽内存时；

**[EADDRNOTAVAIL]** 当尝试创建一个网络地址对应的网络接口不存在的套接字时。

**[EACCES]** 当非特权进程尝试创建原始 IP 套接字时。

设置或获取 IP 选项时可能发生以下 IP 特定错误：

**[EINVAL]** 给定了未知的套接字选项名。

**[EINVAL]** IP 选项字段格式不正确；选项字段短于最小值或长于所提供的选项缓冲区。

尝试通过设置了 `IP_HDRINCL` 选项的“原始套接字”发送 IP 数据报时可能发生以下错误：

**[EINVAL]** 用户提供的 `ip_len` 字段不等于写入套接字的数据报长度。

## 参见

getsockopt(2), recv(2), send(2), byteorder(3), [CMSG_DATA(3)](../man3/cmsg_data.3.md), sourcefilter(3), [dtrace_mib(4)](dtrace_mib.4.md), [icmp(4)](icmp.4.md), [igmp(4)](igmp.4.md), [inet(4)](inet.4.md), [intro(4)](intro.4.md), [multicast(4)](multicast.4.md)

> D. Thaler, B. Fenner, B. Quinn, "Socket Interface Extensions for Multicast Source Filters", RFC 3678, Jan 2004.

## 历史

`ip` 协议出现于 4.2BSD。`ip_mreqn` 结构出现于 Linux 2.4。

## 缺陷

在 FreeBSD 10.0 之前，在原始 IP 套接字上接收的数据包会从 `ip_len` 字段中减去 `ip_hl`。

在 FreeBSD 11.0 之前，在原始 IP 套接字上接收的数据包的 `ip_len` 和 `ip_off` 字段会被转换为主机字节序。写入原始 IP 套接字的数据包应具有主机字节序的 `ip_len` 和 `ip_off`。
