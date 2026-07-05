# ahc.4

`ahc` — Adaptec VL/ISA/PCI SCSI 主机适配器驱动

## 名称

`ahc`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device scbus
> device ahc
> 对于一块或多块 PCI 卡：
> device pci

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
ahc_load="YES"
ahc_isa_load="YES"
ahc_pci_load="YES"
```

## 描述

此驱动提供对连接到 Adaptec AIC77xx 和 AIC78xx 主机适配器芯片的 SCSI 总线的访问。

驱动特性包括支持 twin 和 wide 总线、根据控制器类型支持 fast、ultra 或 ultra2 同步传输、标记队列、SCB 分页以及目标模式。

在引导时可访问的 SCSI-Select 菜单中执行的每目标配置由此驱动遵循。这包括同步/异步传输、最大同步协商速率、wide 传输、断开连接以及主机适配器的 SCSI ID。对于以系统专用方式而非直接连接到 aic7xxx 控制器的串行 EEPROM 来存储非易失性设置的系统，必须启用 BIOS 驱动才能访问此信息。此限制适用于许多芯片直接焊接在主板上的配置。

aic7xxx 产品线的性能和功能集各不相同。下表提供了 `ahc` 驱动支持的不同芯片的比较。请注意，wide 和 twin 通道功能虽然始终由特定芯片支持，但在特定的主板或卡设计中可能被禁用。

| *Chip* | MIPS | Bus | MaxSync | MaxWidth | SCBs | Features |
| --- | --- | --- | --- | --- | --- | --- |
| aic7770 | 10 | VL | 10MHz | 16Bit | 4 | 1 |
| aic7850 | 10 | PCI/32 | 10MHz | 8Bit | 3 |  |
| aic7860 | 10 | PCI/32 | 20MHz | 8Bit | 3 |  |
| aic7870 | 10 | PCI/32 | 10MHz | 16Bit | 16 |  |
| aic7880 | 10 | PCI/32 | 20MHz | 16Bit | 16 |  |
| aic7890 | 20 | PCI/32 | 40MHz | 16Bit | 16 | 3 4 5 6 7 8 |
| aic7891 | 20 | PCI/64 | 40MHz | 16Bit | 16 | 3 4 5 6 7 8 |
| aic7892 | 20 | PCI/64 | 80MHz | 16Bit | 16 | 3 4 5 6 7 8 |
| aic7895 | 15 | PCI/32 | 20MHz | 16Bit | 16 | 2 3 4 5 |
| aic7895C | 15 | PCI/32 | 20MHz | 16Bit | 16 | 2 3 4 5 8 |
| aic7896 | 20 | PCI/32 | 40MHz | 16Bit | 16 | 2 3 4 5 6 7 8 |
| aic7897 | 20 | PCI/64 | 40MHz | 16Bit | 16 | 2 3 4 5 6 7 8 |
| aic7899 | 20 | PCI/64 | 80MHz | 16Bit | 16 | 2 3 4 5 6 7 8 |

- 多路复用 Twin 通道设备——一个控制器服务两条总线。
- 多功能 Twin 通道设备——一个芯片上两个控制器。
- 命令通道辅助 DMA 引擎——允许分散聚集列表和 SCB 预取。
- 64 字节 SCB 支持——SCSI CDB 嵌入 SCB 中以消除额外的一次 DMA。
- 块移动指令支持——使某些 sequencer 操作速度加倍。
- “Bayonet”风格分散聚集引擎——改善 S/G 预取性能。
- 队列寄存器——允许在不暂停 sequencer 的情况下将新事务入队。
- 多目标 ID——允许控制器作为目标在多个 SCSI ID 上响应选择。

## 配置选项

要允许 PCI 适配器在启用时使用内存映射 I/O：

`options AHC_ALLOW_MEMIO=(0 -- 禁用, 1 -- 启用)`

> 内存映射 I/O 比另一种方式（编程 I/O）更高效。
> 大多数 PCI BIOS 会映射设备，使得与卡通信的两种方式都可用。
> 在某些情况下，通常是 PCI 设备位于 PCI->PCI 桥之后时，
> BIOS 可能无法正确初始化芯片以进行内存映射 I/O。此问题的典型症状是
> 尝试内存映射 I/O 时系统挂起。
> 大多数现代主板能正确执行初始化，启用此选项工作正常，
> 这是默认值。此选项也可通过下文所述的 device hint 动态配置。

要将一个或多个控制器静态配置为承担目标角色：

`options AHC_TMODE_ENABLE=<unit 的位掩码>`

> 分配给此选项的值应为需要目标模式的所有 unit 的位图。例如，
> 值 0x25 将在 unit 0、2 和 5 上启用目标模式。值 0x8a 为 unit 1、3 和 7 启用。
> 请注意，控制器可通过下文所述的 device hint 动态配置。

## 引导选项

以下选项可通过在 **`/boot/device.hints`** 中设置值来切换。

它们是：

**`hint.ahc.`** `N``.tmode_enable` 用于定义是否启用 SCSI 目标模式的 hint，默认为禁用（0 -- 禁用，1 -- 启用）。

**`hint.ahc.`** `N``.allow_memio` 用于定义此适配器是否启用或禁用内存映射 I/O 的 hint，默认为启用（0 -- 禁用，1 -- 启用）。

## 硬件

`ahc` 驱动支持以下 VL/ISA/PCI 并行 SCSI 控制器和卡：

- Adaptec AIC7770 host adapter chip
- Adaptec AIC7850 host adapter chip
- Adaptec AIC7860 host adapter chip
- Adaptec AIC7870 host adapter chip
- Adaptec AIC7880 host adapter chip
- Adaptec AIC7890 host adapter chip
- Adaptec AIC7891 host adapter chip
- Adaptec AIC7892 host adapter chip
- Adaptec AIC7895 host adapter chip
- Adaptec AIC7896 host adapter chip
- Adaptec AIC7897 host adapter chip
- Adaptec AIC7899 host adapter chip
- Adaptec 274X(W)
- Adaptec 274X(T)
- Adaptec 2910
- Adaptec 2915
- Adaptec 2920C
- Adaptec 2930C
- Adaptec 2930U2
- Adaptec 2940
- Adaptec 2940J
- Adaptec 2940N
- Adaptec 2940U
- Adaptec 2940AU
- Adaptec 2940UW
- Adaptec 2940UW Dual
- Adaptec 2940UW Pro
- Adaptec 2940U2W
- Adaptec 2940U2B
- Adaptec 2950U2W
- Adaptec 2950U2B
- Adaptec 19160B
- Adaptec 29160B
- Adaptec 29160N
- Adaptec 3940
- Adaptec 3940U
- Adaptec 3940AU
- Adaptec 3940UW
- Adaptec 3940AUW
- Adaptec 3940U2W
- Adaptec 3950U2
- Adaptec 3960
- Adaptec 39160
- Adaptec 3985
- Adaptec 4944UW
- 许多带板载 SCSI 支持的主板

## SCSI 控制块（SCB）

发送到 SCSI 总线上设备的每个事务都会分配一个“SCSI Control Block”（SCB）。SCB 包含控制器处理事务所需的所有信息。芯片特性表列出了可存储在片上内存中的 SCB 数量。所有型号编号大于或等于 7870 的芯片都允许用外部 SRAM 扩充片上 SCB 空间，最多可达 255 个 SCB。很少有 Adaptec 控制器配置带有外部 SRAM。

如果没有外部 SRAM，SCB 是一种有限资源。以直接方式使用 SCB 仅允许驱动处理与物理 SCB 数量相同的并发事务。要充分利用 SCSI 总线及总线上的设备，需要更多的并发。此问题的解决方案是 *SCB 分页*，这是一个类似于内存分页的概念。SCB 分页利用了设备通常长时间断开与 SCSI 总线的连接而不与控制器通信这一事实。断开连接事务的 SCB 仅在传输恢复时对控制器有用。当主机将另一个事务入队交由控制器执行时，控制器固件会使用空闲的 SCB（如果有的话）。否则，最近断开连接（因此最可能保持断开）的 SCB 的状态会通过 DMA 保存到主机内存，本地 SCB 被重用以启动新事务。这使控制器能够排队最多 255 个事务，而不受 SCB 空间大小限制。由于本地 SCB 空间作为断开连接事务的缓存，可用的 SCB 空间越大，保存和恢复 SCB 数据所消耗的主机总线流量就越少。

## 参见

[ahd(4)](ahd.4.md), [cd(4)](cd.4.md), [da(4)](da.4.md), [sa(4)](sa.4.md), [scsi(4)](scsi.4.md)

## 历史

`ahc` 驱动出现于 FreeBSD 2.0。

## 作者

`ahc` 驱动、AIC7xxx sequencer 代码汇编器以及运行在 aic7xxx 芯片上的固件由 Justin T. Gibbs 编写。

## 缺陷

某些 Quantum 驱动器（至少包括 Empire 2100 和 1080s）无法在 AIC7870 Rev B 上以 10MHz 同步模式运行。存在此问题的控制器上有 42 MHz 时钟晶振，运行略高于 10MHz。这会干扰驱动器并挂起总线。在 SCSI-Select 工具中将最大同步协商速率设置为 8MHz 可使其正常工作。

尽管 Ultra2 和 Ultra160 产品有足够的指令 RAM 空间同时支持发起方和目标角色，但此配置被禁用，以支持允许目标角色在多个目标 ID 上响应。应提供一种配置双角色模式的方法。

目标模式下不支持标记队列。

目标模式下的重选在 Adaptec 出厂的所有高压差分板上无法正常工作。有关如何修改 HVD 板以在目标模式下正常工作的信息，可从 Adaptec 获取。
