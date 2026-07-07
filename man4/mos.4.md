# mos(4)

`mos` — Moschip MCS7730/MCS7830/MCS7832 USB 以太网驱动

## 名称

`mos`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device uhci
> device ohci
> device ehci
> device usb
> device miibus
> device uether
> device mos

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_mos_load="YES"
```

## 描述

`mos` 驱动为基于 Moschip MCS7730/MCS7830/MCS7832 芯片组的 USB 以太网适配器提供支持。

包含 Moschip MCS7730/MCS7830/MCS7832 芯片组的适配器将以 100Base-TX 和全双工模式运行。

Moschip 内置带 MII 接口的 10/100 以太网 MAC，设计用于与以太网和 HomePNA 收发器配合工作。虽然设计用于与 100Mbps 外设接口，但仅适用于 USB 2.0。现有 USB 1.0 标准规定的最大传输速率为 12Mbps。因此，USB 1.0 用户不应期望使用这些设备实际达到 100Mbps 的速度。

Moschip 支持 64 位多播哈希表、用于站地址的单一完美过滤条目以及混杂模式。数据包通过独立的 USB 批量传输端点进行接收和发送。

有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`mos` 驱动支持的适配器包括：

- Sitecom LN030

## 参见

[altq(4)](altq.4.md), [arp(4)](arp.4.md), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

> "ADMtek AN986 data sheet", <http://www.moschip.com/data/products/MCS7830/Data%20Sheet_7830.pdf。>

## 历史

`mos` 设备驱动首次出现于 FreeBSD 8.2。

## 作者

`mos` 驱动由 Rick van der Zwet <info@rickvanderzwet.nl> 编写。
