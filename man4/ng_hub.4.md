# ng_hub(4)

`ng_hub` — 数据包分发 netgraph 节点类型

## 名称

`ng_hub`

## 概要

`#include <netgraph/ng_hub.h>`

## 描述

`hub` 节点类型提供了一种在多条链路上分发数据包的简单机制。在任一钩子上收到的数据包会被转发到其他钩子输出。数据包不会以任何方式被修改。

## 钩子

`hub` 节点接受任何连接请求，无论钩子名称如何，只要名称唯一即可。

## 控制消息

本节点类型支持通用控制消息，以及以下消息：

**`NGM_HUB_SET_PERSISTENT`** (`setpersistent`) 此命令设置节点的持久标志，不接受任何参数。

## 关闭

本节点在收到 `NGM_SHUTDOWN` 控制消息时关闭，或在所有钩子都已断开时关闭。通过 `NGM_HUB_SET_PERSISTENT` 控制消息设置持久标志后，最后一个钩子断开时不会自动关闭节点。

## 参见

[netgraph(4)](netgraph.4.md), [ng_bridge(4)](ng_bridge.4.md), [ng_ether(4)](ng_ether.4.md), [ng_one2many(4)](ng_one2many.4.md), ngctl(8), nghook(8)

## 历史

`hub` 节点类型出现于 FreeBSD 5.3。

## 作者

Ruslan Ermilov <ru@FreeBSD.org>
