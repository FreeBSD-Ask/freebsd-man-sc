# ntb_hw_intel(4)

`ntb_hw_intel` — Intel(R) 非透明桥接驱动

## 名称

`ntb_hw_intel`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device ntb
> device ntb_hw_intel

`或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
ntb_hw_intel_load="YES"
```

## 描述

`ntb_hw_intel` 驱动为 Intel Xeon E3/E5 和 S1200 处理器系列中的非透明桥接（NTB）硬件提供支持，这些处理器允许将其某个 PCIe 端口从透明桥接模式切换到非透明桥接模式。在此模式下，桥接看起来不像 PCI 桥，而像 PCI 端点设备。该驱动隐藏硬件细节，通过硬件无关的 KPI 向 [ntb(4)](ntb.4.md) 子系统暴露另一端的内存窗口、scratchpad 和 doorbell。

硬件提供 2 或 3 个内存窗口访问另一系统的内存，16 个 scratchpad 寄存器，以及 14、31 或 34 个 doorbell 用于中断另一系统，具体取决于平台。在 Xeon 处理器上，其中一个内存窗口通常被驱动自身消耗，用于规避多个硬件勘误问题。

## 配置

NTB 配置应由 BIOS 设置。这包括启用 NTB、在 NTB-to-NTB（背靠背）或 NTB-to-Root Port 模式之间选择、启用 split BAR 模式（两个 64 位 BAR 之一可拆分为两个 32 位 BAR）以及为两个 NTB 端以位为单位配置 BAR 大小（从 12 到 29/39）。

推荐的配置为 NTB-to-NTB 模式、启用 split bar 并将所有 BAR 大小设置为 20（1 MiB）。这需要在两个系统上都进行设置。注意，在 Xeon SkyLake 及更新平台上，split bar 模式不可用。

## 参见

[if_ntb(4)](if_ntb.4.md), [ntb(4)](ntb.4.md), [ntb_transport(4)](ntb_transport.4.md)

## 作者

`ntb_hw_intel` 驱动由 Intel 开发，最初由 Carl Delsey <carl@FreeBSD.org> 编写。后续改进由 Conrad E. Meyer <cem@FreeBSD.org> 和 Alexander Motin <mav@FreeBSD.org> 完成。

## 缺陷

NTB-to-Root Port 模式尚不支持，但看起来不太有用。

在 Xeon v2/v3/v4 处理器上，应启用 split BAR 模式以允许驱动应用 SB01BASE_LOCKUP 勘误规避。

一旦链路建立，就无法保护你的系统免受另一系统的恶意行为。在另一系统上拥有 root 或内核访问权限的任何人都可读取或写入你系统上的任何位置。换言之，仅连接彼此完全信任的两个系统。
