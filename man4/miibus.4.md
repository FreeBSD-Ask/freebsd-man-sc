# miibus(4)

`miibus` — IEEE 802.3 媒体独立接口网络总线

## 名称

`miibus`

## 概要

对于大多数网络接口卡（NIC）：device miibus

## 描述

`miibus` 驱动提供媒体访问控制（MAC）子层、物理层实体（PHY）、站点管理（STA）实体与 PHY 层之间的互连，如 IEEE 802.3 标准所定义。

`miibus` 层允许网络设备驱动程序共享各种外部 PHY 设备的通用支持代码。大多数 10/100 网络接口卡要么使用 MII 收发器，要么具有可使用 MII 接口编程的内置收发器。`miibus` 驱动目前使用 ifmedia 接口处理所有媒体检测、选择和报告。对于不由特定驱动处理的所有 PHY，已包含一个通用驱动程序，这是可能的，因为所有 10/100 PHY 都实现了相同的通用寄存器集以及其供应商特定的寄存器集。

以下网络设备驱动程序使用 `miibus` 接口：

**[ae(4)](ae.4.md)** Attansic/Atheros L2 快速以太网

**[age(4)](age.4.md)** Attansic/Atheros L1 千兆以太网

**[alc(4)](alc.4.md)** Atheros AR8131/AR8132 PCIe 以太网

**[ale(4)](ale.4.md)** Atheros AR8121/AR8113/AR8114 PCIe 以太网

**[aue(4)](aue.4.md)** ADMtek USB 以太网

**[axe(4)](axe.4.md)** ASIX Electronics AX88172 USB 以太网

**[axge(4)](axge.4.md)** ASIX Electronics AX88178A/AX88179 USB 以太网

**[bce(4)](bce.4.md)** Broadcom NetXtreme II 千兆以太网

**[bfe(4)](bfe.4.md)** Broadcom BCM4401 以太网

**[bge(4)](bge.4.md)** Broadcom BCM570xx 千兆以太网

**[cas(4)](cas.4.md)** Sun Cassini/Cassini+ 和 National Semiconductor DP83065 Saturn

**[dc(4)](dc.4.md)** DEC/Intel 21143 及各种兼容产品

**ed(4)** NE[12]000, SMC Ultra, 3c503, DS8390 卡

**[et(4)](et.4.md)** Agere ET1310 千兆以太网

**[fxp(4)](fxp.4.md)** Intel EtherExpress PRO/100B

**[gem(4)](gem.4.md)** Sun ERI, Sun GEM 和 Apple GMAC 以太网

**[jme(4)](jme.4.md)** JMicron JMC250 千兆/JMC260 快速以太网

**[lge(4)](lge.4.md)** Level 1 LXT1001 NetCellerator 千兆以太网

**[msk(4)](msk.4.md)** Marvell/SysKonnect Yukon II 千兆以太网

**[nfe(4)](nfe.4.md)** NVIDIA nForce MCP 网络适配器

**[nge(4)](nge.4.md)** National Semiconductor DP83820/DP83821 千兆以太网

**[re(4)](re.4.md)** Realtek 8139C+/8169/8169S/8110S

**[rl(4)](rl.4.md)** Realtek 8129/8139

**[rue(4)](rue.4.md)** Realtek RTL8150 USB 转快速以太网

**[sge(4)](sge.4.md)** Silicon Integrated Systems SiS190/191 以太网

**[sis(4)](sis.4.md)** Silicon Integrated Systems SiS 900/SiS 7016

**[sk(4)](sk.4.md)** SysKonnect SK-984x 和 SK-982x 千兆以太网

**[smsc(4)](smsc.4.md)** SMSC LAN9xxx USB 快速以太网

**[ste(4)](ste.4.md)** Sundance ST201 (D-Link DFE-550TX)

**[stge(4)](stge.4.md)** Sundance/Tamarack TC9021 千兆以太网

**[udav(4)](udav.4.md)** Davicom DM9601 USB 以太网

**[ure(4)](ure.4.md)** Realtek RTL8152 USB 转快速以太网

**[vge(4)](vge.4.md)** VIA VT612x PCI 千兆以太网

**[vr(4)](vr.4.md)** VIA Rhine, Rhine II

**[vte(4)](vte.4.md)** DM&P Vortex86 RDC R6040 快速以太网

**[xl(4)](xl.4.md)** 3Com 3c90x

## 兼容性

`miibus` 的实现最初旨在具有与 BSD/OS 和 NetBSD 类似的 API 接口，但结果是它们不是行为良好的 newbus 设备驱动程序。

## 参见

[ae(4)](ae.4.md), [age(4)](age.4.md), [alc(4)](alc.4.md), [ale(4)](ale.4.md), arp(4), [aue(4)](aue.4.md), [axe(4)](axe.4.md), [axge(4)](axge.4.md), [bce(4)](bce.4.md), [bfe(4)](bfe.4.md), [bge(4)](bge.4.md), [cas(4)](cas.4.md), [dc(4)](dc.4.md), ed(4), [et(4)](et.4.md), [fxp(4)](fxp.4.md), [gem(4)](gem.4.md), [jme(4)](jme.4.md), [lge(4)](lge.4.md), [msk(4)](msk.4.md), [netintro(4)](netintro.4.md), [nfe(4)](nfe.4.md), [nge(4)](nge.4.md), [re(4)](re.4.md), [rgephy(4)](rgephy.4.md), [rl(4)](rl.4.md), [rue(4)](rue.4.md), [sge(4)](sge.4.md), [sis(4)](sis.4.md), [sk(4)](sk.4.md), [smsc(4)](smsc.4.md), [ste(4)](ste.4.md), [stge(4)](stge.4.md), [udav(4)](udav.4.md), [ure(4)](ure.4.md), [vge(4)](vge.4.md), [vr(4)](vr.4.md), [vte(4)](vte.4.md), [xl(4)](xl.4.md)

## 标准

有关 MII 的更多信息可在 IEEE 802.3 标准中找到。

## 历史

`miibus` 驱动首次出现于 FreeBSD 3.3。

## 作者

本手册页由 Tom Rhodes <trhodes@FreeBSD.org> 编写。
