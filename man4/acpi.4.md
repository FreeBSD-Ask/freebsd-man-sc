# acpi.4

`acpi` — 高级配置与电源管理支持

## 名称

`acpi`

## 概要

`device acpi`

`options ACPI_DEBUG options DDB`

## 描述

`acpi` 驱动提供对 Intel/Microsoft/Compaq/Toshiba ACPI 标准的支持。该支持包括平台硬件发现（取代 PnP 和 PCI BIOS），以及电源管理（取代 APM）和其他功能。ACPI 核心支持由 Intel 的 ACPI CA 参考实现提供。

请注意，`acpi` 驱动会由 [loader(8)](../man8/loader.8.md) 自动加载，仅应在 ACPI 为强制要求的平台上编译进内核。

## SYSCTL 变量

`acpi` 驱动旨在无需用户干预的情况下提供电源管理。如果默认设置并非最优，可使用以下 sysctl 来修改或监视 `acpi` 的行为。请注意，某些变量仅在给定硬件支持时才可用（例如 `hw.acpi.acline`）。

**`S1`** 快速挂起到内存。CPU 进入较低功耗状态，但大多数外设继续运行。

**`S2`** 功耗状态低于 `S1`，但基本特征相同。许多系统不支持。

**`S3`** 挂起到内存。大多数设备断电，系统停止运行，仅保留内存刷新。

**`S4`** 挂起到磁盘。所有设备断电，系统停止运行。恢复时，系统如同冷启动一样启动。除非 `S4BIOS` 可用，否则 FreeBSD 尚不支持。

**`S5`** 系统干净关闭并断电。

**`debug.acpi.enable_debug_objects`** 在不带 `options ACPI_DEBUG` 的情况下启用 Debug 对象的转储。默认为 0，忽略 Debug 对象。

**`dev.cpu.N.cx_usage`** 调试信息，列出每个睡眠状态占总使用时长的百分比。修改 `dev.cpu.N.cx_lowest` 时这些值会重置。

**`dev.cpu.N.cx_lowest`** 用于使 CPU 空闲的最低 Cx 状态。调度算法会根据系统负载在 `C1` 和此设置之间选择状态。要启用 ACPI CPU 空闲控制，如果 `machdep.idle_available` 中列出了 `acpi`，应将 `machdep.idle` 设置为 `acpi`。

**`dev.cpu.N.cx_supported`** 支持的 CPU 空闲状态列表及其转换延迟（单位为微秒）。每个状态有一个类型（例如 `C2`）。`C1` 等价于 ia32 `HLT` 指令，`C2` 提供语义相同但更深的睡眠，`C3` 提供最深的睡眠但还需要禁用总线主控。高于 `C3` 的状态在语义与 `C3` 状态相同的情况下提供更多节能。越深的睡眠节能越多，但当中断发生时转换延迟也会增加。

**`dev.cpu.N.cx_method`** 支持的 CPU 空闲状态列表及其转换方法，由固件指定。

**`hw.acpi.acline`** 交流电源状态（1 表示在线，0 表示使用电池供电）。

**`hw.acpi.disable_on_reboot`** 在重启过程中禁用 ACPI。大多数系统在 ACPI 仍然启用时也能正常重启，但有些系统需要先退出到 legacy 模式。默认为 0，保持 ACPI 启用。

**`hw.acpi.handle_reboot`** 使用 ACPI Reset Register 功能重启系统。一些较新的系统要求使用此寄存器，而有些只能使用 legacy 重启支持。

**`hw.acpi.lid_switch_state`** 当合上盖板开关（即笔记本屏幕）时进入的睡眠类型（`awake`、`standby`、`fw_suspend`、`suspend_to_idle`、`fw_hibernate`、`poweroff`），或“`NONE`”（不执行任何操作）。默认为“`NONE`”。

**`hw.acpi.power_button_state`** 当按下电源按钮时进入的睡眠类型（`awake`、`standby`、`fw_suspend`、`suspend_to_idle`、`fw_hibernate`、`poweroff`），或“`NONE`”（不执行任何操作）。默认为 `poweroff`。

