# carp(4)

`carp` — 通用地址冗余协议

## 名称

`carp`

## 概要

`device carp`

## 描述

CARP 允许同一本地网络上的多个主机共享一组 IPv4 和/或 IPv6 地址。其主要目的是确保这些地址始终可用。

要使用 `carp`，管理员至少需要配置一个公共的虚拟主机 ID（vhid），并在参与虚拟组的每台机器上将至少一个 IP 地址附加到此 vhid。还可以在每个 vhid 基础上设置其他参数：`advbase` 和 `advskew`，用于控制当主机是虚拟主机的 master 时发送通告的频率；`pass` 用于对 `carp` 通告进行认证。`advbase` 参数代表“advertisement base”（通告基准）。它以秒为单位测量，指定通告间隔的基准。`advskew` 参数代表“advertisement skew”（通告偏移）。它以 1/256 秒为单位测量。它被加到基准通告间隔上，使一台主机的通告比另一台稍慢。`advbase` 和 `advskew` 都放入 CARP 通告中。这些值可使用 [ifconfig(8)](../man8/ifconfig.8.md) 配置。

CARP 默认使用多播消息，但可使用 `peer` 和 `peer6` 参数配置为向对等方发送单播通告。可使用 `mcast` 和 `mcast6` 恢复默认地址。注意，如果对等方地址不是多播地址，则禁用 TTL 验证。这些值可使用 [ifconfig(8)](../man8/ifconfig.8.md) 配置。

[carp(4)](carp.4.md) 可配置为使用非标准的 CARP 协议或 VRRPv3（RFC 5798）。使用 `carpver` 参数选择 2（CARP）或 3（VRRPv3）。VRRPv3 特定参数可使用 `vrrpprio` 和 `vrrpinterval` 参数配置。

CARP 虚拟主机可在支持多播的接口上配置：以太网、第 2 层 VLAN、FDDI 和令牌环网。一个接口上可配置任意数量的虚拟主机 ID。任意数量的 IPv4 或 IPv6 地址可附加到特定 vhid。重要的是，参与 vhid 的所有主机在 vhid 上配置相同的前缀列表，因为所有前缀都包含在每个通告中提供的加密校验和中。在一个接口上运行的多个 vhid 独立参与 master/backup 选举。

此外，有许多可使用 [sysctl(8)](../man8/sysctl.8.md) 设置的全局参数：

**`net.inet.carp.allow`** 允许 `carp` 操作。禁用时，虚拟主机保持初始状态，既不发送也不接收通告或流量。默认启用。

**`net.inet.carp.preempt`** 允许虚拟主机相互抢占。启用时，处于 backup 状态的 vhid 将抢占以较低 advskew 通告自身的 master。默认禁用。

**`net.inet.carp.dscp`** carp 数据包中的 DSCP 值。有效值为 0 到 63。值为 4 等同于旧的 TOS LOW_DELAY 标准。TOS 值在 1998 年被弃用并由 DSCP 取代。默认值为 56（CS7/Network Control）。

**`net.inet.carp.log`** 决定记录哪些与 `carp` vhid 相关的事件。值为 0 禁用任何日志记录。值为 1 启用 `carp` vhid 状态更改的日志记录。大于 1 的值启用错误 `carp` 数据包的日志记录。默认值为 1。

**`net.inet.carp.demotion`** 此值显示当前的 CARP 降级级别。该值被加到所有 vhid 通告中发送的实际 advskew 中。在正常系统操作期间，降级因子为零。然而，问题情况会提升其级别：当 `carp` 在发送通告时遇到问题、运行 vhid 的接口关闭，或 [pfsync(4)](pfsync.4.md) 接口未同步时。可通过写入 sysctl oid 来调整降级因子。提供给 [sysctl(8)](../man8/sysctl.8.md) 命令的有符号值被加到当前降级因子中。这允许根据某些外部条件（例如某些守护进程实用程序的状态）控制 `carp` 行为。

**`net.inet.carp.ifdown_demotion_factor`** 当运行 vhid 的接口关闭时，此值被加到 `net.inet.carp.demotion`。默认值为 240（最大 advskew 值）。

**`net.inet.carp.senderr_demotion_factor`** 当 `carp` 在发送通告时遇到错误，此值被加到 `net.inet.carp.demotion`。默认值为 240（最大 advskew 值）。

## 状态更改通知

有时获取有关 `carp` 状态更改事件的通知很有用。这可通过使用 devd(8) 钩子来实现。master/slave 事件在系统 `CARP` 下发出信号。subsystem 指定发生 master/slave 事件的 vhid 和接口名。消息的类型显示 vhid 的新状态。请参见 devd.conf(5) 和 Sx EXAMPLES 节以获取更多信息。

## 实例

对于具有多个接口的防火墙和路由器，当一个物理接口关闭时，希望所有运行 `carp` 的地址一起故障转移。这通过使用 preempt 选项实现。在主机 A 和 B 上都启用它：

```sh
sysctl net.inet.carp.preempt=1
```

假设主机 A 是首选 master，我们在 em0 上运行 192.168.1.0/24 前缀，在 em1 上运行 192.168.2.0/24。这是主机 A 的设置（advskew 高于 0，以便在紧急情况下可被另一台主机覆盖）：

```sh
ifconfig em0 vhid 1 advskew 100 pass mekmitasdigoat 192.168.1.1/24
ifconfig em1 vhid 2 advskew 100 pass mekmitasdigoat 192.168.2.1/24
```

主机 B 的设置相同，但具有更高的 `advskew`：

```sh
ifconfig em0 vhid 1 advskew 200 pass mekmitasdigoat 192.168.1.1/24
ifconfig em1 vhid 2 advskew 200 pass mekmitasdigoat 192.168.2.1/24
```

当主机 A 的某个物理接口发生故障时，`advskew` 在其所有 `carp` vhid 上降级到配置值。由于 preempt 选项，主机 B 将开始通告自身，从而在两个接口上抢占主机 A，而不仅仅是故障的接口。

可通过使用以下 devd.conf 规则设置 `carp` 状态更改事件的处理：

```sh
notify 0 {
	match "system"          "CARP";
	match "subsystem"       "[0-9]+@[0-9a-z.]+";
	match "type"            "(MASTER|BACKUP)";
	action "/root/carpcontrol.sh $subsystem $type";
};
```

要在 [tcpdump(1)](../man1/tcpdump.1.md) 输出中查看 `carp` 数据包解码，需要指定 `-T` `carp` 选项，否则 [tcpdump(1)](../man1/tcpdump.1.md) 会将它们解释为 VRRP 数据包：

```sh
tcpdump -npi vlan0 -T carp
```

## 参见

[tcpdump(1)](../man1/tcpdump.1.md), [inet(4)](inet.4.md), [pfsync(4)](pfsync.4.md), devd.conf(5), [rc.conf(5)](../man5/rc.conf.5.md), [ifconfig(8)](../man8/ifconfig.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`carp` 设备首次出现于 OpenBSD 3.5。`carp` 设备被导入 FreeBSD 5.4。在 FreeBSD 10.0 中，`carp` 被大幅重写，不再是伪接口。
