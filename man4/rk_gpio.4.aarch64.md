# rk_gpio.4.aarch64

`rk_gpio` — RockChip SoC 上 GPIO 控制器的驱动

## 名称

`rk_gpio`

## 概要

`options SOC_ROCKCHIP_RK3328`

## 描述

`rk_gpio` 设备驱动为 RockChip SoC 上存在的 GPIO 控制器设备提供支持。

## 硬件

当前版本的 `rk_gpio` 驱动支持具有以下兼容字符串之一的 GPIO bank：

- rockchip,gpio-bank

## 参见

gpiobus(4), [gpioctl(8)](../man8/gpioctl.8.md)

## 历史

`rk_gpio` 设备驱动最早出现在 FreeBSD 12.0 中。

## 作者

`rk_gpio` 设备驱动和手册页由 Emmanuel Vadot <manu@freebsd.org> 编写。
