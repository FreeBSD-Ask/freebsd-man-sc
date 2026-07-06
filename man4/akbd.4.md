# akbd.4

`akbd` — ADB 键盘驱动

## 名称

`akbd`

## 概要

`要将此驱动编译进内核，请将以下行放入你的内核配置文件：`

> device adb

## 描述

`akbd` 驱动为连接到 Apple Desktop Bus（ADB）的所有键盘提供支持。

## 硬件

`akbd` 驱动支持的设备包括：

- Apple Extended Keyboard
- Apple Keyboard II
- Apple iBook 键盘
- Apple PowerBook 键盘

## 事件

`akbd` 驱动在 `PMU` 系统下为以下事件向 devd(8) 发送事件：

- 电源按钮 - `Button` 子系统，`pressed` 类型。

## SYSCTL 变量

`akbd` 驱动支持以下用于配置 Fn 键的 sysctl 变量：

**`dev.akbd.%d.fn_keys_function_as_primary`** 将 Fn 键默认设置为 F 键类型。值为 0 时，F 键默认作为特殊键工作（[abtn(4)](abtn.4.md)），值为 1 时，默认作为 F 键工作。

## 参见

[abtn(4)](abtn.4.md), [adb(4)](adb.4.md), [cuda(4)](cuda.4.md), [pmu(4)](pmu.4.md)

## 历史

`akbd` 设备驱动出现于 FreeBSD 8.0。

## 作者

`akbd` 驱动由 Nathan Whitehorn <nwhitehorn@FreeBSD.org> 编写。
