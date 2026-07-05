# apic.4

`apic` — 高级可编程中断控制器（APIC）驱动

## 名称

`apic`

## 概要

`此驱动是 amd64 内核的必选部分。要将此驱动编译进 i386 内核，请将以下行放入你的内核配置文件中：`

> device apic

`以下可调参数可从 loader(8) 设置：`

`控制事件定时器功能支持。设为 0 则禁用。默认值为 1。`

`将此设为 1 以禁用 APIC 支持，回退到传统 PIC。`

**hint.apic.X.clock**

**hint.apic.X.disabled**

## 描述

Intel APIC 系统有两个组件：本地 APIC（LAPIC）和 I/O APIC。系统中每个 CPU 都有一个本地 APIC。通常系统中的每个外设总线都有一个 I/O APIC。

本地 APIC 管理特定处理器的所有外部中断。此外，它们能够接受和产生处理器间中断（IPI）。

I/O APIC 包含一个重定向表，用于将其从外设总线接收到的中断路由到一个或多个本地 APIC。

每个本地 APIC 包括一个 32 位可编程定时器。此驱动使用它们为内核提供一个名为“LAPIC”的事件定时器。该驱动提供的事件定时器支持单次和周期两种模式。由于本地 APIC 的性质，它是每 CPU 的。定时器频率不由平台报告，因此由驱动在首次使用时自动测量。根据 CPU 型号，此定时器可能在 C3 及更深的 CPU 睡眠状态下停止。驱动会自动调整事件定时器优先级并报告它，以防止在使用时进入危险的睡眠状态。

## 参见

[atrtc(4)](atrtc.4.md), [attimer(4)](attimer.4.md), [eventtimers(4)](eventtimers.4.md), [hpet(4)](hpet.4.md)
