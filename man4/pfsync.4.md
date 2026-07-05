# pfsync.4

`pfsync` — 包过滤器状态表同步接口

## 名称

`pfsync`

## 概要

`device pfsync`

`在 loader.conf(5) 中：net.pfsync.pfsync_buckets`

`在 sysctl.conf(5) 中：net.pfsync.carp_demotion_factor`

## 描述

`pfsync` 接口是一个伪设备，用于暴露 [pf(4)](pf.4.md) 所用状态表的某些变化。通过对 `pfsync` 接口调用 [tcpdump(1)](../man1/tcpdump.1.md) 可查看状态变化。如果配置了物理同步接口，`pfsync` 还将在该接口上发送状态变化，并将该接口上从其他系统接收的状态变化插入到状态表中。

默认情况下，状态表的所有本地变化都通过 `pfsync` 暴露。通过 `pfsync` 从网络接收的包产生的状态变化不会被重新广播。对由标记为 `no-sync` 关键字的规则创建的状态的更新会被 `pfsync` 接口忽略（详情参见 [pf.conf(5)](../man5/pf.conf.5.md)）。

`pfsync` 接口会尽可能将多个状态更新折叠为单个包。在发送 `pfsync` 包之前，单个状态最多可被更新的次数由 ifconfig 的 `maxupd` 参数控制（更多详情参见 [ifconfig(8)](../man8/ifconfig.8.md) 和下文示例）。`pfsync` 包的发送最多会延迟一秒。

## 网络同步

可使用此接口在两个或多个防火墙之间同步状态，方法是使用 [ifconfig(8)](../man8/ifconfig.8.md) 指定同步接口。例如，以下命令将 fxp0 设为同步接口：

```sh
# ifconfig pfsync0 syncdev fxp0
```

默认情况下，状态变化消息通过 IP 多播包发送到 224.0.0.240 组地址的同步接口上。可使用 `syncpeer` 关键字指定 `pfsync` 包的备用目的地址。这可与 [ipsec(4)](ipsec.4.md) 结合使用以保护同步流量。在此类配置中，syncdev 应设为 [enc(4)](enc.4.md) 接口，因为这是流量被解封装后到达的位置，例如：

```sh
# ifconfig pfsync0 syncpeer 10.0.0.2 syncdev enc0
```

由于协议上没有身份验证，并且伪造创建状态的包（绕过 pf 规则集）很容易，因此必须妥善保护 pfsync 流量。要么在受信任的网络上运行 pfsync 协议——理想情况下是专用于 pfsync 消息的网络，例如两个防火墙之间的交叉电缆，要么指定对端地址并使用 [ipsec(4)](ipsec.4.md) 保护流量。

FreeBSD 14.0 中引入了对 IPv6 上 `pfsync` 传输的支持。要使用 IPv6 链路本地地址通过多播设置 `pfsync`，必须将 `syncpeer` 设为 `pfsync` 多播地址，并将 `syncdev` 设为期望 `pfsync` 流量到达的接口。

```sh
# ifconfig pfsync0 syncpeer ff12::f0 syncdev vtnet0
```

当 [pf(4)](pf.4.md) 引入新功能时，`pfsync` 使用的消息格式可能会变化。`pfsync` 默认使用最新格式。如果需要与运行较旧版本 FreeBSD 的对端同步，可使用 `version` 参数。例如：

```sh
# ifconfig pfsync0 version 1301
```

当前支持以下版本：

**`1301`** FreeBSD 13.2 及更早版本。已验证与 FreeBSD 13.1 兼容。

**`1400`** FreeBSD 14.0 版本。

**`1500`** FreeBSD 15.0 版本。

## SYSCTL 变量

以下变量可在 [loader(8)](../man8/loader.8.md) 提示符处输入、在 loader.conf(5) 中设置，或在运行时使用 [sysctl(8)](../man8/sysctl.8.md) 更改：

**`net.pfsync.carp_demotion_factor`** 在 `pfsync` 尝试执行批量更新时添加到 `net.inet.carp.demotion` 的值。更多信息请参见 [carp(4)](carp.4.md)。默认值为 240。

## 加载器可调参数

以下可调参数可在 loader.conf(5) 中或 [loader(8)](../man8/loader.8.md) 提示符处设置：

**`net.pfsync.pfsync_buckets`** `pfsync` 桶数。这会影响性能和内存的权衡。默认为 CPU 数量的两倍。仅在基准测试表明这有助于你的工作负载时才更改。

## 实例

`pfsync` 和 [carp(4)](carp.4.md) 可一起使用，为并行配置的一对防火墙提供自动故障转移。一个防火墙将处理所有流量，直到它死亡、被关闭或被手动降级，此时第二个防火墙将自动接管。

本示例中的两个防火墙都有三个 [sis(4)](sis.4.md) 接口。sis0 是外部接口，位于 10.0.0.0/24 子网上；sis1 是内部接口，位于 192.168.0.0/24 子网上；sis2 是 `pfsync` 接口，使用 192.168.254.0/24 子网。一根交叉电缆通过它们的 sis2 接口连接两个防火墙。在所有三个接口上，防火墙 A 使用 .254 地址，防火墙 B 使用 .253 地址。接口配置如下（除非另有说明，否则为防火墙 A）：

**/etc/rc.conf** 中的接口配置：

```sh
network_interfaces="lo0 sis0 sis1 sis2"
ifconfig_sis0="10.0.0.254/24"
ifconfig_sis0_alias0="inet 10.0.0.1/24 vhid 1 pass foo"
ifconfig_sis1="192.168.0.254/24"
ifconfig_sis1_alias0="inet 192.168.0.1/24 vhid 2 pass bar"
ifconfig_sis2="192.168.254.254/24"
pfsync_enable="YES"
pfsync_syncdev="sis2"
```

还必须配置 [pf(4)](pf.4.md) 以允许 `pfsync` 和 [carp(4)](carp.4.md) 流量通过。应将以下内容添加到 **/etc/pf.conf** 的顶部：

```sh
pass quick on { sis2 } proto pfsync keep state (no-sync)
pass on { sis0 sis1 } proto carp keep state (no-sync)
```

最好由一个防火墙处理所有流量的转发，因此备份防火墙的 [carp(4)](carp.4.md) vhid 上的 `advskew` 应设为高于主防火墙的值。例如，如果防火墙 B 是备份，其 carp1 配置如下所示：

```sh
ifconfig_sis1_alias0="inet 192.168.0.1/24 vhid 2 pass bar advskew 100"
```

还必须将以下内容添加到 **/etc/sysctl.conf**：

```sh
net.inet.carp.preempt=1
```

## 参见

[tcpdump(1)](../man1/tcpdump.1.md), [bpf(4)](bpf.4.md), [carp(4)](carp.4.md), [enc(4)](enc.4.md), [inet(4)](inet.4.md), [inet6(4)](inet6.4.md), [ipsec(4)](ipsec.4.md), [netintro(4)](netintro.4.md), [pf(4)](pf.4.md), [pf.conf(5)](../man5/pf.conf.5.md), [protocols(5)](../man5/protocols.5.md), [rc.conf(5)](../man5/rc.conf.5.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`pfsync` 设备首次出现于 OpenBSD 3.3。它首次导入到 FreeBSD 5.3。

`pfsync` 协议和内核实现在 FreeBSD 9.0 中进行了重大修改。较新的协议与旧协议不兼容，不会与其互操作。
