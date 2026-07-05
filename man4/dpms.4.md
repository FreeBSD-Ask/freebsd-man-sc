# dpms.4

`dpms` — VESA BIOS DPMS 驱动

## 名称

`dpms`

## 概要

`device dpms`

## 描述

`dpms` 驱动使用 VESA BIOS 在挂起和恢复期间管理外部显示器。当机器挂起时，`dpms` 驱动关闭外部显示器。当机器恢复时，它将显示器恢复到驱动首次加载时的状态。

## 参见

[acpi_video(4)](acpi_video.4.md)

## 缺陷

VESA BIOS DPMS 调用不提供任何方式来标识要操作的特定显示器或适配器。因此，此驱动在具有多个显示器和/或适配器的系统上可能会产生意外结果。
