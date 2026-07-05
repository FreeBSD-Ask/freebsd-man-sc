# smbus.4

`smbus` — 系统管理总线

## 名称

`smbus`

## 概要

`device smbus`

`device iicsmb`

## 描述

*smbus* 系统提供了一个统一、模块化且与架构无关的系统，用于实现控制各种 SMB 设备和利用不同 SMB 控制器（I2C、PIIX4、vm86 等）的驱动。

## 系统管理总线

*System Management Bus* 是一种双线接口，简单的电源相关芯片可通过它与系统其余部分通信。它使用 I2C 作为骨干（参见 [iicbus(4)](iicbus.4.md)）。

使用 SMB 的系统通过向设备传递消息来代替触发单独的控制线。

借助 SMBus，设备可以提供制造商信息、告知系统其型号/部件号、为挂起事件保存其状态、报告不同类型的错误、接受控制参数并返回其状态。

只要在内部 SMB 设备和外部 ACCESS 总线设备之间提供适当的电气桥接，SMBus 可与 ACCESS 总线组件共享同一主机设备和物理总线。

## 参见

[iicbus(4)](iicbus.4.md), [iicsmb(4)](iicsmb.4.md), [smb(4)](smb.4.md), smbmsg(8)

> "The SMBus specification".

## 历史

`smbus` 手册页最早出现于 FreeBSD 3.0。

## 作者

本手册页由 Nicolas Souchu 编写。
