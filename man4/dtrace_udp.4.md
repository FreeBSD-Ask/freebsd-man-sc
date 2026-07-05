# dtrace_udp.4

`dtrace_udp` — 用于跟踪与 UDP 协议相关事件的 DTrace provider

## 名称

`dtrace_udp`

## 概要

`Fn udp:::receive pktinfo_t * csinfo_t * ipinfo_t * udpsinfo_t * \ "udpinfo_t *" Fn udp:::send pktinfo_t * csinfo_t * ipinfo_t * udpsinfo_t * \ "udpinfo_t *"`

## 描述

DTrace `udp` provider 允许用户跟踪 [udp(4)](udp.4.md) 协议实现中的事件。`Fn udp:::send` 探针在内核准备传输 UDP 数据包时触发，`Fn udp:::receive` 探针在内核收到 UDP 数据包时触发，但若 UDP 头不完整、目标端口为 0、长度字段无效或校验和错误则不会触发。这些探针的参数可用于获取相应数据包 IP 和 UDP 头的详细信息。

## 参数

`pktinfo_t` 参数目前未实现，仅为与本 provider 的其他实现兼容而保留。其字段为：

**`uintptr_t pkt_addr`** 始终设为 0。

`csinfo_t` 参数目前未实现，仅为与本 provider 的其他实现兼容而保留。其字段为：

**`uintptr_t cs_addr`** 始终设为 0。

**`uint64_t cs_cid`** 指向该数据包对应的 `struct inpcb` 的指针，或为 `NULL`。

**`pid_t cs_pid`** 始终设为 0。

`ipinfo_t` 参数包含 IPv4 和 IPv6 数据包共有的 IP 字段。其字段为：

**`uint8_t ip_ver`** 数据包的 IP 版本，IPv4 数据包为 4，IPv6 数据包为 6。

**`uint32_t ip_plength`** IP 负载大小。不包括 IP 头或 IPv6 选项头的大小。

**`string ip_saddr`** IP 源地址。

**`string ip_daddr`** IP 目标地址。

`udpsinfo_t` 参数包含与该数据包关联的 UDP 连接状态。其字段为：

**`uintptr_t udps_addr`** 指向包含关联 socket IP 状态的 `struct inpcb` 的指针。

**`uint16_t udps_lport`** 本地 UDP 端口。

**`uint16_t udps_rport`** 远程 UDP 端口。

**`string udps_laddr`** 本地 IPv4 或 IPv6 地址。

**`string udps_raddr`** 远程 IPv4 或 IPv6 地址。

`udpinfo_t` 参数是数据包的原始 UDP 头，所有字段均为主机字节序。其字段为：

**`uint16_t udp_sport`** 源 UDP 端口。

**`uint16_t udp_dport`** 目标 UDP 端口。

**`uint16_t udp_length`** UDP 头和负载的长度，以字节为单位。

**`uint16_t udp_checksum`** UDP 头和负载的校验和，若未计算校验和则为 0。

**`struct udphdr *udp_hdr`** 指向原始 UDP 头的指针。

## 文件

**`/usr/lib/dtrace/udp.d`** `udp` provider 的 DTrace 类型和转换器定义。

## 实例

以下脚本按目标端口统计已传输的数据包：

```sh
udp:::send
{
        @num[args[4]->udp_dport] = count();
}
```

此脚本将打印内核发送或接收的每个 UDP 数据包的部分详细信息：

```sh
#pragma D option quiet
#pragma D option switchrate=10Hz
dtrace:::BEGIN
{
        printf(" %10s %36s    %-36s %6sn", "DELTA(us)", "SOURCE",
            "DEST", "BYTES");
        last = timestamp;
}
udp:::send
{
        this->elapsed = (timestamp - last) / 1000;
        self->dest = strjoin(strjoin(args[2]->ip_daddr, ":"),
             lltostr(args[4]->udp_dport));
        printf(" %10d %30s:%-5d -> %-36s %6dn", this->elapsed,
            args[2]->ip_saddr, args[4]->udp_sport,
            self->dest, args[4]->udp_length);
        last = timestamp;
}
udp:::receive
{
        this->elapsed = (timestamp - last) / 1000;
        self->dest = strjoin(strjoin(args[2]->ip_saddr, ":"),
             lltostr(args[4]->udp_sport));
        printf(" %10d %30s:%-5d <- %-36s %6dn", this->elapsed,
            args[2]->ip_daddr, args[4]->udp_dport,
            self->dest, args[4]->udp_length);
        last = timestamp;
}
```

## 兼容性

该 provider 与 Solaris 中的 `udp` provider 兼容。

## 参见

[dtrace(1)](../man1/dtrace.1.md), [dtrace_ip(4)](dtrace_ip.4.md), [dtrace_sctp(4)](dtrace_sctp.4.md), [dtrace_tcp(4)](dtrace_tcp.4.md), [dtrace_udplite(4)](dtrace_udplite.4.md), [udp(4)](udp.4.md), [SDT(9)](../man9/SDT.9.md)

## 历史

`udp` provider 首次出现于 FreeBSD 10.0。

## 作者

本手册页由 Mark Johnston <markj@FreeBSD.org> 编写。
