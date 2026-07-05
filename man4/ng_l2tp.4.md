# ng_l2tp.4

`ng_l2tp` — L2TP 协议 netgraph 节点类型

## 名称

`ng_l2tp`

## 概要

`#include <sys/types.h>`

`#include <netgraph/ng_l2tp.h>`

## 描述

`l2tp` 节点类型实现 RFC 2661 中描述的 L2TP 协议封装层。包括为传出数据包添加 L2TP 包头，以及为传入数据包验证并移除包头。节点维护 L2TP 序列号状态，并处理控制会话数据包的确认和重传。

## 钩子

`l2tp` 节点类型支持以下钩子：

**`lower`** L2TP 帧。

**`ctrl`** 控制数据包。

**`session_hhhh`** 会话 0xhhhh 数据包。

L2TP 控制和数据包通过 `lower` 钩子传输到 L2TP 对端并从中接收。通常此钩子会连接到 [ng_ksocket(4)](ng_ksocket.4.md) 节点的 `inet/dgram/udp` 钩子以实现基于 UDP 的 L2TP。

`ctrl` 钩子连接到本地 L2TP 管理实体。L2TP 控制消息（不带任何 L2TP 头部）通过此钩子发送和接收。写入此钩子的消息保证可靠、有序且无重复地交付给对端。

写入 `ctrl` 钩子的数据包必须包含一个前置的两字节会话 ID（网络字节序）。此会话 ID 会被复制到发出的 L2TP 头部。同样，从 `ctrl` 钩子读取的数据包会带有接收到的会话 ID 作为前缀。

一旦 L2TP 会话创建，相应的会话钩子可用于发送和接收该会话的数据帧：对于会话 ID 为 `0xabcd` 的会话，钩子名为 `session_abcd`。

## 控制消息

本节点类型支持通用控制消息，以及以下消息：

```sh
/* 节点配置 */
struct ng_l2tp_config {
    u_char      enabled;        /* 启用流量 */
    u_char      match_id;       /* 隧道 ID 必须匹配 'tunnel_id' */
    uint16_t    tunnel_id;      /* 本地隧道 ID */
    uint16_t    peer_id;        /* 对端隧道 ID */
    uint16_t    peer_win;       /* 对端最大接收窗口大小 */
    uint16_t    rexmit_max;     /* 失败前的最大重传次数 */
    uint16_t    rexmit_max_to;  /* 重传之间的最大延迟 */
};
```

```sh
/* 会话钩子配置 */
struct ng_l2tp_sess_config {
    uint16_t    session_id;     /* 本地会话 ID */
    uint16_t    peer_id;        /* 对端会话 ID */
    u_char      control_dseq;   /* 是否由我们控制数据序列 */
    u_char      enable_dseq;    /* 是否启用数据序列 */
    u_char      include_length; /* 是否包含长度字段 */
};
```

**`NGM_L2TP_SET_CONFIG`** (`setconfig`) 此命令更新节点配置。它接受 `struct ng_l2tp_config` 作为参数：`enabled` 字段启用数据包处理。每次将此字段改回零时，序列号状态都会被重置。这样可以重用节点。`tunnel_id` 字段配置控制连接的本地隧道 ID。`match_id` 字段确定如何处理隧道 ID 字段不同于 `tunnel_id` 的传入 L2TP 数据包。如果 `match_id` 为非零，它们将被丢弃；否则，仅在隧道 ID 为非零时才丢弃。通常 `tunnel_id` 在知道后立即设置为本地隧道 ID，`match_id` 在收到 SCCRP 或 SCCCN 控制消息后设置为非零。对端的隧道 ID 应在获知后立即设置到 `peer_id`，通常在收到 SCCRQ 或 SCCRP 控制消息后。此值会被复制到传出数据包的 L2TP 头部。`peer_win` 字段应从对端接收的“接收窗口大小”AVP 设置。此字段的默认值为 1；零为无效值。只要 `enabled` 为非零，此值不能减小。`rexmit_max` 和 `rexmit_max_to` 字段配置数据包重传。`rexmit_max_to` 是数据包之间的最大重传延迟（秒）。重传延迟从一个较小的值开始，并指数增长到此限制。`rexmit_max` 设置在宣布故障条件之前数据包未被确认的最大重传次数。一旦宣布故障条件，每次额外重传都会使 `l2tp` 节点向发送最后一条 `NGM_L2TP_SET_CONFIG` 的节点发回 `NGM_L2TP_ACK_FAILURE` (`ackfailure`) 控制消息。然后应采取适当措施关闭控制连接。

