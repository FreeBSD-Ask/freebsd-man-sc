# est.4

`est` — 增强型 SpeedStep 技术

## 名称

`est`

## 概要

`若要将此功能编译进内核，请在内核配置文件中加入以下行：`

> device cpufreq

## 描述

`est` 接口为 Intel 增强型 SpeedStep 技术提供支持。

注意，`est` 功能由 [cpufreq(4)](cpufreq.4.md) 驱动自动加载。

## 加载器可调参数

`est` 接口旨在允许 [cpufreq(4)](cpufreq.4.md) 通过 [acpi(4)](acpi.4.md) 和 acpi_perf 接口访问器访问并实现 Intel 增强型 SpeedStep 技术。如果默认设置并非最优，可使用以下 sysctl 修改或监视 `est` 行为。

**hw.est.msr_info** 尝试从直接探测 msr 推断信息。仅应在诊断情况下使用。（默认 0）

**hw.est.strict** 设置时验证请求的频率是否被 CPU 接受。似乎这只在单核 CPU 上有效。（默认 0）

## SYSCTL 变量

以下 [sysctl(8)](../man8/sysctl.8.md) 值可用

**`dev.est.%d.%desc`** 支持的描述，几乎总是 Enhanced SpeedStep Frequency Control。

**dev.est.0.%desc:** Enhanced SpeedStep Frequency Control

**`dev.est.%d.%driver`** 使用中的驱动，始终为 est。

**dev.est.0.%driver:** est

**`dev.est.%d.%parent`** 暴露这些频率的 CPU。例如 `cpu0`。

**dev.est.0.%parent:** cpu0

**`dev.est.%d.freq_settings`** 。此 CPU 允许的有效频率及其步长值。

**dev.est.0.freq_settings:** 2201/45000 2200/45000 2000/39581 1900/37387 1800/34806 1700/32703 1600/30227 1500/28212 1400/25828 1300/23900 1200/21613 1100/19775 1000/17582 900/15437 800/13723

## 诊断

- est%d: <Enhanced SpeedStep Frequency Control> on cpu%d 指示此接口正常启动。
- est: CPU supports Enhanced Speedstep, but is not recognized.
- est: cpu_vendor GenuineIntel, msr 471c471c0600471c
- device_attach: est%d attach returned 6 指示所有挂载此接口的尝试均失败。通常表明 BIOS 设置不当，限制了操作系统对 CPU 速度的控制。详情请参阅 BIOS 文档。

## 兼容性

`est` 仅在受支持的 Intel CPU 上找到。

## 参见

[cpufreq(4)](cpufreq.4.md)

> "Intel 64 and IA-32 Architectures Software Developer Manuals".

## 作者

本手册页由 Sean Bruno <sbruno@FreeBSD.org> 编写。
