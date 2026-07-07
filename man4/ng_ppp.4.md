# ng_ppp(4)

`ng_ppp` — PPP 协议 netgraph 节点类型

## 名称

`ng_ppp`

## 概要

`#include <sys/types.h>`

`#include <netgraph/ng_ppp.h>`

## 描述

`ppp` 节点类型为 PPP 协议执行多路复用。它仅处理包含数据的数据包，并将协议协商和控制数据包转发给单独的控制实体（例如用户态守护进程）。这种方式将内核实现的快速分派与用户态实现的配置灵活性相结合。PPP 节点类型直接支持多链路 PPP、Van Jacobson 压缩、PPP 压缩、PPP 加密，以及 IP、IPX 和 AppleTalk 协议。单个 PPP 节点对应一个 PPP 多链路束。

PPP 束中的每条 PPP 链路都有独立的钩子，此外还有若干与直接支持的协议相对应的钩子。对于压缩和加密，需要单独的附加节点来完成实际工作。所使用的节点类型取决于协商出的算法。还有一个 `bypass` 钩子，用于处理该节点不直接支持的任何协议。这包括所有控制协议：LCP、IPCP、CCP 等。通常此节点通过 [ng_socket(4)](ng_socket.4.md) 类型节点连接到用户态守护进程。

## 启用功能

一般情况下，当（a）收到启用它的 `NGM_PPP_SET_CONFIG` 消息，且（b）相应钩子已连接时，PPP 节点会启用特定链路或功能。这允许控制实体使用方法（a）或（b）（或两者）来控制节点行为。当链路已连接但被禁用时，流量仍可通过 `bypass` 钩子在该链路上流动（见下文）。

## 链路钩子

在正常操作期间，各 PPP 链路连接到钩子 `link0`、`link1` 等。最多支持 `NG_PPP_MAX_LINKS` 条链路。这些与设备无关的钩子传输和接收完整的 PPP 帧，包括 PPP 协议、地址、控制和信息字段，但不包括校验和或其他链路特定字段。

在出帧上，当已启用协议压缩且协议号适合压缩时，协议字段将被压缩（即作为一个字节而非两个字节发送）。入帧上既接受压缩的协议字段，也接受未压缩的协议字段。类似地，如果已为链路启用地址和控制字段压缩，则地址和控制字段将被省略（除标准要求的 LCP 帧外）。入帧上如果存在地址和控制字段，会自动被剥离。

由于所有协商都在 PPP 节点之外处理，链路在对应的链路进入网络阶段（即 LCP 协商和认证已成功完成）且通过 `NGM_PPP_LINK_CONFIG` 消息告知 PPP 节点链路参数之前，不应被连接和启用。

当链路已连接但被禁用时，所有接收到的帧将直接转发出 `bypass` 钩子，反之，帧也可通过 `bypass` 钩子发送。此模式适用于链路认证阶段。链路一旦被启用，PPP 节点将开始处理在该链路上接收到的帧。

## 压缩与加密

压缩通过 `compress` 和 `decompress` 两个钩子支持。可以通过切换节点配置结构中的 `enableCompression` 和 `enableDecompression` 字段来启用压缩和解压缩。（见下文。）如果 `enableCompression` 设置为 `NG_PPP_COMPRESS_SIMPLE`，则所有出帧都发送到 `compress` 钩子，且在此钩子上接收的所有数据包都被视为已压缩，因此会无条件地打上 COMPD 标签。如果 `enableCompression` 设置为 `NG_PPP_COMPRESS_FULL`，则在 `compress` 钩子上接收的数据包会被原样重发。压缩器节点应在数据包已被压缩时打上标签。如果 `enableDecompression` 设置为 `NG_PPP_DECOMPRESS_SIMPLE`，则节点只会将带有 COMPD 标签的帧发送到 `decompress` 钩子。如果 `enableDecompression` 设置为 `NG_PPP_DECOMPRESS_FULL`，则节点会将所有入站数据包发送到 `decompress` 钩子。通过将 `enableCompression` 和 `enableDecompression` 字段分别设置为 `NG_PPP_COMPRESS_NONE` 和 `NG_PPP_DECOMPRESS_NONE`，可完全禁用压缩和解压缩。

加密通过 `encrypt` 和 `decrypt` 节点以完全类似的方式工作。数据总是先压缩再加密，先解密再解压缩。

仅直接支持束级别的压缩和加密；链路级别的压缩和加密可由下游节点透明处理。

## Van Jacobson 压缩

