# cc_hd(4)

`cc_hd` — HD 拥塞控制算法

## 名称

`cc_hd`

## 描述

HD 拥塞控制算法是 Hamilton 研究所基于延迟的拥塞控制的实现，旨在将网络排队延迟保持在特定阈值（queue_threshold）以下。

HD 根据其对网络排队延迟的估计来概率性地减小拥塞窗口（cwnd）。在 hd_qmin 或以下时，减小 cwnd 的概率为零，随后在 queue_threshold 处升至最大值，然后在最大排队延迟处再回到零。

基于丢包的拥塞控制算法（如 NewReno）通过填充队列直到发生丢包来探测网络容量。HD 通过让其减小 cwnd 的概率从 queue_threshold 处的最大值下降到最大排队延迟处为零，来与基于丢包的拥塞控制算法竞争。已证明此方法在瓶颈链路高度复用的情况下效果良好。

## MIB 变量

该算法在 sysctl(3) MIB 的 `net.inet.tcp.cc.hd` 分支下暴露以下可调变量：

**`queue_threshold`** 排队拥塞阈值（qth），以 tick 为单位。默认值为 20。

**`pmax`** 每个数据包的最大退避概率，以百分比表示。默认值为 5。

**`qmin`** 最小排队延迟阈值（qmin），以 tick 为单位。默认值为 5。

## 参见

[cc_cdg(4)](cc_cdg.4.md), [cc_chd(4)](cc_chd.4.md), [cc_cubic(4)](cc_cubic.4.md), [cc_dctcp(4)](cc_dctcp.4.md), [cc_htcp(4)](cc_htcp.4.md), [cc_newreno(4)](cc_newreno.4.md), [cc_vegas(4)](cc_vegas.4.md), [h_ertt(4)](h_ertt.4.md), [mod_cc(4)](mod_cc.4.md), [tcp(4)](tcp.4.md), [khelp(9)](../man9/khelp.9.md), [mod_cc(9)](../man9/mod_cc.9.md)

> L. Budzisz, R. Stanojevic, R. Shorten, F. Baker, "A strategy for fair coexistence of loss and delay-based congestion control algorithms", *IEEE Commun. Lett.*, 13, 7, pp. 555-557, Jul 2009.

## 致谢

本软件的开发和测试部分得益于 FreeBSD 基金会和 Community Foundation Silicon Valley 下的 Cisco 大学研究计划基金的资助。

## 未来工作

Hamilton 研究所近期对该模块实现的算法做了一些改进，并将其称为 Coexistent-TCP（C-TCP）。这些改进应予以评估，并有可能合并到本模块中。

## 历史

`cc_hd` 拥塞控制模块首次出现于 FreeBSD 9.0。

该模块于 2010 年由 David Hayes 首次发布，当时他在澳大利亚墨尔本斯威本科技大学先进互联网架构中心从事 NewTCP 研究项目。更多详情见：

<http://caia.swin.edu.au/urp/newtcp/>

## 作者

`cc_hd` 拥塞控制模块及本手册页由 David Hayes <david.hayes@ieee.org> 编写。
