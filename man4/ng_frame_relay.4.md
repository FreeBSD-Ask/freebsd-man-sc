# ng_frame_relay.4

`ng_frame_relay` — 帧中继 netgraph 节点类型

## 名称

`ng_frame_relay`

## 概要

`#include <netgraph/ng_frame_relay.h>`

## 描述

`frame_relay` 节点类型使用帧中继协议执行数据包的封装、解封装和多路复用。它最多支持 1024 个 DLCI。LMI 协议由单独的节点类型处理（参见 [ng_lmi(4)](ng_lmi.4.md)）。

`downstream` 钩子应连接到同步线路，即交换机。然后可以通过 `dlci0`、`dlci1` 直到 `dlci1023` 钩子连接到各个 DLCI 通道。

## 钩子

本节点类型支持以下钩子：

**`downstream`** 连接到同步线路。

**`dlciX`** 其中 X 为 0 到 1023 之间的十进制数。此钩子对应 DLCI X 帧中继虚通道。

## 控制消息

本节点类型仅支持通用控制消息。

## 关闭

本节点在收到 `NGM_SHUTDOWN` 控制消息时关闭，或在所有钩子都已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), [ng_lmi(4)](ng_lmi.4.md), ngctl(8)

## 历史

`frame_relay` 节点类型实现于 FreeBSD 4.0。

## 作者

Julian Elischer <julian@FreeBSD.org>

## 缺陷

从技术上讲，在两端的 LMI 协议实体将 DLCI X 配置为活动状态之前，不应将 DLCI X 上的帧发送到交换机。`frame_relay` 节点类型忽略此限制，始终将 DLCI 钩子上接收到的数据传递到 `downstream`。相反，它应先查询 LMI 节点。
