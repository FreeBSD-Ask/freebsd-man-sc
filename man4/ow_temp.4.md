# ow_temp.4

`ow_temp` — Dallas Semiconductor 1-Wire 温度传感器

## 名称

`ow_temp`

## 概要

`device ow_temp`

## 描述

`ow_temp` 模块支持许多 1-Wire 温度传感器。

传感器会被定期读取，结果通过 sysctl(3) 返回，如下所述。

## 硬件

`ow_temp` 驱动支持以下温度传感器：

| DS1820 | 1-Wire 数字温度计 |
| ------ | ----------------- |
| DS18S20 | 高精度 1-Wire 数字温度计 |
| DS18B20 | 可编程分辨率 1-Wire 数字温度计 |
| DS1822 | 经济型 1-Wire 数字温度计 |
| DS1825 | 带 4 位 ID 的可编程分辨率 1-Wire 数字温度计 |
| MAX31820 | 1-Wire 寄生电源环境温度传感器 |

驱动支持家族码 0x10、0x22、0x28 和 0x3b。

## SYSCTL

`ow_temp` 驱动通过 [sysctl(8)](../man8/sysctl.8.md) 树中设备节点下的 [sysctl(8)](../man8/sysctl.8.md) 条目报告数据：

**temperature** 上次读取的温度，单位为毫开尔文。

**badcrc** 从设备读取温度时出现的 CRC 错误次数。少量 CRC 错误是预期之内的。但是，高频率的 CRC 错误通常表明环境噪声大、线缆问题或总线上设备过多。

**badread** 从卡上读取温度时遇到非 CRC 错误的次数。此类错误非常罕见。

**reading_interval** 连续读取传感器之间的时间间隔，单位为 tick。

**parasite** 当设备使用寄生电源模式连接时，此项非零。它也可能指示接线错误。

温度以毫开尔文报告，尽管优质设备的绝对精度约为 0.2 度，廉价设备约为 1 度。设备以 0.0625 度为步长报告。驱动在 [sysctl(8)](../man8/sysctl.8.md) 报告中保留设备测量的精度。这些设备的相对精度和重复性通常远高于其绝对精度。这使得它们非常适合用于追求稳定性且需要保留完整精度的控制回路。

## 参见

[ow(4)](ow.4.md), [owc(4)](owc.4.md), [sysctl(8)](../man8/sysctl.8.md), [owll(9)](../man9/owll.9.md), [own(9)](../man9/own.9.md)

## 法律条款

1-Wire 是 Maxim Integrated Products, Inc. 的注册商标。

## 历史

`ow_temp` 驱动最早出现于 FreeBSD 11.0。

## 作者

`ow_temp` 设备驱动及本手册页由 Warner Losh 编写。

## 缺陷

设备的寄生模式无法工作。它需要 [owc(4)](owc.4.md) 驱动中尚未实现的支持。

来自 *DS1825* 的 ID 位不会被识别或报告。

设备的类型不会通过 [sysctl(8)](../man8/sysctl.8.md) 报告。

不支持告警模式。无法设置低和高告警温度。

无法写入 EEPROM。

“Convert Temperature”请求会直接发送到设备。无法利用 1-Wire 总线的广播能力并行执行所有转换。

无法在支持精度设置的设备上设置精度。

转换时间固定为 1 秒，即使某些设备速度更快。

没有字符设备可用于向程序提供连续的读数流。对温度感兴趣的程序必须轮询 sysctl 来获取温度。
