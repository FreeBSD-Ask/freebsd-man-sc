# cc_cubic(4)

`cc_cubic` — CUBIC 拥塞控制算法

## 名称

`cc_cubic`

## 描述

CUBIC 拥塞控制算法旨在为高速、长距离网络提供更高的吞吐量。CUBIC 拥塞控制算法是 TCP 的默认算法。在与传统 NewReno TCP 竞争时，若处于 NewReno 能正常工作的低速场景下，它会尝试保持公平性。

拥塞窗口作为自上次拥塞事件以来所经过时间的函数来增长。在正常运行期间，窗口增长函数遵循三次函数，其拐点设为上次拥塞事件时达到的拥塞窗口值。CUBIC 还会估算 NewReno 在拥塞事件后某时刻本可达到的拥塞窗口。更新拥塞窗口时，算法会在计算得到的 CUBIC 窗口和估算的 NewReno 窗口之间选择较大者。

CUBIC 还通过将乘性减小因子从 1/2（标准 NewReno TCP 所用）改为 4/5，从而在拥塞时减少回退幅度。

本实现采用净室方式完成，基于下文参见章节中引用的 Internet Draft 和论文。

## MIB 变量

目前没有可调的 MIB 变量。

## 参见

[cc_cdg(4)](cc_cdg.4.md), [cc_chd(4)](cc_chd.4.md), [cc_dctcp(4)](cc_dctcp.4.md), [cc_hd(4)](cc_hd.4.md), [cc_htcp(4)](cc_htcp.4.md), [cc_newreno(4)](cc_newreno.4.md), [cc_vegas(4)](cc_vegas.4.md), [mod_cc(4)](mod_cc.4.md), [tcp(4)](tcp.4.md), [mod_cc(9)](../man9/mod_cc.9.md)

> Sangtae Ha, Injong Rhee, Lisong Xu, "CUBIC for Fast Long-Distance Networks".

> Sangtae Ha, Injong Rhee, Lisong Xu, "CUBIC: a new TCP-friendly high-speed TCP variant", *SIGOPS Oper. Syst. Rev.*, 42, 5, pp. 64-74, July 2008.

## 致谢

本软件的开发和测试部分得益于 FreeBSD 基金会和 Community Foundation Silicon Valley 下的 Cisco 大学研究计划基金的资助。

## 历史

`cc_cubic` 拥塞控制模块首次出现于 FreeBSD 9.0。

在 FreeBSD 14.0 版本中，它成为 FreeBSD 的默认拥塞控制算法，取代了 [cc_newreno(4)](cc_newreno.4.md)。

该模块于 2009 年由 Lawrence Stewart 首次发布，当时他在澳大利亚墨尔本斯威本科技大学先进互联网架构中心学习。更多详情见：

<http://caia.swin.edu.au/urp/newtcp/>

## 作者

`cc_cubic` 拥塞控制模块及本手册页由 Lawrence Stewart <lstewart@FreeBSD.org> 和 David Hayes <david.hayes@ieee.org> 编写。
