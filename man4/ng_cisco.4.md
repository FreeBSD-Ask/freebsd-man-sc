# ng_cisco.4

`ng_cisco` — Cisco HDLC 协议 netgraph 节点类型

## 名称

`ng_cisco`

## 概要

`#include <sys/types.h>`

`#include <netinet/in.h>`

`#include <netgraph/ng_cisco.h>`

## 描述

`cisco` 节点类型使用 Cisco HDLC 协议执行数据包的封装和解封装。这是一种用于通过高速同步线路传输数据包的相当简单的协议。每个数据包前面加上一个 Ethertype，指示协议。还有“keep alive”和“inquire”功能。

`downstream` 钩子应连接到同步线路。节点另一侧是 `inet`、`inet6`、`atalk` 和 `ipx` 钩子，分别发送和接收原始 IP、IPv6、AppleTalk 和 IPX 数据包。通常这些钩子会连接到 [ng_iface(4)](ng_iface.4.md) 类型节点上相应的钩子。

## IP 配置

为使 IP 流量正常工作，必须通知节点本地 IP 地址和子网掩码设置。这是因为协议包含“inquire”数据包，我们必须准备好回答。有两种方法可完成此操作：手动和自动。

每当收到此类 inquire 数据包时，节点会向连接到 `inet` 钩子（如果有）的对等节点发送 `NGM_CISCO_GET_IPADDR` 控制消息。如果对等方响应，则使用该响应。这是自动方法。

如果对等方不响应，节点回退到其缓存的 IP 地址和子网掩码值。可随时使用 `NGM_CISCO_SET_IPADDR` 消息设置此缓存值，这是手动方法。

如果 `inet` 钩子连接到 [ng_iface(4)](ng_iface.4.md) 节点的 `inet` 钩子（通常如此），则配置是自动的，因为 [ng_iface(4)](ng_iface.4.md) 理解 `NGM_CISCO_GET_IPADDR` 消息。

## 钩子

此节点类型支持以下钩子：

**`downstream`** 到同步线路的连接。

**`inet`** IP 钩子。

**`inet6`** IPv6 钩子。

**`atalk`** AppleTalk 钩子。

**`ipx`** IPX 钩子。

## 控制消息

此节点类型支持通用控制消息，外加以下消息：

```sh
struct ngciscostat {
  uint32_t   seqRetries;	/* 未确认的重试次数 */
  uint32_t   keepAlivePeriod;	/* 以秒为单位 */
};
```

**`NGM_CISCO_SET_IPADDR`** (`setipaddr`) 此命令接受两个 `struct in_addr` 参数组成的数组。第一个是相应接口的 IP 地址，第二个是子网掩码。

**`NGM_CISCO_GET_IPADDR`** (`getipaddr`) 此命令以 `NGM_CISCO_SET_IPADDR` 使用的相同格式返回 IP 配置。此命令也在此节点类型收到 IP 地址查询数据包时*发送*给 `inet` 对等方。

**`NGM_CISCO_GET_STATUS`** (`getstats`) 返回 `struct ngciscostat`：

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或当所有钩子都已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), [ng_iface(4)](ng_iface.4.md), ngctl(8)

> D. Perkins, "Requirements for an Internet Standard Point-to-Point Protocol", RFC 1547.

## 法律条款

Cisco 是 Cisco Systems, Inc. 的商标。

## 历史

`cisco` 节点类型实现于 FreeBSD 4.0。

## 作者

Julian Elischer <julian@FreeBSD.org> Archie Cobbs <archie@FreeBSD.org>

## 缺陷

并非所有功能都已实现。例如，节点不支持查询远端的 IP 地址和子网掩码。