**`hw.acpi.reset_video`** 在恢复路径中从实模式重置视频适配器。有些系统需要此帮助，另一些启用后会出现显示问题。默认为 0（禁用）。

**`hw.acpi.s4bios`** 指示系统是否支持 `S4BIOS`。这意味着 BIOS 可以处理将系统挂起到磁盘的所有功能。否则由操作系统负责挂起到磁盘（`S4OS`）。大多数当前系统不支持 `S4BIOS`。

**`hw.acpi.sleep_button_state`** 当按下睡眠按钮时进入的睡眠类型（`awake`、`standby`、`fw_suspend`、`suspend_to_idle`、`fw_hibernate`、`poweroff`）。通常是键盘上的特殊功能按钮。如果支持，默认通常为 `fw_suspend`；如果不支持，则为 `suspend_to_idle`。

**`hw.acpi.sleep_delay`** 在准备系统挂起到实际进入挂起状态之间等待的秒数。默认为 1 秒。

**`hw.acpi.supported_sleep_state`** BIOS 支持的 ACPI S 状态（`S1` 至 `S5`）。

**`hw.acpi.verbose`** 启用各 ACPI 子系统的详细打印输出。

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 **`/boot/loader.conf`** 中。其中许多可调参数也有对应的 [sysctl(8)](../man8/sysctl.8.md) 条目，供引导后访问。

**`acpi_dsdt_load`** 启用加载自定义 ACPI DSDT。

**`acpi_dsdt_name`** 若启用加载，要加载的 DSDT 表名称。

**`debug.acpi.disabled`** 出于调试目的选择性地禁用 ACPI 的某些部分。

**`debug.acpi.interpreter_slack`** 启用较宽松的 ACPI 实现。默认为 1，忽略常见的 BIOS 错误。

**`debug.acpi.max_threads`** 指定引导时启动的任务线程数。将其限制为 1 可能有助于绕过无法处理并行请求的各种 BIOS。默认值为 3。

**`debug.acpi.quirks`** 完全覆盖任何自动 quirk。

**`debug.acpi.resume_beep`** 恢复时使 PC 喇叭发出蜂鸣。这有助于诊断挂起/恢复问题。默认为 0（禁用）。

**`hint.acpi.0.disabled`** 将此项设置为 1 可禁用整个 ACPI。如果系统因 BIOS 黑名单条目而禁用了 ACPI，可将此项设置为 0 以重新启用 ACPI 进行测试。

**`hw.acpi.ec.poll_timeout`** 等待 EC 响应的延迟（单位为毫秒）。如果出现“`AE_NO_HARDWARE_RESPONSE`”错误，可尝试增大此值。

**`hw.acpi.host_mem_start`** 覆盖 PCI 主桥假定的内存起始地址。

**`hw.acpi.install_interface , hw.acpi.remove_interface`** 安装或移除 OS 接口，以控制 `_OSI` 查询方法的返回值。当在 `hw.acpi.install_interface` 中指定某个 OS 接口时，对该接口的 `_OSI` 查询返回*支持*。反之，当在 `hw.acpi.remove_interface` 中指定某个 OS 接口时，`_OSI` 查询返回*不支持*。可以以逗号分隔的列表指定多个接口，前导空白将被忽略。例如，“`FreeBSD, Linux`”是包含“`FreeBSD`”和“`Linux`”两个接口的有效列表。

**`hw.acpi.hw.acpi.override_isa_irq_polarity (x86)`** 强制边沿触发的 ISA 中断使用低电平有效极性。一些较旧系统错误地为 ISA 中断指定了低电平有效极性，此覆盖可修复这些系统。在带有 Intel CPU 的系统上默认启用此覆盖，但可通过显式设置该可调参数来启用或禁用。

**`hw.acpi.reset_video`** 在恢复路径上启用调用 VESA reset BIOS 向量。这可以修复某些显卡在恢复后出现 LCD 白屏等问题。默认为 0（禁用）。

