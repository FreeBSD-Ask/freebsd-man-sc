# cpufreq.4

`cpufreq` — CPU 频率控制框架

## 名称

`cpufreq`

## 概要

`device cpufreq`

`#include <sys/cpu.h>`

`Ft int Fn cpufreq_levels device_t dev struct cf_level *levels int *count Ft int Fn cpufreq_set device_t dev const struct cf_level *level int priority Ft int Fn cpufreq_get device_t dev struct cf_level *level Ft int Fo cpufreq_drv_settings device_t dev struct cf_setting *sets int *count Fc Ft int Fn cpufreq_drv_type device_t dev int *type Ft int Fn cpufreq_drv_set device_t dev const struct cf_setting *set Ft int Fn cpufreq_drv_get device_t dev struct cf_setting *set`

## 描述

`cpufreq` 驱动为 CPU 频率控制驱动提供统一的内核与用户接口。它将提供不同设置的多个驱动组合为涵盖所有可能级别的单一接口。用户可通过 [sysctl(8)](../man8/sysctl.8.md) 直接访问此接口，或通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中指示 **/etc/rc.d/power_profile** 在交流电源状态变化时切换设置。

## sysctl 变量

这些设置可能被请求替代设置的内核驱动所覆盖。如果发生这种情况，一旦该条件消除（例如系统已充分冷却），原始值将被恢复。如果由于覆盖条件导致某个 sysctl 无法设置，它将返回 Er EPERM。

如果 TSC 正作为时间计数器使用且硬件不支持不变 TSC（invariant TSC），则无法更改频率。这是因为时间计数器系统需要使用具有恒定速率的源。（在支持不变 TSC 的硬件上，无论配置的 P 状态如何，TSC 都以 P0 速率运行。）现代硬件大多具有不变 TSC。可使用 `kern.timecounter.hardware` sysctl 更改时间计数器源。可用模式位于 `kern.timecounter.choice` sysctl 条目中。

**`dev.cpu.%d.freq`** 当前活动的 CPU 频率，单位为 MHz。

**`dev.cpu.%d.freq_driver`** 此 CPU 使用的特定 `cpufreq` 驱动。

**`dev.cpu.%d.freq_levels`** CPU 当前可用的级别（频率/功耗）。值以 MHz 和毫瓦为单位。

**`dev.DEVICE.%d.freq_settings`** 驱动当前可用的设置（频率/功耗）。值以 MHz 和毫瓦为单位。这有助于理解哪些设置由哪个驱动提供，便于调试。

**`debug.cpufreq.lowest`** 向用户提供的最低 CPU 频率，单位为 MHz。此设置也可通过同名可调参数访问。可用于禁用在某些系统上可能不可用的极低级别。

**`debug.cpufreq.verbose`** 打印详细消息。此设置也可通过同名可调参数访问。

**`debug.hwpstate_pstate_limit`** 若启用，AMD hwpstate 驱动会将 P 状态的管理控制（包括由 [powerd(8)](../man8/powerd.8.md) 进行的控制）限制为 0xc0010061 MSR 中的值，即"PStateCurLim[CurPstateLimit]"。默认禁用（0）。在某些硬件上，该限制寄存器似乎只是跟随已配置的 P 状态，导致永远无法将 P 状态从降频状态提升回 P0。

## 支持的驱动

以下设备驱动通过 `cpufreq` 接口提供绝对频率控制。通常同一时间只能有一个处于活动状态。

**acpi_perf** ACPI CPU 性能状态
**[est(4)](est.4.md)** Intel Enhanced SpeedStep
**hwpstate** 用于 K10 至 Family 17h 的 AMD Cool'n'Quiet2
**[hwpstate_intel(4)](hwpstate_intel.4.md)** Intel SpeedShift 驱动
**ichss** 用于 ICH 的 Intel SpeedStep
**powernow** 用于 K7 和 K8 的 AMD PowerNow! 和 Cool'n'Quiet
**smist** 用于 PIIX4 的基于 Intel SMI 的 SpeedStep

以下设备驱动提供相对频率控制，具有叠加效果：

**acpi_throttle** ACPI CPU 节流
**p4tcc** Pentium 4 温度控制电路

## 内核接口

