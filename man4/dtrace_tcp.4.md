# dtrace_tcp.4

`dtrace_tcp` — 用于跟踪与

## 名称

`dtrace_tcp` [tcp(4)](tcp.4.md) 协议相关事件的 DTrace 提供者

## 概要

`Fn tcp:::accept-established pktinfo_t * csinfo_t * ipinfo_t * \ "tcpsinfo_t *" "tcpinfo_t *" Fn tcp:::accept-refused pktinfo_t * csinfo_t * ipinfo_t * \ "tcpsinfo_t *" "tcpinfo_t *" Fn tcp:::connect-established pktinfo_t * csinfo_t * ipinfo_t * \ "tcpsinfo_t *" "tcpinfo_t *" Fn tcp:::connect-refused pktinfo_t * csinfo_t * ipinfo_t * \ "tcpsinfo_t *" "tcpinfo_t *" Fn tcp:::connect-request pktinfo_t * csinfo_t * ipinfo_t * \ "tcpsinfo_t *" "tcpinfo_t *" Fn tcp:::receive pktinfo_t * csinfo_t * ipinfo_t * tcpsinfo_t * \ "tcpinfo_t *" Fn tcp:::send pktinfo_t * csinfo_t * ipinfo_t * tcpsinfo_t * \ "tcpinfo_t *" Fn tcp:::state-change void * csinfo_t * void * tcpsinfo_t * void * \ "tcplsinfo_t *" Fn tcp:::siftr siftrinfo_t *`

## 描述

DTrace `tcp` 提供者允许用户跟踪 [tcp(4)](tcp.4.md) 协议实现中的事件。此提供者类似于 [dtrace_ip(4)](dtrace_ip.4.md) 和 [dtrace_udp(4)](dtrace_udp.4.md) 提供者，但还包含对应于比数据包接收和传输更高层级的协议事件的探测。除 Fn tcp:::state-change 和 Fn tcp:::siftr 外，所有 `tcp` 探测具有相同数量和类型的参数。最后三个参数用于描述 TCP 段：`ipinfo_t` 参数公开 IP 头的版本无关字段，`tcpinfo_t` 参数公开 TCP 头，`tcpsinfo_t` 参数描述相应 TCP 连接状态的详细信息（如果有）。其字段在参数节中描述。

Fn tcp:::accept-established 探测在远程发起的主动 TCP 打开成功时触发。此时新连接处于 ESTABLISHED 状态，探测参数公开与三次握手最终 ACK 关联的头。Fn tcp:::accept-refused 探测在 SYN 到达没有监听套接字的端口时触发。探测参数公开为响应 SYN 段而将传输到远程主机的 RST 关联的头。

Fn tcp:::connect-established、Fn tcp:::connect-refused 和 Fn tcp:::connect-request 探测类似于 `accept` 探测，但它们对应于本地发起的 TCP 连接。Fn tcp:::connect-established 探测在从远程主机接收到三次握手的 SYN-ACK 段并准备传输最终 ACK 时触发。这发生在本地连接状态从 SYN-SENT 转换到 ESTABLISHED 之后立即。探测参数描述与接收到的 SYN-ACK 段关联的头。Fn tcp:::connect-refused 探测在本地主机收到 RST 段以响应 SYN 段时触发，表示远程主机拒绝打开连接。探测参数描述与接收到的 RST 段关联的 IP 和 TCP 头。Fn tcp:::connect-request 探测在内核准备传输三次握手的初始 SYN 段时触发。

Fn tcp:::send 和 Fn tcp:::receive 探测分别在主机发送或接收 TCP 数据包时触发。与 [dtrace_udp(4)](dtrace_udp.4.md) 提供者一样，`tcp` 探测仅对本地主机发送或接收的数据包触发；转发的数据包在 IP 层处理，仅对 [dtrace_ip(4)](dtrace_ip.4.md) 提供者可见。

Fn tcp:::state-change 探测在本地 TCP 连接状态转换时触发。其第一、第三和第五个参数当前始终为 `NULL`。其最后一个参数描述转换中的源状态，目标状态可从 `args[3]->tcps_state` 获取。

