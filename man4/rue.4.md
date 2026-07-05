# rue.4

`rue` — Realtek RTL8150 USB 至快速以太网控制器驱动

## 名称

`rue`

## 概要

若要将此驱动程序编译进内核，请在你的内核配置文件中加入以下行：

> device uhci
> device ohci
> device usb
> device miibus
> device uether
> device rue

或者，若要在引导时以模块方式加载驱动程序，在 loader.conf(5) 中加入以下行：

```sh
if_rue_load="YES"
```

## 描述

`rue` 驱动支持基于 Realtek RTL8150 USB 至快速以太网控制器芯片的 USB 以太网适配器。

RTL8150 包含一个集成的快速以太网 MAC，支持 10 和 100Mbps 速度的全双工或半双工模式。虽然设计用于与 100Mbps 外设接口，但现有 USB 标准规定的最大传输速度为 12Mbps。因此，用户不应期望此设备实际达到 100Mbps 的速度。

`rue` 驱动支持以下媒体类型：

**`autoselect`** 启用媒体类型和选项的自动选择。用户可以通过在 **`/etc/rc.conf`** 文件中加入媒体选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。还可使用 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。还可使用 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

`rue` 驱动支持以下媒体选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`rue` 驱动支持基于 Realtek RTL8150 的 USB 以太网适配器，包括：

- Buffalo (Melco Inc.) LUA-KTX
- Green House GH-USB100B
- LinkSys USB100M
- Billionton 10/100 FastEthernet USBKR2

## 诊断

- rue%d: watchdog timeout 一个数据包已排队等待发送并已发出发送命令，但设备在超时到期前未能确认发送。
- rue%d: rx list init failed 驱动无法为发送环分配 mbuf。
- rue%d: no memory for rx list 驱动无法为接收环分配 mbuf。

## 参见

arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

> "Realtek RTL8150 data sheet".

## 历史

`rue` 设备驱动最早出现于 FreeBSD 5.1。

## 作者

`rue` 驱动由 Shunsuke Akiyama <akiyama@FreeBSD.org> 编写。
