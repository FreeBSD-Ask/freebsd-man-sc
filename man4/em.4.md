# em(4)

`em` — Intel(R) PRO/1000 千兆以太网适配器驱动程序

## 名称

`em`, `lem`, `igb`

## 概要

`要将本驱动程序编译进内核，请在你的内核配置文件中加入以下行：`

> device iflib
> device em

`或者，要在引导时以模块方式加载该驱动程序，请在 loader.conf(5) 中加入以下行：`

```sh
if_em_load="YES"
```

## 描述

`igb` 驱动程序为基于 Intel 82540、82541ER、82541PI、82542、82543、82544、82545、82546、82546EB、82546GB 和 82547 控制器芯片的 PCI/PCI-X 千兆以太网适配器提供支持。

`igb` 驱动程序为基于 Intel 82571、82572、82573、82574 和 82583 以太网控制器芯片的 PCI Express 千兆以太网适配器提供支持。

`igb` 驱动程序为连接至 I/O Controller Hub（ICH）和 Platform Controller Hub（PCH）的千兆以太网适配器提供支持，包括 Intel 80003ES2LAN、82562、82566、82567、82577、82578、82579、i217、i218 和 i219。

`igb` 驱动程序为基于 Intel 82575、82576、82580、i210、i211 和 i35x 的 PCI Express 千兆以太网适配器提供支持。这些适配器以 `igb` 接口形式出现，以保持与现有基础设施的兼容性。

除基于 82542 的适配器外，该驱动程序在所有适配器上支持发送/接收校验和卸载及 Jumbo Frames。

此外，除基于 82542、82543、82544 和 82547 控制器芯片的适配器外，该驱动程序在所有适配器上支持 TCP 分段卸载（TSO）。`igb` 驱动程序支持的适配器识别 LED 可通过 [led(4)](led.4.md) API 控制，用于定位目的。有关硬件的更多信息，请参见随驱动程序附带的 `README`。

有关硬件需求的问题，请参阅 Intel PRO/1000 适配器附带的文档。所有列出的硬件需求均适用于在 FreeBSD 上使用。

通过接口 MTU 设置提供对 Jumbo Frames 的支持。使用 [ifconfig(8)](../man8/ifconfig.8.md) 选择大于 1500 字节的 MTU 即可配置适配器收发 Jumbo Frames。Jumbo Frames 的最大 MTU 大小为 16114。

本驱动程序支持硬件辅助 VLAN。`igb` 驱动程序支持以下媒体类型：

**`autoselect`** 启用速度和双工模式的自动协商。

**`10baseT/UTP`** 设置 10Mbps 操作。使用 `mediaopt` 选项选择 `full-duplex` 模式。

**`100baseTX`** 设置 100Mbps 操作。使用 `mediaopt` 选项选择 `full-duplex` 模式。

**`1000baseSX`** 设置 1000Mbps 操作。此速度下仅支持 `full-duplex` 模式。

**`1000baseTX`** 设置 1000Mbps 操作。此速度下仅支持 `full-duplex` 模式。

`igb` 驱动程序支持以下媒体选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

仅使用 `mediaopt` 将驱动程序设置为 `full-duplex`。若未指定 `mediaopt`，驱动程序默认为 `half-duplex`。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`igb` 驱动程序支持基于 Intel 82540、82541ER、82541PI、82542、82543、82544、82545、82546、82546EB、82546GB、82547、82571、82572、82573、82574、82575、82576 和 82580 控制器芯片的千兆以太网适配器：

