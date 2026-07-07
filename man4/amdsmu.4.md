# amdsmu(4)

`amdsmu` — AMD 系统管理单元设备驱动

## 名称

`amdsmu`

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device amdsmu

或者，要在引导时以模块形式加载该驱动，请在 rc.conf(5) 中加入以下行：

```sh
kld_list="amdsmu"
```

## 描述

`amdsmu` 驱动为某些 AMD 移动处理器中的系统管理单元（SMU）提供支持。SMU 是一个固件组件，负责管理系统电源状态，特别是协调进入和退出 S0ix 挂起到空闲睡眠状态。

该驱动通过基于寄存器的邮箱接口与 SMU 通信，以查询固件版本信息、检索电源管理指标，并在系统进入或离开睡眠时向 SMU 发出提示。该驱动注册 ACPI 挂起和恢复事件处理程序，以向 SMU 发送睡眠提示，并在每个睡眠周期后刷新指标。

支持以下 AMD 处理器：

- Cezanne
- Rembrandt
- Phoenix
- Krackan Point

## SYSCTL 变量

该驱动通过 `dev.amdsmu.%d` 树下的以下 [sysctl(8)](../man8/sysctl.8.md) 变量公开信息。

### 固件版本

**`dev.amdsmu.%d.program`** SMU 程序编号。

**`dev.amdsmu.%d.version_major`** SMU 固件主版本号。

**`dev.amdsmu.%d.version_minor`** SMU 固件次版本号。

**`dev.amdsmu.%d.version_revision`** SMU 固件修订号。

### 电源管理指标

以下变量位于 `dev.amdsmu.%d.metrics` 下，反映最近一次睡眠周期的测量值。时间值以微秒为单位。

**`dev.amdsmu.%d.metrics.table_version`** 固件报告的 SMU 指标表版本。

**`dev.amdsmu.%d.metrics.hint_count`** 睡眠提示已发送给 SMU 的次数。每次系统进入挂起到空闲时递增。

**`dev.amdsmu.%d.metrics.s0i3_last_entry_status`** 如果上一次 S0i3 进入成功则设为 1，否则为 0。可用于诊断失败的 S0i3 转换。

**`dev.amdsmu.%d.metrics.time_last_in_s0i2`** 上一次睡眠周期中在 S0i2 中度过的时间。大多数情况下与此无关。

**`dev.amdsmu.%d.metrics.time_last_entering_s0i3`** 上一次睡眠周期中进入 S0i3 所花费的时间。

**`dev.amdsmu.%d.metrics.total_time_entering_s0i3`** 所有睡眠周期中进入 S0i3 所花费的累计总时间。

**`dev.amdsmu.%d.metrics.time_last_resuming`** 从上一次睡眠周期恢复所花费的时间。

**`dev.amdsmu.%d.metrics.total_time_resuming`** 从睡眠恢复所花费的累计总时间。

**`dev.amdsmu.%d.metrics.time_last_in_s0i3`** 上一次睡眠周期中在 S0i3 中度过的时间。

**`dev.amdsmu.%d.metrics.total_time_in_s0i3`** 所有睡眠周期中在 S0i3 中度过的累计总时间。

**`dev.amdsmu.%d.metrics.time_last_in_sw_drips`** 上一次睡眠周期中系统处于清醒状态（即不在 S0i3）的时间。“SW DRIPS”一词略有不当。

**`dev.amdsmu.%d.metrics.total_time_in_sw_drips`** 睡眠周期中系统处于清醒状态的累计总时间。

### IP 模块

SMU 跟踪的每个硬件 IP 模块在 `dev.amdsmu.%d.ip_blocks.<name>` 下公开，其中 **<name>** 为 **DISPLAY、** **CPU、** **GFX、** **VDD、** **ACP、** **VCN、** **ISP、** **NBIO、** **DF、** **LAPIC、** **USB3_0** 到 **USB3_4、** **USB4_0、** **USB4_1、** **MPM、** **JPEG、** **IPU、** **UMSCH、** 或 **VPE** 之一（可用性取决于处理器型号）。每个 IP 块节点包含以下变量：

**`dev.amdsmu.%d.ip_blocks.<name>.active`** 布尔值，指示此 IP 块是否处于活动状态，即是否可能限制 S0i3 进入。

**`dev.amdsmu.%d.ip_blocks.<name>.last_time`** 上一次睡眠周期中此 IP 块处于活动状态（从而阻止 S0i3 进入）的时间（以微秒为单位）。如果此值等于 `dev.amdsmu.%d.metrics.time_last_in_sw_drips` 的值，则在上一个周期中此 IP 块阻止了进入 S0i3。

### 空闲掩码

**`dev.amdsmu.%d.idlemask`** 从 SMU 读取的原始空闲掩码值。这是一个未文档化的寄存器，旨在协助 AMD 调试电源管理问题。其解释是硬件特定的，不由任何公开规范定义。

## 参见

[acpi(4)](acpi.4.md), [amdsmn(4)](amdsmn.4.md), [amdtemp(4)](amdtemp.4.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`amdsmu` 驱动首次出现于 FreeBSD 15.0。

## 作者

Aymeric Wibo <obiwac@FreeBSD.org>

开发由 FreeBSD 基金会赞助。

## 缺陷

`dev.amdsmu.%d.ip_blocks.USB4_0.last_time` 值通常包含垃圾数据，不应依赖此值。

阻止 S0i3 进入的 USB4 似乎由 `USB3_0` 到 `USB3_4` IP 块指标报告，而非通过专用的 USB4 块报告。
