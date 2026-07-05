# cc_cdg.4

`cc_cdg` — CDG 拥塞控制算法

## 名称

`cc_cdg`

## 描述

CAIA-Delay Gradient（CDG）是一种混合拥塞控制算法，对数据包丢失和推断的排队延迟都作出反应。它尽可能尝试作为基于延迟的算法运行，但利用启发式方法检测基于丢失的 TCP 交叉流量，并根据需要有效竞争。因此，CDG 是可增量部署的，适用于共享网络。

在基于延迟的操作期间，CDG 使用基于延迟梯度的概率回退机制，还会尝试推断非拥塞相关的数据包丢失，并在它们发生时避免回退。在基于丢失的操作期间，CDG 本质上恢复为类似 [cc_newreno(4)](cc_newreno.4.md) 的行为。

当 CDG 检测到可配置数量的连续基于延迟的回退没有可衡量的效果时，它会切换到基于丢失的操作。它周期性地尝试返回基于延迟的操作，但会根据需要继续切换回基于丢失的操作。

## MIB 变量

该算法在 sysctl(3) MIB 的 `net.inet.tcp.cc.cdg` 分支中暴露以下变量：

**`version`** 当前算法/实现版本号。

**`beta_delay`** 基于延迟的窗口减少因子，以百分比表示（在基于延迟的回退时，w = w * beta_delay / 100）。默认为 70。

**`beta_loss`** 基于丢失的窗口减少因子，以百分比表示（在基于丢失的回退时，w = w * beta_loss / 100）。默认为 50。

**`exp_backoff_scale`** 概率性指数回退的缩放参数。默认为 2。

**`smoothing_factor`** 用于移动平均平滑的样本数（0 表示不平滑）。默认为 8。

**`loss_compete_consec_cong`** 触发基于丢失的 CC 兼容性的连续基于延迟梯度的拥塞事件数。默认为 5。

**`loss_compete_hold_backoff`** 为基于丢失的 CC 兼容性保持窗口回退的连续基于延迟梯度的拥塞事件数。默认为 5。

**`alpha_inc`** 如果非零，则启用实验模式，其中 CDG 的窗口增加因子（alpha）在拥塞避免模式期间每 `alpha_inc` 个 RTT 增加 1 MSS。（将 `alpha_inc` 设置为 1 会导致窗口增加因子随时间最激进地增长。使用更高的 `alpha_inc` 值可获得较慢的增长。）默认为 0。

## 参见

[cc_chd(4)](cc_chd.4.md), [cc_cubic(4)](cc_cubic.4.md), [cc_dctcp(4)](cc_dctcp.4.md), [cc_hd(4)](cc_hd.4.md), [cc_htcp(4)](cc_htcp.4.md), [cc_newreno(4)](cc_newreno.4.md), [cc_vegas(4)](cc_vegas.4.md), [h_ertt(4)](h_ertt.4.md), [mod_cc(4)](mod_cc.4.md), [tcp(4)](tcp.4.md), [khelp(9)](../man9/khelp.9.md), [mod_cc(9)](../man9/mod_cc.9.md)

> D. A. Hayes, G. Armitage, "Revisiting TCP Congestion Control using Delay Gradients", *Networking 2011 Proceedings, Part II*, pp. 328-341, May 2011。

> N. Khademi, G. Armitage, "Minimising RTT across homogeneous 802.11 WLANs with CAIA Delay-Gradient TCP (v0.1)", November 2012。

## 致谢

本软件的开发和测试部分得益于 FreeBSD 基金会和 Cisco 大学研究计划基金（Silicon Valley Community Foundation 的公司顾问基金）的资助。

## 历史

`cc_cdg` 拥塞控制模块首次出现于 FreeBSD 9.2。

该模块于 2011 年由 David Hayes 首次发布，当时他在澳大利亚墨尔本斯威本科技大学先进互联网架构中心的 NewTCP 研究项目工作。更多详情见：

<http://caia.swin.edu.au/urp/newtcp/>

## 作者

`cc_cdg` 拥塞控制模块由 David Hayes <david.hayes@ieee.org> 编写。本手册页由 Lawrence Stewart <lstewart@FreeBSD.org> 和 Grenville Armitage <garmitage@swin.edu.au> 编写。

## 缺陷

底层算法和参数值仍在开发中，可能不适用于某些网络场景。
