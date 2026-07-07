# inet(4)

`inet` — Internet 协议族

## 名称

`inet`

## 概要

`#include <sys/types.h>`

`#include <netinet/in.h>`

## 描述

Internet 协议族是一组叠加在 *Internet Protocol*（IP）传输层之上并使用 Internet 地址格式的协议集合。Internet 协议族为 `SOCK_STREAM`、`SOCK_DGRAM` 和 `SOCK_RAW` 套接字类型提供协议支持；`SOCK_RAW` 接口提供对 IP 协议的访问。

## 寻址

Internet 地址为四字节数据，按网络标准格式存储（在小端机器上，例如 alpha、amd64 和 i386，这些字节的字与字节顺序均反转）。头文件

`#include <netinet/in.h>`

将该地址定义为判别联合。

绑定到 Internet 协议族的套接字使用以下寻址结构：

```sh
struct sockaddr_in {
	uint8_t		sin_len;
	sa_family_t	sin_family;
	in_port_t	sin_port;
	struct in_addr	sin_addr;
	char		sin_zero[8];
};
```

可使用本地地址 `INADDR_ANY` 创建套接字，以对进入的消息实现“通配”匹配。在 connect(2) 或 sendto(2) 调用中，地址可指定为 `INADDR_ANY`，意为“本主机”。如果首个配置的网络支持广播，则可使用特殊地址 `INADDR_BROADCAST` 作为主网络上广播地址的简写。

## 协议

Internet 协议族由 IP 网络协议、Internet 控制报文协议（ICMP）、Internet 组管理协议（IGMP）、传输控制协议（TCP）和用户数据报协议（UDP）组成。TCP 用于支持 `SOCK_STREAM` 抽象，UDP 用于支持 `SOCK_DGRAM` 抽象。可通过创建 `SOCK_RAW` 类型的 Internet 套接字获得 IP 的原始接口。可通过原始套接字访问 ICMP 报文协议。

接口上的 `inet` 地址由地址本身、网络掩码、广播接口情况下的广播地址或点到点接口情况下的对端地址组成。Internet 域中的数据报套接字支持以下 ioctl(2) 命令：

**`SIOCAIFADDR`** 向接口添加地址。该命令以 `struct in_aliasreq` 作为参数。

**`SIOCDIFADDR`** 从接口删除地址。该命令以 `struct ifreq` 作为参数。

**`SIOCGIFADDR`**

**`SIOCGIFBRDADDR`**

**`SIOCGIFDSTADDR`**

**`SIOCGIFNETMASK`** 从接口返回地址信息。返回值位于 `struct ifreq` 中。这种地址信息检索方式已过时，推荐使用 getifaddrs(3) API。

### MIB（sysctl）变量

除了 `net.inet` 中传输协议所支持的变量（请参阅相应手册页）之外，在 sysctl(3) MIB 的 `net.inet.ip` 分支中还实现了若干通用变量，也可通过 [sysctl(8)](../man8/sysctl.8.md) 读取或修改。定义了以下通用变量：

**`accept_sourceroute`** 布尔值：启用/禁用接收源路由 IP 数据包（默认为 false）。

**`allow_net0`** 布尔值：允许转发地址在 0.0.0.0/8 范围内的数据包，并允许对其回复 ICMP。

**`allow_net240`** 布尔值：允许转发地址在 240.0.0.0/4 范围内的数据包，并允许对其回复 ICMP。

**`curfrags`** 整数：所有 VNET 中所有重组队列中 IPv4 分片的当前数量（只读）。

**`forwarding`** 布尔值：启用/禁用 IP 数据包转发。默认为关闭。

**`fragpackets`** 整数：该 VNET 中 IPv4 分片重组队列条目的当前数量（只读）。

**`fragttl`** 整数：每个 VNET 重组队列中 IPv4 数据包分片的存活时间。

**`loopback_prefixlen`** 整数：为环回用途保留的地址空间的前缀长度。默认为 8，即 127.0.0.0/8 保留给环回，不能在非环回接口上发送、接收或转发。使用其他值属于试验性操作。

**`maxfragbucketsize`** 整数：每个桶中重组队列的最大数量。分片数据包被哈希到桶中。每个桶包含一个重组队列列表。系统必须将进入的数据包与桶中现有的重组队列进行比较，以找到匹配的重组队列。为节省系统资源，系统限制每个桶中允许的重组队列数量。当 mbuf cluster 数量变化或 `maxfragpackets` 的值变化时，会重新计算此限制。这是每 VNET 限制。

**`maxfragpackets`** 整数：主机为特定 VNET 接受并同时保留在重组队列中的分片数据包的最大数量。0 表示该主机不为该 VNET 接受任何分片数据包。-1 表示主机不为该 VNET 应用此限制。当 mbuf cluster 数量变化时，会重新计算此限制。这是每 VNET 限制。

