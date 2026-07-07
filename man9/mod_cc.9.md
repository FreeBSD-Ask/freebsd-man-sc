# mod_cc(9)

`mod_cc` — 模块化拥塞控制

## 名称

`mod_cc`, `DECLARE_CC_MODULE`, `CCV`

## 概要

```c
#include <netinet/tcp.h>
```

```c
#include <netinet/cc/cc.h>
```

```c
#include <netinet/cc/cc_module.h>
```

```c
DECLARE_CC_MODULE(ccname, ccalgo)

CCV(ccv, what)
```

## 描述

`CCV` 框架允许将拥塞控制算法实现为通过 [kld(4)](../man4/kld.4.md) 机制动态加载的内核模块。传输协议可以在每个连接的基础上从可用算法列表中进行选择，也可以使用系统默认算法（更多细节参见 [mod_cc(4)](../man4/mod_cc.4.md)）。

`CCV` 模块由一个 [ascii(7)](../man7/ascii.7.md) 名称和一组封装在 `struct cc_algo` 中的钩子函数标识，该结构具有以下成员：

```c
struct cc_algo {
	char	name[TCP_CA_NAME_MAX];
	int	(*mod_init) (void);
	int	(*mod_destroy) (void);
	size_t  (*cc_data_sz)(void);
	int	(*cb_init) (struct cc_var *ccv, void *ptr);
	void	(*cb_destroy) (struct cc_var *ccv);
	void	(*conn_init) (struct cc_var *ccv);
	void	(*ack_received) (struct cc_var *ccv, uint16_t type);
	void	(*cong_signal) (struct cc_var *ccv, uint32_t type);
	void	(*post_recovery) (struct cc_var *ccv);
	void	(*after_idle) (struct cc_var *ccv);
	int	(*ctl_output)(struct cc_var *, struct sockopt *, void *);
	void    (*rttsample)(struct cc_var *, uint32_t, uint32_t, uint32_t);
	void    (*newround)(struct cc_var *, uint32_t);
};
```

`name` 字段标识算法的唯一名称，长度不应超过 TCP_CA_NAME_MAX-1 个字符（TCP_CA_NAME_MAX 定义位于

```c
#include <netinet/tcp.h>
```

中，出于兼容性原因）。

`mod_init` 函数在新模块加载到系统时、注册过程完成之前被调用。如果模块需要在可供新连接使用之前设置某些全局状态，则应实现该函数。从 `mod_init` 返回非零值将导致模块加载失败。

`mod_destroy` 函数在从内核卸载现有模块之前被调用。如果模块需要在从内核移除之前清理任何全局状态，则应实现该函数。返回值目前被忽略。

`cc_data_sz` 函数由套接字选项代码调用，用于获取 `cb_init` 函数所需的数据大小。套接字选项代码随后预分配模块内存，使 `cb_init` 函数不会失败（套接字选项代码使用 M_WAITOK 且不持有任何锁来完成此操作）。

`cb_init` 函数在创建 TCP 控制块 `struct tcpcb` 时被调用。如果模块需要分配内存来存储私有的每连接状态，则应实现该函数。从 `cb_init` 返回非零值将导致连接建立中止，从而终止连接。注意，应检查传递给该函数的 ptr 参数是否为非 NULL，如果是，则为预分配的内存，cb_init 函数必须使用它而不是自行调用 malloc。

`cb_destroy` 函数在销毁 TCP 控制块 `struct tcpcb` 时被调用。如果模块需要释放 `cb_init` 中分配的内存，则应实现该函数。

`conn_init` 函数在新连接已建立且变量正在初始化时被调用。应实现该函数以初始化新建立连接的拥塞控制算法变量。

`ack_received` 函数在收到 TCP 确认（ACK）包时被调用。模块使用 `type` 参数作为其拥塞管理算法的输入。协议栈当前报告的 ACK 类型有 CC_ACK 和 CC_DUPACK。CC_ACK 表示收到的 ACK 确认了先前未确认的数据。CC_DUPACK 表示收到的 ACK 确认了已经收到过 ACK 的数据。

`cong_signal` 函数在 TCP 协议栈检测到拥塞事件时被调用。模块使用 `type` 参数作为其拥塞管理算法的输入。协议栈当前报告的拥塞事件类型有 CC_ECN、CC_RTO、CC_RTO_ERR 和 CC_NDUPACK。当 TCP 协议栈收到显式拥塞通知（RFC3168）时报告 CC_ECN。当重传超时定时器触发时报告 CC_RTO。当重传超时定时器错误触发时报告 CC_RTO_ERR。当连续收到 N 个重复 ACK 时报告 CC_NDUPACK，其中 N 为快速重传重复 ack 阈值（目前按 RFC5681 为 N=3）。

`post_recovery` 函数在 TCP 连接从拥塞事件恢复之后被调用。应实现该函数以根据需要调整状态。

`after_idle` 函数在空闲期后恢复数据传输时被调用。应实现该函数以根据需要调整状态。

`ctl_output` 函数在 [tcp(4)](../man4/tcp.4.md) 套接字上调用 getsockopt(2) 或 setsockopt(2) 时被调用，`struct sockopt` 指针从 TCP 控制原封不动地转发，还有一个 `void *` 指针指向算法特定的参数。

`rttsample` 函数被调用以将往返时间信息传递给拥塞控制器。该函数的附加参数包括所记录的微秒级 RTT、被确认的数据被重传的次数以及发送时的飞行大小。对于不跟踪发送时飞行大小的传输，此变量将为调用时的当前 cwnd。

