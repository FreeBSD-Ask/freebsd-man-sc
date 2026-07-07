# rk_pinctrl(4)

`rk_pinctrl` — RockChip SoC 上引脚复用的驱动

## 名称

`rk_pinctrl`

## 概要

`options SOC_ROCKCHIP_RK3328`

## 描述

`rk_pinctrl` 设备驱动为 RockChip SoC 上存在的引脚复用设备提供支持。

## 硬件

当前版本的 `rk_pinctrl` 驱动支持具有以下兼容字符串之一的引脚控制器：

- rockchip,rk3328-pinctrl

## 参见

[fdt_pinctrl(4)](fdt_pinctrl.4.md)

## 历史

`rk_pinctrl` 设备驱动最早出现在 FreeBSD 12.0 中。

## 作者

`rk_pinctrl` 设备驱动和手册页由 Emmanuel Vadot <manu@freebsd.org> 编写。
