# acpi_battery(4)

`acpi_battery` — ACPI 电池管理子系统

## 名称

`acpi_battery`

## 概要

`device acpi`

## 描述

`acpi_battery` 是 ACPI 模块电池管理功能的驱动。

兼容 ACPI 的电池设备支持 Control Method Battery 接口或 Smart Battery 子系统接口。前者通过 AML（ACPI Machine Language）代码控制方法访问，后者直接通过 ACPI EC（Embedded Controller）控制，通常经由 SMBus 接口。

此驱动支持 [sysctl(8)](../man8/sysctl.8.md) 和 ioctl(2) 接口，以及 devd(8) 事件通知接口。

## IOCTLS

`acpi_battery` 驱动的每个 ioctl 都以一个表示电池单元编号的整数值作为参数，并为每个请求返回特定的结构。特殊的单元编号 `ACPI_BATTERY_ALL_UNITS` 表示所有已连接的单元，并报告汇总信息。

**`ACPI_BATT_STAT_DISCHARG`** (0x0001) 电池正在放电，

**`ACPI_BATT_STAT_CHARGING`** (0x0002) 电池正在充电，或

**`ACPI_BATT_STAT_CRITICAL`** (0x0004) 剩余电量严重不足。

**`cap`** 电池容量百分比，

**`min`** 剩余电池续航时间（分钟），

**`state`** 电池当前状态，按以下编码：注意当指定 `ACPI_BATTERY_ALL_UNITS` 时，各电池的状态位会被合并。

**`rate`** 当前电池放电速率（mW）。`-1` 表示当前未在放电。

**`ACPI_BIX_REV_0`** (0x0000) ACPI 4.0 中的 `_BIX` 对象。

**`ACPI_BIX_REV_1`** (0x0001) ACPI 6.0 中的 `_BIX` 对象。

**`ACPI_BIX_REV_BIF`** (0xffff) 由系统上的 `_BIF` 对象构建的 `_BIX` 对象。

**ACPI_BIX_UNITS_MW** (0x00000000) 以 mW（功率）为单位

**ACPI_BIX_UNITS_MA** (0x00000001) 以 mA（电流）为单位

**0x00000000** 主电池（不可充电）

**0x00000001** 次电池（可充电）

**ACPI_BIX_SCAP_NO** (0x00000000) 不可热插拔

**ACPI_BIX_SCAP_COLD** (0x00000001) 冷插拔

**ACPI_BIX_SCAP_HOT** (0x00000010) 热插拔

**`rev`** 对象的修订号。已知值如下：注意检查最低修订号时，应使用 `ACPI_BIX_REV_MIN_CHECK` 宏来检查 `rev` 字段。

**`units`** 指示电池报告容量和充电速率所使用的单位，按以下编码：注意容量以 mWh 或 mAh 表示，速率分别以 mW 或 mA 表示。

**`dcap`** 电池的设计容量，即新电池的标称容量。根据 `units` 的值以功率或电流表示。

**`lfcap`** 完全充电时预测的电池容量。通常会随每次充电循环而下降。

**btech** 电池技术：

**`dvol`** 设计电压（mV），即新电池的标称电压。

**`wcap`** 警告容量设计值。当放电中的电池设备达到此容量时，会向系统发送通知。

**`lcap`** 低容量设计值。

**`cycles`** （rev 0 或更高）电池经历的循环次数。一次循环指发生的放电量约等于设计容量值。

**`accuracy`** （rev 0 或更高）电池容量测量的精度，以千分之一百分比为单位。

**`stmax`** （rev 0 或更高）电池的最大采样时间（毫秒）。这是 `_BST` 中规定的电池容量两次连续测量之间的最大间隔。如果两次连续读取 `_BST` 超过此时长，可能返回不同结果。

**`stmin`** （rev 0 或更高）电池的最小采样时间（毫秒）。

**`aimax`** （rev 0 或更高）电池的最大平均间隔（毫秒）。这是电池对 `_BST` 中规定的容量测量进行平均的时间长度。采样时间指定测量的频率，平均间隔指定每次测量的时间窗口宽度。

**`aimin`** （rev 0 或更高）电池的最小平均间隔（毫秒）。

