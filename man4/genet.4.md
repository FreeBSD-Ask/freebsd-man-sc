# genet(4)

`genet` — Raspberry Pi 4 / BCM2711 千兆以太网控制器驱动程序

## 名称

`genet`

## 概要

`要将本驱动程序编译进内核，请在内核配置文件中加入以下行：`

> device miibus
> device genet

## 描述

`genet` 驱动程序支持 Raspberry Pi 4 上的 BCM2711 以太网控制器。

FreeBSD 中的 `genet` 驱动程序支持以下功能：

- IPv4 和 IPv6 的 IP/TCP/UDP 校验和卸载
- 全双工模式下的 10/100/1000Mbps 操作
- 半双工模式下的 10/100Mbps 操作

注意，发送校验和卸载操作在 IPv4 和 IPv6 之间是耦合的；要禁用它，必须同时禁用两者，即使并非同时使用这两种地址族。

`genet` 驱动程序支持以下介质类型：

**`autoselect`** 启用介质类型和选项的自动选择。用户可以通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加介质选项手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`1000baseT`** 设置通过双绞线进行的 1000baseT 操作。仅支持 `full-duplex` 模式。

`genet` 驱动程序支持通过 [ifconfig(8)](../man8/ifconfig.8.md) 命令的 `mediaopt` 选项设置以下介质选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`genet` 驱动程序支持 Raspberry Pi 4 Model B 及相关系统上 Broadcom BCM2711 的以太网控制器部分。它使用 BCM54213PE PHY。

## 加载器可调参数

可在引导内核前在 [loader(8)](../man8/loader.8.md) 提示符下设置可调参数，或存储在 loader.conf(5) 中。以下加载器可调变量可用，并且也可作为只读 [sysctl(8)](../man8/sysctl.8.md) 变量使用：

**`hw.genet.rx_batch`** 一次传递给链路层输入例程的最大数据包数。默认为 16。

## SYSCTL 变量

以下变量可作为 [sysctl(8)](../man8/sysctl.8.md) 变量使用：

**`hw.genet.tx_hdr_min`** 当驱动程序收到的输出数据包所在的缓冲区链中，第一个缓冲区仅包含以太网头时，要添加到第一个缓冲区以太网头之后的数据包字节数。如果此值过小，某些数据包可能会丢失。默认值为 56，对迄今观察到的情况足够。

## 诊断

`genet` 驱动程序在正常操作下不太可能产生诊断信息。但是，当使用 [ifconfig(8)](../man8/ifconfig.8.md) 设置 `debug` 选项时，大多数导致发送和接收路径中丢包的故障都会产生一条晦涩的诊断消息，指出故障名称。这些消息通常只有在查看驱动程序源代码时才有意义。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`genet` 设备驱动程序首次出现于 FreeBSD 13.0。

## 作者

`genet` 驱动程序由 Mike Karels <karels@freebsd.org> 编写。部分内容源自 Jared McNeill 编写的 NetBSD bcmgenet 驱动程序，结构和公共代码的某些部分来自 Jared McNeill 为 Allwinner EMAC 编写的 awg 驱动程序。
