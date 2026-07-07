# etherswitch(4)

`etherswitch` — 以太网交换机框架

## 名称

`etherswitch`

## 概要

`若要将此框架编译进内核，请在内核配置文件中加入以下行：`

> device etherswitch
> device miiproxy
> device iicbus

## 描述

`etherswitch` 驱动为以太网交换机设备提供框架。

## 文件

**`/dev/etherswitch?`** `etherswitch` 设备节点

## 参见

[adm6996fc(4)](adm6996fc.4.md), [ar40xx(4)](ar40xx.4.arm.md), [arswitch(4)](arswitch.4.md), [e6000sw(4)](e6000sw.4.md), [e6060sw(4)](e6060sw.4.md), [iicbus(4)](iicbus.4.md), [ksz8995ma(4)](ksz8995ma.4.md), etherswitchcfg(8)

## 历史

`etherswitch` 框架首次出现于 FreeBSD 10.0。

## 作者

Stefan Bethke
