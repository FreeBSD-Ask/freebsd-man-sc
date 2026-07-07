# nge(4)

`nge` — National Semiconductor PCI 千兆以太网适配器驱动

## 名称

`nge`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device nge

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_nge_load="YES"
```

## 描述

`nge` 驱动为基于 National Semiconductor DP83820 和 DP83821 千兆以太网控制器芯片的各种 NIC 提供支持。

DP83820 支持 TBI（十位接口）和 GMII 收发器，这意味着它可以用于铜缆或 1000baseX 光纤应用。DP83820 支持 TCP/IP 校验和卸载和 VLAN 标记/插入，以及 2048 位多播哈希过滤器和最多 4 个模式匹配缓冲区。

大多数卡还使用 DP83861 10/100/1000 铜缆千兆收发器芯片，支持 10、100 和 1000Mbps 模式的全双工或半双工自动协商。

DP83820 和 DP83821 还支持巨帧，可通过接口 MTU 设置进行配置。使用 [ifconfig(8)](../man8/ifconfig.8.md) 选择大于 1500 字节的 MTU 时，适配器将配置为接收和传输巨帧。使用巨帧可以显著提高某些任务（如文件传输和数据流）的性能。

`nge` 驱动支持以下媒体类型：

**`autoselect`** 启用媒体类型和选项的自动选择。用户可以通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加媒体选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`1000baseTX`** 设置通过双绞线的 1000baseTX 操作。支持 `full-duplex` 和 `half-duplex` 模式。

**`1000baseSX`** 设置 1000Mbps（千兆以太网）操作。支持 `full-duplex` 和 `half-duplex` 模式。

`nge` 驱动支持以下媒体选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`nge` 驱动支持基于 National Semiconductor DP83820 和 DP83821 的千兆以太网适配器，包括：

- Addtron AEG320T
- Ark PC SOHO-GA2500T（32 位 PCI）和 SOHO-GA2000T（64 位 PCI）
- Asante FriendlyNet GigaNIX 1000TA 和 1000TPC
- D-Link DGE-500T
- Linksys EG1032, revision 1
- Netgear GA621
- Netgear GA622T
- SMC EZ Card 1000 (SMC9462TX)
- Surecom Technology EP-320G-TX
- Trendware TEG-PCITX（32 位 PCI）和 TEG-PCITX2（64 位 PCI）

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`dev.nge.%d.int_holdoff`** 延迟中断处理的最大时间量，以 100 微秒为单位。接受范围为 0 到 255，默认为 1（100 微秒）。值为 0 时完全禁用中断适度。更改必须先将接口关闭再重新启动才能生效。

## 诊断

- nge%d: couldn't map memory 已发生致命的初始化错误。
- nge%d: couldn't map ports 已发生致命的初始化错误。
- nge%d: couldn't map interrupt 已发生致命的初始化错误。
- nge%d: no memory for softc struct! 驱动在初始化期间未能为每设备实例信息分配内存。
- nge%d: failed to enable memory mapping! 驱动未能初始化 PCI 共享内存映射。如果卡不在总线主控插槽中可能会发生此情况。
- nge%d: no memory for jumbo buffers! 驱动在初始化期间未能为巨帧分配内存。
- nge%d: watchdog timeout 设备已停止响应网络，或网络连接（电缆）有问题。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [polling(4)](polling.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

> "National Semiconductor DP83820 datasheet".

> "National Semiconductor DP83861 datasheet".

## 历史

`nge` 设备驱动首次出现于 FreeBSD 4.4。

## 作者

`nge` 驱动由 Bill Paul <wpaul@bsdi.com> 编写。
