# ng_echo.4

`ng_echo` — netgraph 回显节点类型

## 名称

`ng_echo`

## 概要

`#include <netgraph/ng_echo.h>`

## 描述

`echo` 节点类型将所有数据和控制消息反射回发送者。此节点类型用于测试和调试。

## 钩子

`echo` 节点接受任何连接请求，无论钩子名如何，只要名称唯一即可。

## 控制消息

此节点类型仅支持通用控制消息。任何其他控制消息都会被反射回发送者。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或当所有钩子都已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), [ng_hole(4)](ng_hole.4.md), ngctl(8)

## 历史

`echo` 节点类型实现于 FreeBSD 4.0。

## 作者

Julian Elischer <julian@FreeBSD.org>
