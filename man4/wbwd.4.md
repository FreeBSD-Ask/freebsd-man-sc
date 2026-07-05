# wbwd.4

`wbwd` — Winbond/Nuvoton Super I/O 芯片看门狗定时器设备驱动

## 名称

`wbwd`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device superio
> device wbwd

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
wbwd_load="YES"
```

## 描述

`wbwd` 驱动为以下至少 Super I/O 芯片中存在的看门狗中断定时器提供 [watchdog(4)](watchdog.4.md) 支持：

- Winbond 83627HF/F/HG/G
- Winbond 83627S
- Winbond 83697HF
- Winbond 83697UG
- Winbond 83637HF
- Winbond 83627THF
- Winbond 83687THF
- Winbond 83627EHF
- Winbond 83627DHG
- Winbond 83627UHG
- Winbond 83667HG
- Winbond 83627DHG-P
- Winbond 83667HG-B
- Nuvoton NCT6775
- Nuvoton NCT6776
- Nuvoton NCT6102
- Nuvoton NCT6779
- Nuvoton NCT6791
- Nuvoton NCT6792

## SYSCTL 变量

`wbwd` 驱动以 [sysctl(8)](../man8/sysctl.8.md) 变量的形式提供以下选项。

**`dev.wbwd.0.timeout_override`** 此变量允许将定时器编程为独立于 [watchdog(4)](watchdog.4.md) 框架提供的值的值，同时仍依赖于例如 [watchdogd(8)](../man8/watchdogd.8.md) 的定期更新。如果你的系统提供了多个看门狗并希望它们以特殊顺序触发（例如在重置超时之前较短时间触发 NMI），则此功能特别有用。设置的值不得低于 [watchdogd(8)](../man8/watchdogd.8.md) 的睡眠时间。值为 0 时禁用此功能，将使用 [watchdog(4)](watchdog.4.md) 提供的超时值。

**`dev.wbwd.0.debug_verbose`** 如果设置，此 sysctl 将指示驱动在每次 [watchdog(9)](../man9/watchdog.9.md) 调用时，在定时器重置之前和之后将其当前状态记录到内核消息缓冲区中以便调试。

**`dev.wbwd.0.debug`** 此只读值给出上次更新时某些寄存器的状态。

`wbwd` 驱动还提供了默认情况下隐藏的其他 sysctl 选项。更多信息参见源代码。

## 参见

[superio(4)](superio.4.md), [watchdog(4)](watchdog.4.md), [device.hints(5)](../man5/device.hints.5.md), [watchdog(8)](../man8/watchdog.8.md), [watchdogd(8)](../man8/watchdogd.8.md), [watchdog(9)](../man9/watchdog.9.md)

## 历史

`wbwd` 驱动最早出现在 FreeBSD 10.0 中。

## 作者

本手册页由 Bjoern A. Zeeb <bz@FreeBSD.org> 编写。
