# dtrace_sctp(4)

`dtrace_sctp` — 用于跟踪与

## 名称

`dtrace_sctp` [sctp(4)](sctp.4.md) 协议相关事件的 DTrace 提供者

## 概要

`Fn sctp:cwnd::init uint32_t uint32_t uintptr_t int int Fn sctp:cwnd::ack uint32_t uint32_t uintptr_t int int Fn sctp:cwnd::rttvar uint64_t uint64_t uint64_t uint64_t uint64_t Fn sctp:cwnd::rttstep uint64_t uint64_t uint64_t uint64_t uint64_t Fn sctp:cwnd::fr uint32_t uint32_t uintptr_t int int Fn sctp:cwnd::to uint32_t uint32_t uintptr_t int int Fn sctp:cwnd::bl uint32_t uint32_t uintptr_t int int Fn sctp:cwnd::ecn uint32_t uint32_t uintptr_t int int Fn sctp:cwnd::pd uint32_t uint32_t uintptr_t int int Fn sctp:rwnd:assoc:val uint32_t uint32_t int int Fn sctp:flightsize:net:val uint32_t uint32_t uintptr_t int int Fn sctp:flightsize:assoc:val uint32_t uint32_t int int Fn sctp:::receive pktinfo_t * csinfo_t * ipinfo_t * sctpsinfo_t * \ "sctpinfo_t *" Fn sctp:::send pktinfo_t * csinfo_t * ipinfo_t * sctpsinfo_t * \ "sctpinfo_t *" Fn sctp:::state-change void * csinfo_t * void * sctpsinfo_t * \ "void *" "sctplsinfo_t *"`

## 描述

DTrace `sctp` 提供者允许用户跟踪 [sctp(4)](sctp.4.md) 协议实现中的事件。此提供者类似于 [dtrace_ip(4)](dtrace_ip.4.md) 和 [dtrace_udp(4)](dtrace_udp.4.md) 提供者，但还包含对应于比数据包接收和传输更高层级的协议事件的探测。

Fn sctp:cwnd:: 探测跟踪 netp 上拥塞窗口的变化。Fn sctp:rwnd:: 探测跟踪 assoc 上接收窗口的变化。Fn sctp:flightsize:net:val 探测跟踪 net 或 assoc 上在途数据量的变化，Fn sctp:flightsize:assoc:val 探测提供总在途数据版本。

除 Fn sctp:cwnd::rtt* 和 Fn sctp::assoc:val 外，所有 `sctp` 探测的参数为：本端的 Vtag、本端端口号、指向 `struct sctp_nets *changing` 的指针、cwnd 的旧值以及 cwnd 的新值。

Fn sctp:::val 的参数与上述类似，区别在于第四个参数为增减量。

Fn sctp:cwnd::rtt* 探测的参数为：`Vtag << 32 | localport << 16 | remoteport` 位图、`obw | nbw` 位图、`bwrtt | newrtt` 位图、`flight`，以及 `(cwnd << 32) | point << 16 | retval(0/1)` 位图。

Fn sctp:cwnd::init 探测在远程发起的主动 SCTP 打开成功时触发。此时新连接处于 ESTABLISHED 状态，探测参数公开与四次握手最终 ACK 关联的头。

Fn sctp:::send 和 Fn sctp:::receive 探测分别在主机发送或接收 SCTP 数据包时触发。与 [dtrace_udp(4)](dtrace_udp.4.md) 提供者一样，`sctp` 探测仅对本地主机发送或接收的数据包触发；转发的数据包在 IP 层处理，仅对 [dtrace_ip(4)](dtrace_ip.4.md) 提供者可见。

Fn sctp:::state-change 探测在本地 SCTP 关联状态转换时触发。其第一、第三和第五个参数当前始终为 `NULL`。其最后一个参数描述转换中的源状态，目标状态可从 `args[3]->sctps_state` 获取。

## 文件

**`/usr/lib/dtrace/sctp.d`** `sctp` 提供者的 DTrace 类型和转换器定义。

## 实例

实时记录 SCTP 数据包的脚本：

```sh
#pragma D option quiet
#pragma D option switchrate=10hz
dtrace:::BEGIN
{
        printf(" %3s %15s:%-5s      %15s:%-5sn", "CPU",
            "LADDR", "LPORT", "RADDR", "RPORT");
}
sctp:::send
{
        printf(" %3d %16s:%-5d -> %16s:%-5dn", cpu,
            args[2]->ip_saddr, args[4]->sctp_sport,
            args[2]->ip_daddr, args[4]->sctp_dport);
}
sctp:::receive
{
        printf(" %3d %16s:%-5d <- %16s:%-5dn", cpu,
            args[2]->ip_daddr, args[4]->sctp_dport,
            args[2]->ip_saddr, args[4]->sctp_sport);
}
```

记录 SCTP 关联状态变化的脚本：

```sh
#pragma D option quiet
#pragma D option switchrate=10
int last[int];
dtrace:::BEGIN
{
        printf(" %3s %12s  %-25s    %-25sn",
            "CPU", "DELTA(us)", "OLD", "NEW");
}
sctp:::state-change
/ last[args[1]->cs_cid] /
{
        this->elapsed = (timestamp - last[args[1]->cs_cid]) / 1000;
        printf(" %3d %12d  %-25s -> %-25sn", cpu, this->elapsed,
            sctp_state_string[args[5]->sctps_state],
            sctp_state_string[args[3]->sctps_state]);
        last[args[1]->cs_cid] = timestamp;
}
sctp:::state-change
/ last[args[1]->cs_cid] == 0 /
{
        printf(" %3d %12s  %-25s -> %-25sn", cpu, "-",
            sctp_state_string[args[5]->sctps_state],
            sctp_state_string[args[3]->sctps_state]);
        last[args[1]->cs_cid] = timestamp;
}
```

## 兼容性

Fn sctp:::send、Fn sctp:::receive 和 Fn sctp:::state-change 探测与 Solaris 中的 `sctp` 提供者兼容。所有其他探测仅在 FreeBSD 中可用。

## 参见

[dtrace(1)](../man1/dtrace.1.md), [dtrace_ip(4)](dtrace_ip.4.md), [dtrace_udp(4)](dtrace_udp.4.md), [dtrace_udplite(4)](dtrace_udplite.4.md), [sctp(4)](sctp.4.md), [SDT(9)](../man9/sdt.9.md)

## 作者

本手册页由 Devin Teske <dteske@FreeBSD.org> 编写。
