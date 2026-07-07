# cc_vegas(4)

`cc_vegas` — Vegas 拥塞控制算法

## 名称

`cc_vegas`

## 描述

Vegas 拥塞控制算法使用作者所称的实际传输速率和期望传输速率来判断网络路径上是否存在拥塞，即：

- 实际速率 = （一个 RTT 内发送的总数据量） / RTT
- 期望速率 = cwnd / RTTmin
- diff = 期望速率 - 实际速率

其中 RTT 是测量到的瞬时往返时间，RTTmin 是连接期间观察到的最小往返时间。

该算法旨在将 diff 保持在两个参数 alpha 和 beta 之间，即：

- alpha < diff < beta

如果 diff > beta，则推断存在拥塞，将 cwnd 减小一个数据包（或最大 TCP 段大小）。如果 diff < alpha，则将 cwnd 增加一个数据包。alpha 和 beta 控制着路径上的缓冲量。

本实现采用净室方式完成，基于下文参见章节中引用的论文。

## 实现说明

从发送一个标记数据包到收到该数据包的确认之间的时间，每 RTT 测量一次。本实现未采用 Brakmo 和 Peterson 原始的重复 ACK 策略，因为当今机器的时钟节拍不像 Vegas 最初设计时那样粗糙（即 500ms）。注意，现代 TCP 恢复过程（如快速重传和 SACK）在 TCP 协议栈中默认启用。

## MIB 变量

该算法在 sysctl(3) MIB 的 `net.inet.tcp.cc.vegas` 分支下暴露以下可调变量：

**`alpha`** 查询或设置 Vegas 的 alpha 参数，以路径上的缓冲区数量表示。设置 alpha 时，该值必须满足：0 < alpha < beta。默认值为 1。

**`beta`** 查询或设置 Vegas 的 beta 参数，以路径上的缓冲区数量表示。设置 beta 时，该值必须满足：0 < alpha < beta。默认值为 3。

## 参见

[cc_cdg(4)](cc_cdg.4.md), [cc_chd(4)](cc_chd.4.md), [cc_cubic(4)](cc_cubic.4.md), [cc_dctcp(4)](cc_dctcp.4.md), [cc_hd(4)](cc_hd.4.md), [cc_htcp(4)](cc_htcp.4.md), [cc_newreno(4)](cc_newreno.4.md), [h_ertt(4)](h_ertt.4.md), [mod_cc(4)](mod_cc.4.md), [tcp(4)](tcp.4.md), [khelp(9)](../man9/khelp.9.md), [mod_cc(9)](../man9/mod_cc.9.md)

> L. S. Brakmo, L. L. Peterson, "TCP Vegas: end to end congestion avoidance on a global internet", *IEEE J. Sel. Areas Commun.*, 13, 8, pp. 1465-1480, October 1995.

## 致谢

本软件的开发和测试部分得益于 FreeBSD 基金会和 Community Foundation Silicon Valley 下的 Cisco 大学研究计划基金的资助。

## 历史

`cc_vegas` 拥塞控制模块首次出现于 FreeBSD 9.0。

该模块于 2010 年由 David Hayes 首次发布，当时他在澳大利亚墨尔本斯威本科技大学先进互联网架构中心从事 NewTCP 研究项目。更多详情见：

<http://caia.swin.edu.au/urp/newtcp/>

## 作者

`cc_vegas` 拥塞控制模块及本手册页由 David Hayes <david.hayes@ieee.org> 编写。
