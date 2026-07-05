# llan.4.powerpc

`llan` — POWER 逻辑局域网

## 名称

`llan`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device llan

## 描述

`llan` 驱动提供对符合 PAPR 规范的 POWER hypervisor（如 PowerVM 和 PowerKVM）提供的分区逻辑 LAN 控制器的支持。在某些固件上，hypervisor 支持高级卸载特性，但当前驱动尚未支持这些特性。

## 参见

[vtnet(4)](vtnet.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`llan` 设备驱动出现于 FreeBSD 10.0。

## 作者

`llan` 驱动由 Nathan Whitehorn <nwhitehorn@FreeBSD.org> 编写。
