# nfe.4

`nfe` — NVIDIA nForce MCP 以太网驱动

## 名称

`nfe`

## 概要

`要将本驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device nfe

`或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_nfe_load="YES"
```

## 描述

`nfe` 驱动支持基于 NVIDIA nForce 媒体与通信处理器（MCP）的 PCI 以太网适配器，例如 nForce、nForce 2、nForce 3、CK804、MCP04、MCP51、MCP55、MCP61、MCP65、MCP67、MCP73、MCP77 和 MCP79 以太网控制器芯片。

支持的特性包括（在硬件支持下）：

- 接收/发送 IP/TCP/UDP 校验和卸载
- 硬件 VLAN 标记插入/剥离
- TCP 分段卸载（TSO）
- MSI/MSI-X
- Jumbo Frames

通过接口 MTU 设置提供对 Jumbo Frames 的支持。使用 [ifconfig(8)](../man8/ifconfig.8.md) 工具选择大于 1500 字节的 MTU 即可配置适配器收发 Jumbo Frames。

`nfe` 驱动支持以下媒体类型：

**`autoselect`** 启用媒体类型和选项的自动选择。

**`10baseT/UTP`** 设置 10Mbps 操作。

**`100baseTX`** 设置 100Mbps（Fast Ethernet）操作。

**`1000baseT`** 设置 1000Mbps（Gigabit Ethernet）操作（仅限较新型号）。

`nfe` 驱动支持以下媒体选项：

**`half-duplex`** 强制半双工操作。

**`full-duplex`** 强制全双工操作。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`nfe` 驱动支持以下 NVIDIA MCP 板载适配器：

- NVIDIA nForce MCP Networking Adapter
- NVIDIA nForce MCP04 Networking Adapter
- NVIDIA nForce 430 MCP12 Networking Adapter
- NVIDIA nForce 430 MCP13 Networking Adapter
- NVIDIA nForce MCP51 Networking Adapter
- NVIDIA nForce MCP55 Networking Adapter
- NVIDIA nForce MCP61 Networking Adapter
- NVIDIA nForce MCP65 Networking Adapter
- NVIDIA nForce MCP67 Networking Adapter
- NVIDIA nForce MCP73 Networking Adapter
- NVIDIA nForce MCP77 Networking Adapter
- NVIDIA nForce MCP79 Networking Adapter
- NVIDIA nForce2 MCP2 Networking Adapter
- NVIDIA nForce2 400 MCP4 Networking Adapter
- NVIDIA nForce2 400 MCP5 Networking Adapter
- NVIDIA nForce3 MCP3 Networking Adapter
- NVIDIA nForce3 250 MCP6 Networking Adapter
- NVIDIA nForce3 MCP7 Networking Adapter
- NVIDIA nForce4 CK804 MCP8 Networking Adapter
- NVIDIA nForce4 CK804 MCP9 Networking Adapter

## 加载器可调参数

可在 [loader(8)](../man8/loader.8.md) 提示符下设置可调参数，或存储在 loader.conf(5) 中。

**`hw.nfe.msi_disable`** 是否在驱动中启用 MSI 支持。默认值为 0。

**`hw.nfe.msix_disable`** 是否在驱动中启用 MSI-X 支持。默认值为 0。

## SYSCTL 变量

以下 [sysctl(8)](../man8/sysctl.8.md) 变量可用于修改或监视 `nfe` 行为。

**`dev.nfe.%d.process_limit`** 在重新调度 taskqueue 之前，事件循环中处理的最大 Rx 事件数。接受范围为 50 到 255，默认值为 192。更改不需要将接口先 down 再 up 即可生效。

## 参见

[altq(4)](altq.4.md), arp(4), [intro(4)](intro.4.md), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [pci(4)](pci.4.md), [polling(4)](polling.4.md), [rgephy(4)](rgephy.4.md), [ifconfig(8)](../man8/ifconfig.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`nfe` 设备驱动首次出现于 OpenBSD 3.9，随后出现于 FreeBSD 7.0。

## 作者

`nfe` 驱动由 Jonathan Gray <jsg@openbsd.org> 和 Damien Bergamini <damien@openbsd.org> 编写。`nfe` 驱动由 Shigeaki Tagashira <shigeaki@se.hiroshima-u.ac.jp> 移植到 FreeBSD。
