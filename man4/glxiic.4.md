# glxiic.4

`glxiic` — Geode LX CS5536 I2C 控制器驱动

## 名称

`glxiic`

## 概要

`要将此驱动编译进内核，请将以下行放入你的内核配置文件：`

> device pci
> device isa
> device glxiic
> device iicbus

`或者，要在引导时以模块形式加载驱动，请将以下行放入 loader.conf(5)：`

```sh
glxiic_load="YES"
```

## 描述

`glxiic` 驱动支持 Geode LX 系列 CS5536 配套设备的系统管理总线控制器。Geode LX 是 AMD Geode 集成 x86 系统芯片系列的成员。

虽然 AMD 将此设备称为系统管理总线（SMBus）控制器，但它实际上是一个 I2C 控制器（缺少 SMBus ALERT# 和 Alert Response 支持）。

`glxiic` 驱动同时支持 I2C 主模式和从模式。

## SYSCTL 变量

`glxiic` 驱动支持以下变量，同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数：

**`dev.glxiic.0.timeout`** 此变量控制 I2C 总线超时（以毫秒为单位）。默认超时为 35 毫秒。值为零时禁用超时。

## 注意事项

`glxiic` 驱动默认使用板载固件配置的中断线号。如果板载固件未配置中断线号（或要覆盖板载固件配置的中断线号），请将以下行放入 [device.hints(5)](../man5/device.hints.5.md)：

> hint.glxiic.0.irq="10"

中断线号必须在 1 到 15 之间。

## 参见

[iicbus(4)](iicbus.4.md), [device.hints(5)](../man5/device.hints.5.md), loader.conf(5), [loader(8)](../man8/loader.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`glxiic` 设备驱动和手册页首次出现于 FreeBSD 9.0。

## 作者

`glxiic` 设备驱动和手册页由 Henrik Brix Andersen <brix@FreeBSD.org> 编写。
