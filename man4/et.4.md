# et(4)

`et` — Agere ET1310 10/100/千兆以太网驱动程序

## 名称

`et`

## 概要

`要将本驱动程序编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device et

`或者，要在引导时以模块方式加载该驱动程序，请在 loader.conf(5) 中加入以下行：`

```sh
if_et_load="YES"
```

## 描述

`et` 驱动程序支持基于 Agere ET1310 芯片的 PCI Express 以太网适配器。

`et` 驱动程序支持以下媒体类型：

**autoselect** 启用媒体类型和选项的自动选择。用户可以通过在 **/etc/rc.conf** 文件中添加媒体选项来手动覆盖自动选择的模式。

**10baseT/UTP** 设置 10Mbps 操作。`mediaopt` 选项也可用于选择 `full-duplex` 或 `half-duplex` 模式。

**100baseTX** 设置 100Mbps（快速以太网）操作。`mediaopt` 选项也可用于选择 `full-duplex` 或 `half-duplex` 模式。

**1000baseT** 设置 1000Mbps（千兆以太网）操作。`mediaopt` 选项只能设为 `full-duplex` 模式。

`et` 驱动程序支持以下 `media` 选项：

**full-duplex** 强制全双工操作。

**half-duplex** 强制半双工操作。

注意，1000baseT 媒体类型仅在适配器支持时可用。有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`et` 驱动程序支持 Agere ET1310 10/100/千兆以太网适配器。

## 可调参数

**`hw.et.rx_intr_npkts`** 此值控制生成接收中断前应接收多少个数据包。默认值为 32。建议将此值设为 38 以上，以防止主机在高负载下发生活锁。

**`hw.et.rx_intr_delay`** 此值以约 4 微秒为单位延迟接收中断的生成。它与 `hw.et.rx_intr_npkts` 配合使用以实现接收中断缓解。默认值为 20。

**`hw.et.tx_intr_nsegs`** 此值控制生成发送中断前应发送多少个段（而非数据包）。默认值为 126。建议将此值设为 280 以下，以防止发送环下溢。

**`hw.et.timer`** 此值控制生成定时器中断的频率。它与 `hw.et.tx_intr_nsegs` 配合使用以实现发送中断缓解。默认值为 1000000000（纳秒）。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`et` 设备驱动程序首次出现于 Dx 1.11。首个包含该驱动程序的 FreeBSD 版本是 FreeBSD 8.0。

## 作者

`et` 驱动程序由 Sepherosa Ziehau <sepherosa@gmail.com> 为 Dx 编写。由 Xin LI <delphij@FreeBSD.org> 移植至 FreeBSD。
