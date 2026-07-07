# udbp(4)

`udbp` — USB 双批量管道驱动

## 名称

`udbp`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device udbp

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
udbp_load="YES"
```

## 描述

`udbp` 驱动提供对包含至少两个批量管道（每个方向一个）的主机到主机电缆的支持。这通常包括标有用于 **Windows USB Easy Transfer** 的电缆，以及许多基于 Prolific PL2xx1 系列 USB 桥接芯片的电缆。下文 Sx 参见 部分列出了兼容 USB 主机电缆的有用（但不全面）列表。

它需要 [netgraph(4)](netgraph.4.md) 可用。可通过在内核配置文件中添加 `options NETGRAPH` 完成，或者将 [netgraph(4)](netgraph.4.md) 作为模块加载——可从 **`/boot/loader.conf`** 或从命令行在 `udbp` 模块之前加载。

## 实例

```sh
options NETGRAPH
```

```sh
device udbp
```

将 `udbp` 驱动加入内核。

```sh
kldload netgraph
```

```sh
kldload udbp
```

加载 [netgraph(4)](netgraph.4.md) 模块，然后加载 `udbp` 驱动。

```sh
ngctl mkpeer udbp0: eiface data ether
```

```sh
ifconfig ngeth0 ether aa:dd:xx:xx:xx
```

```sh
ifconfig ngeth0 inet 169.254.x.x/16
```

创建新的以太网网络接口节点，并将其 ether 钩子连接到 `udbp` 驱动的 data 钩子。

这使 FreeBSD 能与 Linux 对端通信（例如使用 **plusb** 驱动）。Linux 节点应配置为优先使用链路本地 IPv4 地址（例如在 Debian 和 Red Hat 衍生发行版中使用 Network Manager）。

虽然 FreeBSD 和 Linux 在行为上松散地遵循 CDC EEM 1.0 以实现互操作，但两个实现都未 expressly 设计为遵循其规范。

## 参见

[netgraph(4)](netgraph.4.md), [ng_eiface(4)](ng_eiface.4.md), [ohci(4)](ohci.4.md), [uhci(4)](uhci.4.md), [usb(4)](usb.4.md), ngctl(8)

> *Universal Serial Bus: Communications Class Subclass Specification for Ethernet Emulation Model Devices*, Revision 1.0, USB Implementers Forum, Inc., February 2, 2005.

> *Total Commander: Supported cables for USB cable connection*, Ghisler Software GmbH..

## 注意事项

USB 主机-主机链路的点对点特性和附加延迟使其不适合作为以太网 LAN 的 “直接替代”；对于 USB 3.0 SuperSpeed 电缆，延迟可与 100BaseTX 以太网相比（但通常更差），吞吐量可与 2.5GBASE-T 相比。

但是，其能效使其在嵌入式应用中具有吸引力。Plugable PL27A1 电缆声称消耗 24mA 的 USB3 总线功率，而典型的 USB 3.0 转千兆以太网接口为 150mA。

## 历史

`udbp` 驱动首次出现于 FreeBSD 5.0。

## 缺陷

`udbp` 驱动不支持 CDC EEM 规范第 5.1 节中描述的特殊数据包。

## 作者

`udbp` 驱动由 Doug Ambrisko <ambrisko@whistle.com>、Julian Elischer <julian@FreeBSD.org> 和 Nick Hibma <n_hibma@FreeBSD.org> 编写。

本 man 页面由 Nick Hibma <n_hibma@FreeBSD.org> 编写，由 Bruce Simpson <bms@FreeBSD.org> 更新。
