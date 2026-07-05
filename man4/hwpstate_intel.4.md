# hwpstate_intel.4

`hwpstate_intel` — Intel Speed Shift Technology 驱动

## 名称

`hwpstate_intel`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device cpufreq

## 描述

`hwpstate_intel` 驱动为 Intel 平台上硬件控制的性能状态提供支持，也称为 Intel Speed Shift Technology。

## 加载器可调参数

**`hint.hwpstate_intel.0.disabled`** 可用于禁用 `hwpstate_intel`，允许其他兼容驱动管理性能状态，如 [est(4)](est.4.md)。默认为 "0"（启用）。

**`machdep.hwpstate_pkg_ctrl`** 在包级控制（默认）和每核控制之间选择。"1" 选择包级控制，"0" 选择核级控制。

## SYSCTL 变量

以下 [sysctl(8)](../man8/sysctl.8.md) 值可用

**`dev.hwpstate_intel.%d.%desc`** 描述已附加的驱动

**dev.hwpstate_intel.0.%desc:** Intel Speed Shift

**`dev.hwpstate_intel.%d.%driver`** 使用中的驱动，始终为 hwpstate_intel。

**dev.hwpstate_intel.0.%driver:** hwpstate_intel

**`dev.hwpstate_intel.%d.%parent`** 暴露这些频率的 CPU。例如 `cpu0`。

**dev.hwpstate_intel.0.%parent:** cpu0

**`dev.hwpstate_intel.%d.epp`** 能源/性能偏好。有效值范围为 0 到 255。设置此字段向硬件传达偏好提示，0 表示偏向性能，255 表示偏向能效，或介于两者之间。

**dev.hwpstate_intel.0.epp:** 0

## 兼容性

`hwpstate_intel` 仅在受支持的 Intel CPU 上存在。

## 参见

[cpufreq(4)](cpufreq.4.md)

> "Intel 64 and IA-32 Architectures Software Developer Manuals".

## 作者

本手册页由 D Scott Phillips <scottph@FreeBSD.org> 编写。
