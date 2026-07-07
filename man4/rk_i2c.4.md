# rk_i2c(4)

`rk_i2c` — RockChip SoC 上 I2C 控制器的驱动

## 名称

`rk_i2c`

## 概要

`options SOC_ROCKCHIP_RK3328`

## 描述

`rk_i2c` 设备驱动为 RockChip SoC 上存在的 I2C 控制器设备提供支持。

## 硬件

当前版本的 `rk_i2c` 驱动支持具有以下兼容字符串之一的 I2C 控制器：

- rockchip,rk3328-i2c

## 参见

[iic(4)](iic.4.md), [iicbus(4)](iicbus.4.md)

## 历史

`rk_i2c` 设备驱动最早出现在 FreeBSD 12.0 中。

## 作者

`rk_i2c` 设备驱动和手册页由 Emmanuel Vadot <manu@freebsd.org> 编写。
