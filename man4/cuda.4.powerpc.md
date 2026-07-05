# cuda.4.powerpc

`cuda` — Apple CUDA I/O 控制器驱动

## 名称

`cuda`

## 概要

`若要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device adb
> device cuda

## 描述

`cuda` 驱动为预 Core99 Apple 硬件（如 Power Macintosh G3）中的 CUDA VIA（Versatile Interface Attachment，通用接口附件）芯片提供支持。

Apple CUDA 控制器是一种多用途 ASIC，提供电源控制和 [adb(4)](adb.4.powerpc.md) 接口。

## 硬件

`cuda` 驱动支持的芯片包括：

- Apple CUDA I/O 控制器

## 参见

[adb(4)](adb.4.powerpc.md)

## 历史

`cuda` 设备驱动最初出现于 NetBSD 4.0，随后出现于 FreeBSD 8.0。

## 作者

`cuda` 驱动由 Michael Lorenz <macallan@NetBSD.org> 编写，并由 Nathan Whitehorn <nwhitehorn@FreeBSD.org> 移植到 FreeBSD。
