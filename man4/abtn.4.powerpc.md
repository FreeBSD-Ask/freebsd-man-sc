# abtn.4.powerpc

`abtn` — ADB 键盘特殊按键驱动

## 名称

`abtn`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device adb

## 描述

`abtn` 驱动为带有 ADB 接口的 Apple 笔记本上的扩展 Fn 键提供支持。

## 硬件

`abtn` 驱动支持以下设备上的扩展键盘按键（特殊 F 键）：

- Apple iBook Keyboard
- Apple PowerBook Keyboard

## 事件

`abtn` 驱动在 `PMU` 系统和 `keys` 子系统下将以下事件发送给 devd(8)：

- `brightness` — 生成与按下按键匹配的 `up` 和 `down` 通知类型。
- `mute`
- `volume` — 生成与按下按键匹配的 `up` 和 `down` 通知类型。
- `eject`

示例见 **`/etc/devd/apple.conf`**。

## 参见

[adb(4)](adb.4.powerpc.md), [akbd(4)](akbd.4.powerpc.md), [cuda(4)](cuda.4.powerpc.md), [pmu(4)](pmu.4.powerpc.md), devd(8)

## 历史

`abtn` 设备驱动最早出现在 NetBSD 5.0 中，并移植到 FreeBSD 10.0。

## 作者

`abtn` 驱动由 Tsubai Masanari 为 NetBSD 编写，并由 Justin Hibbits 移植到 FreeBSD。
