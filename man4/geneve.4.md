# geneve(4)

`geneve` — 通用网络虚拟化封装接口

## 名称

`geneve`

## 概要

`要将本驱动程序编译进内核，请在你的内核配置文件中加入以下行： device geneve`

`或者，要在引导时以模块方式加载该驱动程序，请在 loader.conf(5) 中加入以下行： if_geneve_load="YES"`

## 描述

`geneve` 驱动程序为 Tentant Systems 在 L3（IP/UDP）底层网络上创建通用网络虚拟化隧道接口，使用 `geneve` 协议提供二层（以太网）或三层服务。

本驱动程序对应 RFC 8926 格式规范，默认使用基于多播学习的方法作为控制平面。为提供控制平面独立性，所有驱动程序特定的操作都使用 [rtnetlink(4)](rtnetlink.4.md) 实现，所有 ioctl(2) 调用都使用 [nv(9)](../man9/nv.9.md) 库实现。每个 `geneve` 接口在运行时通过接口克隆创建。这最易通过 [ifconfig(8)](../man8/ifconfig.8.md) 的 `create` 命令或 [rc.conf(5)](../man5/rc.conf.5.md) 中的 `cloned_interfaces` 变量完成。可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `destroy` 命令删除接口。

`geneve` 接口必须配置为 L2 或 L3 模式。L2 `geneve` 隧道可用作位于 hypervisor、交换机或其他设备中的虚拟交换机之间的背板。

L3 `geneve` 隧道提供类似于 IP/VRF 的虚拟化 IP 转发服务。

默认情况下，`geneve` 驱动程序创建一个支持常见网络 ioctl(2) 的 L2 接口，因此可以像任何其他以太网接口一样与 [ifconfig(8)](../man8/ifconfig.8.md) 一起使用。L2 `geneve` 接口通过在 IP/UDP 和 `geneve` 头之前添加来封装以太网帧。因此，封装后（内部）的帧能够通过路由的三层网络传输到远程主机。

`geneve` 接口可配置为单播或多播模式。在单播模式下，接口创建到单个远程主机的隧道，所有流量都传输到该主机。在多播模式下，接口加入 IP 多播组，接收发往该组地址的数据包，并将数据包发送到多播组地址，或者如果有合适的转发表条目则直接发送到远程主机。

当 `geneve` 接口启动时，会根据配置（如单播模式下的本地地址或多播模式下的组地址，以及监听（本地）端口号）创建 [udp(4)](udp.4.md) [socket(9)](../man9/socket.9.md)。由于可能创建多个使用相同本地地址或加入相同组地址且使用相同端口的 `geneve` 接口，驱动程序可能在多个接口之间共享套接字。但是，每个套接字内的每个接口在每个 vnet(9) 中必须属于唯一的 `geneve` 段。类似的 [vlan(4)](vlan.4.md) 配置是将一个物理接口配置为多个 VLAN 接口的父设备，每个接口具有唯一的 VLAN 标签。每个 `geneve` 段由 `geneve` 头中的 24 位值标识，称为“Virtual Network Identifier”或 VNI。此值可通过 [ifconfig(8)](../man8/ifconfig.8.md) 的 `geneveid` 参数设置。

使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `genevelearn` 参数配置时，接口从接收的数据包中动态创建转发表条目。转发表中的条目将内部源 MAC 地址映射到外部远程 IP 地址。发送时，接口尝试为封装的目标 MAC 地址查找条目。如果找到条目，则使用条目中的 IP 地址直接将封装帧传输到目的地。否则，在多播模式下配置时，接口必须将帧泛洪到组中的所有主机。表中的最大条目数可通过 [ifconfig(8)](../man8/ifconfig.8.md) 的 `genevemaxaddr` 命令配置。表中的过期条目会定期清除。超时时间可通过 [ifconfig(8)](../man8/ifconfig.8.md) 的 `genevetimeout` 命令配置。

### MTU

由于 `geneve` 接口用 IP、UDP 和 `geneve` 头封装以太网帧，生成的帧可能大于物理网络的 MTU。`geneve` 规范建议将物理网络 MTU 配置为使用巨型帧以适应封装后的帧大小。

默认情况下，`geneve` 驱动程序将其 MTU 设置为通常的以太网 MTU 1500 字节，并根据 `genevemode` 减去所添加的 geneve 头的大小。

