# pmu.4.powerpc

`pmu` — Apple PMU99 电源管理驱动

## 名称

`pmu`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device adb
> device pmu

## 描述

`pmu` 驱动为 Apple Core99 硬件中的电源管理单元（PMU）提供支持。这包括晚期 G3 笔记本、所有 G4 机器、早期 G5 台式机和所有 G5 XServe。

Apple PMU 控制器是一款多用途 ASIC，提供电源管理和热控制，以及用于笔记本内置键盘和鼠标的 ADB 总线。

## 硬件

`pmu` 驱动支持的芯片包括：

- Apple KeyLargo PMU
- Apple K2-KeyLargo PMU

## SYSCTL 变量

`pmu` 驱动除提供 [adb(4)](adb.4.powerpc.md) 接口外，还提供电源管理服务。以下 sysctl 可用于控制电源管理行为以及检查当前系统电源和散热状况。

**`dev.pmu.%d.server_mode`** 断电后重启行为（1 表示系统在断电后重启，0 表示系统保持关闭）。

**`dev.pmu.%d.batteries.%d.present`** 指示相关电池是否已插入。

**`dev.pmu.%d.batteries.%d.charging`** 指示电池当前是否正在充电。

**`dev.pmu.%d.batteries.%d.charge`** 当前电池电量，以毫安时为单位。

**`dev.pmu.%d.batteries.%d.maxcharge`** 电池自报的最大电量，以毫安时为单位。

**`dev.pmu.%d.batteries.%d.rate`** 流入电池的电流，以毫安为单位。电池放电时，此值为负。

**`dev.pmu.%d.batteries.%d.voltage`** 电池电压，以毫伏为单位。

**`dev.pmu.%d.batteries.%d.time`** 电池充满（或放完）的估计时间，以分钟为单位。

**`dev.pmu.%d.batteries.%d.life`** 电池当前电量占最大电量的比例，以百分比表示。

## 参见

[acpi(4)](acpi.4.md), [adb(4)](adb.4.powerpc.md), [led(4)](led.4.md)

## 历史

`pmu` 设备驱动出现于 NetBSD 4.0，然后是 FreeBSD 8.0。

## 作者

`pmu` 驱动由 Michael Lorenz <macallan@NetBSD.org> 编写，由 Nathan Whitehorn <nwhitehorn@FreeBSD.org> 移植到 FreeBSD。
