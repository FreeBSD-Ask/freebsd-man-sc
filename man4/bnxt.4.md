# bnxt(4)

`bnxt` — Broadcom NetXtreme 系列 10Gb 至 400Gb 以太网驱动

## 名称

`bnxt`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> device iflib
> device bnxt

或者，要在引导时以模块形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行：

```sh
if_bnxt_load="YES"
```

## 描述

`bnxt` 驱动为基于 Broadcom BCM573XX、BCM574XX、BCM575XX 和 BCM576XX 以太网控制器的 PCIe NIC 提供支持。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`bnxt` 驱动支持以下 Broadcom 10Gb 至 400Gb 以太网控制器：

- Broadcom BCM57301 NetXtreme-C 10Gb 以太网控制器
- Broadcom BCM57302 NetXtreme-C 10Gb/25Gb 以太网控制器
- Broadcom BCM57304 NetXtreme-C 10Gb/25Gb/40Gb/50Gb 以太网控制器
- Broadcom BCM57304 NetXtreme-C 以太网虚拟功能
- Broadcom BCM57314 NetXtreme-C 以太网虚拟功能
- Broadcom BCM57402 NetXtreme-E 10Gb 以太网控制器
- Broadcom BCM57402 NetXtreme-E 以太网分区
- Broadcom BCM57404 NetXtreme-E 10Gb/25Gb 以太网控制器
- Broadcom BCM57404 NetXtreme-E 以太网虚拟功能
- Broadcom BCM57404 NetXtreme-E 分区
- Broadcom BCM57406 NetXtreme-E 10GBASE-T 以太网控制器
- Broadcom BCM57406 NetXtreme-E 分区
- Broadcom BCM57407 NetXtreme-E 10GBase-T 以太网控制器
- Broadcom BCM57407 NetXtreme-E 25Gb 以太网控制器
- Broadcom BCM57407 NetXtreme-E 分区
- Broadcom BCM57412 NetXtreme-E 分区
- Broadcom BCM57414 NetXtreme-E 以太网虚拟功能
- Broadcom BCM57414 NetXtreme-E 分区
- Broadcom BCM57416 NetXtreme-E 分区
- Broadcom BCM57417 NetXtreme-E 以太网分区
- Broadcom BCM57454 NetXtreme-E 10Gb/25Gb/40Gb/50Gb/100Gb 以太网
- Broadcom BCM57502 NetXtreme-E 10Gb/25Gb/50Gb 以太网
- Broadcom N425 BCM57504 NetXtreme-E 10Gb/25Gb 以太网
- Broadcom P425 BCM57504 NetXtreme-E 10Gb/25Gb 以太网
- Broadcom N1100 BCM57504 NetXtreme-E 10Gb/25Gb/50Gb/100Gb 以太网
- Broadcom N2100 BCM57508 Thor 10Gb/25Gb/50Gb/100Gb 以太网
- Broadcom P2100 BCM57508 Thor 10Gb/25Gb/50Gb/100Gb 以太网
- Broadcom N2200 BCM57608 Thor 2 10Gb/25Gb/50Gb/100Gb/200Gb 以太网
- Broadcom P2200 BCM57608 Thor 2 10Gb/25Gb/50Gb/100Gb/200Gb 以太网
- Broadcom N1400 BCM57608 Thor 2 25Gb/50Gb/100Gb/200Gb/400Gb 以太网
- Broadcom P1400 BCM57608 Thor 2 25Gb/50Gb/100Gb/200Gb/400Gb 以太网

## SYSCTL 变量

以下变量必须在加载驱动之前设置，可通过 loader.conf(5) 或通过 [kenv(1)](../man1/kenv.1.md) 设置。这些变量由 [iflib(4)](iflib.4.md) 框架提供，在那里可能有更详细的文档。

**`dev.bnxt.X.iflib.override_nrxds`** 覆盖每个队列的接收描述符数量。该值为以逗号分隔的三个正整数列表：分别是完成环大小、接收环大小和聚合环大小。完成环应至少为聚合环大小加上接收环大小的四倍。这些数字必须是 2 的幂，零表示使用默认值。默认为 0,0,0。

**`dev.bnxt.X.iflib.override_ntxds`** 覆盖每个队列的发送描述符数量。该值为以逗号分隔的两个正整数列表：分别是完成环大小和发送环大小。完成环应至少为发送环大小的两倍。这些数字必须是 2 的幂，零表示使用默认值。默认为 0,0。

