# vr.4

`vr` — VIA Technologies Rhine I/II/III 以太网设备驱动

## 名称

`vr`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device vr

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_vr_load="YES"
```

## 描述

`vr` 驱动为基于 VIA Technologies VT3043 Rhine I、VT86C100A Rhine II 和 VT6105/VT6105M Rhine III 快速以太网控制器芯片的 PCI 以太网适配器和嵌入式控制器提供支持。

VIA Rhine 芯片使用总线主控 DMA，其描述符布局设计得类似于 DEC 21x4x“tulip”芯片。但寄存器布局不同，且 Rhine 芯片中的接收过滤器要简单得多，通过寄存器编程而不是通过发送 DMA 引擎下载专用设置帧来配置。发送和接收 DMA 缓冲区必须按长字对齐。Rhine 芯片通过 MII 总线与外部物理层设备连接。它们在半双工或全双工模式下均支持 10 和 100Mbps 速率。

`vr` 驱动支持以下介质类型：

**autoselect** 启用介质类型和选项的自动选择。用户可通过在 **/etc/rc.conf** 文件中添加介质选项来手动覆盖自动选择的模式。

**10baseT/UTP** 设置 10Mbps 操作。还可使用 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**100baseTX** 设置 100Mbps（快速以太网）操作。还可使用 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

`vr` 驱动支持以下介质选项：

**full-duplex** 强制全双工操作。

**half-duplex** 强制半双工操作。

注意，100baseTX 介质类型仅在适配器支持时可用。有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`vr` 驱动支持基于 VIA Technologies Rhine I、Rhine II 和 Rhine III 的快速以太网适配器，包括：

- AOpen/Acer ALN-320
- D-Link DFE520-TX
- D-Link DFE530-TX
- Hawking Technologies PN102TX
- Soekris Engineering net5501

## SYSCTL 变量

以下变量作为 [sysctl(8)](../man8/sysctl.8.md) 变量可用：

**`dev.vr.%d.stats`** 显示驱动中维护的大量有用的 MAC 计数器。

## 诊断

- vr%d: couldn't map memory 发生了致命的初始化错误。
- vr%d: couldn't map interrupt 发生了致命的初始化错误。
- vr%d: watchdog timeout 设备已停止响应网络，或网络连接（网线）存在问题。
- vr%d: no memory for rx list 驱动未能为接收环分配 mbuf。
- vr%d: no memory for tx list 驱动在分配填充缓冲区或将 mbuf 链合并为簇时，未能为发送环分配 mbuf。
- vr%d: chip is in D3 power state -- setting to D0 此消息仅适用于支持电源管理的适配器。某些操作系统在关机时将控制器置于低功耗模式，而某些 PCI BIOS 在配置芯片之前未能将其从此状态中唤醒。控制器在 D3 状态下会丢失其全部 PCI 配置，因此如果 BIOS 未及时将其恢复到全功耗模式，将无法正确配置。驱动会尝试检测此情况并将适配器恢复到 D0（全功耗）状态，但这可能不足以使驱动恢复到完全可操作的状态。如果在引导时看到此消息且驱动未能将设备附加为网络接口，则需要执行第二次热启动以使设备正确配置。注意，此情况仅在从其他操作系统热启动时发生。如果在引导 FreeBSD 之前关闭系统电源，则网卡应能正确配置。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [polling(4)](polling.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

> "The VIA Technologies VT86C100A data sheet".

## 历史

`vr` 设备驱动最早出现在 FreeBSD 3.0 中。

## 作者

`vr` 驱动由 Bill Paul <wpaul@ctr.columbia.edu> 编写。

## 缺陷

`vr` 驱动在发送前始终将发送 mbuf 链复制到长字对齐的缓冲区中，以迁就 Rhine 芯片。如果缓冲区未正确对齐，芯片会对所提供的缓冲区地址进行舍入，并从错误的位置开始 DMA。此缓冲区复制会损害较慢系统上的发送性能，但无法避免。在较快的机器上（如 Pentium II），性能影响要小得多。
