# fxp.4

`fxp` — Intel EtherExpress PRO/100 以太网设备驱动程序

## 名称

`fxp`

## 概要

`要将本驱动程序编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device fxp

`或者，要在引导时以模块方式加载该驱动程序，请在 loader.conf(5) 中加入以下行：`

```sh
if_fxp_load="YES"
```

## 描述

`fxp` 驱动程序为基于 Intel i82557、i82558、i82559、i82550 和 i82562 芯片的以太网适配器提供支持。该驱动程序在 i82550 和 i82551 上支持 TCP/UDP/IP 收发校验和卸载。在 i82559 上仅支持 TCP/UDP 接收校验和卸载。在 i82550 和 i82551 上支持 IPv4 的 TCP 分段卸载（TSO）以及 VLAN 硬件标签插入/剥离。除 i82557、i82259ER 和早期 i82558 修订版外，所有控制器均提供 Wake On Lan（WOL）支持。

`fxp` 驱动程序支持以下媒体类型：

**`autoselect`** 启用媒体类型和选项的自动选择。可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加媒体选项来覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。

`fxp` 驱动程序支持以下媒体选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

注意，Pro/10 上不可用 100baseTX 媒体类型。有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

`fxp` 驱动程序支持 [vlan(4)](vlan.4.md) 的扩展帧接收和发送。`fxp` 的此能力可通过 [ifconfig(8)](../man8/ifconfig.8.md) 的 `vlanmtu` 参数控制。

`fxp` 驱动程序还支持一个特殊链路选项：

**`link0`** 某些芯片修订版具有可加载的微码，可用于降低主机 CPU 的中断负载。并非所有板卡都支持微码。使用 [ifconfig(8)](../man8/ifconfig.8.md) 设置 `link0` 标志将在微码可用时将其下载到芯片。

## 硬件

`fxp` 驱动程序支持的适配器包括：

- Intel EtherExpress PRO/10
- Intel InBusiness 10/100
- Intel PRO/100B / EtherExpressPRO/100 B PCI Adapter
- Intel PRO/100+ Management Adapter
- Intel PRO/100 VE Desktop Adapter
- Intel PRO/100 VM Network Connection
- Intel PRO/100 M Desktop Adapter
- Intel PRO/100 S Desktop、Server 和 Dual-Port Server Adapters
- 许多 Intel 主板上的板载网络接口

## 加载器可调参数

可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置可调参数，或将其存储在 loader.conf(5) 中。以下变量既可作为 [loader(8)](../man8/loader.8.md) 可调参数，也可作为 [sysctl(8)](../man8/sysctl.8.md) 变量使用：

**`dev.fxp.%d.int_delay`** 以微秒为单位，尝试合并中断时中断可延迟的最大时间。仅在加载了 Intel 微码时有效。接受范围为 300 到 3000，默认为 1000。

**`dev.fxp.%d.bundle_max`** 生成中断前将捆绑的数据包数。仅在加载了 Intel 微码时有效。接受范围为 1 到 65535，默认为 6。

## SYSCTL 变量

以下变量可作为 [sysctl(8)](../man8/sysctl.8.md) 变量使用。

**`dev.fxp.%d.rnr`** 只读变量，显示 RNR（resource not ready）事件数。

**`dev.fxp.%d.stats`** 只读变量，显示驱动程序维护的有用 MAC 计数器。

## 诊断

- `fxp%d: couldn't map memory` 发生致命的初始化错误。
- `fxp%d: couldn't map interrupt` 发生致命的初始化错误。
- `fxp%d: Failed to malloc memory` 没有足够的 mbuf 可供分配。
- `fxp%d: device timeout` 设备已停止响应网络，或网络连接（线缆）存在问题。
- `fxp%d: Microcode loaded, int_delay: %d usec bundle_max: %d` 芯片已成功下载微码，并将参数化值更改为给定设置。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [polling(4)](polling.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`fxp` 设备驱动程序首次出现于 FreeBSD 2.1。

## 作者

`fxp` 设备驱动程序由 David Greenman 编写。随后由 Maxime Henrion 更新为使用 busdma API 并使其与字节序无关。本手册页由 David E. O'Brien 编写。
