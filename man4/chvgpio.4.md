# chvgpio.4

`chvgpio` — Intel Cherry View SoC GPIO 控制器

## 名称

`chvgpio`

## 概要

`device gpio device chvgpio`

## 描述

`chvgpio` 支持 Intel Cherry View SoC 系列中可找到的 GPIO 控制器。

Cherry View SoC 有 5 个 GPIO 引脚组：NORTH、EAST、SOUTHEAST、SOUTHWEST 和 VIRTUAL。除 VIRTUAL 外，所有组都作为 **/dev/gpiocN** 暴露给用户空间，其中 N 为 0-3。每组中的引脚已预先命名，以匹配 Intel® Atom™ Z8000 处理器系列 Vol 2 中的名称

## 参见

gpio(3), [gpio(4)](gpio.4.md), [gpioctl(8)](../man8/gpioctl.8.md)

> "Intel® Atom™ Z8000 Processor Series Vol 1"。

> "Intel® Atom™ Z8000 Processor Series Vol 2"。

## 历史

`chvgpio` 手册页首次出现于 FreeBSD 12。

## 作者

此驱动和手册页由 Tom Jones <tj@enoti.me> 编写。
