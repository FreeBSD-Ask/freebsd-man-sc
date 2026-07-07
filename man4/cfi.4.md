# cfi(4)

`cfi` — Common Flash Interface（CFI）NOR flash 驱动

## 名称

`cfi`, `cfid`

## 概要

`device cfi device cfid options CFI_SUPPORT_STRATAFLASH options CFI_ARMEDANDDANGEROUS`

在 **/boot/device.hints** 中：

`hint.cfi.0.at="nexus0" hint.cfi.0.maddr=0x74000000 hint.cfi.0.msize=0x4000000`

在 DTS 文件中：

`flash@74000000 { compatible = “cfi-flash ” reg = <0x74000000 0x4000000>; };`

## 描述

`cfid` 设备驱动为支持 Common Flash Interface（CFI）规范的 NOR flash 设备提供管理接口。其配套设备 `cfid` 为该设备提供 [geom(4)](geom.4.md) 磁盘接口。

通过 `CFI_SUPPORT_STRATAFLASH` 内核选项，可对 Intel StrataFlash 系列的特性提供特殊支持。通过 `CFI_ARMEDANDDANGEROUS` 内核选项，可额外启用对一次性写入位的支持，以将 Intel StrataFlash 设备的一部分切换为只读。

## 参见

[led(4)](led.4.md)

## 历史

`cfid` 设备驱动首次出现于 FreeBSD 8.0。

## 作者

`cfid` 驱动由 Juniper Networks 编写，StrataFlash 支持由 Sam Leffler 提供。本手册页由 SRI International 和剑桥大学计算机实验室在 DARPA/AFRL 合同（FA8750-10-C-0237）（“CTSRD”）下编写，作为 DARPA CRASH 研究计划的一部分。