**`dev.bnxt.X.iflib.override_qs_enable`** 设置后，允许发送队列和接收队列数量不同。若未设置，将使用发送和接收队列数量中的较小值作为两者共同的数量。

**`dev.bnxt.X.iflib.override_nrxqs`** 设置接收队列数量。若为零，接收队列数量根据连接到控制器的插槽上的核心数推导得出。默认为 0。

**`dev.bnxt.X.iflib.override_ntxqs`** 设置发送队列数量。若为零，发送队列数量根据连接到控制器的插槽上的核心数推导得出。

以下 [sysctl(8)](../man8/sysctl.8.md) 变量可随时更改：

**`dev.bnxt.X.vlan_only`** 要求传入帧必须带有与为 NIC 配置的某个 VLAN 标记匹配的 VLAN 标记。通常，带有匹配 VLAN 标记的帧和无 VLAN 标记的帧都会被接受。默认为 0。

**`dev.bnxt.X.vlan_strip`** 非零时，NIC 在接收时剥离 VLAN 标记。默认为 0。

**`dev.bnxt.X.rx_stall`** 在没有可用的主机接收缓冲区用于 DMA 时，启用缓冲而非丢弃帧。默认为 0。

**`dev.bnxt.X.rss_type`** 要支持的 RSS 哈希类型的逗号分隔列表。默认为所有类型。默认为 ipv4,tcp_ipv4,udp_ipv4,ipv6,tcp_ipv6,udp_ipv6。

**`dev.bnxt.X.rss_key`** 当前 RSS 密钥。默认为每个设备在附加期间生成的随机值。

**`dev.bnxt.X.ver.hwrm_min_ver`** 支持的最低 HWRM（硬件资源管理器）固件 API 版本。如果固件实现的版本较旧，将打印警告，应升级固件。默认为 1.2.2。

以下 [sysctl(8)](../man8/sysctl.8.md) 变量为只读：

**`dev.bnxt.X.if_name`** 设备的当前接口名。通常为 `bnxtX`，但可以使用 `ifconfig name` 更改。此 sysctl 允许将接口与 `dev.bnxt` 的子设备相关联。

**`dev.bnxt.X.nvram.*`** 关于包含设备固件的 NVRAM 设备的信息。

**`dev.bnxt.X.ver.*`** 关于设备和固件的版本相关信息：

**`dev.bnxt.X.ver.hwrm_if`** 当前运行固件支持的 HWRM API 版本。

**`dev.bnxt.X.ver.driver_hwrm_if`** 驱动构建时所支持的 HWRM API 版本。

**`dev.bnxt.X.hwstats.*`** 由硬件跟踪的每队列统计信息。

**`dev.bnxt.X.hwstats.port_stats.*`** 由硬件跟踪的每端口统计信息。

**`dev.bnxt.X.hwstats.rxq0.drop_pkts`** 硬件在队列零上丢弃的数据包数。此数字可能看起来较高，但该计数包括由于错误的目的 MAC、未订阅的多播地址以及其他忽略以太网帧的正常原因而丢弃的数据包。

**`dev.bnxt.X.hwstats.rxq0.tpa_*`** 与 HW LRO 相关的统计信息。

**`dev.bnxt.X.hw_lro.*`** 启用/禁用 HW LRO 功能。默认禁用。在主机上启用转发时，启用 HW LRO 可能会导致问题。

**`dev.bnxt.X.fc`** 启用/禁用流控制功能。默认启用。

## 诊断

- bnxt%d: %s command returned %s error：设备固件拒绝了来自驱动的命令。可能存在驱动/固件 HWRM API 不匹配。
- bnxt%d: Timeout sending %s (timeout: %d) seq %d：设备固件无响应。可能需要 PCI 设备重置。
- bnxt%d: Timeout sending %s (timeout: %d) msg {0x%x 0x%x} len:%d v: %d：固件响应不完整。可能需要 PCI 设备重置。截至本文撰写时，必须重启系统才能启动 PCI 设备重置。

## 参见

[altq(4)](altq.4.md), arp(4), [iflib(4)](iflib.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`bnxt` 设备驱动首次出现于 FreeBSD 11.1。

## 作者

`bnxt` 驱动由 Jack Vogel <jfvogel@gmail.com> 和 Stephen Hurd <shurd@freebsd.org> 编写，目前由 Broadcom Limited <freebsd.pdl@broadcom.com> 维护。
