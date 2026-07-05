# hpet.4

`hpet` — 高精度事件定时器驱动

## 名称

`hpet`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device acpi

以下可调参数可从 loader(8) 设置：

**`hint.hpet.X.allowed_irqs`** 是一个 32 位掩码。每个置位的比特允许驱动使用相应的 IRQ，前提是 BIOS 也在比较器配置寄存器中设置了相应的能力位。默认值为 0xffff0000，某些已知存在缺陷的硬件除外。

**`hint.hpet.X.clock`** 控制事件定时器功能支持。设置为 0 将禁用该功能。默认值为 1。

**`hint.hpet.X.legacy_route`** 控制“LegacyReplacement Route”模式。如果启用，HPET 将占用 i8254 定时器的 IRQ0 和 RTC 的 IRQ8。在使用前，请确保相应驱动未使用中断，方法是同时设置：

```sh
hint.attimer.0.clock=0
hint.atrtc.0.clock=0
```

默认值为 0。

**`hint.hpet.X.per_cpu`** 控制驱动应尝试注册多少个 per-CPU 事件定时器。此功能要求组内每个比较器都有自己不共享的 IRQ，因此取决于硬件能力和中断配置。默认值为 1。

## 描述

此驱动使用高精度事件定时器硬件（芯片组的一部分，通常通过 ACPI 枚举）为内核提供一个时间计数器和若干个（通常为 3 到 8 个）事件定时器。此硬件包括单个具有已知递增频率（10MHz 或更高）的主计数器，以及若干个可编程比较器（可选具备自动重载功能）。当主计数器的值与任一比较器的当前值匹配时，可产生中断。根据硬件能力和配置，中断可作为常规 I/O APIC 中断（ISA 或 PCI，范围从 0 到 31）交付，或作为前端总线中断（类似于 PCI MSI 中断）交付，或在所谓的“LegacyReplacement Route”中由 HPET 占用 i8254 的 IRQ0 和 RTC 的 IRQ8。中断可以是边沿触发或电平触发。在后一种情况下，它们可与 PCI IRQ 安全共享。驱动优先使用 FSB 中断（如果支持）以避免共享。如果不可能，则使用 PCI 范围内的单个可共享 IRQ。其他模式（LegacyReplacement 和 ISA IRQ）需要特别注意来设置，但可通过 device hints 手动配置。

驱动提供的事件定时器同时支持单次和周期模式，且与 CPU 电源状态无关。

根据硬件能力和配置，驱动可将每个比较器作为单独的事件定时器公开，或将它们分组为一个或多个 per-CPU 事件定时器。在后一种情况下，组内每个比较器的中断绑定到特定的 CPU 核心。这仅在组内每个比较器都有自己不可共享的 IRQ 时才可能实现。

## 参见

[acpi(4)](acpi.4.md), [apic(4)](apic.4.md), [atrtc(4)](atrtc.4.md), [attimer(4)](attimer.4.md), [eventtimers(4)](eventtimers.4.md), [timecounters(4)](timecounters.4.md)

## 历史

`hpet` 驱动首次出现于 FreeBSD 6.3。事件定时器支持于 FreeBSD 9.0 中添加。