或者，可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mtu` 命令在 `geneve` 接口上设置固定 MTU 大小，以使封装帧适合物理网络的当前 MTU。如果使用了 `mtu` 命令，系统不再在路由或地址更改时调整 `geneve` 接口的 MTU。

### 跳数限制

`geneve` 接口的 TTL 值可通过 [ifconfig(8)](../man8/ifconfig.8.md) 的 `genevettl` 命令更改，也可以从承载的数据包继承。可将 `genevettl` 设置为数字值或 `inherit` 选项，以在封装和解封装点继承。

### 流量类别

与 TTL 值一样，ToS 值可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `genevedscpinherit` 在封装点继承。如 RFC 8926 所定义，ECN 值对于入口和出口流量均遵循 RFC 6040。

### 不分片

为确保传输期间不发生分片，可将 [ifconfig(8)](../man8/ifconfig.8.md) 的 `genevedf` 值设置为 `set` 值，这会在 IPv4 头上设置 DF 位，并在 IPv4 和 IPv6 套接字上设置 IP_DONTFRAG 选项。与其他选项类似，可设置为 `inherit` 值。

### 多播

要使用多播底层创建 `geneve` 接口，必须使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `genevegroup` 而非 `geneveremote`，并将其设置为多播地址（例如 ff08::db8:0:1，239.0.0.1）。可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `genevedev` 设置出站多播接口，以将其多播组绑定到特定接口。

IPv4 底层必须加载 `ip_mroute` 内核模块，IPv6 底层必须加载 `ip6_mroute` 才能使 [multicast(4)](multicast.4.md) 正常工作。

## 硬件

`geneve` 驱动程序在支持这些功能的物理接口上支持封装流量的硬件校验和卸载（接收和发送）以及 TSO。`geneve` 接口检查 `genevedev` 接口（如果指定）或承载 `genevelocal` 地址的接口，并根据该物理接口的硬件卸载能力配置自身能力。如果多个物理接口将发送或接收 `geneve` 流量，则它们都必须具有相同的硬件能力。如果出站物理接口不支持 `geneve` 接口所请求的卸载功能，`geneve` 接口的发送例程可能以 Er ENXIO 失败。这可能在涉及多个物理接口且硬件能力不同，或在 `geneve` 接口已启动后禁用了某个接口能力时发生。

## 实例

```sh
       Host A (198.51.100.10)
       +--------------------+
       | VNI 100 10.1.1.0/24|
       | VNI 200 10.2.2.0/24|
       +---------+----------+
                 |
         (198.51.100.0/24)
                 |
 +---------------v---------------+
 | Host B (203.0.113.1)          |
 |        +------+-------+       |
 | geneve0|              |geneve1|
 | +------v----+   +-----v-----+ |
 | | bridge0   |   | bridge1   | |
 | | (VNI 100) |   | (VNI 200) | |
 | +------+----+   +----+------+ |
 |        |             |        |
 +--------v-------------v--------+
   epair0b|             |epair1b
   +------+----+   +----+------+
   | Jail A    |   | Jail B    |
   | (10.1.1.x)|   | (10.2.2.x)|
   +-----------+   +-----------+
```

假设主机 A 的（外部）IP 地址为 198.51.100.10，内部地址为 10.1.1.1/24 和 10.2.2.1/24，而主机 B 的外部地址为 203.0.113.10，并有两个独立的 Jail，各有自己的 [VNET(9)](../man9/vnet.9.md)。以下命令将配置隧道：

在主机 A 上，以单播模式创建一个 l2 `geneve` 接口：

```sh
ifconfig geneve0 create geneveid 100 genevelocal 198.51.100.10 geneveremote 203.0.113.1
ifconfig geneve1 create geneveid 200 genevelocal 198.51.100.10 geneveremote 203.0.113.1
```

在主机 B 上：

```sh
ifconfig geneve0 create geneveid 100 genevelocal 203.0.113.1 geneveremote 198.51.100.10
ifconfig geneve1 create geneveid 200 genevelocal 203.0.113.1 geneveremote 198.51.100.10
ifconfig bridge0 addm geneve0 addm epair0a
ifconfig bridge1 addm geneve1 addm epair1a
```

以下示例演示使用 IPv6 的多播配置：

```sh
                      ----------- VNI 42 -----------
                     /                              \
2001:db8::1/64 --- Host A ------ Multicast ------- Host B --- 2001:db8::2/64
                  3fff::1 [em0] ff08::db8:1 [em0]  3fff::2
```

以多播模式创建 `geneve` 接口，`genevelocal` 地址为 3fff::1，`genevegroup` 地址为 ff08::db8:0:1。em0 接口将用于传输多播数据包。在主机 A 上：

```sh
ifconfig geneve0 create geneveid 42 genevelocal 3fff::1 genevegroup ff08::db8:1 genevedev em0
```

在主机 B 上：

```sh
ifconfig geneve0 create geneveid 42 genevelocal 3fff::2 genevegroup ff08::db8:1 genevedev em0
```

创建后，可以使用 [ifconfig(8)](../man8/ifconfig.8.md) 配置 `geneve` 接口。

将以下内容放入文件 **/etc/rc.conf** 将创建名为“`geneve0`”的 geneve 接口，并以单播模式配置该接口。

```sh
cloned_interfaces="geneve0"
create_args_geneve0="geneveid 108 genevelocal 192.168.100.1 geneveremote 192.168.100.2"
```

## 参见

[inet(4)](inet.4.md), [inet6(4)](inet6.4.md), [multicast(4)](multicast.4.md), [rtnetlink(4)](rtnetlink.4.md), [vlan(4)](vlan.4.md), [rc.conf(5)](../man5/rc.conf.5.md), [ifconfig(8)](../man8/ifconfig.8.md), [sysctl(8)](../man8/sysctl.8.md)

> J. Gross, Ed., I. Gross, Ed., T. Sridhar, Ed., "Geneve: Generic Network Virtualization Encapsulation", November 2020, RFC 8926.

## 作者

`geneve` 驱动程序由 Seyed Pouria Mousavizadeh Tehrani <info@spmzt.net> 编写。

## 缺陷

当前基于 netlink 的 geneve 实现在 ifconfig 中克隆接口时，如不指定接口索引，无法设置除 genevemode 之外的 geneve 选项。
