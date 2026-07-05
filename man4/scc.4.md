# scc.4

`scc` — 串行通信控制器驱动

## 名称

`scc`

## 概要

`device scc device uart`

## 描述

`scc` 设备驱动为各类 SCC 提供支持。它是一个伞形驱动，将每个独立通信通道的控制委托给下级驱动。这些下级驱动（如 [uart(4)](uart.4.md)）负责处理通信本身的细节。

## 硬件

`scc` 驱动支持以下类别的串行通信控制器：

- QUICC：Freescale/NXP QUad Integrated Communications Controllers。
- Z8530：基于 Zilog 8530 的串行通信控制器。

## 参见

[puc(4)](puc.4.md), [uart(4)](uart.4.md)

## 历史

`scc` 设备驱动最早出现于 FreeBSD 7.0。

## 作者

`scc` 驱动和本手册页由 Marcel Moolenaar <marcel@xcllnt.net> 编写。
