# dtrace_mib(4)

`dtrace_mib` — 用于管理信息库的 DTrace 提供者

## 名称

`dtrace_mib`

## 概要

`mib:module:count:counter`

`在 config(5) 中：options KDTRACE_MIB_SDT`

## 描述

`mib` 提供者允许跟踪管理信息库（Management Information Base）统计计数器。

已检测的 `module` 列表包括：

**`ah`** IP 认证头（RFC 2402），[ipsec(4)](ipsec.4.md)
**`esp`** IP 封装安全载荷（RFC 1827、RFC 2406），[ipsec(4)](ipsec.4.md)
**`icmp`** [icmp(4)](icmp.4.md)
**`icmp6`** [icmp6(4)](icmp6.4.md)
**`ip`** [ip(4)](ip.4.md)
**`ip6`** [ip6(4)](ip6.4.md)
**`ipcomp`** IP 载荷压缩协议，[ipsec(4)](ipsec.4.md)
**`ipsec`** [ipsec(4)](ipsec.4.md)
**`tcp`** [tcp(4)](tcp.4.md)
**`udp`** [udp(4)](udp.4.md)

`mib:``module``:count:``counter` 探测在 `module` 中的 `counter` 增加时触发。

第一个探测参数 `uint64_t` `args[0]` 是 `counter` 将增加的增量。

注意，某些探测（如 `mib:esp:count:esps_hist` 或 `mib:icmp6:count:icp6s_outhist`）提供额外的探测特定参数。

## 实例

### 实例 1：跟踪 IP 统计计数器

调试网络问题时，一个常见线索是意外递增的错误计数器。这很有帮助，因为它让我们了解可能出了什么问题，但这些计数器通常可能在不同函数中递增。

跟踪 [ip(4)](ip.4.md) 模块中的所有 `mib` 探测，并打印当前计数和栈回溯：

```sh
# dtrace -n 'mib:ip:count: { printf("%d", arg0); stack(); }'
dtrace: description 'mib:ip:count: ' matched 29 probes
CPU     ID                    FUNCTION:NAME
  7  98784               count:ips_localout 1
              kernel`ip_output+0x17a2
              kernel`udp_send+0xaca
              kernel`sosend_dgram+0x315
              kernel`sousrsend+0x79
              kernel`kern_sendit+0x1be
              kernel`sendit+0x1ab
              kernel`sys_sendmsg+0x5b
              kernel`amd64_syscall+0x169
              kernel`0xffffffff81094b8b
```

## 参见

[dtrace(1)](../man1/dtrace.1.md), [dtrace_ip(4)](dtrace_ip.4.md), [dtrace_tcp(4)](dtrace_tcp.4.md), [dtrace_udp(4)](dtrace_udp.4.md), [tracing(7)](../man7/tracing.7.md), [sysctl(8)](../man8/sysctl.8.md)

## 标准

FreeBSD `mib` 提供者中的探测描述与 Solaris/illumos mib 提供者中的不兼容。

## 作者

`mib` 提供者由 Kristof Provost <kp@FreeBSD.org> 添加到 FreeBSD。

本手册页由 Mateusz Piotrowski <0mp@FreeBSD.org> 编写。