Fn tcp:::siftr 探测在主机发送或接收 TCP 段时触发。详细描述见 [siftr(4)](siftr.4.md)。`siftrinfo_t` 参数提供有关 TCP 连接的信息。

## 参数

`pktinfo_t` 参数目前未实现，仅为与此提供者的其他实现兼容而包含。其字段为：

**`uinptr_t pkt_addr`** 始终设置为 0。

`csinfo_t` 参数目前未实现，仅为与此提供者的其他实现兼容而包含。其字段为：

**`uintptr_t cs_addr`** 始终设置为 0。

**`uint64_t cs_cid`** 指向此数据包的 `struct inpcb` 的指针，或 `NULL`。

**`pid_t cs_pid`** 始终设置为 0。

`ipinfo_t` 类型是 IP 头字段的版本无关表示。其字段在 [dtrace_ip(4)](dtrace_ip.4.md) 手册页中描述。

`tcpsinfo_t` 类型用于提供 TCP 连接状态的稳定表示。某些 `tcp` 探测（如 Fn tcp:::accept-refused）在没有 TCP 连接的上下文中触发；在这种情况下此参数为 `NULL`。其字段为：

**`uintptr_t tcps_addr`** 相应 TCP 控制块的地址。当前是指向 `struct tcpcb` 的指针。

**`int tcps_local`** 指示连接是否为本地主机的布尔值。目前未实现，始终设置为 -1。

**`int tcps_active`** 指示连接是否由本地主机发起的布尔值。目前未实现，始终设置为 -1。

**`uint16_t tcps_lport`** 本地 TCP 端口。

**`uint16_t tcps_rport`** 远程 TCP 端口。

**`string tcps_laddr`** 本地地址。

**`string tcps_raddr`** 远程地址。

**`int32_t tcps_state`** 当前 TCP 状态。有效的 TCP 状态值由 **/usr/lib/dtrace/tcp.d** 中以 `TCPS_` 为前缀的常量给出。

**`uint32_t tcps_iss`** 初始发送序列号。

**`uint32_t tcps_suna`** 已发送但未确认数据的初始序列号。

**`uint32_t tcps_snxt`** 下一个发送序列号。

**`uint32_t tcps_rack`** 已接收并确认数据的序列号。

**`uint32_t tcps_rnxt`** 下一个预期接收序列号。

**`u_long tcps_swnd`** TCP 发送窗口大小。

**`int32_t tcps_snd_ws`** TCP 发送窗口的窗口缩放因子。

**`u_long tcps_rwnd`** TCP 接收窗口大小。

**`int32_t tcps_rcv_ws`** TCP 接收窗口的窗口缩放因子。

**`u_long tcps_cwnd`** TCP 拥塞窗口大小。

**`u_long tcps_cwnd_ssthresh`** 慢启动结束和拥塞避免开始的拥塞窗口阈值。

**`uint32_t tcps_sack_fack`** 接收方选择性确认的最后序列号。

**`uint32_t tcps_sack_snxt`** 开始重传的下一个选择性确认序列号。

**`uint32_t tcps_rto`** 往返超时，以毫秒为单位。

**`uint32_t tcps_mss`** 最大段大小。

**`int tcps_retransmit`** 指示本地发送方正重传数据的布尔值。

**`int tcps_srtt`** 平滑往返时间。

`tcpinfo_t` 类型以主机字节序公开 TCP 段头中的字段。其字段为：

**`uint16_t tcp_sport`** 源 TCP 端口。

**`uint16_t tcp_dport`** 目标 TCP 端口。

**`uint32_t tcp_seq`** 序列号。

**`uint32_t tcp_ack`** 确认号。

**`uint8_t tcp_offset`** 数据偏移量，以字节为单位。

**`uint8_t tcp_flags`** TCP 标志。

**`uint16_t tcp_window`** TCP 窗口大小。

**`uint16_t tcp_checksum`** 校验和。

**`uint16_t tcp_urgent`** 紧急数据指针。

**`struct tcphdr *tcp_hdr`** 指向原始 TCP 头的指针。

`tcplsinfo_t` 类型由 Fn tcp:::state-change 探测用于提供转换的源状态。其字段为：

**`int32_t tcps_state`** TCP 状态。有效的 TCP 状态值由 **/usr/lib/dtrace/tcp.d** 中以 `TCPS_` 为前缀的常量给出。

