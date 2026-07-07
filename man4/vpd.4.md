# vpd(4)

`vpd` — 重要产品数据内核接口

## 名称

`vpd`

## 概要

`device vpd`

## 描述

IBM ThinkPad 笔记本（以及大多数 IBM 台式机）在 BIOS Shadow RAM 中有一个 48 字节的重要产品数据（Vital Product Data，VPD）结构。

VPD 提供机型和型号信息、构建 ID（大致相当于 BIOS 版本）以及序列号信息。

`vpd` 驱动扫描 BIOS 区域并声明 VPD 结构使用的内存。它提供 sysctl(3) 分支 `hw.vpd` 以允许用户态访问此信息。以下变量由每个 VPD 附件提供（应当只有一个）：

**`MACHINE_TYPE`**（`machine.type`）机型。

**`MACHINE_MODEL`**（`machine.model`）型号。

**`BUILD_ID`**（`build.id`）BIOS 构建 ID。

**`SERIAL_BOX`**（`serial.box`）机箱序列号。

**`SERIAL_PLANAR`**（`serial.planar`）主板序列号。

## 参见

> "TP General - Using the BIOS Build ID to identify IBM ThinkPad systems", Reference #: MIGR-45120, November 22, 2002.

## 历史

`vpd` 驱动最早出现于 FreeBSD 5.1。

## 作者

`vpd` 驱动及本手册页由 Matthew N. Dodd <mdodd@FreeBSD.org> 编写。
