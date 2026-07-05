# sis.4

`sis` — SiS 900、SiS 7016 和 NS DP83815/DP83816 快速以太网设备驱动

## 名称

`sis`

## 概要

`要将此驱动编译进内核，请将以下行添加到你的内核配置文件中：`

> device miibus
> device sis

`或者，要在引导时以模块形式加载此驱动，请将以下行添加到 loader.conf(5) 中：`

```sh
if_sis_load="YES"
```

## 描述

`sis` 驱动为基于 Silicon Integrated Systems SiS 900 和 SiS 7016 快速以太网控制器芯片的 PCI 以太网适配器和嵌入式控制器提供支持。

此驱动还支持基于 National Semiconductor DP83815（MacPhyter）和 DP83816 PCI 以太网控制器芯片的适配器。

SiS 900 是一款 100Mbps 以太网 MAC 和符合 MII 标准的收发器单封装芯片。它使用总线主控 DMA 和分散/聚集描述符方案。SiS 7016 与 SiS 900 类似，但没有内部 PHY，需要将外部收发器连接到其 MII 接口。SiS 900 和 SiS 7016 都具有 128 位多播哈希过滤器和单个用于站地址的完美过滤器条目。

NS DP83815 也是一款具有集成 PHY 的 100Mbps 以太网 MAC。NatSemi 芯片与 SiS 900 共享许多相同的功能和相当相似的编程接口，因此两者由同一驱动支持。

`sis` 驱动支持以下媒体类型：

**autoselect** 启用媒体类型和选项的自动选择。用户可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加媒体选项来手动覆盖自动选择的模式。

**10baseT/UTP** 设置 10Mbps 操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择"full-duplex"或"half-duplex"模式。

**100baseTX** 设置 100Mbps（快速以太网）操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择"full-duplex"或"half-duplex"模式。

`sis` 驱动支持以下媒体选项：

**full-duplex** 强制全双工操作。

**half-duplex** 强制半双工操作。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`sis` 驱动支持基于 Silicon Integrated Systems SiS 900 和 SiS 7016 的快速以太网适配器和嵌入式控制器，以及基于 National Semiconductor DP83815（MacPhyter）和 DP83816 芯片的快速以太网适配器。支持的适配器包括：

- @Nifty FNECHARD IFC USUP-TX
- MELCO LGY-PCI-TXC
- Netgear FA311-TX（DP83815）
- Netgear FA312-TX（DP83815）
- SiS 630、635 和 735 主板芯片组
- Soekris Engineering net45xx、net48xx、lan1621 和 lan1641

## SYSCTL 变量

以下变量既可作为 [sysctl(8)](../man8/sysctl.8.md) 变量，也可作为 [loader(8)](../man8/loader.8.md) 可调参数使用：

**`dev.sis.%unit.manual_pad`** 此变量控制指定设备上 DP83815/DP83816 控制器如何对短帧进行填充。已知 DP83815/DP83816 控制器会为短帧填充 0xFF，这违反了 RFC 1042。将此变量设为非零值可让驱动手动用零填充每个短帧，代价是额外的 CPU 周期。默认值为 0，让硬件执行自动填充。

## 诊断

- sis%d: couldn't map ports/memory 已发生致命初始化错误。
- sis%d: couldn't map interrupt 已发生致命初始化错误。
- sis%d: watchdog timeout 设备已停止响应网络，或网络连接存在问题（如电缆故障）。
- sis%d: no memory for rx list 驱动未能为接收环分配 mbuf。
- sis%d: no memory for tx list 驱动在分配填充缓冲区或将 mbuf 链合并为簇时未能为发送环分配 mbuf。
- sis%d: chip is in D3 power state -- setting to D0 此消息仅适用于支持电源管理的适配器。某些操作系统在关机时将控制器置于低功耗模式，而某些 PCI BIOS 在配置芯片前未能将其从此状态唤醒。控制器在 D3 状态下会丢失所有 PCI 配置，因此如果 BIOS 未及时将其设回全功率模式，将无法正确配置。驱动会尝试检测此条件并将适配器恢复到 D0（全功率）状态，但这可能不足以使驱动恢复到完全可操作状态。如果在引导时看到此消息且驱动未能将设备附加为网络接口，则需执行热启动以正确配置设备。注意，此条件仅在从其他操作系统热启动时发生。如果在引导 FreeBSD 之前关闭系统电源，则应能正确配置卡。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [polling(4)](polling.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

> "SiS 900 and SiS 7016 datasheets"。

> "NatSemi DP83815 datasheet"。

## 历史

`sis` 设备驱动最早出现于 FreeBSD 3.0。

## 作者

`sis` 驱动由 Bill Paul <wpaul@ee.columbia.edu> 编写。
