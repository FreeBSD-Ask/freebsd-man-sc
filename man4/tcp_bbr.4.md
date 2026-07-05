# tcp_bbr.4

`tcp_bbr` — TCP 瓶颈带宽与往返时间算法

## 名称

`tcp_bbr`

## 概要

`要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
tcp_bbr_load="YES"
```

`要启用 TCP 栈，你必须在 sysctl.conf(5) 中加入以下行：`

```sh
net.inet.tcp.functions_default=bbr
```

## 描述

瓶颈带宽与往返时间（BBR）是一种拥塞控制算法，通过探测 BW 和 RTT 来寻求高吞吐量和小队列。它是对拥塞控制的全面重新设计，不基于丢失、延迟、ECN 或 AIMD。

BBR 的核心设计是通过在每个 ACK 上估计最大 BW 和最小 RTT 来创建网络路径的模型图。

## MIB 变量

该算法在 sysctl(3) MIB 的 `net.inet.tcp.bbr` 分支下暴露以下作用域：

**`cwnd`** Cwnd 控制，例如 “目标 cwnd rtt 测量” 和 “BBR 初始窗口”。

**`measure`** 测量控制。

**`pacing`** 连接 pacing 控制。

**`policer`** 警察控制，例如“误检阈值”和“丢失阈值”。

**`probertt`** 探测 RTT 控制。

**`startup`** 启动控制。

**`states`** 状态控制。

**`timeout`** 超时控制。

除上述作用域中的变量外，`net.inet.tcp.bbr` 分支下还暴露以下变量：

**`clrlost`** 清除丢失计数器。

**`software_pacing`** 软件 paced 流的总数。

**`hdwr_pacing`** 硬件 paced 流的总数。

**`enob_no_hdwr_pacing`** 非硬件 paced 流的 enobufs 总数。

**`enob_hdwr_pacing`** 硬件 paced 流的 enobufs 总数。

**`rtt_tlp_thresh`** TLP rtt/retran 将被加上的除数（1=rtt，2=1/2 rtt 等）。

**`reorder_fade`** 重新排序检测是否消退，如果是，多少毫秒（0 表示从不）。

**`reorder_thresh`** 看到重新排序时为 rack 加上的因子（右移）。

**`bb_verbose`** BBR 黑盒日志是否详细。

**`sblklimit`** 何时开始忽略小的 sack 块。

**`resend_use_tso`** 重传是否可以使用 TSO？

**`data_after_close`** 是否在所有挂起数据被 ack 之前暂缓发送 RST。

**`kill_paceout`** 连续遇到多少错误时终止会话？

**`error_paceout`** 遇到错误时最小 pace out 是多少（微秒）？

**`cheat_rxt`** 重传时是否在发送之间突发 1ms（类似 rack）？

**`minrto`** 最小 RTO（毫秒）。

## 参见

[cc_chd(4)](cc_chd.4.md), [cc_cubic(4)](cc_cubic.4.md), [cc_hd(4)](cc_hd.4.md), [cc_htcp(4)](cc_htcp.4.md), [cc_newreno(4)](cc_newreno.4.md), [cc_vegas(4)](cc_vegas.4.md), [h_ertt(4)](h_ertt.4.md), [mod_cc(4)](mod_cc.4.md), [tcp(4)](tcp.4.md), [tcp_rack(4)](tcp_rack.4.md), [mod_cc(9)](../man9/mod_cc.9.md)

> Neal Cardwell, Yuchung Cheng, Stephen Gunn, Soheil Hassas Yeganeh, Van Jacobson, "BBR: Congestion-Based Congestion Control", *ACM Queue, Vol. 14*, September / October 2016.

> Dominik Scholz, Benedikt Jaeger, Lukas Schwaighofer, Daniel Raumer, Fabien Geyer, Georg Carle, "Towards a Deeper Understanding of TCP BBR Congestion Control", *IFIP Networking 2018*, May 2018.

## 历史

`tcp_bbr` 拥塞控制模块首次出现于 FreeBSD 13.0。

## 作者

`tcp_bbr` 拥塞控制模块由 Randall Stewart <rrs@FreeBSD.org> 编写，由 Netflix, Inc. 赞助。本手册页由 Gordon Bergling <gbe@FreeBSD.org> 编写。
