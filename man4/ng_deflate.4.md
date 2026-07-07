# ng_deflate(4)

`ng_deflate` — Deflate PPP 压缩（RFC 1979）netgraph 节点类型

## 名称

`ng_deflate`

## 概要

`#include <sys/types.h>`

`#include <netgraph/ng_deflate.h>`

## 描述

`deflate` 节点类型实现了压缩控制协议（CCP）的 Deflate 子协议。

节点有两个钩子：用于压缩的 `comp` 和用于解压缩的 `decomp`。同一时间只能连接其中一个，指定节点的操作模式。通常这些钩子会连接到 [ng_ppp(4)](ng_ppp.4.md) 节点类型的同名钩子。相应的 [ng_ppp(4)](ng_ppp.4.md) 节点钩子必须切换到 `NG_PPP_DECOMPRESS_FULL` 模式以允许发送未压缩帧。

## 钩子

此节点类型支持以下钩子：

**`comp`** 连接到 [ng_ppp(4)](ng_ppp.4.md) `comp` 钩子。传入帧（如果可能）被压缩并从同一钩子发回。
**`decomp`** 连接到 [ng_ppp(4)](ng_ppp.4.md) `decomp` 钩子。传入帧（如果已压缩）被解压缩并从同一钩子发回。

同一时间只能连接一个钩子，指定节点的操作模式。

## 控制消息

此节点类型支持通用控制消息，外加以下消息：

```sh
struct ng_deflate_config {
	u_char	enable;			/* 节点已启用 */
	u_char	windowBits;		/* log2(窗口大小) */
};
```

```sh
struct ng_deflate_stats {
	uint64_t	FramesPlain;
	uint64_t	FramesComp;
	uint64_t	FramesUncomp;
	uint64_t	InOctets;
	uint64_t	OutOctets;
	uint64_t	Errors;
};
```

**`NGM_DEFLATE_CONFIG`** (`config`) 此命令重置并为会话（即压缩或解压缩）配置节点。此命令以 `struct ng_deflate_config` 为参数：`enabled` 字段启用通过节点的流量。`windowBits` 指定由 PPP 中压缩控制协议（CCP）协商的压缩窗口大小。

**`NGM_DEFLATE_RESETREQ`** (`resetreq`) 此消息不含参数，且是双向的。如果在解压缩期间检测到错误，此消息由节点发送给发起该会话的 `NGM_DEFLATE_CONFIG` 消息的发起者。接收者应通过向对等方发送 PPP CCP Reset-Request 来响应。当本地 PPP 实体收到 CCP Reset-Request 或 Reset-Ack 时，此消息也可能被此节点类型接收。节点将通过刷新其压缩状态来响应，以便双方可以重新同步。

**`NGM_DEFLATE_GET_STATS`** (`getstats`) 此控制消息获取给定钩子的统计信息。统计信息以 `struct ng_deflate_stats` 返回：

**`NGM_DEFLATE_CLR_STATS`** (`clrstats`) 此控制消息清除给定钩子的统计信息。

**`NGM_DEFLATE_GETCLR_STATS`** (`getclrstats`) 此控制消息获取并清除给定钩子的统计信息。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或当钩子已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), [ng_ppp(4)](ng_ppp.4.md), ngctl(8)

> J. Woods, "PPP Deflate Protocol", RFC 1979.

> W. Simpson, "The Point-to-Point Protocol (PPP)", RFC 1661.

## 作者

Alexander Motin <mav@alkar.net>

## 缺陷

由于 netgraph PPP 实现的性质，在数据包丢失的情况下，数据包与 ResetAck CCP 数据包之间可能存在竞态条件。结果，数据包丢失可能产生比协议预期的更大的性能下降。