当 `vjc_ip`、`vjc_vjcomp`、`vjc_vjuncomp` 和 `vjc_vjip` 四个钩子均已连接且对应的配置标志已启用时，Van Jacobson 压缩和/或解压缩将处于活动状态。通常这些钩子连接到单个 [ng_vjc(4)](ng_vjc.4.md) 节点的相应钩子。PPP 节点与 [ng_vjc(4)](ng_vjc.4.md) 节点类型的“直通”模式兼容。

## 旁路钩子

当在某条链路上接收到具有不受支持协议、被禁用协议或对应钩子未连接的协议的帧时，PPP 节点会将该帧加上四字节前缀后从 `bypass` 钩子转发出去。前缀的前两个字节表示接收到该帧的链路编号（按网络字节序）。对于通过束接收的此类帧（即封装在多链路协议中的帧），使用特殊链路编号 `NG_PPP_BUNDLE_LINKNUM`。两字节链路编号之后是两字节的 PPP 协议编号（同样按网络字节序）。即使原始帧的协议字段已被压缩，PPP 协议编号仍为两字节长。

反之，写入 `bypass` 钩子的任何数据都被假定为采用相同格式。四字节头部被剥离，PPP 协议编号被前置（可能被压缩），帧通过期望的链路投递。如果链路编号为 `NG_PPP_BUNDLE_LINKNUM`，帧将通过多链路束投递；或者，如果多链路被禁用，则通过（单条）PPP 链路投递。

通常，当控制实体在 `bypass` 钩子上收到意外数据包时，它会以丢弃该帧（如果尚未为该协议准备好）或发送 LCP 协议拒绝（如果不识别或未期望该协议）作为响应。

## 多链路操作

要启用多链路 PPP，必须设置相应的配置标志并至少连接一条链路。如果未启用多链路，PPP 节点不允许连接多条链路；多链路操作处于活动状态时也不允许更改某些多链路设置（例如短序列号头部格式）。

由于数据包以分片形式跨多条独立链路发送，当某条链路断开时，立即通过断开相应钩子或通过 `NGM_PPP_SET_CONFIG` 控制消息禁用该链路来通知 PPP 节点非常重要。

每条链路都有延迟（以毫秒为单位）和带宽（以每秒十字节为单位）配置参数。PPP 节点可配置为*轮询*或*优化*数据包投递。

当配置为轮询投递时，延迟和带宽值将被忽略，PPP 节点仅将每个帧作为单个分片发送，在束中的所有链路间交替发送帧。此方案的优点是即使某条链路静默失效，部分数据包仍能通过。其缺点是整体束延迟次优（这对交互式响应时间很重要），且当束中存在带宽不同的链路时整体束带宽也次优。

当配置为优化投递时，PPP 节点会以最小化完整数据包被对端接收所需时间的方式跨链路分发数据包。这涉及考虑每条链路的延迟、带宽和当前队列长度。因此这些数值应尽可能准确地配置。该算法确实需要一些计算，因此可能不适用于非常慢的机器和/或非常快的链路。

作为特例，如果所有链路具有相同的延迟和带宽，则上述算法将被禁用（因为不必要），PPP 节点仅将帧分片为大小相等的部分跨所有链路发送。

## 钩子

此节点类型支持以下钩子：

**`link<N>`** 独立 PPP 链路编号 `<N>`

**`compress`** 连接到压缩引擎

**`decompress`** 连接到解压缩引擎

**`encrypt`** 连接到加密引擎

**`decrypt`** 连接到解密引擎

**`vjc_ip`** 连接到 [ng_vjc(4)](ng_vjc.4.md) 的 `ip` 钩子

**`vjc_vjcomp`** 连接到 [ng_vjc(4)](ng_vjc.4.md) 的 `vjcomp` 钩子

**`vjc_vjuncomp`** 连接到 [ng_vjc(4)](ng_vjc.4.md) 的 `vjuncomp` 钩子

**`vjc_vjip`** 连接到 [ng_vjc(4)](ng_vjc.4.md) 的 `vjip` 钩子

**`inet`** IP 数据包数据

**`ipv6`** IPv6 数据包数据

**`atalk`** AppleTalk 数据包数据

**`ipx`** IPX 数据包数据

**`bypass`** 旁路钩子；帧带有四字节头部，由链路编号和 PPP 协议编号组成。

## 控制消息

此节点类型支持通用控制消息，此外还支持以下消息：

