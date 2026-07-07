# ng_bridge(4)

`ng_bridge` — 以太网桥接 netgraph 节点类型

## 名称

`ng_bridge`

## 概要

`#include <sys/types.h>`

`#include <netgraph/ng_bridge.h>`

## 描述

`bridge` 节点类型在一个或多个链路上执行以太网桥接。每个链路（由已连接的钩子表示）用于发送和接收原始以太网帧。在接收数据包时，节点学习每个主机所在的链路。已知主机的单播数据包仅从相应链路发出，其他链路免受此流量影响。此行为与集线器形成对比，后者始终将每个接收到的数据包转发到其他所有链路。

## 环路检测

`bridge` 节点结合了简单的环路检测算法。环路指两个端口连接到同一物理介质。环路必须避免，因为数据包风暴会严重降低性能。当同一数据包被反复发送和接收时就会产生数据包风暴。如果在链路 A 上检测到主机，然后在该主机首次在链路 A 上被检测到的一定时间段内在链路 B 上被检测到，则链路 B 被视为环回链路。该时间段称为最小稳定时间。

环回链路将被临时静音，即在该链路上接收的所有流量都被忽略。

## IPFW 处理

通过 [ipfirewall(4)](ipfirewall.4.md) 机制按链路处理 IP 数据包尚未实现。

## 钩子

此节点类型支持无限数量的钩子。每个已连接的钩子代表一个桥接链路。钩子命名为 `link0`、`link1` 等。通常这些钩子连接到一个或多个 [ng_ether(4)](ng_ether.4.md) 节点的 `lower` 钩子。要将主机连接到桥接网络，只需将 [ng_ether(4)](ng_ether.4.md) 节点的 `upper` 钩子连接到桥接节点。

除了将钩子命名为 `linkX`，钩子也可命名为 `uplinkX`。节点不在 uplink 钩子上学习 MAC 地址，这使内部地址表保持较小。因此，将 [ng_ether(4)](ng_ether.4.md) 节点的 `lower` 钩子连接到桥接的 `uplink` 钩子，并忽略外部世界的复杂性是可取的。带有未知 MAC 的帧始终发送到 `uplink` 钩子，因此不会丢失功能。`uplink0` 钩子是不允许的。

`linkX` 和 `uplinkX` 钩子编号可自动分配。如果新钩子名指定为 `link` 或 `uplink`，节点会将最低可用有效编号附加到新钩子的名称后。

具有未知目标 MAC 地址的帧被复制到任何可用钩子，除非第一个连接的钩子是 `uplink` 钩子。在这种情况下，节点假定所有未知 MAC 地址仅位于 `uplink` 钩子上，且仅这些钩子将用于发送具有未知目标 MAC 的帧。如果第一个连接的钩子是 `link` 钩子，节点将此类帧复制到所有类型的钩子，即使稍后连接了 `uplink` 钩子。

## 控制消息

此节点类型支持通用控制消息，外加以下消息：

```sh
/* 节点配置结构 */
struct ng_bridge_config {
  u_char      debugLevel;           /* 调试级别 */
  uint32_t    loopTimeout;          /* 链路环回静音时间 */
  uint32_t    maxStaleness;         /* 主机被清除前的最大老化时间 */
  uint32_t    minStableAge;         /* 稳定主机的最短时间 */
};
```

```sh
/* 统计结构（每个链路一个） */
struct ng_bridge_link_stats {
  uint64_t   recvOctets;     /* 链路上接收的总八位组数 */
  uint64_t   recvPackets;    /* 链路上接收的总包数 */
  uint64_t   recvMulticasts; /* 链路上接收的多播包数 */
  uint64_t   recvBroadcasts; /* 链路上接收的广播包数 */
  uint64_t   recvUnknown;    /* 接收的具有未知目标地址的包数 */
  uint64_t   recvRunts;      /* 接收的小于 14 字节的包数 */
  uint64_t   recvInvalid;    /* 接收的具有伪造源地址的包数 */
  uint64_t   xmitOctets;     /* 链路上发送的总八位组数 */
  uint64_t   xmitPackets;    /* 链路上发送的总包数 */
  uint64_t   xmitMulticasts; /* 链路上发送的多播包数 */
  uint64_t   xmitBroadcasts; /* 链路上发送的广播包数 */
  uint64_t   loopDrops;      /* 因环回而丢弃的包数 */
  uint64_t   loopDetects;    /* 环路检测次数 */
  uint64_t   memoryFailures; /* 无法获取内存或 mbuf 的次数 */
};
```

