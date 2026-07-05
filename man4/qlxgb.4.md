# qlxgb.4

`qlxgb` — QLogic 10 千兆以太网与 CNA 适配器驱动程序

## 名称

`qlxgb`

## 概要

若要将此驱动程序编译进内核，请在你的内核配置文件中加入以下行：

> device qlxgb

若要在引导时以模块方式加载驱动程序，在 loader.conf(5) 中加入以下行：

```sh
if_qlxgb_load="YES"
```

## 描述

`qlxgb` 驱动程序支持 IPv4 校验和卸载、IPv4 和 IPv6 的 TCP 与 UDP 校验和卸载、IPv4 和 IPv6 的大段卸载、Jumbo 帧、VLAN 标签以及接收端扩展。有关更多硬件信息，参见 `http://www.qlogic.com/`。

## 硬件

`qlxgb` 驱动程序支持基于以下芯片组的 10 千兆以太网与 CNA 适配器：

- QLogic 3200 系列
- QLogic 8200 系列

## 支持

如需支持，请联系你的 QLogic 授权经销商或 QLogic 技术支持，网址 `http://support.qlogic.com`，或发送电子邮件至 <support@qlogic.com>。

## 参见

[altq(4)](altq.4.md), arp(4), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`qlxgb` 设备驱动程序首次出现于 FreeBSD 10.0。

## 作者

`qlxgb` 驱动程序由 QLogic Corporation 的 David C Somayajulu 编写。
