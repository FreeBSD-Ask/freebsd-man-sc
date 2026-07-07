# ng_one2many(4)

`ng_one2many` — 数据包多路复用 netgraph 节点类型

## 名称

`ng_one2many`

## 概要

`#include <sys/types.h>`

`#include <netgraph/ng_one2many.h>`

## 描述

`one2many` 提供了一种以一对多（以及反向的多对一）方式跨多条链路路由数据包的简单机制。有一个名为 `one` 的钩子，以及多个名为 `many0`、`many1` 等的钩子。在任一 `many` 钩子上接收的数据包会从 `one` 钩子转发出去。在 `one` 钩子上接收的数据包会从一个或多个 `many` 钩子转发出去；具体哪个（些）钩子由节点配置的传输算法决定。数据包不会以任何方式被修改。

每个已连接的 many 链路可以被视为 up 或 down。数据包永远不会从处于 down 状态的 many 钩子输出。如何确定链路处于 up 或 down 状态取决于节点配置的链路故障检测算法。

在将接口或链路并入组之前，其状态必须标记为“up”。这通常在初始引导阶段由 [rc.conf(5)](../man5/rc.conf.5.md) 设置。也可以使用 [ifconfig(8)](../man8/ifconfig.8.md) 工具将接口状态更改为“up”。

## 传输算法

**`NG_ONE2MANY_XMIT_ROUNDROBIN`** 数据包按顺序从 many 钩子输出。每个数据包从一个不同的 `many` 钩子输出。

**`NG_ONE2MANY_XMIT_ALL`** 数据包从所有 `many` 钩子输出。每个数据包从每个 `many` 钩子输出。

**`NG_ONE2MANY_XMIT_FAILOVER`** 数据包从第一个活动的 `many` 钩子输出。

未来可能会添加其他算法。

## 链路故障检测

节点区分活动链路和故障链路。数据只发送到活动链路。可用的链路故障检测算法如下：

**`NG_ONE2MANY_FAIL_MANUAL`** 通过 `NGM_ONE2MANY_SET_CONFIG` 控制消息（见下文）显式告知节点哪些链路处于 up 状态。新连接的链路在另行配置之前处于 down 状态。

**`NG_ONE2MANY_FAIL_NOTIFY`** 节点监听来自 `many` 钩子的流控消息，如果收到 `NGM_LINK_IS_DOWN` 则认为链路故障。如果收到 `NGM_LINK_IS_UP` 消息，节点认为链路活动。

未来可能会添加其他算法。

当所有链路都被视为故障时，节点向 `one` 钩子发送 `NGM_LINK_IS_DOWN` 消息。当至少一条链路 up 时，节点向 `one` 钩子发送 `NGM_LINK_IS_UP` 消息。

## 钩子

本节点类型最多支持 `NG_ONE2MANY_MAX_LINKS` 个名为 `many0`、`many1` 等的钩子，外加一个名为 `one` 的钩子。

## 控制消息

本节点类型支持通用控制消息，以及以下消息：

```sh
/* 节点配置结构 */
struct ng_one2many_config {
  uint32_t    xmitAlg;        /* 如何分发数据包 */
  uint32_t    failAlg;        /* 如何检测链路故障 */
  u_char      enabledLinks[NG_ONE2MANY_MAX_LINKS];
};
```

```sh
/* 统计信息结构（每个链路一个） */
struct ng_one2many_link_stats {
  uint64_t   recvOctets;     /* 链路上接收的总字节数 */
  uint64_t   recvPackets;    /* 链路上接收的总数据包数 */
  uint64_t   xmitOctets;     /* 链路上发送的总字节数 */
  uint64_t   xmitPackets;    /* 链路上发送的总数据包数 */
  uint64_t   memoryFailures; /* 无法获取内存或 mbuf 的次数 */
};
```

**`NGM_ONE2MANY_SET_CONFIG`** (`setconfig`) 使用 `struct ng_one2many_link_config` 作为控制消息参数设置节点配置：当前，`xmitAlg` 字段的有效设置为 `NG_ONE2MANY_XMIT_ROUNDROBIN`（默认）或 `NG_ONE2MANY_XMIT_ALL`。`failAlg` 的有效设置为 `NG_ONE2MANY_FAIL_MANUAL`（默认）或 `NG_ONE2MANY_FAIL_NOTIFY`。

**`NGM_ONE2MANY_GET_CONFIG`** (`getconfig`) 以 `struct ng_one2many_link_config` 形式返回当前节点配置。

**`NGM_ONE2MANY_GET_STATS`** (`getstats`) 此命令接受 32 位链路号作为参数，并返回包含相应 `many` 链路统计信息的 `struct ng_one2many_link_stats`，无论该链路当前是否已连接：要访问 `one` 链路的统计信息，使用链路号 `-1`。

**`NGM_ONE2MANY_CLR_STATS`** (`clrstats`) 此命令接受 32 位链路号作为参数，并清除该链路的统计信息。

**`NGM_ONE2MANY_GETCLR_STATS`** (`getclrstats`) 与 `NGM_ONE2MANY_GET_STATS` 相同，但同时原子性地清除该链路的统计信息。

## 关闭

本节点在收到 `NGM_SHUTDOWN` 控制消息时关闭，或在所有钩子都已断开时关闭。

## 实例

以下命令将设置以太网接口 `fxp0`，使其通过对应于网络接口 `fxp0` 到 `fxp3` 的物理接口交替发送数据包：

```sh
  # 将节点连接在一起
  ngctl mkpeer fxp0: one2many upper one
  ngctl connect fxp0: fxp0:upper lower many0
  ngctl connect fxp1: fxp0:upper lower many1
  ngctl connect fxp2: fxp0:upper lower many2
  ngctl connect fxp3: fxp0:upper lower many3
  # 允许 fxp1 到 fxp3 收发 fxp0 的帧
  ngctl msg fxp1: setpromisc 1
  ngctl msg fxp2: setpromisc 1
  ngctl msg fxp3: setpromisc 1
  ngctl msg fxp1: setautosrc 0
  ngctl msg fxp2: setautosrc 0
  ngctl msg fxp3: setautosrc 0
  # 将所有四条链路配置为 up
  ngctl msg fxp0:upper \
    setconfig "{ xmitAlg=1 failAlg=1 enabledLinks=[ 1 1 1 1 ] }"
  # 启动接口
  ifconfig fxp0 192.168.1.1 netmask 0xfffffffc
```

在对端机器上进行类似设置（使用地址 192.168.1.2），即可实现具有四倍正常带宽的点对点以太网连接。

## 参见

[lagg(4)](lagg.4.md), [netgraph(4)](netgraph.4.md), [ng_bridge(4)](ng_bridge.4.md), [ng_ether(4)](ng_ether.4.md), [ng_hub(4)](ng_hub.4.md), [ifconfig(8)](../man8/ifconfig.8.md), ngctl(8)

## 历史

`one2many` 节点类型实现于 FreeBSD 4.2。

## 作者

`one2many` netgraph 节点（带轮询算法）由 Archie Cobbs <archie@FreeBSD.org> 编写。all 算法由 Rogier R. Mulhuijzen <drwilco@drwilco.net> 添加。

## 缺陷

应支持更多的传输和链路故障算法。Cisco 的 Etherchannel 是一个不错的候选。
