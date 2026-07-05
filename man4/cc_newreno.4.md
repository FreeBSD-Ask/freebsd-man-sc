# cc_newreno.4

`cc_newreno` — NewReno 拥塞控制算法

## 名称

`cc_newreno`

## 概要

`#include <netinet/cc/cc_newreno.h>`

## 描述

有关该算法的详细信息，请参见 RFC5681。

## 套接字选项

`cc_newreno` 模块在 TCP_CCALGOOPT 下支持若干套接字选项（参见 [tcp(4)](tcp.4.md) 和 [mod_cc(9)](../man9/mod_cc.9.md)），可通过 setsockopt(2) 设置、用 getsockopt(2) 测试。`cc_newreno` 套接字选项使用 <sys/netinet/cc/cc_newreno.h> 中定义的以下结构：

```sh
struct cc_newreno_opts {
	int name;
	uint32_t val;
}
```

**`CC_NEWRENO_BETA`** 乘性窗口减小因子，以百分比表示，在响应拥塞信号时应用于拥塞窗口：cwnd = (cwnd * CC_NEWRENO_BETA) / 100。默认值为 50。

**`CC_NEWRENO_BETA_ECN`** 乘性窗口减小因子，以百分比表示，当 `net.inet.tcp.cc.abe=1` 时在响应 ECN 拥塞信号时应用于拥塞窗口：cwnd = (cwnd * CC_NEWRENO_BETA_ECN) / 100。默认值为 80。注意，目前启用 hystart++ 的唯一方式是通过套接字选项。启用时，值为 1 将启用精确的 internet-draft（版本 4）行为（受任何 MIB 变量设置的影响），其他设置（2 和 3）为实验性。

注意，hystart++ 要求 TCP 协议栈能够通过 `newround` 函数和 `rttsample` 函数向拥塞控制器发出调用。目前唯一能向拥塞控制器提供此反馈的 TCP 协议栈是 rack。

## MIB 变量

该算法在 sysctl(3) MIB 的 `net.inet.tcp.cc.newreno` 分支下暴露以下变量：

**`beta`** 乘性窗口减小因子，以百分比表示，在响应拥塞信号时应用于拥塞窗口：cwnd = (cwnd * beta) / 100。默认值为 50。

**`beta_ecn`** 乘性窗口减小因子，以百分比表示，当 `net.inet.tcp.cc.abe=1` 时在响应 ECN 拥塞信号时应用于拥塞窗口：cwnd = (cwnd * beta_ecn) / 100。默认值为 80。

## 参见

[cc_cdg(4)](cc_cdg.4.md), [cc_chd(4)](cc_chd.4.md), [cc_cubic(4)](cc_cubic.4.md), [cc_dctcp(4)](cc_dctcp.4.md), [cc_hd(4)](cc_hd.4.md), [cc_htcp(4)](cc_htcp.4.md), [cc_vegas(4)](cc_vegas.4.md), [mod_cc(4)](mod_cc.4.md), [tcp(4)](tcp.4.md), [mod_cc(9)](../man9/mod_cc.9.md)

> Mark Allman, Vern Paxson, Ethan Blanton, "TCP Congestion Control", RFC 5681.

> Naeem Khademi, Michael Welzl, Grenville Armitage, Gorry Fairhurst, "TCP Alternative Backoff with ECN (ABE)", RFC 8511.

## 致谢

本软件的开发和测试部分得益于 FreeBSD 基金会和 Community Foundation Silicon Valley 下的 Cisco 大学研究计划基金的资助。

## 历史

`cc_newreno` 拥塞控制算法首次以模块化形式出现于 FreeBSD 9.0。

在 FreeBSD 14.0 版本之前，它是 FreeBSD 的默认拥塞控制算法，之后由 [cc_cubic(4)](cc_cubic.4.md) 取代。

该模块于 2007 年由 James Healy 和 Lawrence Stewart 首次发布，当时他们在澳大利亚墨尔本斯威本科技大学先进互联网架构中心从事 NewTCP 研究项目，该项目部分得益于 Community Foundation Silicon Valley 下的 Cisco 大学研究计划基金的资助。更多详情见：

<http://caia.swin.edu.au/urp/newtcp/>

## 作者

`cc_newreno` 拥塞控制模块由 James Healy <jimmy@deefa.com>、Lawrence Stewart <lstewart@FreeBSD.org> 和 David Hayes <david.hayes@ieee.org> 编写。

TCP ABE 支持由 Tom Jones <tj@enoti.me> 添加。

本手册页由 Lawrence Stewart <lstewart@FreeBSD.org> 编写。
