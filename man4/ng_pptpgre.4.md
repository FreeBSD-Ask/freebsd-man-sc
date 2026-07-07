# ng_pptpgre(4)

`ng_pptpgre` — PPTP GRE 协议 netgraph 节点类型

## 名称

`ng_pptpgre`

## 概要

`#include <sys/types.h>`

`#include <netgraph/ng_pptpgre.h>`

## 描述

`pptpgre` 节点类型按 RFC 2637 规定为 PPTP 协议在 IP 上执行通用路由封装（GRE）。这涉及数据包封装、排序、确认以及自适应超时滑动窗口机制。此节点类型不处理 PPTP 定义的任何 TCP 控制协议或呼叫协商。

此节点类型期望在“`lower`”钩子上接收包括 IP 头部在内的完整 IP 数据包，但传输出站帧时不带任何 IP 头部。此节点类型的典型用法是将“`upper`”钩子连接到 [ng_ppp(4)](ng_ppp.4.md) 节点的某个链路钩子，将“`lower`”钩子连接到 [ng_ksocket(4)](ng_ksocket.4.md) 节点的“`inet/raw/gre`”钩子。

## 钩子

此节点类型支持以下钩子：

**`session_hhhh`** 会话 0xhhhh 数据包到上层协议

**`upper`** 与 session_hhhh 相同，但用于具有可配置 cid 的单一会话（旧式）

**`lower`** 到下层协议的连接

## 控制消息

此节点类型支持通用控制消息，此外还支持以下消息：

```sh
/* 会话配置 */
struct ng_pptpgre_conf {
    u_char      enabled;          /* 启用流量 */
    u_char      enableDelayedAck; /* 启用延迟确认 */
    u_char      enableAlwaysAck;  /* 总是随数据附带确认 */
    u_char      enableWindowing;  /* 启用窗口算法 */
    uint16_t    cid;              /* 我的呼叫 ID */
    uint16_t    peerCid;          /* 对端呼叫 ID */
    uint16_t    recvWin;          /* 对端接收窗口大小 */
    uint16_t    peerPpd;          /* 对端数据包处理延迟
                                     （以 1/10 秒为单位） */
};
```

**`NGM_PPTPGRE_SET_CONFIG`**（`setconfig`）此命令重置并配置会话的钩子。如果对应的 session_hhhh 钩子未连接，则配置 upper 钩子。此命令以 `struct ng_pptpgre_conf` 作为参数：`enabled` 字段启用通过节点的流量。`enableDelayedAck` 字段启用延迟确认（最多 250 毫秒），这是一种有用的优化，通常应开启。`enableAlwaysAck` 字段启用随每个数据包发送确认，这可能也有帮助。`enableWindowing` 启用协议规定的 PPTP 数据包窗口机制。禁用此项会导致节点违反协议，可能使其他 PPTP 对端混乱，但通常会带来更好的性能。窗口机制是 PPTP 协议中的设计错误；PPTP 的后继者 L2TP 移除了它。其余字段由 PPTP 虚呼叫建立过程提供。

**`NGM_PPTPGRE_GET_CONFIG`**（`getconfig`）以两字节参数作为 cid，并以 `struct ng_pptpgre_conf` 形式返回当前配置。

**`NGM_PPTPGRE_GET_STATS`**（`getstats`）此命令返回包含各种节点统计信息的 `struct ng_pptpgre_stats`。

**`NGM_PPTPGRE_CLR_STATS`**（`clrstats`）此命令重置节点统计信息。

**`NGM_PPTPGRE_GETCLR_STATS`**（`getclrstats`）此命令原子地获取并重置节点统计信息，返回 `struct ng_pptpgre_stats`。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或在两个钩子均已断开时关闭。

## SYSCTL 变量

一组 [sysctl(8)](../man8/sysctl.8.md) 变量控制此节点处理传输中有时发生的少量数据包重排序的能力。数据包重排序会导致数据包丢弃（除非恢复顺序），因为 PPP 协议无法投递重排序的数据。这些变量及其默认值和含义如下所示：

**`net.graph.pptpgre.reorder_max: 1`** 定义节点的私有重排序队列的最大长度，用于保存等待迟到数据包的数据。零值禁用重排序。默认值允许节点恢复在传输中被交换的两个数据包的顺序。更大的值允许节点投递在序列中落后更多数据包的迟到数据包，但会增加内核内存使用。

**`net.graph.pptpgre.reorder_timeout: 1`** 定义用于等待迟到数据包的时间值（以毫秒为单位）。

## 参见

[netgraph(4)](netgraph.4.md), [ng_ksocket(4)](ng_ksocket.4.md), [ng_ppp(4)](ng_ppp.4.md), ngctl(8), [sysctl(8)](../man8/sysctl.8.md)

> K. Hamzeh, G. Pall, W. Verthein, J. Taarud, W. Little, G. Zorn, "Point-to-Point Tunneling Protocol (PPTP)", RFC 2637.

> S. Hanks, T. Li, D. Farinacci, P. Traina, "Generic Routing Encapsulation over IPv4 networks", RFC 1702.

## 历史

`pptpgre` 节点类型实现于 FreeBSD 4.0。

## 作者

Archie Cobbs <archie@FreeBSD.org>

## 缺陷

节点不应期望传入的 GRE 数据包带有 IP 头部。此行为继承自原始 IP 套接字的（反向）行为。应使用一个在另一个方向上剥离 IP 头部的中间节点。
