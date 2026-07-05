# ng_hole.4

`ng_hole` — netgraph 丢弃节点类型

## 名称

`ng_hole`

## 概要

`#include <sys/types.h>`

`#include <netgraph/ng_hole.h>`

## 描述

`hole` 节点类型会静默丢弃其收到的所有数据和控制消息。此类型用于测试和调试。

## 钩子

`hole` 节点接受任何连接请求，无论钩子名称如何，只要名称唯一即可。

## 控制消息

本节点类型支持通用控制消息，以及以下消息：

**`NGM_HOLE_GET_STATS`** (`getstats`) 此命令接受一个 ASCII 字符串参数（钩子名称），并以 `struct ng_hole_hookstat` 的形式返回与该钩子关联的统计信息。

**`NGM_HOLE_CLR_STATS`** (`clrstats`) 此命令接受一个 ASCII 字符串参数（钩子名称），并清除与该钩子关联的统计信息。

**`NGM_HOLE_GETCLR_STATS`** (`getclrstats`) 此命令与 `NGM_HOLE_GET_STATS` 相同，区别在于还会原子性地清除统计信息。

## 关闭

本节点在收到 `NGM_SHUTDOWN` 控制消息时关闭，或在所有钩子都已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), [ng_echo(4)](ng_echo.4.md), ngctl(8)

## 历史

`hole` 节点类型实现于 FreeBSD 4.0。

## 作者

Julian Elischer <julian@FreeBSD.org>
