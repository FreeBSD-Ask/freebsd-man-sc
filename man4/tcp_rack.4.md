# tcp_rack(4)

`tcp_rack` — TCP RACK-TLP 丢失检测算法

## 名称

`tcp_rack`

## 概要

`要在引导时以模块形式加载 TCP 栈，请在 loader.conf(5) 中加入以下行：`

```sh
tcp_rack_load="YES"
```

`要启用 TCP 栈，请在 sysctl.conf(5) 中加入以下行：`

```sh
net.inet.tcp.functions_default=rack
```

## 描述

RACK-TLP 使用每段传输时间戳和选择性确认（SACK），包含两部分。最近确认（RACK）利用从确认（ACK）反馈得出的基于时间的推断快速启动快速恢复，尾部丢失探测（TLP）利用 RACK 发送探测数据包以触发 ACK 反馈，从而避免重传超时（RTO）事件。

与广泛使用的重复确认（DupAck）阈值方法相比，RACK-TLP 在应用受限数据传输、重传丢失或数据包重排事件中能更高效地检测丢失。

它旨在作为 DupAck 阈值方法的替代。

## MIB 变量

该算法在 sysctl(3) MIB 的 `net.inet.tcp.rack` 分支下暴露以下作用域：

**`net.inet.tcp.rack.misc`** 杂项相关控制

**`net.inet.tcp.rack.features`** 特性控制

**`net.inet.tcp.rack.measure`** 测量相关控制

**`net.inet.tcp.rack.timers`** 定时器相关控制

**`net.inet.tcp.rack.tlp`** TLP 和 Rack 相关控制

**`net.inet.tcp.rack.timely`** Rack Timely RTT 控制

**`net.inet.tcp.rack.hdwr_pacing`** Pacing 相关控制

**`net.inet.tcp.rack.pacing`** Pacing 相关控制

**`net.inet.tcp.rack.tp`** Rack tracepoint 设施

**`net.inet.tcp.rack.probertt`** ProbeRTT 相关控制

**`net.inet.tcp.rack.stats`** Rack 计数器

**`net.inet.tcp.rack.sack_attack`** Rack Sack Attack 计数器和控制

除上述作用域中的变量外，`net.inet.tcp.rack` 分支下还暴露以下变量：

**`net.inet.tcp.rack.clear`** 清除计数器

**`net.inet.tcp.rack.opts`** RACK 选项统计

**`net.inet.tcp.rack.outsize`** MSS 发送大小

**`net.inet.tcp.rack.req_measure_cnt`** 如果进行动态 pacing，开始 pacing 之前必须有多次测量？

**`net.inet.tcp.rack.use_pacing`** 如果设置则使用 pacing，如果清除则仅使用原始突发缓解

**`net.inet.tcp.rack.rate_sample_method`** 速率采样应使用什么方法 0=高，1=低

## 参见

[cc_chd(4)](cc_chd.4.md), [cc_cubic(4)](cc_cubic.4.md), [cc_hd(4)](cc_hd.4.md), [cc_htcp(4)](cc_htcp.4.md), [cc_newreno(4)](cc_newreno.4.md), [cc_vegas(4)](cc_vegas.4.md), [h_ertt(4)](h_ertt.4.md), [mod_cc(4)](mod_cc.4.md), [tcp(4)](tcp.4.md), [tcp_bbr(4)](tcp_bbr.4.md), [mod_cc(9)](../man9/mod_cc.9.md)

> Neal Cardwell, Yuchung Cheng, Nandita Dukkipati, Priyaranjan Jha, "The RACK-TLP Loss Detection Algorithm for TCP", February 2021, RFC 8985.

> M. Allman, V. Paxson, E. Blanton, "TCP Congestion Control", September 2009, RFC 5681.

> M. Mathis, Nandita Dukkipati, Yuchung Cheng, "Proportional Rate Reduction for TCP", May 2013, RFC 6937.

## 历史

`tcp_rack` 拥塞控制模块首次出现于 FreeBSD 13.0。

## 作者

`tcp_rack` 拥塞控制模块由 Randall Stewart <rrs@FreeBSD.org> 编写，由 Netflix, Inc. 赞助。本手册页由 Gordon Bergling <gbe@FreeBSD.org> 编写。
