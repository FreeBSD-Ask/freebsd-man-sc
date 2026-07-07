# siba(4)

`siba` — Sonic Inc. Silicon Backplane 驱动

## 名称

`siba`

## 概要

`要将此驱动编译进内核，请将以下行添加到内核配置文件中：`

> device bhnd
> device siba

`要在引导时以模块形式加载此驱动，请将此行添加到 loader.conf(5) 中：`

```sh
siba_load="YES"
```

## 描述

`siba` 驱动为基于 Sonic Inc. Silicon Backplane 的设备提供 [bhnd(4)](bhnd.4.md) 支持，Silicon Backplane 是早期 Broadcom 家庭网络事业部无线芯片组和嵌入式系统中使用的块间通信架构。

公共互连连接了 Silicon Backplane 的所有功能块。这些功能块（称为核心）使用开放核心协议（OCP）接口与附加到 Silicon Backplane 的代理通信。

每个核心可以有一个发起者代理（将读写请求传递到系统背板）和一个目标代理（返回对这些请求的响应）。并非所有核心都同时包含发起者和目标代理。发起者代理存在于包含主机接口（PCI、PCMCIA）、嵌入式处理器（MIPS）或与通信核心关联的 DMA 处理器的核心中。

## 参见

[bcma(4)](bcma.4.md), [bhnd(4)](bhnd.4.md), [intro(4)](intro.4.md)

## 历史

`siba` 设备驱动最早出现于 FreeBSD 8.0。该驱动在 FreeBSD 11.0 中被重写，以支持通用的 Broadcom [bhnd(4)](bhnd.4.md) 总线接口。

## 作者

`siba` 驱动最初由 Bruce M. Simpson <bms@FreeBSD.org> 和 Weongyo Jeong <weongyo@FreeBSD.org> 编写。该驱动在 FreeBSD 11.0 中由 Landon Fuller <landonf@FreeBSD.org> 重写。