内核组件可通过 `cpufreq` 内核接口查询和设置 CPU 频率。这包括获取 `cpufreq` 设备、调用 Fn cpufreq_levels 获取当前可用的频率级别、使用 Fn cpufreq_get 检查当前级别，以及从列表中使用 Fn cpufreq_set 设置新级别。每个级别实际上可能引用多个 `cpufreq` 驱动，但内核组件无需了解这一点。`struct cf_level` 的 `total_set` 元素提供该级别的频率和功率摘要。未知或不相关的值设为 `CPUFREQ_VAL_UNKNOWN`。

Fn cpufreq_levels 方法接受一个 `cpufreq` 设备和一个空的 `levels` 数组。`count` 值应设为可用的级别数，函数完成后将设为返回的实际级别数。如果级别数多于 `count` 所允许的，应返回 Er E2BIG。

Fn cpufreq_get 方法接受一个用于存储 `level` 的空间指针。成功完成后，输出将为当前活动级别，等于 Fn cpufreq_levels 返回的级别之一。

Fn cpufreq_set 方法接受一个指向 `level` 的指针并尝试激活它。`priority`（例如 `CPUFREQ_PRIO_KERN`）告知 `cpufreq` 在激活此级别时是否覆盖之前的设置。如果 `priority` 高于当前活动级别的优先级，该级别将被保存并以新级别覆盖。如果已保存了某个级别，则设置新级别而不覆盖先前保存的级别。如果调用 Fn cpufreq_set 时 `level` 为 `NULL`，将恢复已保存的级别。如果没有已保存的级别，Fn cpufreq_set 将返回 Er ENXIO。如果 `priority` 低于当前活动级别的优先级，此方法返回 Er EPERM。

## 驱动接口

提供硬件特定 CPU 频率控制的内核驱动通过 `cpufreq` 驱动接口导出其各自的设置。这包括实现以下方法：Fn cpufreq_drv_settings、Fn cpufreq_drv_type、Fn cpufreq_drv_set 和 Fn cpufreq_drv_get。此外，驱动必须将一个设备附加为 CPU 设备的子设备，以便 `cpufreq` 框架能调用这些方法。

Fn cpufreq_drv_settings 方法返回一个当前可用设置的数组，每个设置类型为 `struct cf_setting`。驱动应将未知或不相关的值设为 `CPUFREQ_VAL_UNKNOWN`。每个设置应返回以下所有元素：

```sh
struct cf_setting {
	int	freq;	/* CPU 时钟，单位为 MHz 或百分之一的百分点。 */
	int	volts;	/* 电压，单位为 mV。 */
	int	power;	/* 功耗，单位为 mW。 */
	int	lat;	/* 转换延迟，单位为 us。 */
	device_t dev;	/* 提供此设置的驱动。 */
};
```

进入此方法时，`count` 包含可返回的设置数。成功完成后，驱动将其设为返回的实际设置数。如果驱动提供的设置数多于 `count` 所允许的，应返回 Er E2BIG。

Fn cpufreq_drv_type 方法指示其提供的设置类型，为 `CPUFREQ_TYPE_ABSOLUTE` 或 `CPUFREQ_TYPE_RELATIVE`。此外，如果驱动提供的设置仅供其他驱动参考且不能传递给 Fn cpufreq_drv_set 来激活，则驱动可设置 `CPUFREQ_FLAG_INFO_ONLY` 标志。

Fn cpufreq_drv_set 方法接受一个驱动设置并将其设为活动状态。如果设置无效或当前不可用，应返回 Er EINVAL。

Fn cpufreq_drv_get 方法返回当前活动的驱动设置。返回的 `struct cf_setting` 必须可有效地传递给 Fn cpufreq_drv_set，包括所有元素均已正确填写。如果驱动无法推断当前设置（即使通过 Fn cpu_est_clockrate 估算），则应将所有元素设为 `CPUFREQ_VAL_UNKNOWN`。

## 参见

[acpi(4)](acpi.4.md), [est(4)](est.4.md), [timecounters(4)](timecounters.4.md), [powerd(8)](../man8/powerd.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 作者

Nate Lawson Bruno Ducrot 为 `powernow` 驱动作出了贡献。

## 缺陷

以下驱动尚未转换为 `cpufreq` 接口：[longrun(4)](longrun.4.i386.md)。

CPU 和总线频率变化的通知尚未实现。

当多个 CPU 提供频率控制时，无法将它们设置为不同级别，且必须都提供相同的频率设置。
