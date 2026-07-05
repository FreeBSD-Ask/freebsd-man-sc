# ksz8995ma.4

`ksz8995ma` — Micrel KSZ8995MA 快速以太网交换芯片驱动

## 名称

`ksz8995ma`

## 概要

`device spibus device etherswitch device ksz8995ma`

`hint.ksz8995ma.0.at="spibus0"`

## 描述

`ksz8995ma` 设备驱动提供对 Micrel KSZ8995MA 快速以太网交换芯片的管理接口。此驱动使用 spi 接口。KSZ8995 系列有许多版本，但仅支持 MA/FQ 版本。

此驱动支持 port 和 dot1q vlan。dot1q 支持基于端口的标记/取消标记。

## 实例

通过 etherswitchcfg 命令配置 dot1q vlan。

```sh
# etherswitchcfg config vlan_mode dot1q
```

将端口 5 配置为标记端口。

```sh
# etherswitchcfg port5 addtag
```

## 参见

[etherswitch(4)](etherswitch.4.md), etherswitchcfg(8)

## 历史

`ksz8995ma` 设备驱动最早出现于 FreeBSD 12.0。

## 作者

`ksz8995ma` 驱动由 Hiroki Mori 编写。
