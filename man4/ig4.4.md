# ig4.4

`ig4` — Synopsys DesignWare I2C 控制器

## 名称

`ig4`

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device ig4
> device iicbus

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
ig4_load="YES"
```

## 描述

`ig4` 驱动提供对连接到 I2C 控制器的外设的访问。

## 硬件

`ig4` 支持基于 Synopsys DesignWare IP 的 I2C 控制器，这些控制器可见于自第四代起的 Intel(R) Core(TM) 处理器、Intel(R) Bay Trail、Apollo Lake SoC 系列以及部分 AMD 系统。

## SYSCTL 变量

以下 [sysctl(8)](../man8/sysctl.8.md) 变量可用：

**`debug.ig4_dump`** 此 sysctl 是一个从零开始的位掩码。当任何位被置位时，对于具有相同单元号的 `ig4` 设备，每次 I2C 传输都会打印一次寄存器转储。

## 参见

[iic(4)](iic.4.md), [iicbus(4)](iicbus.4.md)

## 作者

`ig4` 驱动最初由 Matthew Dillon 为 Dx 编写，随后由 Michael Gmelin <freebsd@grem.de> 移植到 FreeBSD。

本手册页由 Michael Gmelin <freebsd@grem.de> 编写。
