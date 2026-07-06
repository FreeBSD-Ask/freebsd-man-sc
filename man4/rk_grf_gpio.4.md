# rk\_grf\_gpio.4

`rk_grf_gpio` — RockChip GPIO_MUTE 引脚驱动

## 名称

`rk_grf_gpio`

## 概要

`options SOC_ROCKCHIP_rk3328`

## 描述

`rk_grf_gpio` 驱动提供了一个单引脚、仅输出的 gpio(3) 单元，其唯一引脚名为 GPIO_MUTE。它控制 SoC 上 GPIO_MUTE 引脚的输出。

此 GPIO 通常用于控制板上的另一设备，因此通常不向用户软件开放。

## 硬件

`rk_grf_gpio` 驱动支持以下 GRF GPIO 控制器：

- rockchip,rk3328-grf-gpio

## 历史

`rk_grf_gpio` 驱动最早出现在 FreeBSD 15.0 中。

## 作者

`rk_grf_gpio` 驱动和手册由 Stephen Hurd <shurd@freebsd.org> 编写。