**`NGM_L2TP_GET_CONFIG`** (`getconfig`) 以 `struct ng_l2tp_config` 形式返回当前配置。

**`NGM_L2TP_SET_SESS_CONFIG`** (`setsessconfig`) 此控制消息配置单个数据会话。在发送此命令之前必须已连接相应的钩子。参数为 `struct ng_l2tp_sess_config`：`session_id` 和 `peer_id` 字段分别配置本地和远程会话 ID。`control_dseq` 和 `enable_dseq` 字段确定是否在 L2TP 数据包中使用序列号。如果 `enable_dseq` 为零，则不发送序列号并忽略传入的序列号。否则，发出数据包包含序列号并检查传入数据包的序列号。如果 `control_dseq` 为非零，则 `enable_dseq` 的设置永远不会更改，除非通过另一条 `NGM_L2TP_SET_SESS_CONFIG` 控制消息。如果 `control_dseq` 为零，则由对端控制是否使用序列号：如果传入 L2TP 数据包包含序列号，`enable_dseq` 设置为 1，反之如果传入 L2TP 数据包不包含序列号，`enable_dseq` 设置为零。`enable_dseq` 的当前值始终可以通过 `NGM_L2TP_GET_SESS_CONFIG` 控制消息访问（见下文）。通常 LNS 会将 `control_dseq` 设置为 1，而 LAC 会将 `control_dseq` 设置为零（如果未发送 Sequencing Required AVP），从而将数据包序列的控制权交给 LNS。`include_length` 字段确定发出的 L2TP 数据包中是否包含 L2TP 头部长度字段。对于传入数据包，存在 L2TP 长度字段时始终会进行检查。

**`NGM_L2TP_GET_SESS_CONFIG`** (`getsessconfig`) 此命令接受两字节会话 ID 作为参数，并以 `struct ng_l2tp_sess_config` 形式返回相应数据会话的当前配置。相应的会话钩子必须已连接。

**`NGM_L2TP_GET_STATS`** (`getstats`) 此命令返回包含 L2TP 隧道统计信息的 `struct ng_l2tp_stats`。

**`NGM_L2TP_CLR_STATS`** (`clrstats`) 此命令清除 L2TP 隧道的统计信息。

**`NGM_L2TP_GETCLR_STATS`** (`getclrstats`) 与 `NGM_L2TP_GET_STATS` 相同，但同时原子性地清除统计信息。

**`NGM_L2TP_GET_SESSION_STATS`** (`getsessstats`) 此命令接受两字节会话 ID 作为参数，并返回包含相应数据会话统计信息的 `struct ng_l2tp_session_stats`。相应的会话钩子必须已连接。

**`NGM_L2TP_CLR_SESSION_STATS`** (`clrsessstats`) 此命令接受两字节会话 ID 作为参数，并清除该数据会话的统计信息。相应的会话钩子必须已连接。

**`NGM_L2TP_GETCLR_SESSION_STATS`** (`getclrsessstats`) 与 `NGM_L2TP_GET_SESSION_STATS` 相同，但同时原子性地清除统计信息。

**`NGM_L2TP_SET_SEQ`** (`setsequence`) 此命令设置尚未启用节点的序列号。它接受 `struct ng_l2tp_seq_config` 作为参数，其中 `xack` 和 `nr` 必须分别与 `ns` 和 `rack` 相同。如果在用户空间完全接收并处理了第一个数据包，并希望将后续处理交给节点，此选项特别有用。

## 关闭

本节点在收到 `NGM_SHUTDOWN` 控制消息时关闭，或在所有钩子都已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), [ng_ksocket(4)](ng_ksocket.4.md), [ng_ppp(4)](ng_ppp.4.md), [ng_pptpgre(4)](ng_pptpgre.4.md), ngctl(8)

> W. Townsley, A. Valencia, A. Rubens, G. Pall, G. Zorn, B. Palter, "Layer Two Tunneling Protocol L2TP", RFC 2661.

## 历史

`l2tp` 节点类型由 Packet Design, LLC (`http://www.packetdesign.com/`) 开发。

## 作者

Archie Cobbs <archie@packetdesign.com>
