# imx_spi.4.arm

`imx_spi` — NXP i.MX 系列 SPI（Serial Peripheral Interface，串行外设接口）驱动

## 名称

`imx_spi`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device imx_spi

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
imx_spi_load="YES"
```

## 描述

`imx_spi` 驱动为 NXP i.MX 系列处理器上存在的“ECSPI”（Enhanced Configurable SPI，增强型可配置 SPI）硬件提供支持。虽然 ECSPI 硬件同时支持主模式和从模式，但此驱动目前仅在主模式下运行。

由于硬件特性，`imx_spi` 驱动要求所有片选引脚均配置为 GPIO 引脚。使用 FDT 属性“cs-gpios”指定哪些引脚用作片选。可使用任意 GPIO 引脚，包括硬件通常用作 SPI 选择引脚的那些；只需在 [fdt_pinctrl(4)](fdt_pinctrl.4.md) 数据中将它们配置为 GPIO 即可。

## SYSCTL 变量

以下变量可通过 [sysctl(8)](../man8/sysctl.8.md) 访问，并可作为 [loader(8)](../man8/loader.8.md) 可调参数：

**`dev.imx_spi.%d.debug`** 非零时输出调试信息。值为 1 时显示总线传输相关信息，值为 2 时增加总线时钟频率和片选活动信息，值为 3 时增加中断处理相关信息。

## 参见

[fdt(4)](fdt.4.md), [fdt_pinctrl(4)](fdt_pinctrl.4.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`imx_spi` 驱动首次出现于 FreeBSD 12.0。