`newround` 函数在每次新的往返时间开始时被调用。单调递增的轮次编号也会传递给拥塞控制器。拥塞控制器可以将其用于各种目的（例如 Hystart++）。

注意，目前并非所有 TCP 协议栈都调用 `rttsample` 和 `newround` 函数，因此对这些函数的依赖还取决于所使用的 TCP 协议栈。

`DECLARE_CC_MODULE` 宏提供了对 [DECLARE_MODULE(9)](declare_module.9.md) 宏的便捷封装，用于向 `CCV` 框架注册 `CCV` 模块。`ccname` 参数指定模块的名称。`ccalgo` 参数指向模块的 `struct cc_algo`。

`CCV` 模块必须实例化一个 `struct cc_algo`，但只要求设置 name 字段，其他函数指针为可选。注意，如果模块定义了 `cb_init` 函数，则还必须定义 `cc_data_sz` 函数。这是因为在从一个拥塞控制模块切换到另一个时，套接字选项代码会为 `cb_init` 函数预分配内存。如果模块的 `cb_init` 没有分配内存，则 `cc_data_sz` 函数应返回 0。

协议栈会跳过调用任何为 NULL 的函数指针，因此不要求实现任何函数指针（除了上述 cb_init 与 cc_data_sz 的依赖关系例外）。鼓励使用 C99 指定初始化器特性来设置字段。

每个处理拥塞控制状态的函数指针都被传递一个指向 `struct cc_var` 的指针，该结构具有以下成员：

```c
struct cc_var {
	void		*cc_data;
	int		bytes_this_ack;
	tcp_seq		curack;
	uint32_t	flags;
	int		type;
	union ccv_container {
		struct tcpcb		*tcp;
		struct sctp_nets	*sctp;
	} ccvc;
	uint16_t	nsegs;
	uint8_t		labc;
};
```

`struct cc_var` 将拥塞控制相关变量分组到一个可嵌入的结构中，并为访问传输协议控制块增加了间接层。最终目标是允许所有拥塞感知传输协议共享同一组 `CCV` 模块，但目前仅支持 [tcp(4)](../man4/tcp.4.md)。

为了辅助向这一目标的最终过渡，强烈不建议直接使用传输协议数据结构中的变量。然而，目前不可避免地需要访问其中一些变量，因此 `CCV` 宏作为便捷访问器存在。`ccv` 参数指向由 `CCV` 框架传入函数的 `struct cc_var`。`what` 参数指定要访问的变量名称。

除了 `type` 和 `ccv_container` 字段外，`struct cc_var` 中的其余字段供 `CCV` 模块使用。

`cc_data` 字段可供需要附加每连接状态的算法用来附加一个动态内存指针。该内存应在模块的 `cb_init` 钩子函数中分配并附加。

`bytes_this_ack` 字段指定最近收到的 ACK 包确认的新字节数。它仅在 `ack_received` 钩子函数中有效。

`curack` 字段指定最近收到的 ACK 包的序列号。它仅在 `ack_received`、`cong_signal` 和 `post_recovery` 钩子函数中有效。

`flags` 字段用于从协议栈向 `CCV` 模块传递有用信息。CCF_ABC_SENTAWND 标志在 `ack_received` 中相关，当适当字节计数（RFC3465）已计数到一个窗口大小的字节已发送时设置。模块有责任在处理该信号后清除该标志。CCF_CWND_LIMITED 标志在 `ack_received` 中相关，当连接发送数据的能力当前受拥塞窗口值约束时设置。算法应利用该标志未被设置的情况，避免拥塞窗口与发送窗口之间累积过大的差异。

`nsegs` 变量用于传入本地 LRO 系统执行了多少压缩。例如，如果 LRO 将三个按序确认合并为一个确认，则该变量将设置为三。

`labc` 变量与 CCF_USE_LOCAL_ABC 标志一起使用，用于覆盖拥塞控制器针对该特定确认将使用的 labc 变量。

## 参见

[cc_cdg(4)](../man4/cc_cdg.4.md), [cc_chd(4)](../man4/cc_chd.4.md), [cc_cubic(4)](../man4/cc_cubic.4.md), [cc_dctcp(4)](../man4/cc_dctcp.4.md), [cc_hd(4)](../man4/cc_hd.4.md), [cc_htcp(4)](../man4/cc_htcp.4.md), [cc_newreno(4)](../man4/cc_newreno.4.md), [cc_vegas(4)](../man4/cc_vegas.4.md), [mod_cc(4)](../man4/mod_cc.4.md), [tcp(4)](../man4/tcp.4.md)

## 致谢

本软件的开发和测试部分得益于 FreeBSD 基金会以及 Cisco 大学研究计划基金（由社区基金会硅谷分部管理）的资助。

## 未来工作

与 [sctp(4)](../man4/sctp.4.md) 集成。

## 历史

模块化拥塞控制（CC）框架首次出现于 FreeBSD 9.0。

该框架于 2007 年由 James Healy 和 Lawrence Stewart 首次发布，当时他们在澳大利亚墨尔本斯威本科技大学高级互联网架构中心从事 NewTCP 研究项目，该项目部分得益于 Cisco 大学研究计划基金（由社区基金会硅谷分部管理）的资助。更多细节参见：

<http://caia.swin.edu.au/urp/newtcp/>

## 作者

`CCV` 框架由 Lawrence Stewart <lstewart@FreeBSD.org>、James Healy <jimmy@deefa.com> 和 David Hayes <david.hayes@ieee.org> 编写。

本手册页由 David Hayes <david.hayes@ieee.org> 和 Lawrence Stewart <lstewart@FreeBSD.org> 编写。
