# alpm(4)

`alpm` — Acer Aladdin 15x3 电源管理控制器驱动

## 名称

`alpm`

## 概要

`device smbus device smb device alpm`

## 描述

此驱动提供对 Aladdin 15x3 电源管理单元的访问。目前仅实现了 smbus 控制器功能。

Aladdin 芯片组的嵌入式 SMBus 控制器可让你访问主板的监控功能。参见 [smb(4)](smb.4.md) 以编写用户代码从主板的监控芯片获取电压、温度等信息。

## 参见

[smb(4)](smb.4.md), [smbus(4)](smbus.4.md)

## 历史

`alpm` 手册页首次出现于 FreeBSD 4.0。

## 作者

本手册页由 Nicolas Souchu <nsouch@FreeBSD.org> 编写。

## 缺陷

仅支持轮询模式。
