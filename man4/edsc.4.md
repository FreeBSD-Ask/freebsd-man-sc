# edsc(4)

`edsc` — 以太网丢弃网络接口

## 名称

`edsc`

## 概要

`device edsc`

## 描述

`edsc` 接口是一种软件丢弃机制，可用于性能分析和软件测试。它模拟以太网设备，因此可与 if_bridge(4) 和 [vlan(4)](vlan.4.md) 等驱动程序配合使用。

与其他网络接口一样，`edsc` 接口必须为每个要使用的地址族分配网络地址。这些地址可通过 `SIOCSIFADDR` ioctl(2) 或 [ifconfig(8)](../man8/ifconfig.8.md) 工具设置或更改。

每个 `edsc` 接口在运行时通过接口克隆创建。最简便的方法是使用 [ifconfig(8)](../man8/ifconfig.8.md) `create` 命令，或使用 [rc.conf(5)](../man5/rc.conf.5.md) 中的 `cloned_interfaces` 变量。

## 参见

ioctl(2), arp(4), if_bridge(4), [inet(4)](inet.4.md), [intro(4)](intro.4.md), [vlan(4)](vlan.4.md), [rc.conf(5)](../man5/rc.conf.5.md), arp(8), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`edsc` 设备派生自 [disc(4)](disc.4.md) 设备，首次出现于 FreeBSD 6.3。本手册页改编自 [disc(4)](disc.4.md)。

## 注意事项

由于外发包会被 `edsc` 直接丢弃，ARP 请求不会被回复。因此，在使用 arp(8) 为其下一跳创建静态 arp(4) 条目之前，IP 包无法通过 `edsc` 发送。

初始时 `edsc` 接口的链路层地址为零。如有需要，可使用 [ifconfig(8)](../man8/ifconfig.8.md) `lladdr` 修改。
