# arswitch(4)

`arswitch` — Atheros AR8000 系列以太网交换机驱动

## 名称

`arswitch`

## 概要

`device mdio device etherswitch device arswitch`

## 描述

`arswitch` 驱动为 Atheros AR8000 系列以太网交换机控制器提供管理接口。该驱动使用 [mdio(4)](mdio.4.md) 或 [miibus(4)](miibus.4.md) 接口配置以太网接口。

此驱动支持基于端口的 VLAN 以及 IEEE 802.1Q（QinQ）。这些选项可使用 etherswitchcfg(8) 命令配置。`arswitch` 支持 `addtag`、`striptag` 和 `doubletag`。`addtag` 和 `striptag` 互斥。

不支持设置交换机 MAC 地址。

## 硬件

`arswitch` 驱动支持以下以太网交换机控制器：

- Atheros AR8327 七端口千兆以太网交换机
- Atheros AR8316 六端口千兆以太网交换机
- Atheros AR8236 六端口快速以太网交换机
- Atheros AR8226 六端口快速以太网交换机
- Atheros AR8216 六端口快速以太网交换机

## 参见

[etherswitch(4)](etherswitch.4.md), etherswitchcfg(8)

## 历史

`arswitch` 设备驱动首次出现于 FreeBSD 12.0。

## 作者

`arswitch` 手册页由 Felix Johnson 编写。
