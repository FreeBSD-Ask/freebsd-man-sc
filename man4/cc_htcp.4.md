# cc_htcp(4)

`cc_htcp` — H-TCP 拥塞控制算法

## 名称

`cc_htcp`

## 描述

H-TCP 拥塞控制算法旨在为高速、长距离网络提供更高的吞吐量。在与传统 NewReno TCP 竞争时，若处于 NewReno 能正常工作的低速场景下，它会尝试保持公平性。

拥塞窗口作为自上次拥塞事件以来所经过时间的函数来增长。窗口增长算法在拥塞事件后的第一秒内像 NewReno 一样运作，随后切换到基于二次增长函数的高速模式。

本实现采用净室方式完成，基于下文参见章节中引用的 Internet Draft 及其他文档。

## MIB 变量

该算法在 sysctl(3) MIB 的 `net.inet.tcp.cc.htcp` 分支下暴露以下可调变量：

**`adaptive_backoff`** 控制是否使用自适应退避算法，该算法旨在使网络队列在拥塞恢复期间保持非空。默认值为 0（禁用）。

**`rtt_scaling`** 控制是否使用 RTT 缩放算法，该算法旨在使拥塞避免模式下的拥塞窗口增长相对于 RTT 保持不变。默认值为 0（禁用）。

## 参见

[cc_cdg(4)](cc_cdg.4.md), [cc_chd(4)](cc_chd.4.md), [cc_cubic(4)](cc_cubic.4.md), [cc_dctcp(4)](cc_dctcp.4.md), [cc_hd(4)](cc_hd.4.md), [cc_newreno(4)](cc_newreno.4.md), [cc_vegas(4)](cc_vegas.4.md), [mod_cc(4)](mod_cc.4.md), [tcp(4)](tcp.4.md), [mod_cc(9)](../man9/mod_cc.9.md)

> D. Leith, R. Shorten, "H-TCP: TCP Congestion Control for High Bandwidth-Delay Product Paths".

> D. Leith, R. Shorten, T. Yee, "H-TCP: A framework for congestion control in high-speed and long-distance networks", *Proc. PFLDnet*, 2005.

> G. Armitage, L. Stewart, M. Welzl, J. Healy, "An independent H-TCP implementation under FreeBSD 7.0: description and observed behaviour", *SIGCOMM Comput. Commun. Rev.*, 38, 3, pp. 27-38, July 2008.

## 致谢

本软件的开发和测试部分得益于 FreeBSD 基金会和 Community Foundation Silicon Valley 下的 Cisco 大学研究计划基金的资助。

## 历史

`cc_htcp` 拥塞控制模块首次出现于 FreeBSD 9.0。

该模块于 2007 年由 James Healy 和 Lawrence Stewart 首次发布，当时他们在澳大利亚墨尔本斯威本科技大学先进互联网架构中心从事 NewTCP 研究项目，该项目部分得益于 Community Foundation Silicon Valley 下的 Cisco 大学研究计划基金的资助。更多详情见：

<http://caia.swin.edu.au/urp/newtcp/>

## 作者

`cc_htcp` 拥塞控制模块由 James Healy <jimmy@deefa.com> 和 Lawrence Stewart <lstewart@FreeBSD.org> 编写。

本手册页由 Lawrence Stewart <lstewart@FreeBSD.org> 和 David Hayes <david.hayes@ieee.org> 编写。