**`hw.acpi.serialize_methods`** 允许覆盖方法是否并行执行。启用此项可获得串行行为，可修复对于确实无法处理并行方法执行的 AML 出现的“`AE_ALREADY_EXISTS`”错误。默认关闭，因为会破坏递归方法，而某些 IBM 使用此类代码。

**`hw.acpi.verbose`** 开启关于 ACPI 正在做什么的详细调试信息。

**`hw.pci.link.%s.%d.irq`** 覆盖此 link 和索引要使用的中断。应谨慎使用此功能，且仅当某设备在启用 `acpi` 时不工作时使用。“%s”是 link 的名称（例如 LNKA）。“%d”是当 link 支持多个 IRQ 时的资源索引。大多数 PCI link 只有一个 IRQ 资源，因此应使用下面的形式。

**`hw.pci.link.%s.irq`** 覆盖要使用的中断。应谨慎使用此功能，且仅当某设备在启用 `acpi` 时不工作时使用。“%s”是 link 的名称（例如 LNKA）。

## 禁用 ACPI

由于不同平台上 ACPI 支持差异很大，因此提供了许多调试和调优选项。

对于已知在启用 `acpi` 时无法工作的机器，有一个 BIOS 黑名单。目前，该黑名单仅控制是否应禁用 `acpi`。未来它将具有更细粒度的功能控制（相关基础设施已就绪）。

要在黑名单中的机器上启用 `acpi`（出于调试目的等），将内核环境变量 `hint.acpi.0.disabled` 设置为 0。在尝试此操作之前，可考虑将 BIOS 更新到可能兼容 ACPI 的较新版本。

要完全禁用 `acpi` 驱动，将内核环境变量 `hint.acpi.0.disabled` 设置为 1。

某些 i386 机器在部分或全部 ACPI 被禁用时完全无法运行。另一些 i386 机器在启用 ACPI 时无法运行。在非 i386 平台（即 ACPI 支持为强制要求的平台）上禁用全部或部分 ACPI 可能导致系统无法使用。

`acpi` 驱动由一组驱动组成，可在出现问题时选择性地禁用。要禁用某个子驱动，将其列在内核环境变量 `debug.acpi.disabled` 中。可列出多个条目，以空格分隔。

可禁用的 ACPI 子设备和功能：

**`all`** 禁用所有 ACPI 功能和设备。

**`acad`** （`device`）支持交流适配器。

**`bus`** （`feature`）探测并附加子设备。禁用后将完全避免扫描 ACPI 命名空间。

**`children`** （`feature`）附加标准 ACPI 子驱动和 ACPI 命名空间中枚举的设备。禁用此项的效果与禁用“`bus`”类似，不同之处在于 ACPI 命名空间仍会被扫描。

**`button`** （`device`）支持 ACPI 按钮设备（通常是电源和睡眠按钮）。

**`cmbat`** （`device`）控制方法电池设备。

**`cpu`** （`device`）支持 CPU 节能和速率设置功能。

**`ec`** （`device`）支持 ACPI 嵌入式控制器接口，用于与嵌入式平台控制器通信。

**`isa`** （`device`）支持 ACPI 命名空间中定义的 ISA 总线桥，通常作为 PCI 总线的子设备。

**`lid`** （`device`）支持 ACPI 笔记本盖板开关，通常会使系统进入睡眠。

**`mwait`** （`feature`）不向固件询问可用的 x86 厂商专用方法来进入 `Cx` 睡眠状态。仅查询并使用基于通用 I/O 的入口方法。提供此开关以绕过固件填写的表中的不一致问题。

**`quirks`** （`feature`）不遵循 quirk。quirirk 会根据 XSDT 表的 OEM 厂商名称和修订日期自动禁用 ACPI 功能。

**`pci`** （`device`）支持 Host 到 PCI 桥。

**`pci_link`** （`feature`）执行 PCI 中断路由。

**`sysresource`** （`device`）包含 ACPI 所声明资源的伪设备。