- Intel Gigabit ET Dual Port Server Adapter（82576）
- Intel Gigabit VT Quad Port Server Adapter（82575）
- Intel Single、Dual 和 Quad Gigabit Ethernet Controller（82580）
- Intel i210 和 i211 Gigabit Ethernet Controller
- Intel i350 和 i354 Gigabit Ethernet Controller
- Intel PRO/1000 CT Network Connection（82547）
- Intel PRO/1000 F Server Adapter（82543）
- Intel PRO/1000 Gigabit Server Adapter（82542）
- Intel PRO/1000 GT Desktop Adapter（82541PI）
- Intel PRO/1000 MF Dual Port Server Adapter（82546）
- Intel PRO/1000 MF Server Adapter（82545）
- Intel PRO/1000 MF Server Adapter（LX）（82545）
- Intel PRO/1000 MT Desktop Adapter（82540）
- Intel PRO/1000 MT Desktop Adapter（82541）
- Intel PRO/1000 MT Dual Port Server Adapter（82546）
- Intel PRO/1000 MT Quad Port Server Adapter（82546EB）
- Intel PRO/1000 MT Server Adapter（82545）
- Intel PRO/1000 PF Dual Port Server Adapter（82571）
- Intel PRO/1000 PF Quad Port Server Adapter（82571）
- Intel PRO/1000 PF Server Adapter（82572）
- Intel PRO/1000 PT Desktop Adapter（82572）
- Intel PRO/1000 PT Dual Port Server Adapter（82571）
- Intel PRO/1000 PT Quad Port Server Adapter（82571）
- Intel PRO/1000 PT Server Adapter（82572）
- Intel PRO/1000 T Desktop Adapter（82544）
- Intel PRO/1000 T Server Adapter（82543）
- Intel PRO/1000 XF Server Adapter（82544）
- Intel PRO/1000 XT Server Adapter（82544）

## 加载器可调参数

可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置可调参数，或将其存储在 loader.conf(5) 中。有关每实例变量，请参见 [iflib(4)](iflib.4.md)。

**`hw.em.disable_crc_stripping`** 禁用或启用硬件剥离 CRC 字段。这在 BMC/IPMI 共享接口上尤为有用，因为剥离 CRC 会导致通过 IPMI 的远程访问失败。默认为 0（启用）。

**`hw.em.eee_setting`** 禁用或启用节能以太网（Energy Efficient Ethernet）。默认为 1（禁用）。

**`hw.em.smart_pwr_down`** 在较新的适配器上启用或禁用智能省电功能。默认为 0（禁用）。

**`hw.em.sbp`** 在混杂模式下显示坏包。默认为 0（关闭）。

**`hw.em.rx_int_delay`** 此值以 1.024 微秒为单位延迟接收中断的生成。默认值为 0，因为启用此功能可能导致适配器挂起。

**`hw.em.rx_abs_int_delay`** 若 `hw.em.rx_int_delay` 非零，此可调参数限制生成接收中断的最大延迟。

**`hw.em.tx_int_delay`** 此值以 1.024 微秒为单位延迟发送中断的生成。默认值为 64。

**`hw.em.tx_abs_int_delay`** 若 `hw.em.tx_int_delay` 非零，此可调参数限制生成发送中断的最大延迟。

**`hw.em.max_interrupt_rate`** 每秒最大中断数。默认值为 8000。

**`hw.em.rx_process_limit`** 一次处理的最大接收数据包数，-1 表示无限制。默认值为 100。

## 文件

**`/dev/led/em*`** 识别 LED 设备节点

## 实例

使 em0 的识别 LED 闪烁：

```sh
echo f2 > /dev/led/em0
```

再次关闭 em0 的识别 LED：

```sh
echo 0 > /dev/led/em0
```

## 诊断

- `em%d: Unable to allocate bus resource: memory` 发生致命的初始化错误。
- `em%d: Unable to allocate bus resource: interrupt` 发生致命的初始化错误。
- `em%d: watchdog timeout -- resetting` 设备已停止响应网络，或网络连接（线缆）存在问题。

## 支持

有关一般信息和支持，请访问 Intel 支持网站：<http://support.intel.com>。

如果在受支持的内核上使用受支持的适配器时发现已发布源代码存在问题，请将与问题相关的具体信息发送至 <freebsd@intel.com>。

## 参见

[altq(4)](altq.4.md), arp(4), [iflib(4)](iflib.4.md), [led(4)](led.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [polling(4)](polling.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`igb` 设备驱动程序首次出现于 FreeBSD 4.4。在 FreeBSD 12.0 中，`igb` 与 `lem` 和 `igb` 设备驱动程序合并，并转换为 [iflib(4)](iflib.4.md) 框架。

## 作者

`igb` 驱动程序最初由 Intel Corporation <freebsd@intel.com> 编写。由 Matthew Macy <mmacy@mattmacy.io> 和 Sean Bruno <sbruno@FreeBSD.org> 将其与 `igb` 驱动程序合并并转换为 [iflib(4)](iflib.4.md) 框架。
