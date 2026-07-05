# epair.4

`epair` — 一对背靠背连接的虚拟以太网接口

## 名称

`epair`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device epair

`或者，若要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_epair_load="YES"
```

## 描述

`epair` 是一对类似以太网的软件接口，它们通过虚拟交叉电缆背靠背连接。

每个 `epair` 接口对在运行时通过接口克隆创建。最简单的方法是使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `create` 命令，或在 [rc.conf(5)](../man5/rc.conf.5.md) 中使用 `cloned_interfaces` 变量。虽然在克隆时只需给出 `epair` 或 `epair<n>`，但 `epair` 对将被命名为 `epair<n>[ab]`。这意味着第一对 `epair` 接口名为 `epair0a` 和 `epair0b`。

与其他以太网接口一样，`epair` 需要有一个网络地址。如果可调参数 `net.link.epair.ether_gen_addr`=0，每个 `epair` 将被分配一个随机本地管理地址，仅保证在单个网络栈中唯一。可调参数 `net.link.epair.ether_gen_addr`=1 将使用 [ether_gen_addr(9)](../man9/ether_gen_addr.9.md) 生成具有 FreeBSD OUI 的稳定 MAC 地址。在 FreeBSD 15.0 FreeBSD 16.0 中此可调参数默认为 1。要更改默认地址，可使用 SIOCSIFADDR ioctl(2) [ifconfig(8)](../man8/ifconfig.8.md)

基本意图是提供两个虚拟网络栈实例之间的连接。当连接到 if_bridge(4) 时，接口对的一端也可以是另一个（虚拟）LAN 的一部分。与其他以太网接口一样，`epair` 可以在其上配置 [vlan(4)](vlan.4.md)。

`epair` 启用 RXCSUM 和 RXCSUM6，因为它可能接收到已由物理接口验证过校验和的数据包。

`epair` 支持 TCP 和 UDP 的 TXCSUM 和 TXCSUM6，但仅通过转发计算校验和的指令实现。因此，使用 `epair` 接口时，TCP 或 UDP 发送方可以将校验和计算卸载到物理接口。注意，如果数据包不离开主机，则校验和是不必要的，若被卸载将被忽略。此类数据包包含不正确的校验和，因为尚未计算。TXCSUM 和 TXCSUM6 在 `epair` 接口对之间同步（即在一端启用/禁用此功能也会在另一端启用/禁用）。如果一端位于网桥中且网桥禁用了 TXCSUM 或 TXCSUM6，则可避免发送方通过另一端向网桥发送带校验和卸载的数据包。

`epair` 支持 VLAN_HWTAGGING，但实际上并不添加 VLAN 标签。发送端 `epair` 仅将卸载信息转发到另一端。接收端 `epair` 保留设置的卸载信息，假装以太网头中曾存在 VLAN 标签但已被移除。为避免接收端 `epair` 禁用 VLAN_HWTAGGING 的情况，此功能在 `epair` 接口对之间同步（即在一端启用/禁用此功能也会在另一端启用/禁用）。

## 参见

ioctl(2), [altq(4)](altq.4.md), [bpf(4)](bpf.4.md), if_bridge(4), [vlan(4)](vlan.4.md), loader.conf(5), [rc.conf(5)](../man5/rc.conf.5.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`epair` 接口首次出现于 FreeBSD 8.0。

## 作者

`epair` 接口由 Bjoern A. Zeeb、CK Software GmbH 在 FreeBSD 基金会赞助下编写。
