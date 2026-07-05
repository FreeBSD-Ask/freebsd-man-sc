# qlnxe.4

`qlnxe` — Cavium 25/40/100 千兆以太网与 CNA 适配器驱动程序

## 名称

`qlnxe`

## 概要

若要将此驱动程序编译进内核，请在你的内核配置文件中加入以下行：

> device qlnxe

若要在引导时以模块方式加载驱动程序，在 loader.conf(5) 中加入以下行：

```sh
if_qlnxe_load="YES"
```

## 描述

`qlnxe` 驱动程序支持 IPv4 校验和卸载、IPv4 和 IPv6 的 TCP 与 UDP 校验和卸载、IPv4 和 IPv6 的大段卸载、Jumbo 帧、VLAN 标签、接收端扩展、硬件与软件 LRO。有关更多硬件信息，参见 `http://www.qlogic.com/`。

## 硬件

`qlnxe` 驱动程序支持基于以下芯片组的 25/40/100 千兆以太网与 CNA 适配器：

- QLogic 45000 系列
- QLogic 41000 系列

## 支持

如需支持，请联系你的 Cavium 授权经销商或 Cavium 技术支持，网址 `http://support.qlogic.com`，或发送电子邮件至 <support@qlogic.com>。

## 参见

[altq(4)](altq.4.md), arp(4), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`qlnxe` 设备驱动程序首次出现于 FreeBSD 11.1。

## 作者

`qlnxe` 驱动程序由 Cavium Inc. 的 David C Somayajulu 编写。
