# bytgpio.4

`bytgpio` — Intel Bay Trail SoC GPIO 控制器

## 名称

`bytgpio`

## 概要

`device gpio device bytgpio`

## 描述

`bytgpio` 是 GPIO 控制器的驱动，该控制器可见于 Intel Bay Trail SoC 系列。

Bay Trail SoC 有三组 GPIO 引脚，以 /dev/gpiocN 的形式暴露给用户态，其中 N 为 0、1 和 2。每组中的引脚已预先命名，以匹配主板原理图上的名称：GPIO_S0_SCnn、GPIO_S0_NCnn 和 GPIO_S5_nn。

## 参见

gpio(3), [gpio(4)](gpio.4.md), [gpioctl(8)](../man8/gpioctl.8.md)

## 历史

`bytgpio` 手册页首次出现于 FreeBSD 11.1。

## 作者

本驱动和手册页由 Oleksandr Tymoshenko <gonzo@FreeBSD.org> 编写。
