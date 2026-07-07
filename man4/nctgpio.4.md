# nctgpio(4)

`nctgpio` — Nuvoton 和 Winbond Super I/O 上的 GPIO 控制器

## 名称

`nctgpio`

## 概要

`device gpio device nctgpio device superio`

## 描述

`nctgpio` 是可在 Nuvoton 和 Winbond Super I/O 芯片中找到的 GPIO 控制器的驱动程序。

`nctgpio` 驱动支持以下芯片：

- Nuvoton NCT5104D
- Nuvoton NCT5104D (PC-Engines APU)
- Nuvoton NCT5104D (PC-Engines APU3)
- Nuvoton NCT5585D
- Nuvoton NCT6116D
- Nuvoton NCT6779
- Nuvoton NCT6796D-E
- Winbond 83627DHG

## 参见

gpio(3), [gpio(4)](gpio.4.md), [gpioctl(8)](../man8/gpioctl.8.md)

## 历史

该驱动首次出现于 FreeBSD 11.0。手册页首次出现于 FreeBSD 14.0。

## 作者

该驱动最初由 Daniel Wyatt <daniel@dewyatt.com> 编写。本手册页由 Stéphane Rochoy <stephane.rochoy@stormshield.eu> 编写。
