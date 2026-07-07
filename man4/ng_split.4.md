# ng_split(4)

`ng_split` — 分离入站和出站数据流的 netgraph 节点

## 名称

`ng_split`

## 概要

`#include <netgraph/ng_split.h>`

## 描述

`split` 节点类型用于将双向数据包流分成两条独立的单向数据包流。

## 钩子

此节点类型支持以下三个钩子：

**`in`** 在 *in* 上接收的数据包会被转发到 *mixed*。

**`out`** 在 *out* 上接收的数据包将作为非法数据包被丢弃。

**`mixed`** 在 *mixed* 上接收的数据包会被转发到 *out*。

## 控制消息

此节点类型仅支持通用控制消息。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或在所有钩子均已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), ngctl(8)

## 历史

`split` 节点类型实现于 FreeBSD 3.5，但直至 FreeBSD 5.0 才被并入 FreeBSD。

## 作者

Julian Elischer <julian@FreeBSD.org> Vitaly V. Belekhov <vitaly@riss-telecom.ru>
