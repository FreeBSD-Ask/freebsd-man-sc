# ng_ip_input(4)

`ng_ip_input` — netgraph IP 输入节点类型

## 名称

`ng_ip_input`

## 概要

`#include <netgraph/ng_ip_input.h>`

## 描述

`ip_input` 节点类型将所有接收到的数据包排队到 IP 输入处理子系统中。

## 钩子

`ip_input` 节点接受任何连接请求，无论钩子名称如何，只要名称唯一即可。

## 控制消息

本节点类型仅支持通用控制消息。其他控制消息会被静默丢弃。

## 关闭

本节点在收到 `NGM_SHUTDOWN` 控制消息时关闭，或在所有钩子都已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), ngctl(8)

## 历史

`ip_input` 节点类型实现于 FreeBSD 5.0。

## 作者

Brooks Davis <brooks@FreeBSD.org>

## 缺陷

`ip_input` 节点类型可能应该保留某种统计信息。
