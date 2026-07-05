# ste.4

`ste` — Sundance Technologies ST201 快速以太网设备驱动

## 名称

`ste`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device ste

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_ste_load="YES"
```

## 描述

`ste` 驱动为基于 Sundance Technologies ST201 PCI 快速以太网控制器芯片的 PCI 以太网适配器和嵌入式控制器提供支持。

Sundance ST201 使用总线主控 DMA，设计为 3Com Etherlink XL 的兼容替代品。它使用相同的 DMA 描述符结构，操作上非常相似，但寄存器布局不同。ST201 具有 64 位多播哈希过滤器和用于站地址的单一完美过滤器条目。它使用 MII 收发器在半双工或全双工下支持 10 和 100Mbps 两种速度。

`ste` 驱动支持以下介质类型：

**autoselect** 启用介质类型和选项的自动选择。用户可通过在 **/etc/rc.conf** 文件中添加介质选项来手动覆盖自动选择的模式。

**10baseT/UTP** 设置 10Mbps 操作。还可使用 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**100baseTX** 设置 100Mbps（快速以太网）操作。还可使用 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

`ste` 驱动支持以下介质选项：

**full-duplex** 强制全双工操作。

**half-duplex** 强制半双工操作。

有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`ste` 驱动支持基于 Sundance Technologies ST201 的快速以太网适配器和嵌入式控制器，包括：

- D-Link DFE-530TXS
- D-Link DFE-550TX
- D-Link DFE-580TX

## SYSCTL 变量

以下变量同时可作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数使用：

**`dev.ste.%d.int_rx_mod`** 延迟 RX 中断的最大时间。有效范围为 0 至 209712，单位为 1us，默认为 150（150us）。值为 0 时实际上禁用 RX 中断适度。计时器的分辨率约为 3.2us，因此无法进行比 3.2us 更精细的调整。更改生效前无需将接口关闭再重新打开。

## 诊断

- ste%d: couldn't map ports/memory 已发生致命的初始化错误。
- ste%d: couldn't map interrupt 已发生致命的初始化错误。
- ste%d: watchdog timeout 设备已停止响应网络，或网络连接（电缆）存在问题。
- ste%d: no memory for rx list 驱动未能为接收环分配 mbuf。
- ste%d: no memory for tx list 驱动在分配填充缓冲区或将 mbuf 链折叠为簇时未能为发送环分配 mbuf。
- ste%d: chip is in D3 power state -- setting to D0 此消息仅适用于支持电源管理的适配器。某些操作系统在关机时将控制器置于低功耗模式，而某些 PCI BIOS 在配置之前未能将芯片从此状态唤醒。控制器在 D3 状态下会丢失其全部 PCI 配置，因此如果 BIOS 未及时将其恢复到全功耗模式，将无法正确配置。驱动会尝试检测此条件并将适配器恢复到 D0（全功耗）状态，但这可能不足以使驱动恢复到完全可操作的状态。如果在引导时看到此消息且驱动未能将设备附加为网络接口，则必须执行第二次热启动才能正确配置设备。注意，此条件仅在从其他操作系统热启动时发生。如果在引导 FreeBSD 之前关闭系统电源，则该卡应被正确配置。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [polling(4)](polling.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

> "Sundance ST201 data sheet".

## 历史

`ste` 设备驱动首次出现于 FreeBSD 3.0。

## 作者

`ste` 驱动由 Bill Paul <wpaul@ee.columbia.edu> 编写。
