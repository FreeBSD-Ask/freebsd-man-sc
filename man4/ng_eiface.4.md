# ng_eiface(4)

`ng_eiface` — 通用以太网接口 netgraph 节点类型

## 名称

`ng_eiface`

## 概要

`#include <netgraph/ng_eiface.h>`

## 描述

`eiface` netgraph 节点实现通用以太网接口。创建 `eiface` 节点时，会出现一个新接口，可通过 [ifconfig(8)](../man8/ifconfig.8.md) 访问。这些接口命名为“`ngeth0`”、“`ngeth1`”等。节点关闭时，相应接口被移除，接口名可供未来的 `eiface` 节点重用。新节点始终占用第一个未使用的接口。

## 钩子

`eiface` 节点有一个名为 `ether` 的钩子，应连接到以太网下游，例如连接到 [ng_vlan(4)](ng_vlan.4.md) 节点。通过接口传输的数据包从此钩子流出。类似地，在钩子上接收的数据包作为由任何真实以太网接口接收的数据包送入协议栈。

## 控制消息

此节点类型支持通用控制消息，外加以下消息：

**`NGM_EIFACE_SET`** (`set`) 设置接口的链路层地址。需要 `struct ether_addr` 作为参数。此消息还有 ASCII 版本，名为“`set`”，需要由 6 个冒号分隔的十六进制数字组成的 ASCII 字符串作为参数。

**`NGM_EIFACE_GET_IFNAME`** (`getifname`) 返回关联接口的名称，作为以 `NULL` 结尾的 ASCII 字符串。

**`NGM_EIFACE_GET_IFADDRS`** 返回与节点关联的链路层地址列表。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时关闭。关联接口被移除，其名称可供未来的 `eiface` 节点重用。

与大多数其他节点类型不同，`eiface` 节点在所有钩子都已断开时*不会*消失；而是需要显式的 `NGM_SHUTDOWN` 控制消息。

## 参见

[netgraph(4)](netgraph.4.md), [ng_ether(4)](ng_ether.4.md), [ng_iface(4)](ng_iface.4.md), [ng_vlan(4)](ng_vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md), ngctl(8)

## 历史

`eiface` 节点类型实现于 FreeBSD 4.6。

## 作者

`eiface` 节点类型由 Vitaly V Belekhov 编写。本手册页由 Gleb Smirnoff 编写。
