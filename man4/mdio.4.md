# mdio(4)

`mdio` — IEEE 802.3 管理数据输入/输出接口

## 名称

`mdio`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device mdio

## 描述

`mdio` 驱动提供媒体访问控制（MAC）子层与物理层（PHY）实体的控制和状态寄存器之间的互连，如 IEEE 802.3 标准所定义。

`mdio` 层允许设备驱动程序共享各种外部 PHY 设备的通用支持代码。

MDIO 是构成 IEEE 802.3 标准定义的媒体独立接口（MII）的两种信号接口之一。[miibus(4)](miibus.4.md) 驱动为需要完整 MII 支持的设备提供支持。

## 参见

[miibus(4)](miibus.4.md)

## 标准

有关 MDIO 的更多信息可在 IEEE 802.3 标准中找到。

## 历史

`mdio` 驱动首次出现于 FreeBSD 10.0。

## 作者

该驱动由 Stefan Bethke <stb@lassitu.de> 编写。
