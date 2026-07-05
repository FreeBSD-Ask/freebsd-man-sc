# ng_ether.4

`ng_ether` — 以太网 netgraph 节点类型

## 名称

`ng_ether`

## 概要

`#include <netgraph/ng_ether.h>`

## 描述

`ether` netgraph 节点类型允许以太网接口与 [netgraph(4)](netgraph.4.md) 网络子系统交互。一旦 `ether` 模块加载到内核中，系统中的每个以太网接口都会自动创建一个节点。每个节点会尝试以关联接口的名称为自己命名。

该节点类型支持三个钩子：`lower`、`upper` 和 `orphans`。钩子名 `divert` 可作为 `lower` 的别名使用，提供向后兼容性。实际上，这两个名称代表同一个钩子。

`lower` 钩子连接到原始以太网设备。连接后，所有传入的数据包都会被转发到该钩子，而不是交给内核进行上层处理。写入该钩子的数据会作为原始以太网帧由设备发送。`lower` 连接后，正常的发出数据包不受影响。

`upper` 钩子连接到上层协议。连接后，所有发出的数据包都会被转发到该钩子，而不是由设备发送。写入该钩子的数据会作为原始以太网帧被内核接收，如同从网线上接收的一样。`upper` 连接后，正常的传入数据包不受影响。

`orphans` 钩子等价于 `lower`，区别在于只有无法识别的数据包（否则会被丢弃）会被写入该钩子，而其他正常的传入流量不受影响。如果 `orphans` 已连接，写入 `upper` 的无法识别的数据包会被转发回 `orphans`。

在所有情况下，帧都是带有标准 14 字节以太网头部（但无校验和）的原始以太网帧。

当没有钩子连接时，`upper` 和 `lower` 实际上连接在一起，因此数据包可以正常向上和向下流动。

## 钩子

本节点类型支持以下钩子：

**`lower`** 连接到下层设备链路层。

**`upper`** 连接到上层协议。

**`orphans`** 类似于 `lower`，但只接收无法识别的数据包。

## 控制消息

本节点类型支持通用控制消息，以及以下消息：

**`NGM_ETHER_GET_IFNAME`** (`getifname`) 以 `NUL` 结尾的 ASCII 字符串形式返回关联接口的名称。通常与节点名称相同。

**`NGM_ETHER_GET_IFINDEX`** (`getifindex`) 以 32 位整数形式返回关联接口的全局索引。

**`NGM_ETHER_GET_ENADDR`** (`getenaddr`) 返回设备的唯一六字节以太网地址。

**`NGM_ETHER_SET_ENADDR`** (`setenaddr`) 设置设备的唯一六字节以太网地址。此控制消息等价于使用 `SIOCSIFLLADDR` ioctl(2) 系统调用。

**`NGM_ETHER_SET_PROMISC`** (`setpromisc`) 启用或禁用混杂模式。此消息包含一个 32 位整数标志，用于在接口上启用或禁用混杂模式。任何非零值都会启用混杂模式。

**`NGM_ETHER_GET_PROMISC`** (`getpromisc`) 获取节点混杂标志的当前值。返回值始终为一或零。注意，此标志反映的是节点自身的混杂设置，不一定反映实际接口的混杂状态，后者可能受其他方式影响（例如 [bpf(4)](bpf.4.md)）。

**`NGM_ETHER_SET_AUTOSRC`** (`setautosrc`) 设置自动源地址覆盖标志。此消息包含一个 32 位整数标志，使所有发出数据包的源以太网地址字段都被设备的唯一以太网地址覆盖。如果此标志设置为零，发出数据包中的源地址不会被修改。此标志的默认设置为禁用。

**`NGM_ETHER_GET_AUTOSRC`** (`getautosrc`) 获取节点源地址覆盖标志的当前值。返回值始终为一或零。

**`NGM_ETHER_ADD_MULTI`** (`addmulti`) 加入以太网多播组。此控制消息等价于使用 `SIOCADDMULTI` ioctl(2) 系统调用。

**`NGM_ETHER_DEL_MULTI`** (`delmulti`) 离开以太网多播组。此控制消息等价于使用 `SIOCDELMULTI` ioctl(2) 系统调用。

**`NGM_ETHER_DETACH`** (`detach`) 从底层以太网接口分离并关闭节点。

## 关闭

收到 `NGM_SHUTDOWN` 控制消息时，所有钩子都会断开，混杂模式被禁用，但节点不会被移除。只能使用 `NGM_ETHER_DETACH` 控制消息关闭节点。如果接口本身被分离（例如因 PC Card 拔出），节点也会消失。

## 实例

以下命令将“`fxp0`”接口接收的所有无法识别的数据包以十六进制和 ASCII 形式解码后输出到标准输出：

```sh
nghook -a fxp0: orphans
```

以下命令将 `sample.pkt` 的内容通过“`fxp0`”接口发送出去：

```sh
cat sample.pkt | nghook fxp0: orphans
```

以下命令在 `lower` 和 `upper` 协议层之间插入一个 [ng_tee(4)](ng_tee.4.md) 节点，可用于跟踪数据包流、统计等：

```sh
ngctl mkpeer fxp0: tee lower right
ngctl connect fxp0: lower upper left
```

## 参见

arp(4), [netgraph(4)](netgraph.4.md), [netintro(4)](netintro.4.md), [ifconfig(8)](../man8/ifconfig.8.md), ngctl(8), nghook(8)

## 作者

Julian Elischer <julian@FreeBSD.org> Archie Cobbs <archie@FreeBSD.org>

## 缺陷

适用于大多数其他 Netgraph 节点类型的自动 KLD 模块加载机制对 `ether` 节点类型不起作用，因为 `ether` 节点不是按需创建的；它们是在以太网接口附加时或 KLD 首次加载时创建的。因此，如果 KLD 没有静态编译进内核，必须手动加载 KLD 才能使 `ether` 节点存在。
