# cc_chd.4

`cc_chd` — CHD 拥塞控制算法

## 名称

`cc_chd`

## 描述

CHD 对 [cc_hd(4)](cc_hd.4.md) 中实现的 HD 算法进行了增强。它对非拥塞相关的丢包提供了容忍能力，并改善了与传统基于丢包的 TCP 流的共存表现，特别是在瓶颈链路复用程度较低时。

与 HD 一样，该算法旨在将网络排队延迟保持在特定阈值（queue_threshold）以下，并根据其对网络排队延迟的估计来概率性地决定是否减小拥塞窗口（cwnd）。

它与 HD 在三个方面有所不同：

- 拥塞导致 cwnd 减小的概率每往返时间（RTT）计算一次，而非像 [cc_hd(4)](cc_hd.4.md) 那样每收到一个确认就计算一次。
- 当排队延迟小于 queue_threshold 时发生的丢包不会导致 cwnd 减小。
- CHD 使用影子窗口来帮助在与基于丢包的 TCP 流竞争时恢复丢失的传输机会。

## MIB 变量

该算法在 sysctl(3) MIB 的 `net.inet.tcp.cc.chd` 分支下暴露以下可调变量：

**`queue_threshold`** 排队拥塞阈值（qth），以 tick 为单位。默认值为 20。

**`pmax`** 每个 RTT 的最大退避概率，以百分比表示。默认值为 50。

**`qmin`** 最小排队延迟阈值（qmin），以 tick 为单位。默认值为 5。

**`loss_fair`** 若为 1，则在检测到与拥塞相关的丢包时使用影子窗口调整 cwnd。默认值为 1。

**`use_max`** 若为 1，则将测量期内观察到的最大 RTT 用作算法的基本延迟测量值；否则使用采样的 RTT 测量值。默认值为 1。

## 参见

[cc_cdg(4)](cc_cdg.4.md), [cc_cubic(4)](cc_cubic.4.md), [cc_dctcp(4)](cc_dctcp.4.md), [cc_hd(4)](cc_hd.4.md), [cc_htcp(4)](cc_htcp.4.md), [cc_newreno(4)](cc_newreno.4.md), [cc_vegas(4)](cc_vegas.4.md), [h_ertt(4)](h_ertt.4.md), [mod_cc(4)](mod_cc.4.md), [tcp(4)](tcp.4.md), [khelp(9)](../man9/khelp.9.md), [mod_cc(9)](../man9/mod_cc.9.md)

> D. A. Hayes, G. Armitage, "Improved coexistence and loss tolerance for delay based TCP congestion control", *in 35th Annual IEEE Conference on Local Computer Networks*, pp. 24-31, October 2010.

## 致谢

本软件的开发和测试部分得益于 FreeBSD 基金会和 Community Foundation Silicon Valley 下的 Cisco 大学研究计划基金的资助。

## 历史

`cc_chd` 拥塞控制模块首次出现于 FreeBSD 9.0。

该模块于 2010 年由 David Hayes 首次发布，当时他在澳大利亚墨尔本斯威本科技大学先进互联网架构中心从事 NewTCP 研究项目。更多详情见：

<http://caia.swin.edu.au/urp/newtcp/>

## 作者

`cc_chd` 拥塞控制模块及本手册页由 David Hayes <david.hayes@ieee.org> 编写。
