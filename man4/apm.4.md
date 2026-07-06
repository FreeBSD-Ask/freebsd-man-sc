# apm.4

`apm` — APM BIOS 接口

## 名称

`apm`

## 概要

`device apm`

## 弃用通知

此驱动计划在 FreeBSD 13.0 发布之前移除。

## 描述

`apm` 是笔记本电脑上 Intel / Microsoft APM（高级电源管理）BIOS 的接口。

`apm` 提供以下电源管理功能。

`#include <machine/apm_bios.h>`

**APMIO_SUSPEND** 挂起系统。

**APMIO_GET** 获取电源管理信息。

**APMIO_ENABLE**

**APMIO_DISABLE** 启用/禁用电源管理。

**APMIO_HALTCPU**

**APMIO_NOTHALTCPU** 控制内核上下文切换例程中 HLT 的执行。

**APMIO_GETPWSTATUS** 获取每个电池的信息。某些 APM 实现在“*Idle CPU*”调用中执行 HLT（暂停 CPU 直到中断发生）指令，而其他实现则不会。因此，启用此选项可能导致冗余的 HLT 执行，因为“*Idle CPU*”是从本质上执行 HLT 的内核上下文切换例程中调用的。这可能会降低系统峰值性能。此外，如果在内核上下文切换例程中禁用了 HLT 指令，并且机器的 APM 实现不在“*Idle CPU*”中执行 HLT，系统将挂起。在某些不支持 CPU 时钟减速的实现上，APM 可能不执行 HLT。`apm` 在此类机器上禁用 **APMIO_NOTHALTCPU** 操作。当前版本的 `apm` 在不支持时钟减速时不会从内核上下文切换例程调用“*Idle CPU*”，并默认执行 HLT 指令。因此，在大多数情况下无需使用这两个操作。

| **名称** | **动作** | **描述** |
| --- | --- | --- |
| `PMEV_STANDBYREQ` | 挂起系统 | 待机请求 |
| `PMEV_SUSPENDREQ` | 挂起系统 | 挂起请求 |
| `PMEV_USERSUSPENDREQ` | 挂起系统 | 用户挂起请求 |
| `PMEV_CRITSUSPEND` | 挂起系统 | 紧急挂起请求 |
| `PMEV_NORMRESUME` | 恢复系统 | 正常恢复 |
| `PMEV_CRITRESUME` | 恢复系统 | 紧急恢复 |
| `PMEV_STANDBYRESUME` | 恢复系统 | 待机恢复 |
| `PMEV_BATTERYLOW` | 通知消息 | 电池电量低 |
| `PMEV_UPDATETIME` | 调整时钟 | 更新时间 |

- 当系统从挂起模式唤醒时，`apm` 将系统时钟调整为 RTC。
- 当系统从挂起模式唤醒时，`apm` 向 syslogd(8) 传递一条消息，包含系统唤醒时间和挂起模式期间的经过时间。
- 当没有系统活动（可运行进程、中断等）时，`apm` 减慢 CPU 时钟。此功能仅在 APM 支持 CPU 空闲的系统上可用。
- `apm` 将应用程序接口导出为字符设备。应用程序可以通过此接口控制 APM 或检索 APM 状态信息。`apm` 导出以下接口。这些符号定义在这些接口由 apm(8) 使用。
- `apm` 轮询 APM 事件并处理以下事件。

## 参见

apm(8), zzz(8)

## 作者

Tatsumi Hosokawa <hosokawa@jp.FreeBSD.org>

## 缺陷

警告！如今笔记本电脑中许多甚至大多数 APM-bios 实现都存在缺陷。使用此接口可能会使你的 LCD 显示器和电池面临风险。（这对 MS-Windows 不是问题，因为它们使用实模式接口。）如果你在使用此代码时发现系统有任何异常行为，请立即拔下电源和电池，并禁用此代码。

我们对使此代码正常工作非常感兴趣，因此请将你观察到的任何异常行为发送给我们。

当 `apm` 处于活动状态时，使用热键调用 BIOS 设置例程可能会在恢复系统时导致严重问题。BIOS 设置程序应在引导期间或从 DOS 调用。

某些 APM 实现无法处理按下电源按钮或合上盖子等事件。在此类实现上，系统`必须`仅使用 apm(8) 或 zzz(8) 挂起。

当前版本不支持磁盘停转、LCD 背光控制和按需供电。
