# amdpm.4

`amdpm` — AMD 756/766/768/8111 电源管理控制器驱动

## 名称

`amdpm`

## 概要

`device smbus device smb device amdpm`

## 描述

此驱动提供对 AMD 756/766/768/8111 电源管理控制器的访问。目前仅实现了 SMBus 1.0 控制器功能。AMD 8111 控制器的 SMBus 2.0 功能由 [amdsmb(4)](amdsmb.4.md) 驱动支持。

AMD 756 芯片组的嵌入式 SMBus 控制器可让你访问主板的监控功能。参见 [smb(4)](smb.4.md) 以编写用户代码从主板的监控芯片获取电压、温度等信息。

## 参见

[amdsmb(4)](amdsmb.4.md), [intpm(4)](intpm.4.md), [smb(4)](smb.4.md), [smbus(4)](smbus.4.md)

## 历史

`amdpm` 驱动首次出现于 FreeBSD 4.5。

## 作者

此驱动由 Matthew C. Forman 编写。大量基于 Nicolas Souchu 编写的 `alpm` 驱动。本手册页由 Murray Stokely <murray@FreeBSD.org> 编写。

## 缺陷

仅支持轮询模式。
