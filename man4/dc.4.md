# dc.4

`dc` — DEC/Intel 21143 及其兼容芯片的 10/100 以太网驱动

## 名称

`dc`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device miibus
> device dc

`或者，若要在引导时以模块方式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_dc_load="YES"
```

## 描述

`dc` 驱动为基于 DEC/Intel 21143 芯片组及其兼容芯片的多种 PCI 快速以太网适配器和嵌入式控制器提供支持。

所有受支持的芯片组都具有相同的通用寄存器布局、DMA 描述符格式和操作方法。所有兼容芯片均基于 21143 设计并进行了各种修改。21143 本身支持 10baseT、BNC、AUI、MII 和 symbol 媒体连接、10 和 100Mbps 全双工或半双工、内置 NWAY 自动协商和局域网唤醒。21143 还提供多种接收过滤器编程选项，包括完美过滤、反向完美过滤和哈希表过滤。

某些兼容芯片相当接近地复制了 21143，而另一些仅保持了表面上的相似性。有些仅支持 MII 媒体连接。其他的使用不同的接收过滤器编程机制。至少有一种仅支持链式 DMA 描述符（大多数同时支持链式描述符和连续分配的固定大小环）。某些芯片（尤其是 PNIC）还有特殊的错误。`dc` 驱动尽最大努力为所有这些芯片组提供通用支持，以尽量减少特殊情形代码。

这些芯片被许多厂商使用，因此难以提供所有受支持网卡的完整列表。

`dc` 驱动支持以下媒体类型：

**`autoselect`** 启用媒体类型和选项的自动选择。用户可通过在 **`/etc/rc.conf`** 文件中加入媒体选项来手动覆盖自动选择的模式。注意：原始 PNIC 82c168 芯片上的内置 NWAY 自动协商存在严重缺陷，目前 `dc` 驱动不支持（详情见 Sx BUGS 节）。原始 82c168 出现在非常早期的 LinkSys LNE100TX 和 Matrox FastNIC 修订版上。

**`10baseT/UTP`** 设置 10Mbps 操作。也可使用 `mediaopt` 选项启用 `full-duplex` 操作。未指定 `full-duplex` 则意味着 `half-duplex` 模式。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。也可使用 `mediaopt` 选项启用 `full-duplex` 操作。未指定 `full-duplex` 则意味着 `half-duplex` 模式。

`dc` 驱动支持以下媒体选项：

**`full-duplex`** 强制全双工操作。如果未指定此媒体选项，接口将以半双工模式操作。

注意，某些仅支持 10Mbps 媒体连接的 Intel 21143 适配器可能不支持 100baseTX 媒体类型。有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`dc` 驱动为以下芯片组提供支持：

- DEC/Intel 21143
- ADMtek AL981 Comet、AN985 Centaur、ADM9511 Centaur II 和 ADM9513 Centaur II
- ALi/ULi M5261 和 M5263
- ASIX Electronics AX88140A 和 AX88141
- Conexant LANfinity RS7112（miniPCI）
- Davicom DM9009、DM9100、DM9102 和 DM9102A
- Lite-On 82c168 和 82c169 PNIC
- Lite-On/Macronix 82c115 PNIC II
- Macronix 98713、98713A、98715、98715A、98715AEC-C、98725、98727 和 98732
- Xircom X3201（仅 cardbus）

目前已知可与 `dc` 驱动配合工作的网卡有：

- 3Com OfficeConnect 10/100B（ADMtek AN985 Centaur-P）
- Abocom FE2500
- Accton EN1217（98715A）
- Accton EN2242 MiniPCI
- Adico AE310TX（98715A）
- Alfa Inc GFC2204（ASIX AX88140A）
- Compaq Presario 7900 系列台式机内置的仅 10Mbps 以太网（21143，非 MII）
- LinkSys EtherFast 10/100 Instant GigaDrive 内置以太网（DM9102，MII）
- CNet Pro110B（ASIX AX88140A）
- CNet Pro120A（98715A 或 98713A）和 CNet Pro120B（98715）
- Compex RL100-TX（98713 或 98713A）
- D-Link DFE-570TX（21143，MII，四端口）
- Digital DE500-BA 10/100（21143，非 MII）
- ELECOM Laneed LD-CBL/TXA（ADMtek AN985）
- Hawking CB102 CardBus
- IBM EtherJet Cardbus Adapter
- Intel PRO/100 Mobile Cardbus（使用 X3201 芯片组的版本）
- Jaton XpressNet（Davicom DM9102）
- Kingston KNE100TX（21143，MII）
- Kingston KNE110TX（PNIC 82c169）
- LinkSys LNE100TX（PNIC 82c168、82c169）
- LinkSys LNE100TX v2.0（PNIC II 82c115）
- LinkSys LNE100TX v4.0/4.1（ADMtek AN985 Centaur-P）
- Matrox FastNIC 10/100（PNIC 82c168、82c169）
- Melco LGY-PCI-TXL
- Microsoft MN-120 10/100 CardBus（ADMTek Centaur-C）
- Microsoft MN-130 10/100 PCI（ADMTek Centaur-P）
- NDC SOHOware SFA110A（98713A）
- NDC SOHOware SFA110A Rev B4（98715AEC-C）
- NetGear FA310-TX Rev. D1、D2 或 D3（PNIC 82c169）
- Netgear FA511
- PlaneX FNW-3602-T（ADMtek AN985）
- SMC EZ Card 10/100 1233A-TX（ADMtek AN985）
- SVEC PN102-TX（98713）
- Xircom Cardbus Realport
- Xircom Cardbus Ethernet 10/100
- Xircom Cardbus Ethernet II 10/100

