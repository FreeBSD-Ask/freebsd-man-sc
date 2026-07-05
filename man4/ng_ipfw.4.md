# ng_ipfw.4

`ng_ipfw` — netgraph 与 IP 防火墙之间的接口

## 名称

`ng_ipfw`

## 概要

`#include <netinet/ip_var.h>`

`#include <netgraph/ng_ipfw.h>`

## 描述

`ipfw` 节点实现 ipfw(4) 与 [netgraph(4)](netgraph.4.md) 子系统之间的接口。

## 钩子

`ipfw` 节点支持任意数量的钩子，钩子名称必须仅使用数字字符。

## 操作

一旦 `ipfw` 模块加载到内核中，会自动创建一个名为 `ipfw` 的单一节点。无法创建更多的 `ipfw` 节点。一旦销毁，重新创建该节点的唯一方法是重新加载 `ipfw` 模块。

可以使用 [ipfw(8)](../man8/ipfw.8.md) 工具的 `netgraph` 或 `ngtee` 命令将数据包注入 [netgraph(4)](netgraph.4.md)。这些命令需要提供一个数字 cookie 作为参数。数据包从名称等于 cookie 值的钩子发出。如果没有匹配的钩子，数据包将被丢弃。通过 `netgraph` 命令注入的数据包会被标记为 `struct ipfw_rule_ref`。此标记包含的信息有助于数据包在从 [netgraph(4)](netgraph.4.md) 返回 ipfw(4) 时重新进入 ipfw(4) 处理。

节点从 [netgraph(4)](netgraph.4.md) 子系统接收的数据包必须带有 `struct ipfw_rule_ref` 标记。数据包在下一条规则处重新进入 IP 防火墙处理。如果未提供标记，数据包将被丢弃。

## 控制消息

本节点类型仅支持通用控制消息。

## 关闭

本节点在收到 `NGM_SHUTDOWN` 控制消息时关闭。不要这样做，因为新的 `ipfw` 节点只能通过重新加载 `ipfw` 模块来创建。

## 参见

ipfw(4), [netgraph(4)](netgraph.4.md), [ipfw(8)](../man8/ipfw.8.md), [mbuf_tags(9)](../man9/mbuf_tags.9.md)

## 历史

`ipfw` 节点类型实现于 FreeBSD 6.0。

## 作者

`ipfw` 节点由 Gleb Smirnoff <glebius@FreeBSD.org> 编写。
