# ng_rfc1490(4)

`ng_rfc1490` — RFC 1490 netgraph 节点类型

## 名称

`ng_rfc1490`

## 概要

`#include <netgraph/ng_rfc1490.h>`

## 描述

`rfc1490` 节点类型按 RFC 1490（之后已被 RFC 2427 更新）执行协议封装、解封装和多路复用。这种特定类型的封装常用于帧中继 DLCI 信道之上。

`downstream` 钩子用于传输和接收封装帧。在节点的另一侧，`inet` 和 `ppp` 钩子分别用于传输和接收原始 IP 帧和 PPP 帧。PPP 帧按 RFC 1973 传输和接收；特别是，出现在 `ppp` 钩子上的帧以 PPP 协议号开头。`ethernet` 钩子可用于按 RFC 1490 的桥接格式传输和接收以太网帧（不带校验和）。

通常 `inet` 钩子连接到 [ng_iface(4)](ng_iface.4.md) 节点的 `inet` 钩子。

## 钩子

此节点类型支持以下钩子：

**`downstream`** 连接到 RFC 1490 对端实体。

**`ethernet`** 传输和接收桥接的原始以太网帧，不带校验和。

**`inet`** 传输和接收原始 IP 帧。

**`ppp`** 传输和接收 PPP 帧。

## 控制消息

此节点类型支持通用控制消息，此外还支持以下消息：

**""** `ietf-ip` IP 数据包使用简单的 RFC1490/2427 封装发送。

**""** `ietf-snap` IP 数据包在 SNAP 帧内发送。同样符合 RFC1490/2427。

**""** `cisco` IP 数据包使用专有的 Cisco 封装方法发送和接收。

**`NGM_RFC1490_SET_ENCAP`**（`setencap`）此命令设置节点的封装方法。所需方法必须作为字符串消息参数传递，且必须是以下受支持的封装模式之一：

**`NGM_RFC1490_GET_ENCAP`**（`getencap`）此命令返回节点当前的封装方法。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或在所有钩子均已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), [ng_frame_relay(4)](ng_frame_relay.4.md), [ng_iface(4)](ng_iface.4.md), ngctl(8)

> C. Brown, A. Malis, "Multiprotocol Interconnect over Frame Relay", RFC 2427.

> W. Simpson, "PPP in Frame Relay", RFC 1973.

`http://www.cisco.com/warp/public/121/frf8modes.pdf`

## 历史

`rfc1490` 节点类型实现于 FreeBSD 4.0。

## 作者

Julian Elischer <julian@FreeBSD.org>

## 缺陷

未实现 RFC 1490 的全部内容。
