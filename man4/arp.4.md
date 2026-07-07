# arp(4)

`arp` — 地址解析协议

## 名称

`arp`

## 概要

`device ether`

## 描述

地址解析协议（ARP）用于在协议地址（如 IP 地址）和本地网络地址（如以太网地址）之间动态映射。本实现将 IP 地址映射到以太网地址。所有以太网接口驱动程序都使用它。

ARP 缓存 Internet-以太网地址映射。当接口请求的映射不在缓存中时，ARP 会将需要该映射的消息排队，并在关联的网络上广播请求地址映射的消息。如果收到响应，新映射将被缓存，挂起的消息将被传输。ARP 在等待映射请求响应期间最多缓存 `net.link.ether.inet.maxhold` 个数据包；仅保留最近“传输”的数据包。如果目标主机在多次请求后未响应，则认为该主机已宕机，从而允许向传输尝试返回错误。对该映射的进一步需求会导致 ARP 请求重传，重传速率限制为每秒一个数据包。对于无响应的目标主机，错误为 `EHOSTDOWN`；对于无响应的路由器，错误为 `EHOSTUNREACH`。

ARP 缓存存储在每个接口的链路级表中。

可以使用 arp(8) 工具添加、删除或更改 ARP 条目。手动添加的条目可以是临时的或永久的，也可以是“发布的”，在这种情况下，系统会响应对该主机的 ARP 请求，就如同它是请求的目标一样。

过去，ARP 用于协商使用尾部封装。这不再受支持。

ARP 被动监视冒充本地主机的主机（即响应对本地主机地址的 ARP 映射请求的主机）。

代理 ARP 是一项功能，本地主机以自己的地址响应除自身以外的地址请求。通常，FreeBSD 中的代理 ARP 使用 arp(8) 工具按主机逐个设置，通过为给定子网内需要代理 ARP 请求的每个主机添加条目。但是，“proxy all”功能使本地主机充当通过某些其他网络接口（与请求进入的接口不同）可达的*所有*主机的代理。可以通过将 [sysctl(8)](../man8/sysctl.8.md) MIB 变量 `net.link.ether.inet.proxyall` 设置为 1 来启用。

## MIB 变量

ARP 协议在 [sysctl(3)](../man3/sysctl.3.md) MIB 的 `net.link.ether.inet` 分支中实现了许多可配置变量。

**`allow_multicast`** 安装硬件地址中设置了多播位的 ARP 条目。安装此类条目违反 RFC 1812，但某些专有负载均衡技术要求路由器这样做。默认关闭。

**`garp_rexmit_count`** 在向接口添加 IPv4 地址时重传无偿 ARP（GARP）数据包。当向接口添加 IPv4 地址时总是会传输一个 GARP。非零值会使 GARP 数据包重传指定的次数。每次重传间隔加倍，因此重传间隔为：{1, 2, 4, 8, 16, ...}（秒）。默认值零表示仅发送初始 GARP；不重传额外的 GARP 数据包。最大值为十六。单个 GARP 数据包的默认行为通常已足够。但是，单个 GARP 在某些情况下可能会被丢弃或丢失。当共享地址在集群节点之间传递时，这尤其有害。网络链路上的邻居随后可能会使用过期的 ARP 缓存工作，并将发往该地址的数据包发送给先前拥有该地址的节点，而该节点可能不会响应。

**`log_arp_movements`** 记录 IP 地址从一个硬件地址移动到另一个硬件地址。参见下文的“诊断”。默认开启。

**`log_arp_permanent_modify`** 记录远程主机尝试修改永久 ARP 条目。参见下文的“诊断”。默认开启。

**`log_arp_wrong_iface`** 记录在某个接口上插入 ARP 条目的尝试，而该地址所属的 IP 网络连接到另一个接口。参见下文的“诊断”。默认开启。

**`max_log_per_second`** 将远程触发的日志事件限制为每秒配置的次数。默认为每秒 1 条日志消息。

**`max_age`** ARP 条目在缓存中保留的时间，直到需要刷新。默认为 1200 秒。

**`maxhold`** 在条目解析期间保留在每个条目输出队列中的数据包数量。默认为 16 个数据包。

**`maxtries`** 在认为主机已宕机并返回错误之前的重传次数。默认为 5 次尝试。

**`proxyall`** 启用 ARP 代理。默认关闭。

**`wait`** 不完整 ARP 条目的生存期。默认为 20 秒。

## 诊断

- arp: %x:%x:%x:%x:%x:%x is using my IP address %d.%d.%d.%d on %s! ARP 已发现本地网络上的另一台主机响应对其自身 Internet 地址的映射请求时使用了不同的以太网地址，通常表示两台主机尝试使用相同的 Internet 地址。
- arp: link address is broadcast for IP address %d.%d.%d.%d! ARP 请求关于某主机的信息，并收到指示该主机的以太网地址为以太网广播地址的答复。这表示设备配置错误或损坏。
- arp: %d.%d.%d.%d moved from %x:%x:%x:%x:%x:%x to %x:%x:%x:%x:%x:%x on %s ARP 具有引用主机以太网地址的缓存值，但收到指示该主机位于新地址的回复。当主机硬件地址更改时，或当移动节点到达或离开本地子网时，这可以正常发生。它也可能表示代理 ARP 存在问题。仅当 sysctl `net.link.ether.inet.log_arp_movements` 设置为 1（系统的默认行为）时才会发出此消息。
- arpresolve: can't allocate llinfo for %d.%d.%d.%d 引用主机的路由指向需要 ARP 的设备，但 ARP 无法分配用于存储主机 MAC 地址的路由表条目。这通常指向配置错误的路由表。如果内核无法分配内存，也可能发生这种情况。
- arp: %d.%d.%d.%d is on if0 but got reply from %x:%x:%x:%x:%x:%x on if1 在 if0 和 if1 上都存在到同一逻辑 IP 网络的物理连接。如果上述 IP 地址的 ARP 缓存中已存在条目，并且电缆已从 if0 断开，然后重新连接到 if1，也可能发生这种情况。仅当 sysctl `net.link.ether.inet.log_arp_wrong_iface` 设置为 1（系统的默认行为）时才会发出此消息。
- arp: %x:%x:%x:%x:%x:%x attempts to modify permanent entry for %d.%d.%d.%d on %s ARP 收到尝试覆盖本地 ARP 表中永久条目的 ARP 回复。仅当 sysctl `net.link.ether.inet.log_arp_permanent_modify` 设置为 1（系统的默认行为）时才会记录此错误。
- arp: %x:%x:%x:%x:%x:%x is multicast 内核拒绝安装具有多播硬件地址的条目。如果确实要安装此类地址，请将 sysctl `net.link.ether.inet.allow_multicast` 设置为正值。

## 参见

[inet(4)](inet.4.md), [route(4)](route.4.md), arp(8), [ifconfig(8)](../man8/ifconfig.8.md), [route(8)](../man8/route.8.md), [sysctl(8)](../man8/sysctl.8.md)

> Plummer, D., "RFC826", *An Ethernet Address Resolution Protocol*.

> Leffler, S.J., Karels, M.J., "RFC893", *Trailer Encapsulations*.
