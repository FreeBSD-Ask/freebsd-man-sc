# netlink(4)

`Netlink` — 内核网络配置协议

## 名称

`Netlink`

## 概要

`#include <netlink/netlink.h>`

`#include <netlink/netlink_route.h>`

`Ft int Fn socket AF_NETLINK SOCK_RAW int family`

## 描述

Netlink 是一种基于消息的用户-内核通信协议，主要用于网络栈配置。Netlink 易于扩展，支持大批量数据转储和事件通知，全部通过单个 socket 完成。该协议完全异步，允许同时发出并跟踪多个请求。Netlink 由多个族组成，通常将属于特定内核子系统的命令归为一组。目前支持的族为：

NETLINK_ROUTE	网络配置，
NETLINK_GENERIC	“容器”族

`NETLINK_ROUTE` 族处理所有接口、地址、邻居、路由和 VNET 配置。更多细节可在 [rtnetlink(4)](rtnetlink.4.md) 中找到。`NETLINK_GENERIC` 族作为“容器”，允许在 `NETLINK_GENERIC` 伞下注册其他族。此方法允许使用单个 netlink socket 同时与多个 netlink 族交互。更多细节可在 [genetlink(4)](genetlink.4.md) 中找到。

Netlink 有自己的 sockaddr 结构：

```sh
struct sockaddr_nl {
	uint8_t		nl_len;		/* sizeof(sockaddr_nl) */
	sa_family_t	nl_family;	/* netlink 族 */
	uint16_t	nl_pad;		/* 保留，设置为 0 */
	uint32_t	nl_pid;		/* 自动选择，设置为 0 */
	uint32_t	nl_groups;	/* 要绑定到的多播组掩码 */
};
```

通常，对于 socket 操作并不需要填写此结构。这里列出仅为完整性。

## 协议说明

该协议基于消息。每条消息以强制的 `nlmsghdr` 头部开始，后跟族特定的头部以及类型-长度-值对（TLV）列表。TLV 可以嵌套。所有头部和 TLV 都填充到 4 字节边界。每次 send(2) recv(2) 系统调用可能包含多条消息。

### 基础头部

```sh
struct nlmsghdr {
	uint32_t nlmsg_len;   /* 消息长度（含头部） */
	uint16_t nlmsg_type;  /* 消息类型标识符 */
	uint16_t nlmsg_flags; /* 标志（NLM_F_） */
	uint32_t nlmsg_seq;   /* 序列号 */
	uint32_t nlmsg_pid;   /* 发送进程端口 ID */
};
```

`nlmsg_len` 字段存储整条消息的字节长度，包括头部。在迭代消息时，此长度必须向上舍入到最近的 4 字节边界。`nlmsg_type` 字段表示命令/请求类型。此值是族特定的。支持的命令列表可在相关族头文件中找到。`nlmsg_seq` 是用户提供的请求标识符。应用程序可使用 `NLMSG_ERROR` 消息并匹配 `nlmsg_seq` 来跟踪操作结果。`nlmsg_pid` 字段是消息发送者 ID。此字段对用户空间是可选的。内核发送者 ID 为零。`nlmsg_flags` 字段包含消息特定的标志。定义了以下通用标志：

NLM_F_REQUEST	指示该消息是对内核的实际请求
NLM_F_ACK	请求带有操作结果的显式 ACK 消息

为“GET”请求类型定义了以下通用标志：

NLM_F_ROOT	返回整个数据集
NLM_F_MATCH	返回所有匹配条件的条目

这两个标志通常一起使用，别名为 `NLM_F_DUMP`

为“NEW”请求类型定义了以下通用标志：

NLM_F_CREATE	如果对象不存在则创建
NLM_F_EXCL	如果对象存在则不替换
NLM_F_REPLACE	替换已有的匹配对象
NLM_F_APPEND	追加到已有对象

为回复定义了以下通用标志：

NLM_F_MULTI	指示该消息是消息组的一部分
NLM_F_DUMP_INTR	指示状态转储未完成
NLM_F_DUMP_FILTERED	指示转储已按请求过滤
NLM_F_CAPPED	指示原始消息已被截断为其头部
NLM_F_ACK_TLVS	指示已包含扩展 ACK TLV

### TLV

大多数消息将其属性编码为类型-长度-值对（TLV）。基础 TLV 头部：

```sh
struct nlattr {
	uint16_t nla_len;	/* 总属性长度 */
	uint16_t nla_type;	/* 属性类型 */
};
```

TLV 类型（`nla_type`）的作用域通常是族内的消息类型或组。例如，`RTN_MULTICAST` 类型值仅对 `RTM_NEWROUTE`、`RTM_DELROUTE` 和 `RTM_GETROUTE` 消息有效。TLV 可以嵌套；在这种情况下，内部 TLV 可能有自己的子类型。所有 TLV 都以 4 字节填充打包。

### 控制消息

每个族中都保留了一些通用控制消息。

