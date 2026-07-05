# ure.4

`ure` — Realtek RTL8152/RTL8153/RTL8156 USB 以太网驱动

## 名称

`ure`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device uhci
> device ohci
> device usb
> device miibus
> device uether
> device ure

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
if_ure_load="YES"
```

## 描述

`ure` 驱动支持 Realtek USB 以太网控制器系列。

`ure` 驱动支持以下媒体类型：

**`autoselect`** 启用媒体类型和选项的自动选择。用户可以通过在 **/etc/rc.conf** 文件中添加媒体选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。也可以使用 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。也可以使用 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`1000baseTX`** 设置通过双绞线进行 1000baseTX（千兆以太网）操作。Realtek 千兆芯片仅支持 `full-duplex` 模式下的 1000Mbps。

**`2500base-T`** 设置通过双绞线进行 2500Base-T 操作。Realtek 8156/8156B 芯片仅支持 `full-duplex` 模式下的 2500Mbps。

`ure` 驱动为 10/100 操作支持以下媒体选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`ure` 驱动支持以下 USB 以太网控制器：

| Model: | Speed (Mbps): |
| --- | --- |
| Realtek RTL8156/RTL8156B/RTL8156BG | 10, 100, 1000, and 2500 |
| Realtek RTL8153/RTL8153B | 10, 100, and 1000 |
| Realtek RTL8152 | 10 and 100 |
| Realtek RTL8168/8169/8110/8211 via rgephy(4) | 10, 100, and 1000 |

## 诊断

- ure%d: watchdog timeout 一个数据包已排队等待发送并发出传输命令，但设备在超时之前未能确认传输。

## 参见

arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 作者

`ure` 驱动由 Kevin Lo <kevlo@FreeBSD.org> 编写。
