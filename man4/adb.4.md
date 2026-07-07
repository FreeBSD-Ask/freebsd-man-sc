# adb(4)

`adb` — Apple Desktop Bus

## 名称

`adb`

## 概要

`要将此驱动编译进内核，请将以下行放入你的内核配置文件：`

> device adb

## 描述

`adb` 驱动为 Apple Desktop Bus 提供支持，这是一种简单的多点总线，通常用于较老 Apple Macintosh 硬件的输入外设。

Apple Desktop Bus 提供最多 16 个设备的连接，包括多个同类型设备，但不支持热插拔。

## 参见

Apple Tech Note HW01: ADB - The Untold Story: Space Aliens Ate My Mouse: `http://developer.apple.com/legacy/mac/library/technotes/hw/hw_01.html`

[akbd(4)](akbd.4.md), [ams(4)](ams.4.md), [cuda(4)](cuda.4.md), [pmu(4)](pmu.4.md)

## 历史

`adb` 设备驱动出现于 FreeBSD 8.0。

## 作者

`adb` 驱动由 Nathan Whitehorn <nwhitehorn@FreeBSD.org> 编写。
