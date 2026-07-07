# sym(4)

`sym` — NCR/Symbios/LSI Logic 53C8XX PCI SCSI 主机适配器驱动

## 名称

`sym`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device pci
> device scbus
> device sym

`要禁用 PCI 奇偶校验（用于有缺陷的桥）：options SYM_SETUP_PCI_PARITY=<boolean>`

`要控制驱动对 HVD 总线的探测：options SYM_SETUP_SCSI_DIFF=<bit combination>`

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
sym_load="YES"
```

## 描述

此驱动为 Symbios/LSI Logic 53C8XX PCI SCSI 控制器提供支持。

驱动特性包括根据控制器能力支持宽 SCSI 总线以及 fast10、fast20、fast40 和 fast80-dt 同步数据传输。它还提供诸如标记命令队列和自动请求 sense 等通用 SCSI 特性。此驱动默认配置为每总线最多 446 个未完成命令、每个目标 8 个 LUN、每个 LUN 64 个标记任务。这些数字与其说是设计上的限制，不如说是当前 SCSI 技术的合理值。可通过更改驱动头文件中的相应常量来增加这些值（不推荐）。

此驱动支持整个 Symbios 53C8XX 系列 PCI SCSI 控制器。它还提供了仅较新芯片才有的架构改进优势。

`sym` 特别处理 53C896、53C895A 和 53C1010 核心的 SCRIPTS 中的相位失配。因此，它保证每次 IO 完成向 CPU 传递的中断不超过 1 次，并且在正常情况下 SCRIPTS 处理器永远不会因等待 CPU 关注而停顿。

`sym` 还对支持它的芯片使用 LOAD/STORE SCRIPTS 指令。只有早期 810、815 和 825 NCR 芯片不支持 LOAD/STORE。使用 LOAD/STORE 代替 MEMORY MOVE 允许 SCRIPTS 访问芯片内部的 IO 寄存器（无外部 PCI 周期）。因此，驱动保证对于支持 LOAD/STORE 的芯片不会发生 PCI 自主主控。

LOAD/STORE 指令也比 MEMORY MOVE 更快，因为它们不涉及芯片 DMA FIFO，且编码为 2 个 DWORD 而非 3 个。

对于早期 NCR 810、815 和 825 芯片，驱动使用单独的 SCRIPTS 集，该集使用 MEMORY MOVE 指令进行数据移动。这是因为这些芯片不支持 LOAD/STORE。

支持 HVD/LVD 的控制器（895、895A、896 和 897）在 STEST4 芯片 IO 寄存器中报告实际总线模式。此特性允许驱动安全地探测总线模式并相应地设置芯片。默认情况下，驱动仅对这些芯片支持 HVD。对于其他可支持 HVD 但不支持 LVD 的芯片，驱动必须探测实现相关寄存器（GPIO）以检测 HVD 总线模式。驱动只能检测符合 Symbios Logic 建议的 HVD 实现。当 `SYM_SETUP_SCSI_DIFF` 内核选项赋值为 1 时，驱动还将对 825a、875、876 和 885 芯片探测 HVD，假定 HVD 实现与 Symbios Logic 兼容。

当 `SYM_SETUP_PCI_PARITY` 赋值为 0 时，驱动将不为 53C8XX 设备启用 PCI 奇偶校验。对于 PCI SCSI 控制器而言，PCI 奇偶校验不应是可选的，但据报告，由于检测到虚假或永久性 PCI 奇偶校验错误，某些系统在使用 53C8XX 芯片时会失败。提供此选项是为了方便，但既不推荐也不受支持。

此驱动提供当前未导出给用户的其他选项。它们在 `sym_conf.h` 驱动文件中定义和记录。除非绝对必要，否则不建议更改这些选项。某些选项计划在未来的驱动版本中通过 sysctl(3) 或等效机制导出，因此不保证兼容性。

初始化时，驱动尝试检测和读取控制器 NVRAM 中的用户设置。目前支持 Symbios/Logic NVRAM 布局和 Tekram NVRAM 布局。如果成功读取 NVRAM，以下设置将被纳入并报告给 CAM：

| *Host settings | Symbios | Tekram* |
| --- |
| SCSI parity checking | Y | N |
| Host SCSI ident | Y | Y |
| Verbose messages | Y | N |
| Scan targets hi-lo | Y | N |
| Avoid SCSI bus reset | Y | N |

| *Device settings | Symbios | Tekram* |
| --- |
| Synchronous period | Y | Y |
| SCSI bus width | Y | Y |
| Queue tag enable | Y | Y |
| Number of tags | NA | Y |
| Disconnect enable | Y | Y |
| Scan at boot time | Y | N |
| Scan LUN | Y | N |

在 NVRAM 中被配置为禁用“扫描”的设备不会在系统启动时报告给 CAM。可稍后使用 `camcontrol rescan` 命令发现它们。

下表总结了 NCR/Symbios/LSI Logic 53C8XX 系列 PCI SCSI 控制器的主要特性和能力。

| *Chip | Sync | Width | SRAM | PCI64 | Supported* |
| --- |
| sym53c810 | 10MHz | 8Bit | N | N | Y |
| sym53c810a | 10MHz | 8Bit | N | N | Y |
| sym53c815 | 10MHz | 8Bit | N | N | Y |
| sym53c825 | 10MHz | 16Bit | N | N | Y |
| sym53c825a | 10MHz | 16Bit | 4KB | N | Y |
| sym53c860 | 20MHz | 8Bit | N | N | Y |
| sym53c875 | 20MHz | 16Bit | 4KB | N | Y |
| sym53c876 | 20MHz | 16Bit | 4KB | N | Y |
| sym53c885 | 20MHz | 16Bit | 4KB | N | Y |
| sym53c895 | 40MHz | 16Bit | 4KB | N | Y |
| sym53c895A | 40MHz | 16Bit | 8KB | N | Y |
| sym53c896 | 40MHz | 16Bit | 8KB | Y | Y |
| sym53c897 | 40MHz | 16Bit | 8KB | Y | Y |
| sym53c1510D | 40MHz | 16Bit | 4KB | Y | Y |
| sym53c1010 | 80MHz | 16Bit | 8KB | Y | Y |

## 硬件

`sym` 驱动为以下 Symbios/LSI Logic PCI SCSI 控制器提供支持：

- 53C810
- 53C810A
- 53C815
- 53C825
- 53C825A
- 53C860
- 53C875
- 53C876
- 53C895
- 53C895A
- 53C896
- 53C897
- 53C1000
- 53C1000R
- 53C1010-33
- 53C1010-66
- 53C1510D

`sym` 支持的 SCSI 控制器可以是主板内置的，也可以是以下附加板卡之一：

- ASUS SC-200, SC-896
- Data Technology DTC3130（所有变体）
- DawiControl DC2976UW
- Diamond FirePort（全部）
- NCR 卡（全部）
- Symbios 卡（全部）
- Tekram DC390W, 390U, 390F, 390U2B, 390U2W, 390U3D 和 390U3W
- Tyan S1365

## 杂项

DEC KZPCA-AA 是重新标识的 SYM8952U。

## 参见

[cd(4)](cd.4.md), [da(4)](da.4.md), [sa(4)](sa.4.md), [scsi(4)](scsi.4.md), [camcontrol(8)](../man8/camcontrol.8.md)

## 历史

`sym` 驱动出现于 FreeBSD 4.0。

## 作者

`sym` 驱动由 Gerard Roudier 编写，源自同一作者的 Linux sym53c8xx 驱动。sym53c8xx 驱动源自 ncr53c8xx 驱动，后者从 FreeBSD ncr(4) 驱动移植到 Linux-1.2.13。原始 ncr(4) 驱动由 Wolfgang Stanglmeier 和 Stefan Esser 为 386BSD 和 FreeBSD 编写。

## 缺陷

无已知缺陷。
