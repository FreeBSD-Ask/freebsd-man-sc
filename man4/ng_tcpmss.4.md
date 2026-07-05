# ng_tcpmss.4

`ng_tcpmss` — 调整 TCP MSS 选项的 netgraph 节点

## 名称

`ng_tcpmss`

## 概要

`#include <netgraph.h>`

`#include <netgraph/ng_tcpmss.h>`

## 描述

`tcpmss` 节点类型用于修改 TCP 数据包的最大段大小（Maximum Segment Size）选项。此节点接受任意数量的钩子。新钩子初始被视为未配置。使用 `NG_TCPMSS_CONFIG` 控制消息配置钩子。

## 控制消息

此节点类型支持通用控制消息，此外还支持以下消息。

```sh
struct ng_tcpmss_config {
	char		inHook[NG_HOOKSIZ];
	char		outHook[NG_HOOKSIZ];
	uint16_t	maxMSS;
}
```

```sh
struct ng_tcpmss_hookstat {
	uint64_t	Octets;		/* 总字节数 */
	uint64_t	Packets;	/* 总数据包数 */
	uint16_t	maxMSS;		/* 最大 MSS */
	uint64_t	SYNPkts;	/* TCP SYN 数据包 */
	uint64_t	FixedPkts;	/* 已更改的数据包 */
};
```

**`NGM_TCPMSS_CONFIG`**（`config`）此控制消息配置节点以在特定钩子上执行给定的 MSS 调整。它要求以 `struct ng_tcpmss_config` 作为参数：含义为：在 `inHook` 上接收的数据包将检查 TCP MSS 选项，如果超过 `maxMSS` 则将其降低到 `maxMSS`。之后，数据包将发送到钩子 `outHook`。

**`NGM_TCPMSS_GET_STATS`**（`getstats`）此控制消息获取给定钩子的统计信息。统计信息以 `struct ng_tcpmss_hookstat` 形式返回：

**`NGM_TCPMSS_CLR_STATS`**（`clrstats`）此控制消息清零给定钩子的统计信息。

**`NGM_TCPMSS_GETCLR_STATS`**（`getclrstats`）此控制消息获取并清零给定钩子的统计信息。

## 实例

在以下示例中，使用 [ng_ipfw(4)](ng_ipfw.4.md) 节点将数据包注入到 `tcpmss` 节点。

```sh
# 创建 tcpmss 节点并将其连接到 ng_ipfw 节点
ngctl mkpeer ipfw: tcpmss 100 qqq
# 将 MSS 调整为 1452
ngctl msg ipfw:100 config '{ inHook="qqq" outHook="qqq" maxMSS=1452 }'
# 将流量分流到 tcpmss 节点
ipfw add 300 netgraph 100 tcp from any to any tcpflags syn out via fxp0
# 让数据包在被修改后继续在 ipfw 中处理
sysctl net.inet.ip.fw.one_pass=0
```

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或在所有钩子均已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), [ng_ipfw(4)](ng_ipfw.4.md)

## 历史

`tcpmss` 节点类型实现于 FreeBSD 6.0。

## 作者

Alexey Popov <lollypop@flexuser.ru> Gleb Smirnoff <glebius@FreeBSD.org>

## 缺陷

在 SMP 上运行时，系统统计信息可能损坏。
