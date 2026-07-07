# rl(4)

`rl` — Realtek 8129/8139 快速以太网设备驱动

## 名称

`rl`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus
> device rl

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_rl_load="YES"
```

## 描述

`rl` 驱动为基于 Realtek 8129 和 8139 快速以太网控制器芯片的 PCI 以太网适配器和嵌入式控制器提供支持。

Realtek 8129/8139 系列控制器使用总线主控 DMA，但不使用基于描述符的数据传输机制。接收方使用一个固定大小的环形缓冲区，必须从中将数据包复制到 mbuf 中。发送方只有四个外发数据包地址寄存器，要求所有外发数据包都作为连续缓冲区存储。此外，外发数据包缓冲区必须按长字对齐，否则发送将失败。

8129 与 8139 的区别在于：8139 拥有通过特殊直接访问寄存器控制的内部 PHY，而 8129 通过 MII 总线使用外部 PHY。8139 在全双工或半双工下均支持 10 和 100Mbps 速率。在配备合适 PHY 芯片的情况下，8129 可支持相同的速率和模式。

注意：对 8139C+ 芯片的支持由 [re(4)](re.4.md) 驱动提供。

`rl` 驱动支持以下介质类型：

**autoselect** 启用介质类型和选项的自动选择。仅当连接到 Realtek 控制器的 PHY 芯片支持 NWAY 自动协商时才支持此项。用户可通过在 **`/etc/rc.conf`** 文件中添加介质选项来手动覆盖自动选择的模式。

**10baseT/UTP** 设置 10Mbps 操作。也可使用 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**100baseTX** 设置 100Mbps（快速以太网）操作。也可使用 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

`rl` 驱动支持以下介质选项：

**full-duplex** 强制全双工操作。

**half-duplex** 强制半双工操作。

注意，100baseTX 介质类型仅在适配器支持时可用。有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`rl` 驱动支持的适配器包括：

- Accton "Cheetah" EN1207D (MPX 5030/5038; Realtek 8139 兼容)
- Allied Telesyn AT2550
- Allied Telesyn AT2500TX
- Belkin F5D5000
- BUFFALO (Melco INC.) LPC-CB-CLX (CardBus)
- Compaq HNE-300
- CompUSA 无名 10/100 PCI 以太网 NIC
- Corega FEther CB-TXD
- Corega FEtherII CB-TXD
- D-Link DFE-520TX (rev. C1)
- D-Link DFE-528TX
- D-Link DFE-530TX+
- D-Link DFE-538TX
- D-Link DFE-690TXD
- Edimax EP-4103DL CardBus
- Encore ENL832-TX 10/100 M PCI
- Farallon NetLINE 10/100 PCI
- Genius GF100TXR
- GigaFast Ethernet EE100-AXP
- KTX-9130TX 10/100 快速以太网
- LevelOne FPC-0106TX
- Longshine LCS-8038TX-R
- NDC Communications NE100TX-E
- Netronix Inc. EA-1210 NetEther 10/100
- Nortel Networks 10/100BaseTX
- OvisLink LEF-8129TX
- OvisLink LEF-8139TX
- Peppercon AG ROL-F
- Planex FNW-3603-TX
- Planex FNW-3800-TX
- SMC EZ Card 10/100 PCI 1211-TX
- SOHO (PRAGMATIC) UE-1211C

## 加载器可调参数

**`dev.rl.%unit.prefer_iomap`** 此可调参数控制指定设备上应使用哪种寄存器映射。非零值启用 I/O 空间寄存器映射。对于没有 I/O 空间寄存器映射的控制器，应将此可调参数设置为 0 以使用内存空间寄存器映射。默认值为 1，使用 I/O 空间寄存器映射。

**`dev.rl.%unit.twister_enable`** 非零值启用指定设备上的长电缆调优。默认禁用。

## 诊断

- rl%d: couldn't map memory 发生致命的初始化错误。
- rl%d: couldn't map interrupt 发生致命的初始化错误。
- rl%d: watchdog timeout 设备已停止响应网络，或网络连接（电缆）存在问题。
- rl%d: no memory for rx list 驱动未能为接收环分配 mbuf。
- rl%d: no memory for tx list 驱动在分配填充缓冲区或将 mbuf 链折叠为簇时，未能为发送环分配 mbuf。
- rl%d: chip is in D3 power state -- setting to D0 此消息仅适用于支持电源管理的适配器。某些操作系统在关机时将控制器置于低功耗模式，而某些 PCI BIOS 在配置之前未能将芯片从此状态唤醒。控制器在 D3 状态下会丢失其全部 PCI 配置，因此如果 BIOS 未能及时将其设置回全功耗模式，将无法正确配置。驱动会尝试检测此状况并将适配器恢复至 D0（全功耗）状态，但这可能不足以使驱动恢复到完全可用状态。如果在引导时看到此消息且驱动未能将设备附加为网络接口，你需要执行第二次热启动才能正确配置设备。注意，此状况仅在从其他操作系统热启动时发生。如果在引导 FreeBSD 之前关机，网卡应能被正确配置。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [polling(4)](polling.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

> *The Realtek 8129, 8139 and 8139C+ datasheets*。

## 历史

`rl` 设备驱动最早出现在 FreeBSD 3.0 中。

## 作者

`rl` 驱动由 Bill Paul <wpaul@ctr.columbia.edu> 编写。

## 缺陷

由于外发数据包必须按长字对齐，发送例程必须在发送前将未对齐的数据包复制到 mbuf 簇缓冲区中。该驱动利用了这样一个事实：簇缓冲区池在系统启动时分配于以页边界起始的连续区域中。由于簇缓冲区大小为 2048 字节，按定义即按长字对齐。该驱动或许不应依赖于这一特性。

Realtek 数据手册的质量尤其低劣，许多信息缺失，特别是关于接收操作的部分。数据手册未提及的一个特别重要的事实与芯片填充接收缓冲区的方式有关。当中断发出表示已接收到一帧的信号时，在驱动忙于处理第一帧时，可能另一帧正被复制到接收缓冲区中。如果驱动恰好在芯片完成下一帧其余部分的 DMA 之前完成对第一帧的处理，驱动可能会在芯片有机会完成整帧 DMA 之前就尝试处理缓冲区中的下一帧。

驱动可通过检查实际数据包数据之前头部中的帧长度来检测不完整帧：不完整帧会具有魔数长度 0xFFF0。当驱动遇到此值时，它知道已处理完所有当前可用的数据包。无论是此魔数值还是其意义，都未在 Realtek 数据手册中任何地方加以记录。
