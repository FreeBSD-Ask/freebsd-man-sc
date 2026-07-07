# ng_iface(4)

`ng_iface` — 接口 netgraph 节点类型

## 名称

`ng_iface`

## 概要

`#include <netgraph/ng_iface.h>`

## 描述

`iface` 节点既是 netgraph 节点，也是系统网络接口。创建 `iface` 节点时，会出现一个新接口，可通过 [ifconfig(8)](../man8/ifconfig.8.md) 访问。`iface` 节点接口命名为 `ng0`、`ng1` 等。当节点关闭时，相应的接口被移除，接口名称可供将来的 `iface` 节点重用；新节点始终使用第一个未使用的接口。节点本身会被分配与其接口相同的名称，除非该名称已存在，这种情况下节点保持未命名状态。

`iface` 节点对每个支持的协议都有一个对应的钩子。通过接口发送的数据包从相应的协议特定钩子流出。同样，在钩子上收到的数据包会作为接收到的数据包出现在接口上，进入相应的协议栈。目前支持的协议是 IP 和 IPv6。

`iface` 节点可以配置为点对点接口或广播接口。只有在接口处于 down 状态时才能更改配置。默认模式为点对点。

`iface` 节点支持 Berkeley 包过滤器（BPF）。

## 钩子

本节点类型支持以下钩子：

**`inet`** IP 数据包的发送和接收。

**`inet6`** IPv6 数据包的发送和接收。

## 控制消息

本节点类型支持通用控制消息，以及以下消息：

**`NGM_IFACE_GET_IFNAME`** (`getifname`) 以 `NUL` 结尾的 ASCII 字符串形式返回关联接口的名称。通常与节点名称相同。

**`NGM_IFACE_GET_IFINDEX`** (`getifindex`) 以 32 位整数形式返回关联接口的全局索引。

**`NGM_IFACE_POINT2POINT`** (`point2point`) 将接口设置为点对点模式。接口当前必须处于 down 状态。

**`NGM_IFACE_BROADCAST`** (`broadcast`) 将接口设置为广播模式。接口当前必须处于 down 状态。

## 关闭

本节点在收到 `NGM_SHUTDOWN` 控制消息时关闭。关联的接口被移除，并可供将来的 `iface` 节点使用。

与大多数其他节点类型不同，当所有钩子都已断开时，`iface` 节点*不会*消失；而是需要显式的 `NGM_SHUTDOWN` 控制消息。

## ALTQ 支持

`iface` 接口支持 ALTQ 带宽管理功能。但 `iface` 是一种特殊情况，因为它不是带宽有限的物理接口。如果 `iface` 对应于某种隧道连接（如 PPPoE 或 PPTP），则不应在其上启用 ALTQ。这种情况下，应在用于传输封装数据包的接口上配置 ALTQ。如果图最终连接到某种串行线路（同步或调制解调器），则 `iface` 是启用 ALTQ 的合适位置。

## 嵌套

`iface` 支持嵌套，即一个 `iface` 接口的流量流经另一个 `iface` 接口的配置。默认的最大允许嵌套级别为 2。可在运行时通过将 [sysctl(8)](../man8/sysctl.8.md) 变量 `net.graph.iface.max_nesting` 设置为所需的嵌套级别来更改。

## 参见

[altq(4)](altq.4.md), [bpf(4)](bpf.4.md), [netgraph(4)](netgraph.4.md), [ng_cisco(4)](ng_cisco.4.md), [ifconfig(8)](../man8/ifconfig.8.md), ngctl(8), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`iface` 节点类型实现于 FreeBSD 4.0。

## 作者

Archie Cobbs <archie@FreeBSD.org>
