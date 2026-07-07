# viapm(4)

`viapm` — VIA 芯片组电源管理控制器驱动

## 名称

`viapm`

## 概要

`device iicbb device iicbus device iicsmb device smbus device smb device viapm`

## 描述

此驱动提供对 VIA 芯片组电源管理单元（Power Management Unit）系列的访问。包括 VT82C586B、VT82C596A、VT82C596B、VT82C686A 和 VT8233。

VIA 芯片组的嵌入式控制器可让你访问主板的监控设施。

586B 的支持通过软件实现，而其他控制器通过硬件支持 SMBus 协议。参见 [smb(4)](smb.4.md) 了解如何编写用户代码以从主板监控芯片中读取电压、温度等信息。

## 参见

[iicbb(4)](iicbb.4.md), [iicbus(4)](iicbus.4.md), [iicsmb(4)](iicsmb.4.md), [smb(4)](smb.4.md), [smbus(4)](smbus.4.md)

## 历史

`viapm` 手册页最早出现于 FreeBSD 4.5。

## 作者

本手册页由 Nicolas Souchu <nsouch@FreeBSD.org> 编写。

## 缺陷

仅支持轮询模式。
