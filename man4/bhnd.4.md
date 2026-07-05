# bhnd.4

`bhnd` — Broadcom 家庭网络部门互连总线

## 名称

`bhnd`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device bhnd

要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
bhnd_load="YES"
```

## 描述

`bhnd` 驱动为 Broadcom 家庭网络部门（HND）设备中使用的片上互连提供统一的内核总线接口。

Broadcom HND 设备家族由 SoC（System On a Chip，片上系统）和主机连接的芯片组组成，基于通过内部硬件总线架构连接的通用 Broadcom IP 核库。这些核心的驱动针对统一的 `bhnd` 接口实现。

早期 HND 设备中使用的 Sonic Inc. Silicon Backplane 由 [siba(4)](siba.4.md) BHND 驱动支持。

后续 HND 设备中使用的基于 ARM AMBA 的互连由 [bcma(4)](bcma.4.md) BHND 驱动支持。

## 参见

[bcma(4)](bcma.4.md), [bhndb(4)](bhndb.4.md), [intro(4)](intro.4.md), [siba(4)](siba.4.md)

## 历史

`bhnd` 设备驱动首次出现于 FreeBSD 11.0。

## 作者

`bhnd` 驱动由 Landon Fuller <landonf@FreeBSD.org> 编写。
