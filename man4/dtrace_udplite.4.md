# dtrace_udplite(4)

`dtrace_udplite` — 用于跟踪与 UDP-Lite 协议相关事件的 DTrace 提供者

## 名称

`dtrace_udplite`

## 概要

`Fn udplite:::receive pktinfo_t * csinfo_t * ipinfo_t * udplitesinfo_t * \ "udpliteinfo_t *" Fn udplite:::send pktinfo_t * csinfo_t * ipinfo_t * udplitesinfo_t * \ "udpliteinfo_t *"`

## 描述

DTrace `udplite` 提供者允许用户跟踪 [udplite(4)](udplite.4.md) 协议实现中的事件。Fn udplite:::send 探测在内核准备传输 UDP-Lite 数据包时触发，Fn udplite:::receive 探测在内核接收到 UDP-Lite 数据包时触发；但当 UDP-Lite 头不完整、目标端口为 0、长度字段无效或校验和错误时，该探测不会触发。这些探测的参数可用于获取相应数据包 IP 和 UDP-Lite 头的详细信息。

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

`udplitesinfo_t` 参数包含与该数据包关联的 UDP-Lite 连接的状态。其字段为：

**`uintptr_t udplites_addr`** 指向包含关联套接字 IP 状态的 `struct inpcb` 的指针。

**`uint16_t udplites_lport`** 本地 UDP-Lite 端口。

**`uint16_t udplites_rport`** 远程 UDP-Lite 端口。

**`string udplites_laddr`** 本地 IPv4 或 IPv6 地址。

**`string udplites_raddr`** 远程 IPv4 或 IPv6 地址。

`udpliteinfo_t` 参数为数据包的原始 UDP-Lite 头，所有字段均为主机字节序。其字段为：

**`uint16_t udplite_sport`** 源 UDP-Lite 端口。

**`uint16_t udplite_dport`** 目标 UDP-Lite 端口。

**`uint16_t udplite_coverage`** UDP-Lite 头的校验和覆盖范围，以字节为单位，或为 0 表示完全覆盖。

**`uint16_t udplite_checksum`** UDP-Lite 头和负载的校验和，若未计算校验和则为 0。

**`struct udplitehdr *udplite_hdr`** 指向原始 UDP-Lite 头的指针。

## 文件

**`/usr/lib/dtrace/udplite.d`** `udplite` 提供者的 DTrace 类型和转换器定义。

## 实例

以下脚本按目标端口对已传输数据包进行计数。

```sh
udplite:::send
{
        @num[args[4]->udplite_dport] = count();
}
```

此脚本在内核发送或接收每个 UDP-Lite 数据包时打印一些详细信息：

```sh
#pragma D option quiet
#pragma D option switchrate=10Hz
dtrace:::BEGIN
{
        printf(" %10s %36s    %-36s %6sn", "DELTA(us)", "SOURCE",
            "DEST", "COV");
        last = timestamp;
}
udplite:::send
{
        this->elapsed = (timestamp - last) / 1000;
        self->dest = strjoin(strjoin(args[2]->ip_daddr, ":"),
             lltostr(args[4]->udplite_dport));
        printf(" %10d %30s:%-5d -> %-36s %6dn", this->elapsed,
            args[2]->ip_saddr, args[4]->udplite_sport,
            self->dest, args[4]->udplite_coverage);
        last = timestamp;
}
udplite:::receive
{
        this->elapsed = (timestamp - last) / 1000;
        self->dest = strjoin(strjoin(args[2]->ip_saddr, ":"),
             lltostr(args[4]->udplite_sport));
        printf(" %10d %30s:%-5d <- %-36s %6dn", this->elapsed,
            args[2]->ip_daddr, args[4]->udplite_dport,
            self->dest, args[4]->udplite_coverage);
        last = timestamp;
}
```

## 参见

[dtrace(1)](../man1/dtrace.1.md), [dtrace_ip(4)](dtrace_ip.4.md), [dtrace_sctp(4)](dtrace_sctp.4.md), [dtrace_tcp(4)](dtrace_tcp.4.md), [dtrace_udp(4)](dtrace_udp.4.md), [udplite(4)](udplite.4.md), [SDT(9)](../man9/sdt.9.md)

## 历史

`udplite` 提供者首次出现于 FreeBSD 12.0。

## 作者

本手册页由 Mark Johnston <markj@FreeBSD.org> 和 Michael Tuexen <tuexen@FreeBSD.org> 编写。
