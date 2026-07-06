# abtn.4

`abtn` — ADB 键盘特殊键驱动

## 名称

`abtn`

## 概要

`要将此驱动编译进内核，请将以下行放入你的内核配置文件：`

> device adb

## 描述

`abtn` 驱动为带有 ADB 接口的 Apple 笔记本上的扩展 Fn 键提供支持。

## 硬件

`abtn` 驱动支持以下设备上的扩展键盘键（特殊 F 键）：

- Apple iBook 键盘
- Apple PowerBook 键盘

## 事件

`abtn` 驱动在 `PMU` 系统和 `keys` 子系统下，为以下事件向 devd(8) 发送事件：

- `brightness` - 生成与按下的键匹配的 `up` 和 `down` 通知类型。
- `mute`
- `volume` - 生成与按下的键匹配的 `up` 和 `down` 通知类型。
- `eject`

示例包含在 **`/etc/devd/apple.conf`** 中。

## 参见

[adb(4)](adb.4.md), [akbd(4)](akbd.4.md), [cuda(4)](cuda.4.md), [pmu(4)](pmu.4.md), devd(8)

## 历史

`abtn` 设备驱动首次出现于 NetBSD 5.0，并移植到 FreeBSD 10.0。

## 作者

`abtn` 驱动由 Tsubai Masanari 为 NetBSD 编写，并由 Justin Hibbits 移植到 FreeBSD。
