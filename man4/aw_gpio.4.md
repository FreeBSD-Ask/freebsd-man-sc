# aw_gpio(4)

`aw_gpio` — Allwinner SoC 上 GPIO 与引脚复用功能驱动

## 名称

`aw_gpio`

## 概要

`device gpio options SOC_ALLWINNER_A10 options SOC_ALLWINNER_A13 options SOC_ALLWINNER_A20 options SOC_ALLWINNER_A31 options SOC_ALLWINNER_A31S options SOC_ALLWINNER_A33 options SOC_ALLWINNER_A83T options SOC_ALLWINNER_H2PLUS options SOC_ALLWINNER_H3 options SOC_ALLWINNER_A64 options SOC_ALLWINNER_H5 options SOC_ALLWINNER_D1`

## 描述

`aw_gpio` 设备驱动为 Allwinner SoC 上的 Allwinner 引脚复用和 GPIO 提供支持。

## 硬件

当前版本的 `aw_gpio` 驱动支持具有以下兼容字符串之一的 GPIO/引脚复用控制器：

- allwinner,sun4i-a10-pinctrl
- allwinner,sun5i-a13-pinctrl
- allwinner,sun7i-a20-pinctrl
- allwinner,sun6i-a31-pinctrl
- allwinner,sun6i-a31s-pinctrl
- allwinner,sun6i-a31-r-pinctrl
- allwinner,sun6i-a33-pinctrl
- allwinner,sun8i-a83t-pinctrl
- allwinner,sun8i-a83t-r-pinctrl
- allwinner,sun8i-h3-pinctrl
- allwinner,sun50i-h5-pinctrl
- allwinner,sun8i-h3-r-pinctrl
- allwinner,sun50i-a64-pinctrl
- allwinner,sun50i-a64-r-pinctrl
- allwinner,sun20i-d1-pinctrl

## 参见

[fdt(4)](fdt.4.md), [gpio(4)](gpio.4.md)

## 历史

`aw_gpio` 设备驱动首次出现于 FreeBSD 10.0。

## 作者

`aw_gpio` 设备驱动最初由 Ganbold Tsagaankhuu <ganbold@freebsd.org> 编写。本手册页由 Emmanuel Vadot <manu@freebsd.org> 编写。
