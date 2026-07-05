# h_ertt.4

`h_ertt` — 增强往返时间 Khelp 模块

## 名称

`h_ertt`

## 概要

`#include <netinet/khelp/h_ertt.h>`

## 描述

`h_ertt` Khelp 模块在 [khelp(9)](../man9/khelp.9.md) 框架内工作，为 TCP 提供每连接、低噪声的瞬时 RTT 估计。该实现在面对延迟确认、TCP 分段卸载 (TSO)、操纵 TCP 时间戳的接收方以及完全没有 TCP 时间戳选项的情况时，力求保持稳健。

使用延迟确认的 TCP 接收方要么确认每个第二数据包（反映第一个数据包的时间戳），要么在没有第二个数据包到达时使用超时触发确认。如果 `h_ertt` 使用的启发式方法确定接收方使用了延迟确认，它会使用第二个数据包（触发确认的那个）测量 RTT。如果确认是针对第一个数据包的，则不测量 RTT，因为无法准确判定。

启用 TSO 时，`h_ertt` 会在标记用于新测量的数据包时暂时禁用 TSO。此过程对连接的影响可忽略不计。

`h_ertt` 将以下结构体与每个连接的 TCP 控制块关联：

```sh
struct ertt {
	TAILQ_HEAD(txseginfo_head, txseginfo) txsegi_q;	/* 私有。 */
	long		bytes_tx_in_rtt;		/* 私有。 */
	long		bytes_tx_in_marked_rtt;
	unsigned long	marked_snd_cwnd;
	int		rtt;
	int		maxrtt;
	int		minrtt;
	int		dlyack_rx;			/* 私有。 */
	int		timestamp_errors;		/* 私有。 */
	int		markedpkt_rtt;			/* 私有。 */
	uint32_t	flags;
};
```

标记为私有的字段不应被 `h_ertt` 实现以外的任何代码操纵。非私有字段提供以下数据：

**`bytes_tx_in_marked_rtt`** 在 `markedpkt_rtt` 中传输的字节数。

**`marked_snd_cwnd`** 标记 rtt 测量时的 cwnd 值。

**`rtt`** 最近的 RTT 测量值。

**`maxrtt`** 已获取的最长 RTT 测量值。

**`minrtt`** 已获取的最短 RTT 测量值。

**`flags`** 当有新测量可用时，实现会设置 ERTT_NEW_MEASUREMENT 标志。如果 `h_ertt` 的使用者希望将其作为新测量的通知方法，则有责任清除该标志。

## 参见

[cc_chd(4)](cc_chd.4.md), [cc_hd(4)](cc_hd.4.md), [cc_vegas(4)](cc_vegas.4.md), [mod_cc(4)](mod_cc.4.md), [hhook(9)](../man9/hhook.9.md), [khelp(9)](../man9/khelp.9.md)

## 致谢

本软件的开发和测试部分得益于 FreeBSD Foundation 和 Community Foundation Silicon Valley 的 Cisco University Research Program Fund 的资助。

## 历史

`h_ertt` 模块首次出现于 FreeBSD 9.0。

该模块由 David Hayes 于 2010 年在澳大利亚墨尔本斯威本科技大学先进互联网架构中心 (Centre for Advanced Internet Architectures, Melbourne, Australia) 进行 NewTCP 研究项目时首次发布。更多细节见：

<http://caia.swin.edu.au/urp/newtcp/>

## 作者

`h_ertt` Khelp 模块和本手册页由 David Hayes <david.hayes@ieee.org> 编写。

## 缺陷

该模块为加载时间之后创建的所有新 TCP 连接维护增强 RTT 估计。查看是否可能让该模块只影响真正关心 ERTT 估计的连接可能是有益的。
