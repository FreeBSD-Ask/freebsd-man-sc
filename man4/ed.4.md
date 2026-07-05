# ed.4

`ed` — NE-2000 和 WD-80x3 以太网驱动程序

## 名称

`ed`

## 概要

`要将本驱动程序编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device ed

`或者，要在引导时以模块方式加载该驱动程序，请在 loader.conf(5) 中加入以下行：`

```sh
if_ed_load="YES"
```

## 弃用通知

`ed` 驱动程序在 FreeBSD 13.0 及以后版本中不再存在。详见 <https://github.com/freebsd/fcp/blob/master/fcp-0101.md>。

## 描述

`ed` 驱动程序为基于 National Semiconductor DS8390 及其他公司制造的类似 NIC 的 8 位和 16 位以太网卡提供支持。`ed` 驱动程序还支持许多通过 MII 与 PHY 接口的 PC Card 芯片。Axiom 的 AX88790、AX88190 和 AX88190A；DLink 的 DL10019 和 DL10022；以及 Tamarack 的 TC5299J 芯片均支持内部或外部 MII/PHY 组合。Realtek 基于 RTL80x9 的 PCI 和 ISA 卡也被支持。对于这些芯片组，支持自动协商和状态报告。

除标准的端口和 IRQ 规格外，`ed` 驱动程序还支持多个标志，可强制 8/16 位模式、启用/禁用多缓冲，以及选择默认接口类型（AUI/BNC，对于带双绞线的卡则为 AUI/10BaseT）。

标志为位字段，概述如下：

**`0x01`** 禁用收发器。在支持此功能的卡上，该标志会使收发器被禁用，并默认使用 AUI 连接。

**`0x02`** 强制 8 位模式。该标志强制卡工作于 8 位模式，而不论卡自身如何识别。这对于某些错误地自识别为 16 位但实际上只有 8 位接口的兼容卡可能是必需的。该标志优先于强制 16 位模式。

**`0x04`** 强制 16 位模式。该标志强制卡工作于 16 位模式，而不论卡自身如何识别。这对于某些错误地自识别为 8 位但实际上具有 16 位 ISA 接口的兼容卡可能是必需的。

**`0x08`** 禁用发送器多缓冲。该标志禁用多个发送缓冲区的使用，在数据包发送速度超过对端机器处理能力（表现为严重的丢包）的罕见情况下可能必要。某些（非 FreeBSD :-)）机器以太网性能极差，无法应对 1100K+ 的数据速率。使用此标志还可多提供一个数据包的接收缓冲，在 8 位卡上可能有助于减少接收丢包。

使用 3c503 卡时，可通过向 ifconfig(8) 指定 `link2` 选项来选择 AUI 连接（默认为 BNC）。

## 硬件

`ed` 驱动程序支持以下以太网 NIC：

- 3Com 3c503 Etherlink II（选项 ED_3C503）
- AR-P500 Ethernet
- Accton EN1644（旧型号）、EN1646（旧型号）、EN2203（旧型号）（110 引脚）（flags 0xd00000）
- Accton EN2212/EN2216/UE2216
- Allied Telesis CentreCOM LA100-PCM_V2
- Allied Telesis LA-98（flags 0x000000）（PC-98）
- Allied Telesis SIC-98、SIC-98NOTE（110 引脚）、SIU-98（flags 0x600000）（PC-98）
- Allied Telesis SIU-98-D（flags 0x610000）（PC-98）
- AmbiCom 10BaseT 卡（8002、8002T、8010 和 8610）
- Bay Networks NETGEAR FA410TXC Fast Ethernet
- Belkin F5D5020 PC Card Fast Ethernet
- Billionton LM5LT-10B Ethernet/Modem PC Card
- Billionton LNT-10TB、LNT-10TN Ethernet PC Card
- Bromax iPort 10/100 Ethernet PC Card
- Bromax iPort 10 Ethernet PC Card
- Buffalo LPC2-CLT、LPC3-CLT、LPC3-CLX、LPC4-TX、LPC-CTX PC Card
- Buffalo LPC-CF-CLT CF Card
- CNet BC40 adapter
- Compex Net-A adapter
- Compex RL2000
- Contec C-NET(98)、RT-1007(98)、C-NET(9N)（110 引脚）（flags 0xa00000）（PC-98）
- Contec C-NET(98)E-A、C-NET(98)L-A、C-NET(98)P（flags 0x300000）（PC-98）
- Corega Ether98-T（flags 0x000000）（PC-98）
- Corega Ether PCC-T/EtherII PCC-T/FEther PCC-TXF/PCC-TXD PCC-T/Fether II TXD
- Corega LAPCCTXD（TC5299J）
- CyQ've ELA-010
- DEC EtherWorks DE305
- Danpex EN-6200P2
- D-Link DE-298、DE-298P（flags 0x500000）（PC-98）
- D-Link DE-660、DE-660+
- D-Link IC-CARD/IC-CARD+ Ethernet
- ELECOM LD-98P（flags 0x500000）（PC-98）
- ELECOM LD-BDN、LD-NW801G（flags 0x200000）（PC-98）
- ELECOM Laneed LD-CDL/TX、LD-CDF、LD-CDS、LD-10/100CD、LD-CDWA（DP83902A）
- Hawking PN652TX PC Card（AX88790）
- HP PC Lan+ 27247B 和 27252A（选项 ED_HPP）
- IBM Creditcard Ethernet I/II
- ICM AD-ET2-T、DT-ET-25、DT-ET-T5、IF-2766ET、IF-2771ET、NB-ET-T（110 引脚）（flags 0x500000）（PC-98）
- I-O DATA LA/T-98、LA/T-98SB、LA2/T-98、ET/T-98（flags 0x900000）（PC-98）
- I-O DATA ET2/T-PCI
- I-O DATA PCLATE
- Kansai KLA-98C/T（flags 0x900000）（PC-98）
- Kingston KNE-PC2、CIO10T、KNE-PCM/x Ethernet
- KTI ET32P2 PCI
- Linksys EC2T/PCMPC100/PCM100、PCMLM56
- Linksys EtherFast 10/100 PC Card、Combo PCMCIA Ethernet Card（PCMPC100 V2）
- Logitec LAN-98T（flags 0xb00000）（PC-98）
- MACNICA Ethernet ME1 for JEIDA
- MACNICA ME98（flags 0x900000）（PC-98）
- MACNICA NE2098（flags 0x400000）（PC-98）
- MELCO EGY-98（flags 0x300000）（PC-98）
- MELCO LGH-98、LGY-98、LGY-98-N（110 引脚）、IND-SP、IND-SS（flags 0x400000）（PC-98）
- MELCO LGY-PCI-TR
- MELCO LPC-T/LPC2-T/LPC2-CLT/LPC2-TX/LPC3-TX/LPC3-CLX
- NDC Ethernet Instant-Link
- NEC PC-9801-77、PC-9801-78（flags 0x910000）（PC-98）
- NEC PC-9801-107、PC-9801-108（flags 0x800000）（PC-98）
- National Semiconductor InfoMover NE4100
- NetGear FA-410TX
- NetVin NV5000SC
- Network Everywhere Ethernet 10BaseT PC Card
- Networld 98X3（flags 0xd00000）（PC-98）
- Networld EC-98X、EP-98X（flags 0xd10000）（PC-98）
- New Media LANSurfer 10+56 Ethernet/Modem
- New Media LANSurfer
- Novell NE1000/NE2000/NE2100
- PLANEX ENW-8300-T
- PLANEX EN-2298-C（flags 0x200000）（PC-98）
- PLANEX EN-2298P-T、EN-2298-T（flags 0x500000）（PC-98）
- PLANEX FNW-3600-T
- Psion 10/100 LANGLOBAL Combine iT
- RealTek 8019
- RealTek 8029
- Relia Combo-L/M-56k PC Card
- SMC Elite 16 WD8013
- SMC Elite Ultra
- SMC EtherEZ98（flags 0x000000）（PC-98）
- SMC WD8003E/WD8003EBT/WD8003S/WD8003SBT/WD8003W/WD8013EBT/WD8013W 及兼容产品
- SMC EZCard PC Card、8040-TX、8041-TX（AX88x90）、8041-TX V.2（TC5299J）
- Socket LP-E、ES-1000 Ethernet/Serial、LP-E CF、LP-FE CF
- Surecom EtherPerfect EP-427
- Surecom NE-34
- TDK 3000/3400/5670 Fast Ethernet/Modem
- TDK LAK-CD031、Grey Cell GCS2000 Ethernet Card
- TDK DFL5610WS Ethernet/Modem PC Card
- Telecom Device SuperSocket RE450T
- Toshiba LANCT00A PC Card
- VIA VT86C926
- Winbond W89C940
- Winbond W89C940F

支持 C-Bus、ISA、PCI 和 PC Card 设备。

`ed` 驱动程序不支持以下以太网 NIC：

- Mitsubishi LAN Adapter B8895

## 诊断

- `ed%d: failed to clear shared memory at %x - check configuration.` 在系统引导时探测卡时，`ed` 驱动程序发现无法清除卡的共享内存。这通常由 BIOS 扩展 ROM 被配置在与以太网卡共享内存相同的地址空间所致。请找到引发冲突的卡并将其 BIOS ROM 改至不冲突的地址，或者更改 **/etc/device.hints** 中的设置，将卡的共享内存映射至不冲突的地址。

- `ed%d: Invalid irq configuration (%d) must be 2-5 for 3c503.` 在 device.hints(5) 文件中指定的 IRQ 号对 3Com 3c503 卡无效。3c503 只能分配 IRQ 2 到 5。

- `ed%d: Cannot find start of RAM.`

- `ed%d: Cannot find any RAM, start : %d, x = %d.` 对 Gateway 卡的探测未能成功配置卡的包内存。这通常表明该卡被错误地识别为 Gateway，或卡本身有缺陷。

- `ed: packets buffered, but transmitter idle.` 表明驱动程序中存在逻辑问题。不应发生。

- `ed%d: device timeout` 表示预期的发送器中断未发生。通常由 ISA 总线上与其他卡的中断冲突引起。如果内核配置的 IRQ 通道与卡实际使用的不同，也会出现此情况。此时你需要使用 DOS 工具重新配置卡，或相应地设置卡上的跳线。

- `ed%d: NIC memory corrupt - invalid packet length %d.` 表示收到的数据包长度大于 IEEE 802.3 标准允许的最大值或小于最小值。通常由 ISA 总线上与其他卡的冲突引起，但在某些情况下也可能表示线缆故障。

- `ed%d: remote transmit DMA failed to complete.` 表示向 NE1000 或 NE2000 风格卡的程序化 I/O 传输未能正确完成。通常由 ISA 总线速度设置过快引起。

- `ed%d: Invalid irq configuration (%ld) must be %s for %s` 表示设备使用了与支持或预期不同的 IRQ。

- `ed%d: Cannot locate my ports!` 设备使用了驱动程序未知的不同 I/O 端口。

- `ed%d: Cannot extract MAC address` 获取 MAC 地址失败。

- `ed%d: Missing mii!` 探测 MII 总线失败。这表明 PC Card 附件代码中存在错误，因为产生此错误消息的芯片需要 PHY。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [device.hints(5)](../man5/device.hints.5.md), ifconfig(8)

## 历史

`ed` 设备驱动程序首次出现于 FreeBSD 1.0。

## 作者

`ed` 设备驱动程序和本手册页由 David Greenman 编写。

## 注意事项

早期版本的 DS8390 芯片存在问题。每当接收环形缓冲区溢出时它们会锁死。它们偶尔会交换包环形头中长度字段的字节序（多种原因均与差一字节对齐有关）——导致出现“NIC memory corrupt - invalid packet length”消息。出现这些问题时卡会被复位，但除此之外从这些情况中恢复并无问题。

对 3Com 和 Novell 卡的 NIC 内存访问比 WD/SMC 卡慢得多；8 位板上不到 1MB/秒，16 位卡上不到 2MB/秒。这可能导致环形缓冲区溢出，在网络流量大时丢包。

Mitsubishi B8895 PC Card 使用 DP83902，但其 ASIC 部分无文档。NE2000 和 WD83x0 驱动程序均无法在此卡上工作。

## 缺陷

`ed` 驱动程序在收到任何坏包时复位卡的行为过于激进。结果，它可能丢弃一些已接收但尚未从卡传输到主内存的好包。

按现今标准，`ed` 驱动程序速度较慢。

PC Card 附件目前仅支持 D-Link DMF650TX LAN/Modem 卡的以太网端口。

`ed` 支持的某些设备不会生成 devd(8) 用于启动 dhclient(8) 所需的链路状态改变事件。如果你遇到 dhclient(8) 不启动的问题，且设备始终连接到网络，可以尝试将 **/etc/rc.conf** 中 ifconfig_ed0 条目里的“DHCP”改为“SYNCDHCP”作为变通方案。
