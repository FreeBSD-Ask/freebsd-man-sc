# ng_pred1.4

`ng_pred1` — Predictor-1 PPP 压缩（RFC 1978）netgraph 节点类型

## 名称

`ng_pred1`

## 概要

`#include <sys/types.h>`

`#include <netgraph/ng_pred1.h>`

## 描述

`pred1` 节点类型实现压缩控制协议（CCP）的 Predictor-1 子协议。

该节点有两个钩子，`comp` 用于压缩，`decomp` 用于解压缩。同一时间只能连接其中一个，以指定节点的操作模式。通常这些钩子会连接到 [ng_ppp(4)](ng_ppp.4.md) 节点类型的同名钩子。

## 钩子

此节点类型支持以下钩子：

**`comp`** 连接到 [ng_ppp(4)](ng_ppp.4.md) 的 `compress` 钩子。入帧被压缩后从同一钩子发回。
**`decomp`** 连接到 [ng_ppp(4)](ng_ppp.4.md) 的 `decompress` 钩子。入帧被解压缩后从同一钩子发回。

同一时间只能连接一个钩子，以指定节点的操作模式。

## 控制消息

此节点类型支持通用控制消息，此外还支持以下消息：

```sh
struct ng_pred1_config {
	u_char		enable;			/* 节点已启用 */
};
```

```sh
struct ng_pred1_stats {
	uint64_t	FramesPlain;
	uint64_t	FramesComp;
	uint64_t	FramesUncomp;
	uint64_t	InOctets;
	uint64_t	OutOctets;
	uint64_t	Errors;
};
```

**`NGM_PRED1_CONFIG`**（`config`）此命令重置并为会话（即压缩或解压缩）配置节点。此命令以 `struct ng_pred1_config` 作为参数：`enable` 字段启用通过节点的流量。

**`NGM_PRED1_RESETREQ`**（`resetreq`）此消息不包含参数，是双向的。如果在解压缩过程中检测到错误，此消息会由节点发送给发起该会话的 `NGM_PRED1_CONFIG` 消息的发起者。接收者应通过向对端发送 PPP CCP Reset-Request 来响应。当本地 PPP 实体收到 CCP Reset-Request 或 Reset-Ack 时，此节点类型也可能收到此消息。节点会通过刷新其压缩状态来响应，以便双方可以重新同步。

**`NGM_PRED1_GET_STATS`**（`getstats`）此控制消息获取给定钩子的统计信息。统计信息以 `struct ng_pred1_stats` 形式返回：

**`NGM_PRED1_CLR_STATS`**（`clrstats`）此控制消息清零给定钩子的统计信息。

**`NGM_PRED1_GETCLR_STATS`**（`getclrstats`）此控制消息获取并清零给定钩子的统计信息。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或在钩子已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), [ng_ppp(4)](ng_ppp.4.md), ngctl(8)

> D. Rand, "PPP Predictor Compression Protocol", RFC 1978.

> W. Simpson, "The Point-to-Point Protocol (PPP)", RFC 1661.

## 作者

Alexander Motin <mav@alkar.net>

## 缺陷

由于 netgraph PPP 实现的特性，在数据包丢失的情况下，数据包与 ResetAck CCP 数据包之间可能存在竞态条件。结果是，数据包丢失可能造成比协议所预期更大的性能下降。