**`thermal`** （`device`）支持系统散热和热量管理。

**`timer`** （`device`）使用 ACPI 固定频率定时器实现 timecounter。

**`video`** （`device`）支持 [acpi_video(4)](acpi_video.4.md)，可能与 [agp(4)](agp.4.md) 设备冲突。

也可通过在内核环境变量 `debug.acpi.avoid` 中列出要避免的区域的根的完整路径，来避开可能引起问题的 ACPI 命名空间部分。在对命名空间进行 bus/children 扫描期间，该对象及其所有子对象将被忽略。ACPI CA 代码仍会知道被避开的区域。

## 调试输出

要启用调试输出，`acpi` 必须以 `options ACPI_DEBUG` 编译。调试输出按层（layer）和级别（level）划分，其中层是 ACPI 子系统的一个组件，级别是一种特定类型的调试输出。

层和级别均以空白分隔的 token 列表指定，层列在 `debug.acpi.layer` 中，级别列在 `debug.acpi.level` 中。

第一组层用于 ACPI-CA 组件，第二组用于 FreeBSD 驱动。ACPI-CA 层描述包含其所指文件的前缀。支持的层有：

**`ACPI_UTILITIES`** 实用工具（"ut"）函数
**`ACPI_HARDWARE`** 硬件访问（"hw"）
**`ACPI_EVENTS`** 事件和 GPE（"ev"）
**`ACPI_TABLES`** 表访问（"tb"）
**`ACPI_NAMESPACE`** 命名空间求值（"ns"）
**`ACPI_PARSER`** AML 解析器（"ps"）
**`ACPI_DISPATCHER`** 解释器状态的内部表示（"ds"）
**`ACPI_EXECUTER`** 执行 AML 方法（"ex"）
**`ACPI_RESOURCES`** 资源解析（"rs"）
**`ACPI_CA_DEBUGGER`** 调试器实现（"db"、"dm"）
**`ACPI_OS_SERVICES`** 用户态支持例程（"os"）
**`ACPI_CA_DISASSEMBLER`** 反汇编器实现（未使用）
**`ACPI_ALL_COMPONENTS`** 上述所有 ACPI-CA 组件
**`ACPI_AC_ADAPTER`** 交流适配器驱动
**`ACPI_BATTERY`** 控制方法电池驱动
**`ACPI_BUS`** ACPI、ISA 和 PCI 总线驱动
**`ACPI_BUTTON`** 电源和睡眠按钮驱动
**`ACPI_EC`** 嵌入式控制器驱动
**`ACPI_FAN`** 风扇驱动
**`ACPI_OEM`** 用于热键、LED 等的平台专用驱动
**`ACPI_POWERRES`** 电源资源驱动
**`ACPI_PROCESSOR`** CPU 驱动
**`ACPI_SPMC`** 系统电源管理控制器驱动
**`ACPI_THERMAL`** 散热区域驱动
**`ACPI_TIMER`** 定时器驱动
**`ACPI_ALL_DRIVERS`** 上述所有 FreeBSD ACPI 驱动

支持的级别有：

