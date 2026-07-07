# axge(4)

`axge` — ASIX Electronics AX88178A/179/179A USB 千兆以太网驱动

## 名称

`axge`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> device xhci
> device ehci
> device uhci
> device ohci
> device usb
> device miibus
> device uether
> device axge

或者，要在引导时以模块形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行：

```sh
if_axge_load="YES"
```

## 描述

`axge` 驱动为基于 ASIX Electronics AX88179/AX88179A USB 3.0 和 AX88178A USB 2.0 芯片组的 USB 千兆以太网适配器提供支持。

AX88179、AX88179A 和 AX88178A 包含带 GMII 接口的 10/100/1000 以太网 MAC，用于与千兆以太网 PHY 接口。

这些设备可与 USB 1.x 和 USB 2.0 控制器一起工作，AX88179/AX88179A 还可与 USB 3.0 控制器一起工作。数据包通过独立的 USB 批量传输端点接收和发送。

`axge` 驱动支持以下媒体类型：

**`autoselect`** 启用媒体类型和选项的自动选择。用户可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加媒体选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`1000baseT`** 设置 1000Mbps（千兆以太网）操作（仅 AX88178）。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

`axge` 驱动支持以下媒体选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`axge` 驱动支持以下 USB 千兆以太网控制器：

- ASIX Electronics AX88179A
- ASIX Electronics AX88179
- ASIX Electronics AX88178A

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [rgephy(4)](rgephy.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`axge` 设备驱动首次出现于 FreeBSD 10.1。

## 作者

`axge` 驱动由 Kevin Lo <kevlo@FreeBSD.org> 和 Li-Wen Hsu <lwhsu@FreeBSD.org> 编写。本手册页由 Mark Johnston <markj@FreeBSD.org> 从 [axe(4)](axe.4.md) 手册页改编。
