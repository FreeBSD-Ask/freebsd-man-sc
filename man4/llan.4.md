# llan(4)

`llan` — POWER 逻辑局域网

## 名称

`llan`

## 概要

`要将此驱动编译进内核，请将以下行放入你的内核配置文件：`

> device llan

## 描述

`llan` 驱动为符合 PAPR 的 POWER hypervisor（如 PowerVM 和 PowerKVM）提供的分区逻辑 LAN 控制器提供支持。在某些固件上，hypervisor 支持高级卸载功能，但驱动目前不支持这些功能。

## 参见

[vtnet(4)](vtnet.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`llan` 设备驱动出现于 FreeBSD 10.0。

## 作者

`llan` 驱动由 Nathan Whitehorn <nwhitehorn@FreeBSD.org> 编写。
