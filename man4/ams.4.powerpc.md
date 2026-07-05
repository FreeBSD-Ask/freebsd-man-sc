# ams.4.powerpc

`ams` — ADB 鼠标驱动

## 名称

`ams`

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device adb

## 描述

`ams` 驱动为连接到 Apple Desktop Bus（ADB）的鼠标和触控板提供支持，实现了基础和扩展 ADB 鼠标协议。

## 硬件

`ams` 驱动支持的设备包括：

- Apple Mouse
- ADB Extended Mouse
- MacAlly 2-Button Mouse
- Apple iBook Trackpad
- Apple PowerBook Trackpad

## SYSCTL 变量

**`dev.ams.%d.tapping`** 在 ADB 触控板上，将此 sysctl 设为 1 会使触控板上的点按被解释为按钮点击。

## 参见

Apple Tech Note HW01: ADB - The Untold Story: Space Aliens Ate My Mouse: `http://developer.apple.com/legacy/mac/library/technotes/hw/hw_01.html`

[adb(4)](adb.4.powerpc.md), [cuda(4)](cuda.4.powerpc.md), [pmu(4)](pmu.4.powerpc.md)

## 历史

`ams` 设备驱动首次出现于 FreeBSD 8.0。

## 作者

`ams` 驱动由 Nathan Whitehorn <nwhitehorn@FreeBSD.org> 编写。
