# smu.4

`smu` — Apple System Management Unit 驱动

## 名称

`smu`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device smu

## 描述

`smu` 驱动为许多 Apple G5 系统中的 System Management Unit (SMU) 提供支持。这包括大多数 Power Macintosh G5 和所有 iMac G5 系统。

Apple SMU 控制器提供软件电源管理和热控制功能，并负责管理系统冷却设备。

## 硬件

`smu` 驱动支持的芯片包括：

- Apple System Management Unit

## 热管理

`smu` 驱动提供基本的自动热管理。在没有用户空间守护进程提供更高级控制的情况下，驱动会通过粗粒度地控制系统冷却设备来尝试将系统温度维持在保守范围内（见下文）。如果用户空间冷却设置调整之间间隔超过 3 秒，内核级自动热控制将接管。

## SYSCTL 变量

`smu` 驱动通过 sysctl 接口提供电源管理服务和热读数。以下 sysctl 可用于控制电源管理行为以及检查当前系统电源和热状态。

**`dev.smu.%d.server_mode`** 断电后重启行为（1 表示系统在断电后重启，0 表示系统保持关闭）。

**`dev.smu.%d.target_temp`** 目标系统温度，以摄氏度为单位。`smu` 驱动会尝试调整风扇，将系统中最热组件的温度维持在此水平或以下。

**`dev.smu.%d.critical_temp`** 系统临界温度，以摄氏度为单位。如果系统中任何组件超过此温度，机器将在 500 ms 内关机。

**`dev.smu.%d.fans.%s.minrpm`** 此风扇允许的最低转速。

**`dev.smu.%d.fans.%s.maxrpm`** 此风扇允许的最高转速。

**`dev.smu.%d.fans.%s.rpm`** 此风扇的当前转速。可通过更改此 sysctl 来调整风扇转速。如果风扇转速调整之间间隔超过 3 秒，内核将恢复对风扇的自动控制。

**`dev.smu.%d.sensors.%s`** 此传感器的当前读数。支持四种传感器类型。温度传感器单位为摄氏度，电流传感器单位为毫安，电压传感器单位为毫伏，功率传感器单位为毫瓦。

## LED 接口

`smu` 驱动在 **/dev/led/sleepled** 处提供 [led(4)](led.4.md) 标示器接口。

## 参见

[acpi(4)](acpi.4.md), [led(4)](led.4.md), [pmu(4)](pmu.4.powerpc.md)

## 历史

`smu` 设备驱动首次出现于 FreeBSD 8.0。

## 作者

`smu` 驱动由 Nathan Whitehorn <nwhitehorn@FreeBSD.org> 编写。
