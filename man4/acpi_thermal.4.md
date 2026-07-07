# acpi_thermal(4)

`acpi_thermal` — ACPI 散热管理子系统

## 名称

`acpi_thermal`

## 概要

`device acpi`

## 描述

`acpi_thermal` 驱动提供 ACPI 模块的散热管理功能。此驱动具有 [sysctl(8)](../man8/sysctl.8.md) 接口和 devd(8) 通知接口。sysctl 导出每个 ACPI 散热区域对象的属性。

一个系统中可以有多个散热区域。例如，每个 CPU 和机箱都可以是独立的散热区域，各自有自己的设定点和冷却设备。散热区域按其在 AML 中出现的顺序依次编号。

`acpi_thermal` 驱动还会根据每个散热区域的设定点激活主动冷却系统。

## SYSCTL 变量

**`hw.acpi.thermal.min_runtime`** 一旦启动主动冷却后持续运行的秒数。在此间隔结束前不会选择新的主动冷却级别。

**`hw.acpi.thermal.polling_rate`** 两次轮询当前温度之间的秒数。

**`hw.acpi.thermal.user_override`** 若设为 1，允许用户覆盖以下各种设定点。这些设置的原始值从 BIOS 获取，更改可能导致系统过热并可能造成损坏。默认为 0（不覆盖）。

**`hw.acpi.thermal.tz%d.active`** 当前主动冷却系统状态。如果此值为非负，则相应的 _AC%d 对象正在运行。将此值设置为所需的主动冷却级别可强制将相应风扇对象置于相应级别。

**`hw.acpi.thermal.tz%d.passive_cooling`** 若设为 1，则启用被动冷却。它使用 [cpufreq(4)](cpufreq.4.md) 作为控制 CPU 速度的机制，无需风扇即可冷却。在 tz0 上默认启用（如果可用）。

**`hw.acpi.thermal.tz%d.thermal_flags`** 当前散热区域状态。这些是位掩码值。

**`hw.acpi.thermal.tz%d.temperature`** 此区域的当前温度。

**`hw.acpi.thermal.tz%d._PSV`** 通过降低 CPU 速度等方式开始被动冷却的温度。此值可由用户覆盖。

**`hw.acpi.thermal.tz%d._CR3`** 开始关键挂起到内存（S3）的温度。此值可由用户覆盖。

**`hw.acpi.thermal.tz%d._HOT`** 开始关键挂起到磁盘（S4）的温度。此值可由用户覆盖。

**`hw.acpi.thermal.tz%d._CRT`** 开始关键关机（S5）的温度。此值可由用户覆盖。

**`hw.acpi.thermal.tz%d._ACx`** 切换到相应主动冷却级别的温度。_ACx 值越低，冷却功率越高。

所有温度以摄氏度打印。值可以以摄氏度设置（通过附加 "C"）或开尔文设置（通过省略任何尾随字母）。通过 [sysctl(8)](../man8/sysctl.8.md) 设置值时，不要指定尾随小数（即使用 90C 而非 90.0C）。

## 通知

通知通过 devd(8) 传递到用户态。示例见 **`/etc/devd.conf`** 和 devd.conf(5)。`acpi_thermal` 驱动发送的事件具有以下属性：

**`0x80`** 当前温度已更改。
**`0x81`** 一个或多个触发点（_ACx、_PSV）已更改。
**`0x82`** 一个或多个设备列表（_ALx、_PSL、_TZD）已更改。
**`0xcc`** 非标准通知，表示如果温度在再经过一个轮询周期后仍高于_CRT 或 _HOT，系统将关机。

**system** `ACPI`
**subsystem** `Thermal`
**type** ASL 中完全限定的散热区域对象路径。
**notify** 表示事件的整数：

## 参见

[acpi(4)](acpi.4.md), [cpufreq(4)](cpufreq.4.md), acpidump(8)

## 作者

Michael Smith

本手册页由 Takanori Watanabe 编写。
