# vxlan.4

`vxlan` — 虚拟可扩展局域网接口

## 名称

`vxlan`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device vxlan

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_vxlan_load="YES"
```

## 描述

`vxlan` 驱动在 `vxlan` 段中创建虚拟隧道端点。`vxlan` 段是叠加在三层（IP/UDP）网络之上的虚拟二层（以太网）网络。`vxlan` 类似于 [vlan(4)](vlan.4.md)，但设计上更适合大型、多租户数据中心环境。

每个 `vxlan` 接口在运行时通过接口克隆创建。这最常通过 [ifconfig(8)](../man8/ifconfig.8.md) `create` 命令或使用 [rc.conf(5)](../man5/rc.conf.5.md) 中的 `cloned_interfaces` 变量完成。可使用 [ifconfig(8)](../man8/ifconfig.8.md) `destroy` 命令移除该接口。

`vxlan` 驱动创建一个伪以太网网络接口，支持常规的网络 ioctl(2)，因此可像任何其他以太网接口一样与 [ifconfig(8)](../man8/ifconfig.8.md) 配合使用。`vxlan` 接口通过在前面添加 IP/UDP 和 `vxlan` 头来封装以太网帧。因此，封装的（内部）帧能够通过路由的三层网络传输到远程主机。

`vxlan` 接口可配置为单播或多播模式。在单播模式下，接口创建到单个远程主机的隧道，所有流量都传输到该主机。在多播模式下，接口加入 IP 多播组，接收发往该组地址的数据包，并将数据包传输到多播组地址，或在有适当的转发表条目时直接传输到远程主机。

当 `vxlan` 接口启动时，会根据配置（如单播模式的本地地址或多播模式的组地址，以及监听（本地）端口号）创建 [udp(4)](udp.4.md) [socket(9)](../man9/socket.9.md)。由于可能创建多个使用相同本地地址或加入相同组地址且使用相同端口的 `vxlan` 接口，驱动可在多个接口之间共享套接字。但是，一个套接字内的每个接口必须属于唯一的 `vxlan` 段。类似的 [vlan(4)](vlan.4.md) 配置是将一个物理接口配置为多个 VLAN 接口的父设备，每个 VLAN 接口具有唯一的 VLAN 标签。每个 `vxlan` 段由 `vxlan` 头中的 24 位值标识，称为“VXLAN 网络标识符”或 VNI。

使用 [ifconfig(8)](../man8/ifconfig.8.md) `vxlanlearn` 参数配置时，接口会从接收到的数据包动态创建转发表条目。转发表中的条目将内部源 MAC 地址映射到外部远程 IP 地址。发送时，接口尝试查找与封装的目标 MAC 地址匹配的条目。如果找到条目，则使用该条目中的 IP 地址将封装帧直接传输到目标。否则，在多播模式下配置时，接口必须将帧泛洪到组中的所有主机。表中的最大条目数可通过 [ifconfig(8)](../man8/ifconfig.8.md) `vxlanmaxaddr` 命令配置。表中的过期条目会定期清理。超时时间可通过 [ifconfig(8)](../man8/ifconfig.8.md) `vxlantimeout` 命令配置。可使用 [sysctl(8)](../man8/sysctl.8.md) `net.link.vxlan.N.ftable.dump` 命令查看该表。

## MTU

由于 `vxlan` 接口用以太网帧封装 IP、UDP 和 `vxlan` 头，生成的帧可能大于物理网络的 MTU。`vxlan` 规范建议将物理网络 MTU 配置为使用 jumbo frames 以适应封装帧的大小。

默认情况下，`vxlan` 驱动将其 MTU 设置为常规的以太网 MTU 1500 字节，减去预置在封装数据包前的 vxlan 头的大小。

或者，可使用 [ifconfig(8)](../man8/ifconfig.8.md) `mtu` 命令在 `vxlan` 接口上设置固定 MTU 大小，以使封装帧能适应当前物理网络的 MTU。如果使用了 `mtu` 命令，系统将不再在路由或地址更改时调整 `vxlan` 接口 MTU。

## 硬件

`vxlan` 驱动在支持这些功能的物理接口上，支持封装流量的硬件校验和卸载（接收和发送）以及 TSO。`vxlan` 接口会检查 `vxlandev` 接口（如果指定了的话）或托管 `vxlanlocal` 地址的接口，并根据该物理接口的硬件卸载能力配置自身能力。如果多个物理接口将为 `vxlan` 收发流量，则它们必须具有相同的硬件能力。如果出站物理接口不支持 `vxlan` 接口请求的卸载，`vxlan` 接口的发送例程可能失败并返回 Er ENXIO。如果涉及多个具有不同硬件能力的物理接口，或在 `vxlan` 接口已启动后禁用了某接口能力，则可能发生此情况。

目前，能够在硬件中对内部帧生成校验和并执行 TSO 的设备有：[cxgbe(4)](cxgbe.4.md)。

## 实例

以 192.168.100.1 的 `vxlanlocal` 隧道地址和 192.168.100.2 的 `vxlanremote` 隧道地址，在单播模式下创建 `vxlan` 接口。

```sh
ifconfig vxlan create vxlanid 108 vxlanlocal 192.168.100.1 vxlanremote 192.168.100.2
```

在多播模式下创建 `vxlan` 接口，`local` 地址为 192.168.10.95，`group` 地址为 224.0.2.6。em0 接口将用于传输多播数据包。

```sh
ifconfig vxlan create vxlanid 42 vxlanlocal 192.168.10.95 vxlangroup 224.0.2.6 vxlandev em0
```

创建后，可使用 [ifconfig(8)](../man8/ifconfig.8.md) 配置 `vxlan` 接口。

将以下内容放入 **/etc/rc.conf** 文件将创建名为“`vxlan0`”的 vxlan 接口，并以单播模式配置该接口。

```sh
cloned_interfaces="vxlan0"
create_args_vxlan0="vxlanid 108 vxlanlocal 192.168.100.1 vxlanremote 192.168.100.2"
```

## 参见

[inet(4)](inet.4.md), [inet6(4)](inet6.4.md), [vlan(4)](vlan.4.md), [rc.conf(5)](../man5/rc.conf.5.md), [ifconfig(8)](../man8/ifconfig.8.md), [sysctl(8)](../man8/sysctl.8.md)

> M. Mahalingam, et al, "Virtual eXtensible Local Area Network (VXLAN): A Framework for Overlaying Virtualized Layer 2 Networks over Layer 3 Networks", 2014 年 8 月，RFC 7348.

## 作者

`vxlan` 驱动由 Bryan Venteicher <bryanv@freebsd.org> 编写。无状态硬件卸载支持由 Navdeep Parhar <np@freebsd.org> 在 FreeBSD 13.0 中添加。
