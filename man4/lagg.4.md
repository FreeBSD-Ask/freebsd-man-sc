# lagg(4)

`lagg` — 链路聚合和链路故障转移接口

## 名称

`lagg`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device lagg

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_lagg_load="YES"
```

## 描述

`lagg` 接口允许将多个网络接口聚合为一个虚拟 `lagg` 接口，以提供容错和高带宽链路。

每个 `lagg` 接口在运行时通过接口克隆创建。最简单的方法是使用 [ifconfig(8)](../man8/ifconfig.8.md) `create` 命令或使用 [rc.conf(5)](../man5/rc.conf.5.md) 中的 `cloned_interfaces` 变量。

可使用 `ifconfig lagg``N` `create` 命令创建 `lagg` 接口。可使用 `laggproto` `proto` 选项指定不同的链路聚合协议。可使用 `laggport` `child-iface` 选项添加子接口，使用 `-laggport` `child-iface` 选项删除。

驱动当前支持的聚合协议有 `failover`（默认）、`lacp`、`loadbalance`、`roundrobin`、`broadcast` 和 `none`。这些协议决定哪些端口用于传出流量以及特定端口是否接受传入流量。接口链路状态用于验证端口是否处于活动状态。

**`failover`** 仅通过活动端口发送流量。如果主端口不可用，则使用下一个活动端口。第一个添加的接口是主端口；之后添加的任何接口都用作故障转移设备。默认情况下，仅当通过活动端口接收流量时才接受接收的流量。可通过将 `net.link.lagg.failover_rx_all` [sysctl(8)](../man8/sysctl.8.md) 变量设置为非零值来放宽此约束，这对某些桥接网络设置很有用。

**`lacp`** 支持 IEEE 802.1AX（原 802.3ad）链路聚合控制协议（LACP）和标记协议。LACP 将与对端协商一组可聚合链路，组成一个或多个链路聚合组（LAG）。每个 LAG 由相同速度、设置为全双工操作的端口组成。流量将在具有最大总速度的 LAG 中的端口之间平衡，大多数情况下只有一个包含所有端口的 LAG。在物理连接发生更改时，链路聚合将快速收敛到新配置。

**`loadbalance`** 根据哈希的协议头信息在活动端口之间平衡传出流量，并接受来自任何活动端口的传入流量。这是静态设置，不与对端协商聚合，也不交换帧来监控链路。哈希包括以太网源地址和目标地址，如果可用还包括 VLAN 标签，以及 IP 源地址和目标地址。

**`roundrobin`** 通过所有活动端口使用轮询调度程序分发传出流量，并接受来自任何活动端口的传入流量。使用 `roundrobin` 模式可能导致客户端出现数据包乱序到达。由于客户端执行 CPU 密集型的数据包重排序，吞吐量可能受限。

**`broadcast`** 将帧发送到 LAG 的所有端口，并在 LAG 的任何端口上接收帧。

**`none`** 此协议旨在不执行任何操作：它禁用所有流量而不禁用 `lagg` 接口本身。

要添加的第一个接口的 MTU 用作 lagg MTU。所有其他接口必须具有完全相同的值。

`loadbalance` 和 `lacp` 模式将在可用时使用网卡提供的 RSS 哈希，以避免计算哈希；如果哈希无效或使用的协议头信息较少，可能导致流量分布不佳。可通过在每个接口上设置 `-use_flowid` [ifconfig(8)](../man8/ifconfig.8.md) 标志来强制本地哈希计算。新接口的默认值通过 `net.link.lagg.default_use_flowid` [sysctl(8)](../man8/sysctl.8.md) 设置。

创建 `lagg` 接口时，可将 `laggtype` 指定为 `ethernet` 或 `infiniband`。如果两者都未指定，则默认为 `ethernet`。

## 实例

使用两个 [bge(4)](bge.4.md) 千兆以太网接口通过 LACP 创建链路聚合：

```sh
# ifconfig bge0 up
# ifconfig bge1 up
# ifconfig lagg0 create
# ifconfig lagg0 laggproto lacp laggport bge0 laggport bge1 e
	192.168.1.1 netmask 255.255.255.0
```

使用两个 [bge(4)](bge.4.md) 千兆以太网接口通过 ROUNDROBIN 创建链路聚合，并设置每个接口 500 个数据包的步幅：

```sh
# ifconfig bge0 up
# ifconfig bge1 up
# ifconfig lagg0 create
# ifconfig lagg0 laggproto roundrobin laggport bge0 laggport bge1 e
	192.168.1.1 netmask 255.255.255.0
# ifconfig lagg0 rr_limit 500
```

以下示例使用活动故障转移接口在有线和无线网络之间设置漫游，使用两个网络设备。每当有线主接口被拔出时，将使用无线故障转移设备：

```sh
# ifconfig em0 ether 00:11:22:33:44:55 up
# ifconfig wlan0 create wlandev ath0 ssid my_net up
# ifconfig lagg0 create
# ifconfig lagg0 laggproto failover laggport em0 laggport wlan0 e
	192.168.1.1 netmask 255.255.255.0
```

（注意，有线设备的 MAC 地址被强制匹配无线设备的 MAC 地址，本例中为“00:11:22:33:44:55”，因为某些常见无线设备不允许更改 MAC 地址。）

以下示例展示如何创建 infiniband 故障转移接口。

```sh
# ifconfig ib0 up
# ifconfig ib1 up
# ifconfig lagg0 create laggtype infiniband
# ifconfig lagg0 laggproto failover laggport ib0 laggport ib1 e
	1.1.1.1 netmask 255.255.255.0
```

在 **/etc/rc.conf** 中使用静态 IP 配置两个以太网接口进行故障转移：

```sh
cloned_interfaces="lagg0"
ifconfig_lagg0="laggproto failover laggport bge0 laggport bge1 e
	10.1.29.21/24"
ifconfig_bge0="up"
ifconfig_bge1="up"
```

## 参见

ng_one2many(4), [rc.conf(5)](../man5/rc.conf.5.md), [ifconfig(8)](../man8/ifconfig.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`lagg` 设备最早出现于 FreeBSD 6.3。

## 作者

`lagg` 驱动以 `trunk` 的名称由 Reyk Floeter <reyk@openbsd.org> 编写。LACP 实现由 YAMAMOTO Takashi 为 NetBSD 编写。

## 缺陷

无法配置 LACP 管理变量，包括系统和端口优先级。当前实现始终执行主动模式 LACP，并使用 0x8000 作为系统和端口优先级。
