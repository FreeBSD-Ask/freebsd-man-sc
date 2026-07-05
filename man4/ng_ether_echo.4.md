# ng_ether_echo.4

`ng_ether_echo` — netgraph ether_echo 节点类型

## 名称

`ng_ether_echo`

## 概要

`#include <netgraph/ng_ether_echo.h>`

## 描述

`ether_echo` 节点类型会将所有数据和控制消息回送给发送方。它假设（但不检查）数据包是以太网帧，并在回送前交换源地址和目的地址。此节点类型用于测试和调试。

## 钩子

`ether_echo` 节点接受任何连接请求，无论钩子名称如何，只要名称唯一即可。

## 控制消息

本节点类型仅支持通用控制消息。任何其他控制消息都会被回送给发送方。

## 关闭

本节点在收到 `NGM_SHUTDOWN` 控制消息时关闭，或在所有钩子都已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), [ng_echo(4)](ng_echo.4.md), [ng_ether(4)](ng_ether.4.md), [ng_hole(4)](ng_hole.4.md), ngctl(8)

## 历史

`ether_echo` 节点类型实现于 FreeBSD 8.0。

## 作者

Julian Elischer <julian@FreeBSD.org>