`NLMSG_ERROR` 在被请求时报告操作结果，可选后跟元数据 TLV。`nlmsg_seq` 的值设置为原消息中的值，而 `nlmsg_pid` 设置为原 socket 的 socket pid。操作结果通过 `struct nlmsgerr` 报告：

```sh
struct nlmsgerr {
	int	error;		/* 标准 errno */
	struct	nlmsghdr msg;	/* 原始消息头部 */
};
```

如果未设置 `NETLINK_CAP_ACK` socket 选项，原消息的剩余部分将跟随其后。如果设置了 `NETLINK_EXT_ACK` socket 选项，内核可添加一个 `NLMSGERR_ATTR_MSG` 字符串 TLV，包含文本错误描述，可选后跟 `NLMSGERR_ATTR_OFFS` TLV，指示从消息开始触发错误的偏移量。某些操作可能返回封装在 `NLMSGERR_ATTR_COOKIE` TLV 中的额外元数据。元数据格式特定于操作。如果操作回复是多部分消息，则不会生成 `NLMSG_ERROR` 回复，只有一条 `NLMSG_DONE` 消息结束多部分序列。

`NLMSG_DONE` 指示消息组的结束：通常是转储的结束。它包含单个 `int` 字段，将转储结果描述为标准 errno 值。

## SOCKET 选项

Netlink 支持多个自定义 socket 选项，可使用 setsockopt(2) 在 `SOL_NETLINK` `level` 下设置：

**`NETLINK_ADD_MEMBERSHIP`** 订阅特定组的通知（int）。

**`NETLINK_DROP_MEMBERSHIP`** 取消订阅特定组的通知（int）。

**`NETLINK_LIST_MEMBERSHIPS`** 以位掩码形式列出成员关系。

**`NETLINK_CAP_ACK`** 指示内核在回复中发送原始消息头部而不带消息体。

**`NETLINK_EXT_ACK`** 确认能够在 ACK 消息中接收额外 TLV。

**`NETLINK_GET_STRICT_CHK`** 启用严格头部检查。

**`NETLINK_MSG_INFO`** （FreeBSD 特有）通过 socket 控制消息（cmsg）接收消息发起者数据。

此外，netlink 覆盖了 `SOL_SOCKET` `level` 的以下 socket 选项：

**`SO_RCVBUF`** 设置 socket 接收缓冲区的最大大小。如果调用者拥有 `PRIV_NET_ROUTE` 权限，该值可超过当前设置的 `kern.ipc.maxsockbuf` 值。

## SYSCTL 变量

一组 [sysctl(8)](../man8/sysctl.8.md) 变量可用于调整运行时参数：

**`net.netlink.sendspace`** netlink socket 的默认发送缓冲区。注意 socket sendspace 必须至少与此 socket 可传输的最长消息一样长。

**`net.netlink.recvspace`** netlink socket 的默认接收缓冲区。注意 socket recvspace 必须至少与此 socket 可接收的最长消息一样长。

**`net.netlink.nl_maxsockbuf`** 可通过 `SO_RCVBUF` socket 选项设置的 netlink socket 最大接收缓冲区。

## 调试

Netlink 实现了按功能单元的调试，通过 `net.netlink.debug` 分支控制不同严重级别。这些消息记录在内核消息缓冲区中，可在 [dmesg(8)](../man8/dmesg.8.md) 中查看。定义了以下严重级别：

**`LOG_DEBUG(7)`** 罕见事件或每 socket 错误在此报告。这是默认级别，不影响生产性能。

**`LOG_DEBUG2(8)`** 记录 socket 事件，如组成员关系、权限检查、命令和转储。此级别不会带来显著性能开销。

**`LOG_DEBUG3(9)`** 所有 socket 事件，每个转储或修改的实体都会被记录。开启它可能导致显著的性能开销。

## 错误

Netlink 通过为每条请求消息发送一条 `NLMSG_ERROR` 消息来报告操作结果，包括错误和错误元数据。可能返回以下错误：

**[Er** EPERM] 当前权限不足以执行所需操作时；

**[Er** ENOBUFS ][Er ENOMEM ]]] 系统内部数据结构耗尽内存时；

**[Er** ENOTSUP] 请求的命令不被该族支持或该族不受支持时；

**[Er** EINVAL] 某些必要 TLV 缺失或无效时，详细信息可在 NLMSGERR_ATTR_MSG 和 NLMSGERR_ATTR_OFFS TLV 中提供；

**[Er** ENOENT] 尝试删除不存在的对象时。此外，socket 操作本身可能因 socket(2)、recv(2) 或 send(2) 中指定的某种错误而失败

## 参见

[snl(3)](../man3/snl.3.md), [genetlink(4)](genetlink.4.md), [rtnetlink(4)](rtnetlink.4.md)

> J. Salim, H. Khosravi, A. Kleen, A. Kuznetsov, "Linux Netlink as an IP Services Protocol", RFC 3549.

## 历史

netlink 协议出现于 FreeBSD 13.2。

## 作者

netlink 由 Alexander Chernikov <melifaro@FreeBSD.org> 实现。它源自 Ng Peng Nam Sean 在 2021 年 Google Summer of Code 中的项目。
