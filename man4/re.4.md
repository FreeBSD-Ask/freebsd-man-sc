# re.4

`re` — Realtek 8139C+/8169/816xS/811xS/8168/810xE/8111 PCI/PCIe 以太网适配器驱动

## 名称

`re`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device re

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_re_load="YES"
```

## 描述

`re` 驱动为基于 Realtek RTL8139C+、RTL8169、RTL816xS、RTL811xS、RTL8168、RTL810xE 和 RTL8111 PCI 及 PCIe 以太网控制器的各种 NIC 提供支持。

基于 8139C+ 和 810xE 的 NIC 可在 CAT5 电缆上以 10 和 100Mbps 速率运行。基于 8169、816xS、811xS、8168 和 8111 的 NIC 可在 10、100 和 1000Mbps 速率下运行。

`re` 驱动支持的所有 NIC 都具有 TCP/IP 校验和卸载和硬件 VLAN 标签/插入功能，并使用基于描述符的 DMA 机制。它们还支持 TCP 大发送（TCP 分段卸载）。

8139C+ 是单芯片方案，集成了 10/100 MAC 和 PHY。8169 仅为 10/100/1000 MAC，需要外接 GMII 或 TBI PHY。816xS、811xS、8168 和 8111 是单芯片器件，集成了 10/100/1000 MAC 和 10/100/1000 铜缆 PHY。独立的 10/100/1000 卡有 32 位 PCI 和 64 位 PCI 两种型号。8110S 专为嵌入式板载局域网（LAN-on-motherboard）应用设计。

8169、8169S、8110S、8168 和 8111 还支持 jumbo frames，可通过接口 MTU 设置进行配置。最大 MTU 取决于芯片版本：8169、8169S 和 8110S 最多支持 7422 字节；8168C/8111C 和 8168E-VL/8111E-VL 最多支持约 6100 字节；8168D/8111D 及后续版本最多支持约 9200 字节。通过 [ifconfig(8)](../man8/ifconfig.8.md) 实用程序选择大于 1500 字节的 MTU 可配置适配器收发 jumbo frames。

`re` 驱动支持以下介质类型：

**`autoselect`** 启用介质类型和选项的自动选择。用户可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加介质选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`1000baseTX`** 设置通过双绞线的 1000baseTX 操作。Realtek 千兆芯片仅在 `full-duplex` 模式下支持 1000Mbps。

`re` 驱动支持以下介质选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`re` 驱动支持基于 Realtek RTL8139C+、RTL8169、RTL816xS、RTL811xS、RTL8168、RTL810xE 和 RTL8111 的快速以太网和千兆以太网适配器，包括：

- Alloy Computer Products EtherGOLD 1439E 10/100 (8139C+)
- Compaq Evo N1015v 集成以太网 (8139C+)
- Corega CG-LAPCIGT 千兆以太网 (8169S)
- D-Link DGE-528(T) 千兆以太网 (8169S)
- D-Link DGE-530(T) 千兆以太网 (8169S)
- Killer E2600 千兆以太网 (8168)
- Gigabyte 7N400 Pro2 集成千兆以太网 (8110S)
- LevelOne GNC-0105T (8169S)
- LinkSys EG1032 (32 位 PCI)
- PLANEX COMMUNICATIONS Inc. GN-1200TC (8169S)
- TP-Link TG-3468 v2 千兆以太网 (8168)
- USRobotics USR997902 千兆以太网 (8169S)
- Xterasys XN-152 10/100/1000 NIC (8169)

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`hw.re.intr_filter`** 此可调参数使驱动在支持 MSI/MSI-X 能力的控制器上使用中断过滤器处理程序。如果管理员禁用了 MSI/MSI-X，此可调参数无效，驱动将使用中断过滤器处理程序。默认值为 0，使用中断线程处理程序。

**`hw.re.msi_disable`** 此可调参数禁用以太网硬件上的 MSI 支持。默认值为 0。

**`hw.re.msix_disable`** 此可调参数禁用以太网硬件上的 MSI-X 支持。默认值为 0。

**`hw.re.prefer_iomap`** 此可调参数控制指定设备上应使用哪种寄存器映射。非零值启用 I/O 空间寄存器映射。默认值为 0，使用内存空间寄存器映射。

## SYSCTL 变量

以下变量同时可作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数使用：

**`dev.re.%d.int_rx_mod`** 延迟接收中断处理的最大时间（单位为 1 微秒）。接受范围为 0 至 65，默认值为 65（65 微秒）。值为 0 时完全禁用中断适度。更改生效前需将接口关闭再重新打开。

## 诊断

- re%d: couldn't map memory 发生致命的初始化错误。
- re%d: couldn't map ports 发生致命的初始化错误。
- re%d: couldn't map interrupt 发生致命的初始化错误。
- re%d: no memory for softc struct! 驱动在初始化期间未能为每设备实例信息分配内存。
- re%d: failed to enable memory mapping! 驱动未能初始化 PCI 共享内存映射。当网卡未插在总线主控插槽中时可能发生此情况。
- re%d: no memory for jumbo buffers! 驱动在初始化期间未能为 jumbo frames 分配内存。
- re%d: watchdog timeout 设备已停止响应网络，或网络连接（电缆）存在问题。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [polling(4)](polling.4.md), [rge(4)](rge.4.md), [rgephy(4)](rgephy.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

> "Realtek Semiconductor RTL8139C+, RTL8169, RTL8169S and RTL8110S datasheets"。

## 历史

`re` 设备驱动最早出现在 FreeBSD 5.2 中。

## 作者

`re` 驱动由 Bill Paul <wpaul@windriver.com> 编写。

## 缺陷

Xterasys XN-152 32 位 PCI NIC 使用 RTL8169 MAC 和 Marvell 88E1000 PHY，存在一个缺陷：当板卡插入 64 位 PCI 插槽时会导致 DMA 数据损坏。该缺陷在于板卡设计而非芯片本身：PCI REQ64# 和 ACK64# 信号线应上拉为高电平，但实际并未如此。结果是 8169 芯片被误导，执行了 64 位 DMA 传输，尽管 NIC 与总线之间实际上不存在 64 位数据路径。

遗憾的是，此问题无法通过软件纠正，但可以检测到。加载 `re` 驱动时，它会运行一个诊断例程，通过将芯片置于数字环回模式并启动数据包发送来验证 DMA 操作。如果网卡工作正常，发送的数据将被原样回送。如果回送的数据已损坏，驱动将在控制台上打印一条错误消息并中止设备附加。用户应确保将 NIC 安装在 32 位 PCI 插槽中以避免此问题。

Realtek 8169、8169S 和 8110S 芯片似乎最多只能发送大小为 7.5K 的 jumbo frames。

如果此驱动出现问题，可在 Ports net/realtek-re-kmod 下找到来自厂商的更新驱动。
