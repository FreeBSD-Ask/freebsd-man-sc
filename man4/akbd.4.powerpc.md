# akbd.4.powerpc

`akbd` — ADB 键盘驱动

## 名称

`akbd`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device adb

## 描述

`akbd` 驱动为所有连接到 Apple Desktop Bus (ADB) 的键盘提供支持。

## 硬件

`akbd` 驱动支持的设备包括：

- Apple Extended Keyboard
- Apple Keyboard II
- Apple iBook Keyboard
- Apple PowerBook Keyboard

## 事件

`akbd` 驱动在 `PMU` 系统下将以下事件发送给 devd(8)：

- 电源按钮 — `Button` 子系统，`pressed` 类型。

## SYSCTL 变量

`akbd` 驱动支持以下 sysctl 变量用于配置 Fn 键：

**`dev.akbd.%d.fn_keys_function_as_primary`** 将 Fn 键默认设置为其 F 键类型。值为 0 使 F 键默认作为特殊键工作（[abtn(4)](abtn.4.powerpc.md)），值为 1 使它们默认作为 F 键工作。

## 参见

[abtn(4)](abtn.4.powerpc.md), [adb(4)](adb.4.powerpc.md), [cuda(4)](cuda.4.powerpc.md), [pmu(4)](pmu.4.powerpc.md)

## 历史

`akbd` 设备驱动出现在 FreeBSD 8.0 中。

## 作者

`akbd` 驱动由 Nathan Whitehorn <nwhitehorn@FreeBSD.org> 编写。
