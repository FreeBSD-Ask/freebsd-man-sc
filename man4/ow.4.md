# ow(4)

`ow` — Dallas Semiconductor 1-Wire 总线

## 名称

`ow`

## 概要

`device ow`

## 描述

`ow` 模块实现 Dallas Semiconductor 1-Wire 总线。它附加到 [owc(4)](owc.4.md) 驱动，后者实现 1-Wire 总线的低层信令。

## 参见

[ow_temp(4)](ow_temp.4.md), [owc(4)](owc.4.md), [owll(9)](../man9/owll.9.md), [own(9)](../man9/own.9.md)

## 法律条款

1-Wire 是 Maxim Integrated Products, Inc. 的注册商标。

## 历史

`ow` 驱动最早出现于 FreeBSD 11.0。

## 作者

`ow` 设备驱动及本手册页由 Warner Losh 编写。
