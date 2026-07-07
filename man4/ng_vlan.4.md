# ng_vlan(4)

`ng_vlan` — IEEE 802.1Q VLAN 标记 netgraph 节点类型

## 名称

`ng_vlan`

## 概要

`#include <sys/types.h>`

`#include <netgraph.h>`

`#include <netgraph/ng_vlan.h>`

## 描述

`vlan` 节点类型在不同钩子之间多路复用按 IEEE 802.1Q 标准标记的帧。

每个节点有两个特殊钩子，`downstream` 和 `nomatch`，以及任意数量的“vlan”钩子，每个钩子与特定的 VLAN 标签关联。

在 `downstream` 钩子上接收到的、带有节点已配置过滤标签的 `ETHERTYPE_VLAN` 帧会从相应的“vlan”钩子发出。如果它不匹配任何已配置的标签，或者不是 `ETHERTYPE_VLAN` 类型，则从 `nomatch` 钩子发出。如果 `nomatch` 钩子未连接，则丢弃该数据包。

在 `nomatch` 钩子上接收的以太网帧原样传递给 `downstream` 钩子。

在任何一个“vlan”钩子上接收的以太网帧会相应地加上标签并从 `downstream` 钩子发出。

## 钩子

此节点类型支持以下钩子：

**`downstream`** 通常此钩子会使用 `lower` 钩子连接到 [ng_ether(4)](ng_ether.4.md) 节点。

**`nomatch`** 通常此钩子也会使用 `upper` 钩子连接到 [ng_ether(4)](ng_ether.4.md) 类型节点。

**<*任何** 有效名称*>** 任何其他钩子名都会被接受，并应在之后与特定标签关联。通常此钩子会使用 `ether` 钩子附加到 [ng_eiface(4)](ng_eiface.4.md) 类型节点。

## 控制消息

此节点类型支持通用控制消息，此外还支持以下消息：

**`NGM_VLAN_ADD_FILTER`**（`addfilter`）将钩子与标签关联。

**`NGM_VLAN_DEL_FILTER`**（`delfilter`）解除钩子与标签的关联。

**`NGM_VLAN_GET_TABLE`**（`gettable`）返回所有钩子/标签关联的表。

## 实例

```sh
#!/bin/sh
ETHER_IF=rl0
ngctl -f- <<EOF
shutdown ${ETHER_IF}:
mkpeer ${ETHER_IF}: vlan lower downstream
name ${ETHER_IF}:lower vlan
connect ${ETHER_IF}: vlan: upper nomatch
EOF
ngctl mkpeer vlan: eiface vlan123 ether
ngctl msg vlan: addfilter '{ vlan=123 hook="vlan123" }'
```

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或在所有钩子均已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), [ng_eiface(4)](ng_eiface.4.md), [ng_ether(4)](ng_ether.4.md), ngctl(8), nghook(8)

## 历史

`vlan` 节点类型出现于 FreeBSD 4.10。

## 作者

Ruslan Ermilov <ru@FreeBSD.org>