```sh
/* 单链路配置结构 */
struct ng_ppp_link_conf {
  u_char    enableLink;     /* 启用此链路 */
  u_char    enableProtoComp;/* 启用协议字段压缩 */
  u_char    enableACFComp;  /* 启用地址/控制字段压缩 */
  uint16_t  mru;            /* 对端 MRU */
  uint32_t  latency;        /* 链路延迟（毫秒） */
  uint32_t  bandwidth;      /* 链路带宽（字节/秒/10） */
};
/* 束配置结构 */
struct ng_ppp_bund_conf {
  uint16_t  mrru;                   /* 多链路对端 MRRU */
  u_char    enableMultilink;        /* 启用多链路 */
  u_char    recvShortSeq;           /* 接收多链路短序列号 */
  u_char    xmitShortSeq;           /* 发送多链路短序列号 */
  u_char    enableRoundRobin;       /* 发送完整数据包 */
  u_char    enableIP;               /* 启用 IP 数据流 */
  u_char    enableIPv6;             /* 启用 IPv6 数据流 */
  u_char    enableAtalk;            /* 启用 AppleTalk 数据流 */
  u_char    enableIPX;              /* 启用 IPX 数据流 */
  u_char    enableCompression;      /* 启用 PPP 压缩 */
  u_char    enableDecompression;    /* 启用 PPP 解压缩 */
  u_char    enableEncryption;       /* 启用 PPP 加密 */
  u_char    enableDecryption;       /* 启用 PPP 解密 */
  u_char    enableVJCompression;    /* 启用 VJ 压缩 */
  u_char    enableVJDecompression;  /* 启用 VJ 解压缩 */
};
struct ng_ppp_node_conf {
  struct ng_ppp_bund_conf   bund;
  struct ng_ppp_link_conf   links[NG_PPP_MAX_LINKS];
};
```

**`NGM_PPP_SET_CONFIG`**（`setconfig`）此命令配置节点的所有方面。包括启用多链路 PPP、加密、压缩、Van Jacobson 压缩，以及 IP、IPv6、AppleTalk 和 IPX 数据包投递。它包括每条链路的配置，包括启用链路、设置延迟和带宽参数，以及启用协议字段压缩。注意，在对应的钩子也连接上之前，任何链路或功能都不会处于活动状态。此命令以 `struct ng_ppp_node_conf` 作为参数：

**`NGM_PPP_GET_CONFIG`**（`getconfig`）以 `struct ng_ppp_node_conf` 形式返回当前配置。

**`NGM_PPP_GET_LINK_STATS`**（`getstats`）此命令以两字节链路编号作为参数，返回包含对应链路统计信息的 `struct ng_ppp_link_stat`。这里的 `NG_PPP_BUNDLE_LINKNUM` 是与多链路束对应的有效链路编号。

**`NGM_PPP_GET_LINK_STATS64`**（`getstats64`）与 NGM_PPP_GET_LINK_STATS 相同，但返回包含 64 位计数器的 `struct ng_ppp_link_stat64`。

**`NGM_PPP_CLR_LINK_STATS`**（`clrstats`）此命令以两字节链路编号作为参数，清零该链路的统计信息。

**`NGM_PPP_GETCLR_LINK_STATS`**（`getclrstats`）与 `NGM_PPP_GET_LINK_STATS` 相同，但同时会原子地清零统计信息。

**`NGM_PPP_GETCLR_LINK_STATS64`**（`getclrstats64`）与 NGM_PPP_GETCLR_LINK_STATS 相同，但返回包含 64 位计数器的 `struct ng_ppp_link_stat64`。

此节点类型还接受 [ng_vjc(4)](ng_vjc.4.md) 节点类型所接受的控制消息。收到时，这些消息会被简单地转发到相邻的 [ng_vjc(4)](ng_vjc.4.md) 节点（如果有）。这在各 PPP 链路能够生成 `NGM_VJC_RECV_ERROR` 消息时特别有用（详见 [ng_vjc(4)](ng_vjc.4.md) 的描述）。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或在所有钩子均已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), [ng_async(4)](ng_async.4.md), [ng_iface(4)](ng_iface.4.md), [ng_mppc(4)](ng_mppc.4.md), [ng_pppoe(4)](ng_pppoe.4.md), [ng_vjc(4)](ng_vjc.4.md), ngctl(8)

> W. Simpson, "The Point-to-Point Protocol (PPP)", RFC 1661.

> K. Sklower, B. Lloyd, G. McGregor, D. Carr, T. Coradetti, "The PPP Multilink Protocol (MP)", RFC 1990.

## 历史

`ppp` 节点类型实现于 FreeBSD 4.0。

## 作者

Archie Cobbs <archie@FreeBSD.org>
