# rk_grf(4)

`rk_grf` — RockChip SoC 上通用寄存器文件（General Register Files）控制器的驱动

## 名称

`rk_grf`

## 概要

`options SOC_ROCKCHIP_rk3328`

## 描述

`rk_grf` 设备驱动为 RockChip 通用寄存器文件系统控制器提供支持。

## 硬件

当前版本的 `rk_grf` 驱动支持具有以下兼容字符串之一的 GRF 控制器：

- rockchip,rk3328-grf

## 历史

`rk_grf` 设备驱动最早出现在 FreeBSD 12.0 中。

## 作者

`rk_grf` 设备驱动和手册页由 Emmanuel Vadot <manu@freebsd.org> 编写。