## 诊断

- dc%d: couldn't map ports/memory 发生了致命的初始化错误。
- dc%d: couldn't map interrupt 发生了致命的初始化错误。
- dc%d: watchdog timeout 一个数据包已排队等待传输并且已发出传输命令，但设备在超时之前未能确认传输。如果设备因某种原因无法传递中断，或者网络连接存在问题（线缆或网络设备）导致链路丢失，则可能发生此情况。
- dc%d: no memory for rx list 驱动未能为接收环分配一个 mbuf。
- dc%d: TX underrun -- increasing TX threshold 设备在尝试 DMA 并传输数据包时发生传输欠载错误。如果主机无法足够快地将数据包数据 DMA 到网卡的 FIFO 中，就会发生这种情况。驱动会动态增加传输起始阈值，以便在 NIC 开始将其发送到线缆之前必须有更多数据被 DMA 到 FIFO 中。
- dc%d: TX underrun -- using store and forward mode 在尝试了所有可能的传输起始阈值设置后，设备仍继续产生传输欠载，因此驱动将芯片编程为存储转发模式。在此模式下，NIC 在整个数据包传输到其 FIFO 内存之前不会开始传输。
- dc%d: chip is in D3 power state -- setting to D0 此消息仅适用于支持电源管理的适配器。某些操作系统在关机时将控制器置于低功耗模式，而某些 PCI BIOS 在配置芯片之前未能将其从该状态唤醒。控制器在 D3 状态下会丢失其所有 PCI 配置，因此如果 BIOS 未及时将其设置回全功率模式，则无法正确配置。驱动会尝试检测此情况并将适配器恢复到 D0（全功率）状态，但这可能不足以使驱动恢复到完全可操作的状态。如果在引导时看到此消息且驱动未能将设备附加为网络接口，则必须执行第二次热启动才能正确配置设备。注意，此情况仅在从其他操作系统热启动时发生。如果在引导 FreeBSD 之前关机，网卡应能正确配置。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [polling(4)](polling.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

> "ADMtek AL981, AL983 and AL985 data sheets".

> "ASIX Electronics AX88140A and AX88141 data sheets".

> "Davicom DM9102 data sheet".

> "Intel 21143 Hardware Reference Manual".

> "Macronix 98713/A, 98715/A and 98725 data sheets".

> "Macronix 98713/A and 98715/A app notes".

## 历史

`dc` 设备驱动首次出现于 FreeBSD 4.0。

## 作者

`dc` 驱动由 Bill Paul <wpaul@ee.columbia.edu> 编写。

## 缺陷

Macronix 应用说明声称，为了使芯片正常工作，驱动必须向 CSR16 寄存器写入某个魔数。这些数字在应用说明中有记载，但其位的精确含义并未说明。

98713A 似乎在 10Mbps 全双工模式下存在问题。发送器可工作，但接收器往往会产生许多无法解释的错误，导致整体性能很差。98715A 不存在此问题。98713A 的所有其他模式似乎都能正常工作。

原始 82c168 PNIC 芯片具有内置 NWAY 支持，用于某些早期的 LinkSys LNE100TX 和 Matrox FastNIC 网卡，但它存在严重缺陷且难以可靠使用。因此，目前不支持此芯片组的自动协商：驱动默认将 NIC 设置为 10baseT 半双工，由操作员在必要时手动选择其他模式。（后续网卡使用外部 MII 收发器实现 NWAY 自动协商，可正常工作。）

`dc` 驱动默认将 82c168 和 82c169 PNIC 芯片编程为使用存储转发设置作为传输起始阈值。这是为了解决某些 NIC/PCI 总线组合的问题，其中 PNIC 在 100Mbps 操作时可能发送损坏的帧，可能是由于 PCI DMA 突发传输错误所致。

82c168 和 82c169 PNIC 芯片还有一个接收错误，有时在繁重的接收和发送活动期间表现出来，芯片会错误地将接收到的帧 DMA 到主机。芯片似乎连同接收帧数据一起上传了几 KB 的垃圾数据，污染了多个 RX 缓冲区而不仅仅是预期的一个。`dc` 驱动会检测此情况并挽救帧；但在此过程中会产生严重的性能损失。

当驱动尝试下载接收过滤器设置帧时，PNIC 芯片有时也会产生传输欠载错误，可能导致接收过滤器被错误编程。`dc` 驱动会监视此情况并重新排队设置帧，直到其成功传输。

观察到 ADMtek AL981 芯片（可能也包括 AN985）有时在传输时会卡住：这似乎发生在驱动排队一系列帧导致其从发送描述符环末尾回绕到开头时。`dc` 驱动通过在 Fn dc_start 例程的单次调用期间不排队任何越过发送环末尾的帧来尝试避免此情况。此变通方法对传输性能的影响可忽略不计。