```sh
struct ng_bridge_move_host {
  u_char  addr[ETHER_ADDR_LEN];	/* 以太网地址 */
  char    hook[NG_HOOKSIZ];	/* 可找到 addr 的链路 */
};
```

**`NGM_BRIDGE_SET_CONFIG`** (`setconfig`) 设置节点配置。此命令以 `struct ng_bridge_config` 为参数：`debugLevel` 字段设置节点的调试级别。级别为 2 或更高时，检测到的环路会被记录。默认级别为 1。`loopTimeout` 确定环回链路被静音的时间长度（以秒为单位）。默认为 60 秒。`maxStaleness` 参数确定主机条目被遗忘之前的不活动时间长度。默认为 15 分钟。`minStableAge` 确定主机必须从一个链路跳到另一个链路多快才会被声明为环回状态。默认为一秒。

**`NGM_BRIDGE_GET_CONFIG`** (`getconfig`) 返回当前配置，作为 `struct ng_bridge_config`。

**`NGM_BRIDGE_RESET`** (`reset`) 使节点忘记所有主机并取消静音所有链路。节点配置不会更改。

**`NGM_BRIDGE_GET_STATS`** (`getstats`) 此命令以四字节链路号为参数，返回包含相应 `link` 统计信息的 `struct ng_bridge_link_stats`，该链路必须当前已连接：负数指 `uplink` 钩子。因此查询 -7 将获取钩子 `uplink7` 的统计信息。

**`NGM_BRIDGE_CLR_STATS`** (`clrstats`) 此命令以四字节链路号为参数，并清除该链路的统计信息。

**`NGM_BRIDGE_GETCLR_STATS`** (`getclrstats`) 同 `NGM_BRIDGE_GET_STATS`，但同时原子性地清除统计信息。

**`NGM_BRIDGE_GET_TABLE`** (`gettable`) 返回用于引导数据包的当前主机映射表，作为 `struct ng_bridge_host_ary`。

**`NGM_BRIDGE_SET_PERSISTENT`** (`setpersistent`) 此命令在节点上设置持久标志，不带参数。

**`NGM_BRIDGE_MOVE_HOST`** (`movehost`) 此命令以 `struct ng_bridge_move_host` 为参数。它将 MAC `addr` 分配给 `hook`。如果 `hook` 是空字符串，则使用控制消息的传入钩子作为回退。如有必要，MAC 将从当前分配的钩子中移除并移动到新钩子。如果 MAC 的移动速度快于 `minStableAge`，该钩子被视为环路并将阻塞 `loopTimeout` 秒的流量。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或当所有钩子都已断开时关闭。通过 `NGM_BRIDGE_SET_PERSISTENT` 控制消息设置持久标志可在最后一个钩子断开时禁用自动节点关闭。

## 文件

**`/usr/share/examples/netgraph/ether.bridge`** 演示如何设置桥接网络的示例脚本

## 参见

if_bridge(4), [netgraph(4)](netgraph.4.md), [ng_ether(4)](ng_ether.4.md), [ng_hub(4)](ng_hub.4.md), [ng_one2many(4)](ng_one2many.4.md), ngctl(8)

## 历史

`bridge` 节点类型实现于 FreeBSD 4.2。

## 作者

Archie Cobbs <archie@FreeBSD.org>

## 缺陷

`bridge` 节点拒绝创建 `uplink0` 钩子，以避免之后与 `NGM_BRIDGE_GET_STATS` 消息产生歧义。
