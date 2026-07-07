# ng_UI(4)

`ng_UI` — UI netgraph 节点类型

## 名称

`ng_UI`

## 概要

`#include <netgraph/ng_UI.h>`

## 描述

`UI` 节点类型有两个钩子：`upstream` 和 `downstream`。在 `downstream` 上接收的数据包必须以 0x03（指示无编号信息）作为第一个字节；否则数据包将被丢弃。然后此字节被剥离，数据包的其余部分从 `upstream` 发出。

反之，在 `upstream` 上接收的数据包在转发到 `downstream` 钩子之前会在前面加上一个 0x03 字节。

## 钩子

此节点类型支持以下钩子：

**`downstream`** 下游连接。此节点侧的数据包以 0x03 作为第一个字节。

**`upstream`** 上游连接。此节点侧的数据包已剥离初始的 0x03 字节。

## 控制消息

此节点类型仅支持通用控制消息。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或当两个钩子都已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), ngctl(8)

## 历史

`UI` 节点类型实现于 FreeBSD 4.0。

## 作者

Julian Elischer <julian@FreeBSD.org>
