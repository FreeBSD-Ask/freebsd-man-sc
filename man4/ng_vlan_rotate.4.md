# ng_vlan_rotate.4

`ng_vlan_rotate` — IEEE 802.1ad VLAN 操控 netgraph 节点类型

## 名称

`ng_vlan_rotate`

## 概要

`#include <sys/types.h>`

`#include <netgraph.h>`

`#include <netgraph/ng_vlan_rotate.h>`

## 描述

`ng_vlan_rotate` 节点类型在不同钩子之间操控按 IEEE 802.1ad（IEEE 802.1Q 的扩展）标准标记的帧的 VLAN 标签顺序。

每个节点有四个特殊钩子：`original`、`ordered`、`excessive` 和 `incomplete`。

在 `original` 钩子上接收的、带有任意数量 `ETHERTYPE_VLAN`、`ETHERTYPE_QINQ` 和 `0x9100` 标签的帧将被重新排列为这些标签的新顺序，并从“ordered”钩子发出。成功处理后，所观察到的栈大小的 `histogram` 计数器递增。

如果栈中的 VLAN 数量少于配置的 `min` 限制，则该帧从 `incomplete` 钩子发出，`incomplete` 计数器递增。

如果栈中的 VLAN 数量多于配置的 `max` 限制，则该帧从 `excessive` 钩子发出，`excessive` 计数器递增。

如果目标钩子未连接，则丢弃该帧，`drops` 计数器递增。

对于在 `ordered` 钩子上接收的以太网帧，执行反向变换并传递给 `original` 钩子。请注意，此过程与上面描述的过程相同，只是 ordered/original 钩子互换，且变换是反向的。

在 `incomplete` 或 `excessive` 钩子上接收的以太网帧原样转发给 `original` 钩子，不做任何修改。

此节点目前仅支持一种操作：栈中 VLAN 的旋转。将配置参数 `rot` 设为正值时，栈将向上滚动该数量。负值将向下滚动。典型场景是将值设为 1，以将最内层的 VLAN 标签移到最外层。旋转包括 VLAN id、ether type 以及 QOS 参数 pcp 和 cfi。典型的 QOS 处理参考最外层设置，因此请小心保持 QOS 不变。

## 钩子

此节点类型支持以下钩子：

**`original`** 通常此钩子会使用 `lower` 钩子连接到 [ng_ether(4)](ng_ether.4.md) 节点，连接到承载网络。

**`ordered`** 通常此钩子会使用 `downstream` 钩子连接到 [ng_vlan(4)](ng_vlan.4.md) 类型节点，以分离服务。

**`excessive`** 见下文。

**`incomplete`** 通常这些钩子会使用 `ether` 钩子附加到 [ng_eiface(4)](ng_eiface.4.md) 类型节点，用于异常监控目的。

## 控制消息

此节点类型支持通用控制消息，此外还支持以下消息：

**`NGM_VLANROTATE_GET_CONF`**（`getconf`）读取当前配置。

**`NGM_VLANROTATE_SET_CONF`**（`setconf`）设置当前配置。

**`NGM_VLANROTATE_GET_STAT`**（`getstat`）读取当前统计信息。

**`NGM_VLANROTATE_CLR_STAT`**（`clrstat`）将统计信息清零。

**`NGM_VLANROTATE_GETCLR_STAT`**（`getclrstat`）一步读取当前统计信息并将其清零。

## 实例

第一个示例展示如何旋转双标签或三标签帧，使最内层的 C-VLAN 可用作服务判别器。单标签或双标签帧（已移除 C-VLAN）被发送到指向不同基础设施的接口。

```sh
#!/bin/sh
BNG_IF=ixl3
VOIP_IF=bge2
ngctl -f- <<EOF
mkpeer ${BNG_IF}: vlan_rotate lower original
name ${BNG_IF}:lower rotate
msg rotate: setconf { min=2 max=3 rot=1 }
mkpeer rotate: vlan ordered downstream
name rotate:ordered services
connect services: ${VOIP_IF} voip lower
msg services: addfilter { vlan=123 hook="voip" }
EOF
```

现在在 `BNG_IF` 接口上注入以下示例帧：

```sh
00:00:00:00:01:01 > 00:01:02:03:04:05,
 ethertype 802.1Q-9100 (0x9100), length 110: vlan 2, p 1,
 ethertype 802.1Q-QinQ, vlan 101, p 0,
 ethertype 802.1Q, vlan 123, p 7,
 ethertype IPv4, (tos 0x0, ttl 64, id 15994, offset 0, flags [none],
  proto ICMP (1), length 84) 192.168.140.101 > 192.168.140.1:
  ICMP echo request, id 40234, seq 0, length 64
```

从 `ordered` 钩子弹出的帧将如下所示：

```sh
00:00:00:00:01:01 > 00:01:02:03:04:05,
 ethertype 802.1Q (0x8100), length 110: vlan 123, p 7,
 ethertype 802.1Q-9100, vlan 2, p 1,
 ethertype 802.1Q-QinQ, vlan 101, p 0,
 ethertype IPv4, (tos 0x0, ttl 64, id 15994, offset 0, flags [none],
  proto ICMP (1), length 84) 192.168.140.101 > 192.168.140.1:
  ICMP echo request, id 40234, seq 0, length 64
```

因此，推送到 `VOIP_IF` 的帧将具有以下形式：

```sh
00:00:00:00:01:01 > 00:01:02:03:04:05,
 ethertype 802.1Q-9100, vlan 2, p 1,
 ethertype 802.1Q-QinQ, vlan 101, p 0,
 ethertype IPv4, (tos 0x0, ttl 64, id 15994, offset 0, flags [none],
  proto ICMP (1), length 84) 192.168.140.101 > 192.168.140.1:
  ICMP echo request, id 40234, seq 0, length 64
```

第二个示例区分双标签帧和单标签帧。

```sh
#!/bin/sh
IN_IF=bge1
ngctl -f- <<EOF
mkpeer ${IN_IF}: vlan_rotate lower original
name ${IN_IF}:lower separate
msg separate: setconf { min=1 max=1 rot=0 }
mkpeer separate: eiface incomplete ether
name separate:incomplete untagged
mkpeer separate: eiface ordered ether
name separate:ordered tagged
EOF
```

将 `rot` 参数设为零（或省略）不会改变帧内标签的顺序。带有更多 VLAN 标签的帧将被丢弃。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或在所有钩子均已断开时关闭。

## 参见

[netgraph(4)](netgraph.4.md), [ng_eiface(4)](ng_eiface.4.md), [ng_ether(4)](ng_ether.4.md), [ng_vlan(4)](ng_vlan.4.md), ngctl(8)

## 作者

Lutz Donnerhacke <lutz@donnerhacke.de>