**`gra1`** `low` 与 `warning` 之间的电池容量粒度。根据 `units` 的值以功率或电流表示。

**`gra2`** `warning` 与 `full` 之间的电池容量粒度。根据 `units` 的值以功率或电流表示。

**`model`** 电池型号字符串。

**`serial`** 电池序列号字符串。

**`type`** 电池类型标识符字符串。

**`oeminfo`** 电池的 OEM 专用信息字符串。

**`scap`** （rev 1 或更高）电池插拔能力，按以下编码：

**`state`** 电池状态。该值的编码方式与 `struct acpi_battinfo` 的 `state` 相同。

**`rate`** 电池当前充电或放电速率。该值的单位取决于 `struct acpi_bif` 的 `unit`。

**`cap`** 电池剩余容量。该值的单位取决于 `struct acpi_bif` 的 `unit`。

**`volt`** 电池当前电压。

**`ACPIIO_BATT_GET_UNITS`** `int` 返回系统中的电池单元数量。单元编号参数将被忽略。

**`ACPIIO_BATT_GET_BATTINFO`** `struct acpi_battinfo` 返回以下内容：

**`ACPIIO_BATT_GET_BIX`** `struct acpi_bix` 返回由 ACPI `_BIX`（Battery Information）对象给出的电池信息，这是 Control Method Battery 信息的静态部分。对于连接到 SMBus 的 Smart Battery 或具有 `_BIF` 对象的 Control Method Battery，此 ioctl 会根据获取的信息构建 `struct acpi_bix` 结构并返回。

**`ACPIIO_BATT_GET_BIF`** `struct acpi_bif` （已弃用）返回由 ACPI `_BIF`（Battery Information）对象给出的电池信息，该对象在 ACPI 4.0 规范中已弃用。该数据结构是 `struct acpi_bix` 的子集。注意，即使此对象不可用而找到 `_BIX` 对象，此 ioctl 也会根据获取的信息构建 `struct acpi_bif` 结构。

**ACPIIO_BATT_GET_BST** `struct acpi_bst` 返回由 ACPI `_BST`（Battery Status）对象给出的电池信息，即当前电池状态。对于连接到 SMBus 的 Smart Battery，此 ioctl 会根据获取的信息构建 `struct acpi_bst` 结构并返回。

## SYSCTL 变量

以下 [sysctl(8)](../man8/sysctl.8.md) 变量导出电池状态。注意它们是所有已连接电池的汇总状态：

**`hw.acpi.battery.info_expire`** 信息缓存过期时间（秒）。通过 `_BIX` 或 `_BIF` 对象获取的电池信息会在指定时间内被存储并复用于对该 MIB 的后续读访问。

**`hw.acpi.battery.units`** 系统中的电池单元数量。

**`hw.acpi.battery.state`** 当前电池充电状态。与 `struct acpi_battinfo` 的 `state` 相同。

**`hw.acpi.battery.rate`** 当前电池放电速率（mW）。

**`hw.acpi.battery.time`** 剩余电池续航时间（分钟）。如果电池未在放电，该值为 `-1`。

**`hw.acpi.battery.life`** 电池容量百分比。

## 事件通知

与电池相关的事件通知通过 devd(8) 接口发送到用户态。详见 **`/etc/devd.conf`** 和 devd.conf(5)。注意仅 Control Method Battery 支持通知。

`acpi_battery` 驱动发送的事件具有以下属性：

**`0x80`** 电池状态已更改。
**`0x81`** 电池信息已更改。

**system** `ACPI`
**subsystem** `CMBAT`
**type** ASL 中完全限定的电池对象路径。
**notify** 表示事件的整数：

## 参见

[acpi(4)](acpi.4.md), acpiconf(8)

## 作者

Nate Lawson <njl@FreeBSD.org>, Munehiro Matsuda, Takanori Watanabe <takawata@FreeBSD.org>, Mitsuru IWASAKI <iwasaki@FreeBSD.org>, Hans Petter Selasky <hselasky@FreeBSD.org>, and Hiroki Sato <hrs@FreeBSD.org>.

本手册页由 Takanori Watanabe <takawata@FreeBSD.org> 和 Hiroki Sato <hrs@FreeBSD.org> 编写。