**`maxfrags`** 整数：主机在所有 VNET 中所有重组队列中接受并同时保留的分片的最大数量。设为 0 则禁用重组。设为 -1 则不应用此限制。当 mbuf cluster 数量变化时，会重新计算此限制。这是全局限制。

**`maxfragsperpacket`** 整数：主机为单个数据包接受并保留在重组队列中的分片的最大数量。0 表示主机不为该 VNET 接受任何分片数据包。这是每 VNET 限制。

**`mcast`** `net.inet.ip.mcast` 节点下的变量在 [ip(4)](ip.4.md) 中说明。

**`no_same_prefix`** 布尔值：拒绝在不同接口上创建相同前缀。这是每 VNET 值。

**`portrange`** `net.inet.ip.portrange` 节点下的变量控制传输协议使用的端口范围；详见 [ip(4)](ip.4.md)。

**`process_options`** 整数：控制 IP 选项处理。将此变量设为 0 时，进入数据包中的所有 IP 选项将被忽略，数据包将不加修改地传递。设为 1 时，进入数据包中的 IP 选项将相应地处理。设为 2 时，将向带 IP 选项的进入数据包回复 ICMP“prohibited by filter”消息。默认为 1。此 [sysctl(8)](../man8/sysctl.8.md) 变量既影响发往本机的数据包，也影响转发至其他主机的数据包。

**`random_id`** 布尔值：控制 IP ID 生成行为。将此 [sysctl(8)](../man8/sysctl.8.md) 设为 1 会导致*非原子* IP 数据报（或在禁用 `rfc6864` 时的所有 IP 数据报）中的 ID 字段随机化，而非每生成一个数据包递增 1。这关闭了一个轻微的信息泄漏，使远程观察者无法通过观察计数器来确定机器上数据包生成的速率。同时，在高速链路上，这可能大幅缩短 ID 重用周期。默认为 0（顺序 IP ID）。IPv6 flow ID 和分片 ID 始终是随机的。

**`random_id_collisions`** 整数：IP ID 冲突计数（只读，每 VNET）。

**`random_id_period`** 整数：IP ID 数组的大小，即为其记录 ID 的先前数据包数量。该数字必须在 512 到 32768 之间（含）。这是每 VNET 值。

**`random_id_total`** 整数：已创建的 IP ID 计数（只读，每 VNET）。

**`reass_hashsize`** IPv4 重组队列中的哈希槽数量（loader 可调参数）。

**`redirect`** 布尔值：启用/禁用对已知存在更佳且发送方可直接到达的路由和下一跳的 IP 数据包发送 ICMP 重定向。默认为开启。

**`rfc1122_strong_es`** 布尔值：在非转发模式（转发已禁用）下，按 RFC1122 部分实现强端系统模型。如果目的地为本地的数据包到达的接口与地址所属接口不同，该数据包将被静默丢弃。启用此选项可能破坏某些配置，例如在环回上具有预期可由外部流量访问的别名地址。启用某些其他网络功能（例如 [carp(4)](carp.4.md) 或目标地址重写 pfil(4) 过滤器）可能覆盖并绕过此检查。默认禁用。

**`rfc6864`** 布尔值：控制 IP ID 生成行为。为 true 时启用 RFC6864 支持，该规范规定*原子*数据报的 IP ID 字段可设置为任意值。FreeBSD 实现默认启用。

**`source_address_validation`** 布尔值：对发往本地主机的数据包执行源地址验证。可视为遵循 RFC3704/BCP84 第 3.2 节，将本地主机视为我们自己的基础设施。转发的数据包不受此影响，因此不应将其视为路由器的反欺骗功能。默认启用。

**`sourceroute`** 布尔值：启用/禁用源路由 IP 数据包的转发（默认为 false）。

**`ttl`** 整数：用于外出 IP 数据包的默认生存时间（“TTL”）。

## 参见

ioctl(2), socket(2), getifaddrs(3), sysctl(3), [icmp(4)](icmp.4.md), [intro(4)](intro.4.md), [ip(4)](ip.4.md), [ipfirewall(4)](ipfirewall.4.md), [route(4)](route.4.md), [tcp(4)](tcp.4.md), [udp(4)](udp.4.md), [sysctl(8)](../man8/sysctl.8.md), [pfil(9)](../man9/pfil.9.md)

> "An Introductory 4.3 BSD Interprocess Communication Tutorial", *PS1*, 7.

> "An Advanced 4.3 BSD Interprocess Communication Tutorial", *PS1*, 8.

## 历史

`inet` 协议接口出现于 4.2BSD。“协议克隆”代码出现于 FreeBSD 2.1。

## 注意事项

Internet 协议支持会随着 Internet 协议的发展而变化。用户不应依赖当前实现的细节，而应依赖其导出的服务。
