# sbni(4)

`sbni` — Granch SBNI12 专线调制解调器驱动

## 名称

`sbni`

## 概要

`device sbni`

## 描述

`sbni` 驱动支持以下型号的专线调制解调器：

- SBNI12-02, SBNI12D-02
- SBNI12-04, SBNI12D-04
- SBNI12-05, SBNI12D-05, ISA 和 PCI
- SBNI12-10, SBNI12D-10, ISA 和 PCI

以及用于语音频带数据链路的套件：

- SBNI12-11, SBNI12D-11, ISA 和 PCI。

除标准端口和 IRQ 规格外，`sbni` 驱动还支持多个 `flags`，可设置波特率、接收电平以及以太网 MAC 地址的低三字节（高三字节始终为 `00:ff:01`），因为 Granch 调制解调器以类以太网网卡的形式呈现给系统。

`flags` 的高字节是一个位字段，用于指定 SBNI 适配器接收电平/波特率：

**00** - 0 波特率（快速模式 2Mb / 慢速模式 500kb）
**01** - 1 波特率（1Mb/250kb）
**10** - 2 波特率（500kb/125kb）
**11** - 3 波特率（250kb/62.5kb）

**位** 0-3：接收电平（0x00..0x0f）

**位** 4-5：波特率编号：

**位** 6：使用固定接收电平，如果设置位 6，则根据位 0-3 的值设置接收电平，否则自动检测接收电平

**位** 7：使用固定波特率，如果设置位 7，则根据位 4-5 的值设置波特率，否则波特率设置为 2Mb

## 文件

驱动源码位于：

**`/sys/dev/sbni/if_sbni.c`**
**`/sys/dev/sbni/if_sbnireg.h`**
**`/sys/dev/sbni/if_sbnivar.h`**

## 参见

arp(4), [netintro(4)](netintro.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`sbni` 设备驱动最早出现于 FreeBSD 4.6。

## 作者

用于 FreeBSD 4.x 的 `sbni` 设备驱动由 Denis I. Timofeev 编写，部分基于 David Greenman 的 ed(4) 驱动。早期版本（可在 `ftp.granch.com` 上获取）由 Alexey V. Zverev 编写。

SBNI12 硬件由 Alexey V. Chirkov 设计。
