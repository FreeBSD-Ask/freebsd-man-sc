# timecounters(4)

`timecounters` — 内核时间计数器子系统

## 名称

`timecounters`

## 概要

`内核使用多种类型的时间相关设备，例如：实时时钟、时间计数器和事件定时器。实时时钟负责跟踪真实世界时间，主要在系统关闭时。时间计数器负责在系统运行时进行跟踪。事件定时器负责在指定时间或定期生成中断，以运行不同的基于时间的事件。本页是关于第二种的。`

## 描述

时间计数器是内核中时间跟踪的最低级别。它们提供具有已知宽度和更新频率的单调递增时间戳。它们可能溢出、漂移等，因此原始形式只能用于非常有限的性能关键位置，如进程调度器。

更有用的时间是通过对从所选时间计数器读取的值进行缩放并将其与某个偏移量组合而创建的，该偏移量在 Fn hardclock 调用时由 Fn tc_windup 定期更新。

不同平台提供不同类型的定时器硬件。时间计数器子系统的目标是提供统一的方式来访问该硬件。

实现时间计数器的每个驱动程序都将其注册到子系统。可以通过 `kern.timecounter` [sysctl(8)](../man8/sysctl.8.md) 变量查看存在的时间计数器列表：

```sh
kern.timecounter.choice: TSC-low(-100) HPET(950) i8254(0) ACPI-fast(900) dummy(-1000000)
kern.timecounter.tc.ACPI-fast.mask: 16777215
kern.timecounter.tc.ACPI-fast.counter: 13467909
kern.timecounter.tc.ACPI-fast.frequency: 3579545
kern.timecounter.tc.ACPI-fast.quality: 900
kern.timecounter.tc.i8254.mask: 65535
kern.timecounter.tc.i8254.counter: 62692
kern.timecounter.tc.i8254.frequency: 1193182
kern.timecounter.tc.i8254.quality: 0
kern.timecounter.tc.HPET.mask: 4294967295
kern.timecounter.tc.HPET.counter: 3013495652
kern.timecounter.tc.HPET.frequency: 14318180
kern.timecounter.tc.HPET.quality: 950
kern.timecounter.tc.TSC-low.mask: 4294967295
kern.timecounter.tc.TSC-low.counter: 4067509463
kern.timecounter.tc.TSC-low.frequency: 11458556
kern.timecounter.tc.TSC-low.quality: -100
```

输出节点定义如下：

**`kern.timecounter.tc.`** `X``.mask` 是位掩码，定义有效的计数器位，

**`kern.timecounter.tc.`** `X``.counter` 是当前计数器值，

**`kern.timecounter.tc.`** `X``.frequency` 是计数器更新频率，

**`kern.timecounter.tc.`** `X``.quality` 是整数值，定义此时间计数器与其他时间计数器相比的质量。负值表示此时间计数器已损坏，不应使用。

内核的时间管理代码在注册时会自动切换到更高质量的时间计数器，除非已使用 `kern.timecounter.hardware` sysctl 选择特定设备。

一旦时间计数器注册到内核，就无法注销。如果动态加载的模块包含时间计数器，则无法卸载该模块，即使它包含的时间计数器不是当前正在使用的。

## 参见

[attimer(4)](attimer.4.md), [eventtimers(4)](eventtimers.4.md), [ffclock(4)](ffclock.4.md), [hpet(4)](hpet.4.md)
