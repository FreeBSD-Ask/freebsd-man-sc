# bcma(4)

`bcma` — Broadcom AMBA 背板驱动

## 名称

`bcma`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device bhnd
> device bcma

要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
bcma_load="YES"
```

## 描述

`bcma` 驱动为基于 ARM AMBA 的背板架构设备提供 [bhnd(4)](bhnd.4.md) 支持，该架构见于后续的 Broadcom 家庭网络部门的网络芯片组和嵌入式系统中。

公共互连连接背板的所有功能块。这些功能块（称为核心）使用 ARM AMBA AXI 或 APB 接口与连接到互连的设备通信。

[siba(4)](siba.4.md) 设备中使用的 IP 核由 Broadcom 进行了适配，以与新的互连兼容。

## 参见

[bhnd(4)](bhnd.4.md), [intro(4)](intro.4.md), [siba(4)](siba.4.md)

## 历史

`bcma` 设备驱动首次出现于 FreeBSD 11.0。

## 作者

`bcma` 驱动由 Landon Fuller <landonf@FreeBSD.org> 编写。
