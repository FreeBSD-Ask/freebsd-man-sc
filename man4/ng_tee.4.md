# ng_tee(4)

`ng_tee` — netgraph“tee”节点类型

## 名称

`ng_tee`

## 概要

`#include <sys/types.h>`

`#include <netgraph/ng_tee.h>`

## 描述

`tee` 节点类型的用途类似于 tee(1) 命令。`Tee` 节点可用于调试或“窥探”两个 netgraph 节点之间的连接。`Tee` 节点有四个钩子：`right`、`left`、`right2left` 和 `left2right`。在 `right` 上接收的所有数据都被原样发送到 *both* `left` 和 `right2left` 钩子。类似地，在 `left` 上接收的所有数据都被原样发送到 `right` 和 `left2right` 两个钩子。

数据包也可以在 `right2left` 和 `left2right` 上接收；如果是这样，它们会原样分别从 `right` 和 `left` 钩子转发出去。

## 钩子

此节点类型支持以下钩子：

**`right`** 到右侧节点的连接。

**`left`** 到左侧节点的连接。

**`right2left`** 右到左流量的监听点。

**`left2right`** 左到右流量的监听点。

## 控制消息

此节点类型支持通用控制消息，此外还支持以下消息。

**`NGM_TEE_GET_STATS`**（`getstats`）获取统计信息，以 `struct ng_tee_stats` 形式返回。

**`NGM_TEE_CLR_STATS`**（`clrstats`）清零统计信息。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或在所有钩子均已断开时关闭。如果 `right` 和 `left` 钩子都存在，节点会温和地将自身从链中移除，将 `right` 和 `left` 直接相连。

## 参见

tee(1), [netgraph(4)](netgraph.4.md), ngctl(8)

## 历史

`Tee` 节点类型实现于 FreeBSD 4.0。

## 作者

Julian Elischer <julian@FreeBSD.org>
