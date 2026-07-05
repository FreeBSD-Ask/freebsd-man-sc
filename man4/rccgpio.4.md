# rccgpio.4

`rccgpio` — ADI Engineering RCC-VE 与 RCC-DFF/DFFv2 GPIO 控制器

## 名称

`rccgpio`

## 概要

`device rccgpio device gpio device gpioled`

## 描述

`rccgpio` 提供了一个简单接口，用于读取复位开关状态并控制状态 LED。

已知的由软件控制的复位开关仅出现在 Netgate 的主板上。大多数用户得到的是一个硬件复位按钮。

所有 GPIO 引脚都被锁定在其预期设置中，以禁止任何可能有害的设置（即可能导致短路的设置）。

## 参见

gpio(3), [gpio(4)](gpio.4.md), [gpioled(4)](gpioled.4.md), [gpioctl(8)](../man8/gpioctl.8.md)

## 历史

`rccgpio` 手册页最早出现在 FreeBSD 11.0 中。

## 作者

`rccgpio` 驱动由 Luiz Otavio O Souza <loos@FreeBSD.org> 编写。
