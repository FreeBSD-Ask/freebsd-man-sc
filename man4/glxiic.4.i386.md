# glxiic.4.i386

`glxiic` — Geode LX CS5536 I2C 控制器驱动

## 名称

`glxiic`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device pci
> device isa
> device glxiic
> device iicbus

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
glxiic_load="YES"
```

## 描述

`glxiic` 驱动支持 Geode LX 系列 CS5536 Companion Device 的 System Management Bus 控制器。Geode LX 是 AMD Geode 系列 x86 集成系统芯片的一员。

虽然 AMD 将此设备称为 System Management Bus（SMBus）控制器，但它实际上是一个 I2C 控制器（缺少 SMBus ALERT# 和 Alert Response 支持）。

`glxiic` 驱动同时支持 I2C 主模式和从模式。

## SYSCTL 变量

`glxiic` 驱动支持以下变量，它们既是 [sysctl(8)](../man8/sysctl.8.md) 变量，也是 [loader(8)](../man8/loader.8.md) 可调参数：

**`dev.glxiic.0.timeout`** 此变量控制 I2C 总线超时（以毫秒为单位）。默认超时为 35 毫秒。值为零时禁用超时。

## 注意事项

`glxiic` 驱动默认使用由板载固件配置的中断线号。如果板载固件未配置中断线号（或要覆盖板载固件配置的中断线号），请在 [device.hints(5)](../man5/device.hints.5.md) 中加入以下行：

> hint.glxiic.0.irq="10"

中断线号必须介于 1 到 15 之间。

## 参见

[iicbus(4)](iicbus.4.md), [device.hints(5)](../man5/device.hints.5.md), loader.conf(5), [loader(8)](../man8/loader.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`glxiic` 设备驱动和手册页首次出现于 FreeBSD 9.0。

## 作者

`glxiic` 设备驱动和手册页由 Henrik Brix Andersen <brix@FreeBSD.org> 编写。
