# eventtimers(4)

`eventtimers` — 内核事件定时器子系统

## 名称

`eventtimers`

## 概要

`内核使用多种与时间相关的设备，例如：实时时钟、时间计数器和事件定时器。实时时钟负责跟踪真实世界时间，主要在系统关机时使用。时间计数器负责在系统运行时生成单调递增的时间戳，用于精确跟踪系统运行时间。事件定时器负责在指定时间或周期性地生成中断，以运行各种基于时间的事件。本页介绍最后一种。`

## 描述

内核基于 [callout(9)](../man9/callout.9.md) 机制将基于时间的事件用于多种用途：调度、统计、计时、性能分析等等。这些用途现在被归为三个主要回调：

**Fn** hardclock [callout(9)](../man9/callout.9.md) 和计时事件的入口。以 `hz` 变量定义的频率调用，通常为 1000Hz。

**Fn** statclock 统计和调度器事件的入口。以约 128Hz 的频率调用。

**Fn** profclock 性能分析器事件的入口。启用时以约 8KHz 的频率调用。

不同平台提供不同类型的定时器硬件。事件定时器子系统的目标是提供统一的方式来控制这些硬件，并使用它为内核提供所有必需的基于时间的事件。

每个实现事件定时器的驱动程序都会在子系统中注册它们。可以通过 `kern.eventtimer` sysctl 查看现有事件定时器的列表，如下所示：

```sh
kern.eventtimer.choice: HPET(550) LAPIC(400) i8254(100) RTC(0)
kern.eventtimer.et.LAPIC.flags: 15
kern.eventtimer.et.LAPIC.frequency: 0
kern.eventtimer.et.LAPIC.quality: 400
kern.eventtimer.et.i8254.flags: 1
kern.eventtimer.et.i8254.frequency: 1193182
kern.eventtimer.et.i8254.quality: 100
kern.eventtimer.et.RTC.flags: 17
kern.eventtimer.et.RTC.frequency: 32768
kern.eventtimer.et.RTC.quality: 0
kern.eventtimer.et.HPET.flags: 7
kern.eventtimer.et.HPET.frequency: 14318180
kern.eventtimer.et.HPET.quality: 550
```

其中：

**1** 支持周期模式，
**2** 支持单次模式，
**4** 定时器为每 CPU，
**8** CPU 进入睡眠状态时定时器可能停止，
**16** 定时器仅支持 2 的幂次除数。

**`kern.eventtimer.et.`** `X``.flags` 是定义事件定时器能力的位掩码：

**`kern.eventtimer.et.`** `X``.frequency` 是定时器的基础频率，

**`kern.eventtimer.et.`** `X``.quality` 是整数值，定义此定时器与其他定时器相比的优劣程度。

内核的定时器管理代码从该列表中选择一个定时器。当前选择可通过 `kern.eventtimer.timer` 可调参数/sysctl 读取和影响。还有其他几个可调参数/sysctl 影响此定时器的确切使用方式：

**`kern.eventtimer.periodic`** 允许选择周期模式和单次操作模式。在周期模式下，来自定时器硬件的周期性中断被作为时间事件的唯一时间源。单次模式则使用当前选定的时间计数器来精确调度所有需要的事件，并安排事件定时器在指定时间精确生成中断。默认值取决于所选定时器的能力，但首选单次模式，除非用户或硬件强制其他模式。

**`kern.eventtimer.singlemul`** 在周期模式下指定定时器频率应高多少倍，以避免 Fn hardclock 和 Fn statclock 事件的严格混叠。默认值为 1、2 或 4，取决于配置的 HZ 值。

**`kern.eventtimer.idletick`** 使每个 CPU 无论是否繁忙都接收每个定时器中断。默认禁用此选项。如果所选定时器为每 CPU 且运行于周期模式，此选项无效——所有中断始终生成。

## 参见

[apic(4)](apic.4.md), [atrtc(4)](atrtc.4.md), [attimer(4)](attimer.4.md), [hpet(4)](hpet.4.md), [timecounters(4)](timecounters.4.md), [eventtimers(9)](../man9/eventtimers.9.md)
