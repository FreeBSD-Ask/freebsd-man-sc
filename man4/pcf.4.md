# pcf(4)

`pcf` — Philips I2C 总线控制器

## 名称

`pcf`

## 概要

`device pcf`

`在 /boot/device.hints 中：hint.pcf.0.at="isa" hint.pcf.0.port="0x320" hint.pcf.0.irq="5"`

`对于一个或多个 iicbus 总线：device iicbus`

## 描述

*pcf* 驱动为 [iicbus(4)](iicbus.4.md) 系统提供对 Philips PCF8584 I2C 控制器的支持。

PCF8584 是一种采用 CMOS 技术设计的集成电路，用作大多数标准并行总线微控制器/微处理器与串行 I2C 总线之间的接口。PCF8584 同时提供主控和从控功能。与 I2C 总线的通信以字节为单位，使用中断或轮询握手方式进行。它控制所有 I2C 总线特定的序列、协议、仲裁和时序。PCF8584 允许并行总线系统与 I2C 总线进行双向通信。

## 参见

[iicbus(4)](iicbus.4.md)

## 历史

`pcf` 手册页最早出现于 FreeBSD 3.0。

## 作者

本手册页由 Nicolas Souchu 编写。
