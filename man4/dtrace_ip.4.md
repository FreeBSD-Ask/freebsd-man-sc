# dtrace_ip.4

`dtrace_ip` — 用于跟踪 IPv4 和 IPv6 协议相关事件的 DTrace 提供者

## 名称

`dtrace_ip`

## 概要

`Fn ip:::receive pktinfo_t * csinfo_t * ipinfo_t * ifinfo_t * \ "ipv4info_t *" "ipv6info_t *" Fn ip:::send pktinfo_t * csinfo_t * ipinfo_t * ifinfo_t * \ "ipv4info_t *" "ipv6info_t *"`

## 描述

DTrace `ip` 提供者允许用户跟踪 [ip(4)](ip.4.md) 和 [ip6(4)](ip6.4.md) 协议实现中的事件。Fn ip:::send 探测在内核准备传输 IP 数据包时触发，Fn ip:::receive 探测在内核接收 IP 数据包时触发。这些探测的参数可用于获取相应数据包 IP 头的详细信息，以及发送或接收数据包的网络接口。与 [dtrace_tcp(4)](dtrace_tcp.4.md) 和 [dtrace_udp(4)](dtrace_udp.4.md) 提供者不同，`ip` 提供者的探测由转发的数据包触发。也就是说，探测将在非发往本地主机的数据包上触发。

## 参数

`pktinfo_t` 参数目前未实现，仅为与此提供者的其他实现兼容而包含。其字段为：

**`uintptr_t pkt_addr`** 始终设置为 0。

`csinfo_t` 参数目前未实现，仅为与此提供者的其他实现兼容而包含。其字段为：

**`uintptr_t cs_addr`** 始终设置为 0。

**`uint64_t cs_cid`** 指向此数据包的 `struct inpcb` 的指针，或 `NULL`。

**`pid_t cs_pid`** 始终设置为 0。

`ipinfo_t` 参数包含 IPv4 和 IPv6 数据包共有的 IP 字段。其字段为：

**`uint8_t ip_ver`** 数据包的 IP 版本，IPv4 数据包为 4，IPv6 数据包为 6。

**`uint32_t ip_plength`** IP 负载大小。不包括 IP 头或 IPv6 选项头的大小。

**`string ip_saddr`** IP 源地址。

**`string ip_daddr`** IP 目标地址。

`ifinfo_t` 参数分别描述 Fn ip:::send 和 Fn ip:::receive 探测中数据包的传出和传入接口。其字段为：

**`string if_name`** 接口名称。

**`int8_t if_local`** 指示接口是否为环回接口的布尔值。

**`uintptr_t if_addr`** 指向描述该接口的 `struct ifnet` 的指针。参见 [ifnet(9)](../man9/ifnet.9.md) 手册页。

`ipv4info_t` 参数包含 IPv4 数据包 IP 头的字段。对于 IPv6 数据包，此参数为 `NULL`。DTrace 脚本应使用 `ipinfo_t` 参数中的 Fn ip_ver 字段来确定是否使用此参数。其字段为：

**`uint8_t ipv4_ver`** IP 版本。对于 IPv4 数据包始终为 4。

**`uint8_t ipv4_ihl`** IP 头长度，包括选项，以 32 位字为单位。

**`uint8_t ipv4_tos`** IP 服务类型字段。

**`uint16_t ipv4_length`** 数据包总长度，包括头，以字节为单位。

**`uint16_t ipv4_ident`** 标识字段。

**`uint8_t ipv4_flags`** IP 标志。

**`uint16_t ipv4_offset`** 数据包的分片偏移量。

**`uint8_t ipv4_ttl`** 生存时间字段。

**`uint8_t ipv4_protocol`** 下一层协议 ID。

**`string ipv4_protostr`** 包含封装协议名称的字符串。协议字符串定义在 **/usr/lib/dtrace/ip.d** 中的 `protocol` 数组中

**`uint16_t ipv4_checksum`** IP 校验和。

**`ipaddr_t ipv4_src`** IPv4 源地址。

**`ipaddr_t ipv4_dst`** IPv4 目标地址。

**`string ipv4_saddr`** 源地址的字符串表示。

**`string ipv4_daddr`** 目标地址的字符串表示。

**`ipha_t *ipv4_hdr`** 指向原始 IPv4 头的指针。

`ipv6info_t` 参数包含 IPv6 数据包 IP 头的字段。对于 IPv4 数据包其字段未设置；与 `ipv4info_t` 参数一样，应使用 Fn ip_ver 字段确定此参数是否有效。其字段为：

**`uint8_t ipv6_ver`** IP 版本。对于 IPv6 数据包始终为 6。

**`uint8_t ipv6_tclass`** 流量类别，用于设置差异化服务代码点和扩展拥塞通知标志。

**`uint32_t ipv6_flow`** 数据包的流标签。

**`uint16_t ipv6_plen`** IP 负载大小，包括扩展头，以字节为单位。

**`uint8_t ipv6_nexthdr`** 下一头类型的标识符。

**`string ipv6_nextstr`** 下一头类型的字符串表示。

**`uint8_t ipv6_hlim`** 跳数限制。

**`ip6_addr_t *ipv6_src`** IPv6 源地址。

**`ip6_addr_t *ipv6_dst`** IPv6 目标地址。

**`string ipv6_saddr`** 源地址的字符串表示。

**`string ipv6_daddr`** 目标地址的字符串表示。

**`struct ip6_hdr *ipv6_hdr`** 指向原始 IPv6 头的指针。

## 文件

**`/usr/lib/dtrace/ip.d`** `ip` 提供者的 DTrace 类型和转换器定义。

## 实例

以下脚本按远程主机地址统计接收的数据包。

```sh
ip:::receive
{
        @num[args[2]->ip_saddr] = count();
}
```

此脚本将打印内核发送或接收的每个 IP 数据包的一些详细信息：

```sh
#pragma D option quiet
#pragma D option switchrate=10Hz
dtrace:::BEGIN
{
        printf(" %10s %30s    %-30s %8s %6sn", "DELTA(us)", "SOURCE",
            "DEST", "INT", "BYTES");
        last = timestamp;
}
ip:::send
{
        this->elapsed = (timestamp - last) / 1000;
        printf(" %10d %30s -> %-30s %8s %6dn", this->elapsed,
            args[2]->ip_saddr, args[2]->ip_daddr, args[3]->if_name,
            args[2]->ip_plength);
        last = timestamp;
}
ip:::receive
{
        this->elapsed = (timestamp - last) / 1000;
        printf(" %10d %30s <- %-30s %8s %6dn", this->elapsed,
            args[2]->ip_daddr, args[2]->ip_saddr, args[3]->if_name,
            args[2]->ip_plength);
        last = timestamp;
}
```

## 兼容性

此提供者与 Solaris 和 Darwin 中的 `ip` 提供者兼容。

## 参见

[dtrace(1)](../man1/dtrace.1.md), [dtrace_mib(4)](dtrace_mib.4.md), [dtrace_tcp(4)](dtrace_tcp.4.md), [dtrace_udp(4)](dtrace_udp.4.md), [ip(4)](ip.4.md), [ip6(4)](ip6.4.md), [ifnet(9)](../man9/ifnet.9.md), [SDT(9)](../man9/SDT.9.md)

## 历史

`ip` 提供者首次出现于 FreeBSD 10.0。

## 作者

本手册页由 Mark Johnston <markj@FreeBSD.org> 编写。