`siftrinfo_t` 类型由 Fn tcp:::siftr 探测用于提供 TCP 连接的状态。其字段为：

**`uint8_t direction`** 触发日志消息的数据包方向。"0" 表示入，"1" 表示出。

**`uint8_t ipver`** 使用的 IP 协议版本。"1" 表示 IPv4，"2" 表示 IPv6。

**`uint16_t lport`** 本地主机通信所用的 TCP 端口。

**`uint16_t rport`** 远程主机通信所用的 TCP 端口。

**`string laddr`** 本地主机的 IPv4 或 IPv6 地址。

**`string raddr`** 远程主机的 IPv4 或 IPv6 地址。

**`uint32_t snd_cwnd`** 流的当前拥塞窗口（CWND），以字节为单位。

**`uint32_t snd_wnd`** 流的当前发送窗口，以字节为单位。报告缩放后的值，但在初始握手（前几个数据包）期间报告未缩放的值。

**`uint32_t rcv_wnd`** 流的当前接收窗口，以字节为单位。始终报告缩放后的值。

**`uint32_t t_flags2`** 流的 t_flags2 的当前值。

**`uint32_t snd_ssthresh`** 流的慢启动阈值（SSTHRESH），以字节为单位。

**`int conn_state`** TCP 状态。有效的 TCP 状态值由 **/usr/lib/dtrace/tcp.d** 中以 `TCPS_` 为前缀的常量给出。

**`uint32_t mss`** 流的最大段大小（MSS），以字节为单位。

**`uint32_t srtt`** 流的当前平滑 RTT（SRTT），以微秒为单位。

**`u_char sack_enabled`** SACK 启用指示符。1 表示启用 SACK，0 表示未启用。

**`u_char snd_scale`** 发送窗口的当前窗口缩放因子。

**`u_char rcv_scale`** 接收窗口的当前窗口缩放因子。

**`u_int t_flags`** 流的 t_flags 的当前值。

**`uint32_t rto`** 流的当前重传超时（RTO），以微秒为单位。除以 HZ 可得以秒为单位的超时长度。

**`u_int snd_buf_hiwater`** 套接字发送缓冲区的当前大小，以字节为单位。

**`u_int snd_buf_cc`** 套接字发送缓冲区中的当前字节数。

**`u_int rcv_buf_hiwater`** 套接字接收缓冲区的当前大小，以字节为单位。

**`u_int rcv_buf_cc`** 套接字接收缓冲区中的当前字节数。

**`u_int sent_inflight_bytes`** 当前未确认的在途字节数。通过 SACK 确认的字节不从此计数中排除。

**`int t_segqlen`** 重组队列中的当前段数。

**`u_int flowid`** 连接的 Flowid。注意事项：零 '0' 可能表示有效的 flowid 或未设置 flowid 时的默认值。

**`u_int flowtype`** 连接的流类型。Flowtype 定义了哪些协议字段被哈希以产生 flowid。完整列表可在 **/usr/include/sys/mbuf.h** 中的 `M_HASHTYPE_*` 下找到。

## 文件

**`/usr/lib/dtrace/tcp.d`** `tcp` 提供者除 `siftr` 探测外所有探测的 DTrace 类型和转换器定义。
**`/usr/lib/dtrace/siftr.d`** `tcp` 提供者 `siftr` 探测的 DTrace 类型和转换器定义。

## 实例

以下脚本实时记录 TCP 段：

