# ntb_hw_plx(4)

`ntb_hw_plx` — PLX/Avago/Broadcom 非透明桥接驱动

## 名称

`ntb_hw_plx`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device ntb
> device ntb_hw_plx

`或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
ntb_hw_plx_load="YES"
```

`以下可调参数可在 loader(8) 中设置：`

`设置为 1（默认）时，告诉附接到 NTB 虚拟接口（Virtual Interface）的驱动以 NTB-to-NTB（背靠背）模式工作，设置为 0 时为 NTB-to-Root Port 模式。附接到链路接口（Link Interface，从 Root Port 侧可见）的驱动会自动切换到 NTB-to-Root Port 模式，但附接到虚拟接口的驱动无法检测另一侧是什么，需要外部知识。`

`设置为大于零的值时，使用地址查找表（A-LUT）将 BAR2 拆分为 2^x 个内存窗口。`

**hint.ntb_hw.X.b2b**

**hint.ntb_hw.X.split**

## 描述

`ntb_hw_plx` 驱动为 PLX PCIe 桥接芯片中的非透明桥接（NTB）硬件提供支持，这些芯片允许将其最多两个 PCIe 端口从透明桥接模式切换到非透明桥接模式。在此模式下，桥接看起来不像 PCI 桥，而像 PCI 端点设备。该驱动隐藏硬件细节，通过硬件无关的 KPI 向 [ntb(4)](ntb.4.md) 子系统暴露另一端的内存窗口、scratchpad 和 doorbell。

每个 PLX NTB 提供最多 2 个 64 位或 4 个 32 位内存窗口访问另一系统的内存，6 或 12 个 scratchpad 寄存器以及 16 个 doorbell 用于中断另一系统。如果启用地址查找表（A-LUT），BAR2 可拆分为多个（最多 128 个）内存窗口。在 NTB-to-NTB 模式下，其中一个内存窗口（如果大于 1MB 则为其一半）由驱动自身消耗，用于访问另一端的 scratchpad 和 doorbell 寄存器。

## 硬件

`ntb_hw_plx` 驱动支持以下 PLX/Avago/Broadcom 芯片：

- PEX 8713
- PEX 8717
- PEX 8725
- PEX 8733
- PEX 8749

，但也可能与其他兼容芯片一起工作。

## 配置

基本的芯片配置应由串行 EEPROM 或通过 i2c 完成。这包括在一个或两端启用 NTB（在 NTB-to-NTB（背靠背）和 NTB-to-Root Port 模式之间选择）以及配置 BAR 大小。

推荐的模式为 NTB-to-NTB 模式，因为虽然 NTB-to-Root Port 通常被驱动支持，但它需要在 Root Port 上进行 PCI 热插拔处理，这可能比较困难或导致各种问题。

## 参见

[if_ntb(4)](if_ntb.4.md), [ntb(4)](ntb.4.md), [ntb_transport(4)](ntb_transport.4.md)

## 作者

`ntb_hw_plx` 驱动由 Alexander Motin <mav@FreeBSD.org> 编写。

## 缺陷

一旦链路建立，就无法保护你的系统免受另一系统的恶意行为。在另一系统上拥有 root 或内核访问权限的任何人都可读取或写入你系统上的任何位置。换言之，仅连接彼此完全信任的两个系统。