**`ACPI_LV_INIT`** 初始化进度
**`ACPI_LV_DEBUG_OBJECT`** 对象存储
**`ACPI_LV_INFO`** 一般信息和进度
**`ACPI_LV_REPAIR`** 修复预定义方法的常见问题
**`ACPI_LV_ALL_EXCEPTIONS`** 上述所有级别
**`ACPI_LV_PARSE`**
**`ACPI_LV_DISPATCH`**
**`ACPI_LV_EXEC`**
**`ACPI_LV_NAMES`**
**`ACPI_LV_OPREGION`**
**`ACPI_LV_BFIELD`**
**`ACPI_LV_TABLES`**
**`ACPI_LV_VALUES`**
**`ACPI_LV_OBJECTS`**
**`ACPI_LV_RESOURCES`**
**`ACPI_LV_USER_REQUESTS`**
**`ACPI_LV_PACKAGE`**
**`ACPI_LV_VERBOSITY1`** 上述所有级别
**`ACPI_LV_ALLOCATIONS`**
**`ACPI_LV_FUNCTIONS`**
**`ACPI_LV_OPTIMIZATIONS`**
**`ACPI_LV_VERBOSITY2`** 上述所有级别
**`ACPI_LV_ALL`** “`ACPI_LV_VERBOSITY2`”的同义词
**`ACPI_LV_MUTEX`**
**`ACPI_LV_THREADS`**
**`ACPI_LV_IO`**
**`ACPI_LV_INTERRUPTS`**
**`ACPI_LV_VERBOSITY3`** 上述所有级别
**`ACPI_LV_AML_DISASSEMBLE`**
**`ACPI_LV_VERBOSE_INFO`**
**`ACPI_LV_FULL_TABLES`**
**`ACPI_LV_EVENTS`**
**`ACPI_LV_VERBOSE`** “`ACPI_LV_VERBOSITY3`”之后的所有级别
**`ACPI_LV_INIT_NAMES`**
**`ACPI_LV_LOAD`**

选择合适的层和级别值非常重要，以避免产生大量调试输出。例如，以下配置是收集初始信息的良好方式。它为 ACPI-CA 和 `acpi` 驱动都启用调试输出，打印关于错误、警告和进度的基本信息。

```sh
debug.acpi.layer="ACPI_ALL_COMPONENTS ACPI_ALL_DRIVERS"
debug.acpi.level="ACPI_LV_ALL_EXCEPTIONS"
```

ACPI CA 子系统的调试输出以小写模块名作为前缀，后跟源行号。来自 FreeBSD 本地代码的输出遵循相同格式，但模块名为大写。

## 覆盖 BIOS 字节码

ACPI 在引导时将 BIOS 厂商提供的名为 AML（ACPI Machine Language）的字节码作为内存映像进行解释。有时，AML 代码包含在 Microsoft 实现下解析时不显现的 bug。FreeBSD 提供了一种用你自己的 AML 代码覆盖它的方法，以绕过或调试此类问题。请注意，DSDT 和任何 SSDT 表中的所有 AML 都会被覆盖。

要加载你的 AML 代码，必须编辑 **`/boot/loader.conf`** 并加入以下行。

```sh
acpi_dsdt_load="YES"
acpi_dsdt_name="/boot/acpi_dsdt.aml" # 你可以更改此名称。
```

要准备你的 AML 代码，需要 acpidump(8) 和 iasl(8) 工具以及一些 ACPI 知识。

## 兼容性

ACPI 仅在 i386/ia32 和 amd64 上存在并受支持。

## 参见

[kenv(1)](../man1/kenv.1.md), [acpi_thermal(4)](acpi_thermal.4.md), [device.hints(5)](../man5/device.hints.5.md), loader.conf(5), acpiconf(8), acpidump(8), [config(8)](../man8/config.8.md), iasl(8)

> Compaq Computer Corporation, Intel Corporation, Microsoft Corporation, Phoenix Technologies Ltd., Toshiba Corporation, "Advanced Configuration and Power Interface Specification", August 25, 2003.

## 作者

ACPI CA 子系统由 Intel Architecture Labs 开发和维护。

以下人员对 FreeBSD 中的 ACPI 子系统做出了重要贡献：Michael Smith、Takanori Watanabe <takawata@jp.FreeBSD.org>、Mitsuru IWASAKI <iwasaki@jp.FreeBSD.org>、Munehiro Matsuda、Nate Lawson、位于 <acpi-jp@jp.FreeBSD.org> 的 ACPI-jp 邮件列表，以及许多其他贡献者。

本手册页由 Michael Smith <msmith@FreeBSD.org> 编写。

## 缺陷

许多 BIOS 版本存在严重 bug，可能导致系统不稳定、破坏挂起/恢复，或因 IRQ 路由问题导致设备无法正常工作。在认定是 `acpi` 的问题之前，请先将 BIOS 升级到厂商提供的最新版本。