```sh
#pragma D option quiet
#pragma D option switchrate=10hz
dtrace:::BEGIN
{
        printf(" %3s %15s:%-5s      %15s:%-5s %6s  %sn", "CPU",
            "LADDR", "LPORT", "RADDR", "RPORT", "BYTES", "FLAGS");
}
tcp:::send
{
        this->length = args[2]->ip_plength - args[4]->tcp_offset;
        printf(" %3d %16s:%-5d -> %16s:%-5d %6d  (", cpu, args[2]->ip_saddr,
            args[4]->tcp_sport, args[2]->ip_daddr, args[4]->tcp_dport,
            this->length);
        printf("%s", args[4]->tcp_flags & TH_FIN ? "FIN|" : "");
        printf("%s", args[4]->tcp_flags & TH_SYN ? "SYN|" : "");
        printf("%s", args[4]->tcp_flags & TH_RST ? "RST|" : "");
        printf("%s", args[4]->tcp_flags & TH_PUSH ? "PUSH|" : "");
        printf("%s", args[4]->tcp_flags & TH_ACK ? "ACK|" : "");
        printf("%s", args[4]->tcp_flags & TH_URG ? "URG|" : "");
        printf("%s", args[4]->tcp_flags == 0 ? "null " : "");
        printf("b)n");
}
tcp:::receive
{
        this->length = args[2]->ip_plength - args[4]->tcp_offset;
        printf(" %3d %16s:%-5d <- %16s:%-5d %6d  (", cpu,
            args[2]->ip_daddr, args[4]->tcp_dport, args[2]->ip_saddr,
            args[4]->tcp_sport, this->length);
        printf("%s", args[4]->tcp_flags & TH_FIN ? "FIN|" : "");
        printf("%s", args[4]->tcp_flags & TH_SYN ? "SYN|" : "");
        printf("%s", args[4]->tcp_flags & TH_RST ? "RST|" : "");
        printf("%s", args[4]->tcp_flags & TH_PUSH ? "PUSH|" : "");
        printf("%s", args[4]->tcp_flags & TH_ACK ? "ACK|" : "");
        printf("%s", args[4]->tcp_flags & TH_URG ? "URG|" : "");
        printf("%s", args[4]->tcp_flags == 0 ? "null " : "");
        printf("b)n");
}
```

以下脚本在 TCP 连接状态变化发生时记录：

```sh
#pragma D option quiet
#pragma D option switchrate=25hz
int last[int];
dtrace:::BEGIN
{
        printf("   %12s %-20s    %-20s %sn",
            "DELTA(us)", "OLD", "NEW", "TIMESTAMP");
}
tcp:::state-change
{
        this->elapsed = (timestamp - last[args[1]->cs_cid]) / 1000;
        printf("   %12d %-20s -> %-20s %dn", this->elapsed,
            tcp_state_string[args[5]->tcps_state],
            tcp_state_string[args[3]->tcps_state], timestamp);
        last[args[1]->cs_cid] = timestamp;
}
tcp:::state-change
/last[args[1]->cs_cid] == 0/
{
        printf("   %12s %-20s -> %-20s %dn", "-",
            tcp_state_string[args[5]->tcps_state],
            tcp_state_string[args[3]->tcps_state], timestamp);
        last[args[1]->cs_cid] = timestamp;
}
```

以下脚本使用 siftr 探测在发送或接收数据包时显示 CWND 和 SSTHRESH 的当前值：

```sh
#pragma D option quiet
#pragma D option switchrate=10hz
dtrace:::BEGIN
{
        printf(" %3s %16s:%-5s %16s:%-5s %10s %10sn",
            "DIR", "LADDR", "LPORT", "RADDR", "RPORT", "CWND", "SSTHRESH");
}
tcp:::siftr
{
        printf(" %3s %16s:%-5d %16s:%-5d %10u %10un",
            siftr_dir_string[args[0]->direction],
            args[0]->laddr, args[0]->lport, args[0]->raddr, args[0]->rport,
            args[0]->snd_cwnd, args[0]->snd_ssthresh);
}
```

## 兼容性

此提供者与 Solaris 中的 `tcp` 提供者兼容。

## 参见

[dtrace(1)](../man1/dtrace.1.md), [dtrace_ip(4)](dtrace_ip.4.md), [dtrace_mib(4)](dtrace_mib.4.md), [dtrace_sctp(4)](dtrace_sctp.4.md), [dtrace_udp(4)](dtrace_udp.4.md), [dtrace_udplite(4)](dtrace_udplite.4.md), [siftr(4)](siftr.4.md), [tcp(4)](tcp.4.md), [SDT(9)](../man9/SDT.9.md)

## 历史

`tcp` 提供者首次出现于 FreeBSD 10.0。

## 作者

本手册页由 Mark Johnston <markj@FreeBSD.org> 编写。

## 缺陷

`tcpsinfo_t` 的 `tcps_local` 和 `tcps_active` 字段未由转换器填充。
