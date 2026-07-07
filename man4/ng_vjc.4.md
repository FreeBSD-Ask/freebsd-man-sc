# ng_vjc(4)

`ng_vjc` — Van Jacobson 压缩 netgraph 节点类型

## 名称

`ng_vjc`

## 概要

`#include <sys/types.h>`

`#include <netinet/in.h>`

`#include <netinet/in_systm.h>`

`#include <netinet/ip.h>`

`#include <net/slcompress.h>`

`#include <netgraph/ng_vjc.h>`

## 描述

`vjc` 节点类型执行 Van Jacobson 压缩，用于在 PPP、SLIP 和其他点到点 IP 连接上压缩 TCP 数据包头。`ip` 钩子代表节点的未压缩侧，而 `vjcomp`、`vjuncomp` 和 `vjip` 钩子代表节点的压缩侧。在 `ip` 上接收的数据包将视情况被压缩或直通。在其他三个钩子上接收的数据包将视情况被解压缩。此节点还在任一方向上支持“始终直通”模式。

Van Jacobson 压缩仅适用于 TCP 数据包。只有“正常”（即常见情况）TCP 数据包会被实际压缩，这些数据包从 `vjcomp` 钩子输出。其他 TCP 数据包会经过状态机但不被压缩，这些数据包出现在 `vjuncomp` 钩子上。其他非 TCP IP 数据包原样转发到 `vjip`。

当连接到 [ng_ppp(4)](ng_ppp.4.md) 节点时，`ip`、`vjuncomp`、`vjcomp` 和 `vjip` 钩子应分别连接到 [ng_ppp(4)](ng_ppp.4.md) 节点的 `vjc_ip`、`vjc_vjcomp`、`vjc_vjuncomp` 和 `vjc_ip` 钩子。

## 钩子

此节点类型支持以下钩子：

**`ip`** 上游（未压缩）IP 数据包。

**`vjcomp`** 下游已压缩 TCP 数据包。

**`vjuncomp`** 下游未压缩 TCP 数据包。

**`vjip`** 下游未压缩 IP 数据包。

## 控制消息

此节点类型支持通用控制消息，此外还支持以下消息：

```sh
struct ngm_vjc_config {
  u_char   enableComp;    /* 启用压缩 */
  u_char   enableDecomp;  /* 启用解压缩 */
  u_char   maxChannel;    /* 出站通道数 - 1 */
  u_char   compressCID;   /* 可以压缩出站 CID */
};
```

`#include <net/slcompress.h>`

**`NGM_VJC_SET_CONFIG`**（`setconfig`）此命令重置压缩状态并根据提供的 `struct ngm_vjc_config` 参数对其进行配置。此结构包含以下字段：当 `enableComp` 设置为零时，所有在 `ip` 钩子上接收的数据包原样从 `vjip` 钩子转发出去。类似地，当 `enableDecomp` 设置为零时，所有在 `vjip` 钩子上接收的数据包原样从 `ip` 钩子转发出去，且 `vjcomp` 和 `vjuncomp` 钩子上不接受数据包。节点首次创建时，压缩和解压缩均被禁用，因此节点处于双向“直通”模式。启用压缩时，`maxChannel` 应设置为出站压缩通道数减一，取值范围在 3 到 15（含）之间。`compressCID` 字段指示是否可以压缩出站已压缩 TCP 数据包的 CID 头部字段。除非（a）出站帧不可能丢失，或（b）丢失的帧可以被可靠检测并立即报告给对端的解压缩引擎（见下文 `NGM_VJC_RECV_ERROR`），否则此值应为零。

**`NGM_VJC_GET_STATE`**（`getstate`）此命令返回由 `struct slcompress` 结构描述的节点当前状态，该结构定义于

**`NGM_VJC_CLR_STATS`**（`clrstats`）清零节点统计计数器。每当 `enableComp` 或 `enableDecomp` 字段由 `NGM_VJC_SET_CONFIG` 控制消息从零变为一时，统计信息也会被清零。

**`NGM_VJC_RECV_ERROR`**（`recverror`）当对端启用了 CID 头部字段压缩时，在检测到接收到的帧因校验和错误或任何其他原因丢失后，必须立即将此消息发送给本地 `vjc` 节点。未这样做可能导致 TCP 流数据损坏。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或在所有钩子均已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), [ng_iface(4)](ng_iface.4.md), [ng_ppp(4)](ng_ppp.4.md), ngctl(8)

> V. Jacobson, "Compressing TCP/IP Headers", RFC 1144.

> G. McGregor, "The PPP Internet Control Protocol (IPCP)", RFC 1332.

## 历史

`vjc` 节点类型实现于 FreeBSD 4.0。

## 作者

Archie Cobbs <archie@FreeBSD.org>

## 缺陷

由于 Van Jacobson 压缩的内核实现中的初始化例程会同时初始化压缩和解压缩，此节点不允许在单独的操作中分别启用压缩和解压缩。要在已启用其中一个时启用另一个，必须先禁用两者，然后再启用两者。这当然会重置节点状态。此限制可能在以后版本中被移除。

作为可加载内核模块构建时，此模块包含文件 `net/slcompress.c`。虽然如果 `net/slcompress.c` 已存在于内核中，加载此模块应失败，但目前不会，且重复的文件副本不会相互干扰。但是，这在未来可能发生变化。
